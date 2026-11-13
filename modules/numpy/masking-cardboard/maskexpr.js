/* A tiny NumPy-like engine for the Cardboard Masking Lab.
 *
 * It reads an expression such as `(A > 2) & (A < 9)` or
 * `np.any(A % 2 == 0, axis=1)`, evaluates it on a small array with Python's
 * operator precedence and NumPy's broadcasting, and fails with the same kind
 * of error NumPy would raise. Nothing is passed to eval().
 *
 * Works in the browser (window.MaskExpr) and in Node (module.exports), so it
 * can be tested against real NumPy.
 */
(function (root, factory) {
  if (typeof module === "object" && module.exports) module.exports = factory();
  else root.MaskExpr = factory();
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";

  class NumpyError extends Error {
    constructor(type, message) {
      super(message);
      this.type = type;
    }
  }

  const AMBIGUOUS =
    "The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()";
  const UFUNC_TAIL =
    "not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''";

  /* ------------------------------------------------------------------ */
  /* Arrays: { shape, data (flat, row-major), dtype: bool|int|float, tag } */
  /* `tag` remembers whether a 1D result came from a row or a column test. */
  /* ------------------------------------------------------------------ */
  const size = (shape) => shape.reduce((p, d) => p * d, 1);
  const fmtShape = (s) => (s.length === 1 ? `(${s[0]},)` : `(${s.join(",")})`);
  const make = (shape, data, dtype, tag = null) => ({ shape, data, dtype, tag });
  const scalarOf = (v, dtype) => make([], [v], dtype);
  const isFloat = (x) => x.dtype === "float";

  function broadcastShape(sa, sb) {
    const n = Math.max(sa.length, sb.length);
    const out = [];
    for (let i = 1; i <= n; i++) {
      const da = i <= sa.length ? sa[sa.length - i] : 1;
      const db = i <= sb.length ? sb[sb.length - i] : 1;
      if (da !== db && da !== 1 && db !== 1) {
        throw new NumpyError(
          "ValueError",
          `operands could not be broadcast together with shapes ${fmtShape(sa)} ${fmtShape(sb)}`,
        );
      }
      out.unshift(Math.max(da, db));
    }
    return out;
  }

  function elementAt(x, outShape, flat) {
    if (x.data.length === 1) return x.data[0];
    if (x.shape.length === outShape.length && x.shape.every((d, i) => d === outShape[i])) {
      return x.data[flat];
    }
    const coords = [];
    let rem = flat;
    for (let i = outShape.length - 1; i >= 0; i--) {
      coords[i] = rem % outShape[i];
      rem = Math.floor(rem / outShape[i]);
    }
    let idx = 0;
    let stride = 1;
    for (let k = 1; k <= x.shape.length; k++) {
      const d = x.shape[x.shape.length - k];
      const c = coords[outShape.length - k];
      idx += (d === 1 ? 0 : c) * stride;
      stride *= d;
    }
    return x.data[idx];
  }

  function combineTag(a, b) {
    if (a.tag && b.tag && a.tag !== b.tag) {
      throw new NumpyError(
        "ValueError",
        "This lab cannot combine a row mask with a column mask. Use one axis at a time.",
      );
    }
    return a.tag || b.tag;
  }

  function zip(a, b, fn, dtype) {
    const shape = broadcastShape(a.shape, b.shape);
    const n = size(shape);
    const data = new Array(n);
    for (let i = 0; i < n; i++) data[i] = fn(elementAt(a, shape, i), elementAt(b, shape, i));
    return make(shape, data, dtype, combineTag(a, b));
  }

  /* ------------------------------ operators ------------------------------ */
  function arith(op, a, b) {
    const flt = isFloat(a) || isFloat(b);
    if (op === "-" && a.dtype === "bool" && b.dtype === "bool") {
      throw new NumpyError(
        "TypeError",
        "numpy boolean subtract, the `-` operator, is not supported, use the bitwise_xor, the `^` operator, or the logical_xor function instead.",
      );
    }
    if (a.dtype === "bool" && b.dtype === "bool" && (op === "+" || op === "*")) {
      return zip(a, b, op === "+" ? (x, y) => x | y : (x, y) => x & y, "bool");
    }
    if (op === "/") return zip(a, b, (x, y) => x / y, "float");
    if (op === "**") {
      if (!flt && b.data.some((v) => v < 0)) {
        throw new NumpyError("ValueError", "Integers to negative integer powers are not allowed.");
      }
      return zip(a, b, Math.pow, flt ? "float" : "int");
    }
    const f = {
      "+": (x, y) => x + y,
      "-": (x, y) => x - y,
      "*": (x, y) => x * y,
      "%": flt ? (x, y) => x - Math.floor(x / y) * y : (x, y) => (y === 0 ? 0 : ((x % y) + y) % y),
      "//": flt ? (x, y) => Math.floor(x / y) : (x, y) => (y === 0 ? 0 : Math.floor(x / y)),
    }[op];
    return zip(a, b, f, flt ? "float" : "int");
  }

  function bitwise(op, a, b) {
    const name = { "&": "bitwise_and", "|": "bitwise_or", "^": "bitwise_xor" }[op];
    if (isFloat(a) || isFloat(b)) {
      throw new NumpyError("TypeError", `ufunc '${name}' ${UFUNC_TAIL}`);
    }
    const bothBool = a.dtype === "bool" && b.dtype === "bool";
    const f = op === "&" ? (x, y) => x & y : op === "|" ? (x, y) => x | y : (x, y) => x ^ y;
    return zip(a, b, f, bothBool ? "bool" : "int");
  }

  const CMP = {
    "<": (x, y) => x < y,
    "<=": (x, y) => x <= y,
    ">": (x, y) => x > y,
    ">=": (x, y) => x >= y,
    "==": (x, y) => x === y,
    "!=": (x, y) => x !== y,
  };
  const compare = (op, a, b) => zip(a, b, (x, y) => (CMP[op](x, y) ? 1 : 0), "bool");

  function invert(a) {
    if (isFloat(a)) throw new NumpyError("TypeError", `ufunc 'invert' ${UFUNC_TAIL}`);
    if (a.dtype === "bool") return make(a.shape, a.data.map((v) => (v ? 0 : 1)), "bool", a.tag);
    return make(a.shape, a.data.map((v) => ~v), "int", a.tag);
  }

  function negate(a) {
    if (a.dtype === "bool") {
      throw new NumpyError(
        "TypeError",
        "The numpy boolean negative, the `-` operator, is not supported, use the `~` operator or the logical_not function instead.",
      );
    }
    return make(a.shape, a.data.map((v) => -v), a.dtype, a.tag);
  }

  /* Python's `and`, `or`, `not` and chained comparisons need a single truth value. */
  function truth(a) {
    if (size(a.shape) > 1) throw new NumpyError("ValueError", AMBIGUOUS);
    return a.data[0] !== 0;
  }

  function reduce(kind, x, axis) {
    const test = kind === "any" ? (vals) => vals.some((v) => v !== 0) : (vals) => vals.every((v) => v !== 0);
    if (axis === null) return scalarOf(test(x.data) ? 1 : 0, "bool");
    const nd = x.shape.length;
    const ax = axis < 0 ? axis + nd : axis;
    if (ax < 0 || ax >= nd) {
      throw new NumpyError("AxisError", `axis ${axis} is out of bounds for array of dimension ${nd}`);
    }
    if (nd === 1) return scalarOf(test(x.data) ? 1 : 0, "bool");
    const [r, c] = x.shape;
    if (ax === 1) {
      const out = [];
      for (let i = 0; i < r; i++) out.push(test(x.data.slice(i * c, (i + 1) * c)) ? 1 : 0);
      return make([r], out, "bool", "row");
    }
    const out = [];
    for (let j = 0; j < c; j++) {
      const col = [];
      for (let i = 0; i < r; i++) col.push(x.data[i * c + j]);
      out.push(test(col) ? 1 : 0);
    }
    return make([c], out, "bool", "col");
  }

  /* ------------------------------- parser -------------------------------- */
  const TOKEN =
    /\s*(?:(\d+\.\d*|\.\d+|\d+)|([A-Za-z_][A-Za-z_0-9]*(?:\.[A-Za-z_][A-Za-z_0-9]*)*)|(\*\*|\/\/|==|!=|<=|>=|[-+*\/%&|^~<>()=,]))/y;

  function tokenize(text) {
    const tokens = [];
    TOKEN.lastIndex = 0;
    let pos = 0;
    while (pos < text.length) {
      if (/^\s*$/.test(text.slice(pos))) break;
      TOKEN.lastIndex = pos;
      const m = TOKEN.exec(text);
      if (!m) {
        const ch = text[pos + (text.slice(pos).length - text.slice(pos).trimStart().length)];
        if (ch === "@") throw new NumpyError("NotInThisLab", "The operator @ is not available in this lab.");
        throw new NumpyError("SyntaxError", "invalid syntax");
      }
      pos = TOKEN.lastIndex;
      if (m[1] !== undefined) tokens.push({ t: "num", v: parseFloat(m[1]), float: m[1].includes(".") });
      else if (m[2] !== undefined) tokens.push({ t: "name", v: m[2] });
      else tokens.push({ t: "op", v: m[3] });
    }
    return tokens;
  }

  function parse(text) {
    const toks = tokenize(text);
    let i = 0;
    const peek = () => toks[i];
    const isOp = (v) => toks[i] && toks[i].t === "op" && toks[i].v === v;
    const isKw = (v) => toks[i] && toks[i].t === "name" && toks[i].v === v;
    const fail = () => {
      throw new NumpyError("SyntaxError", "invalid syntax");
    };
    const expect = (v) => {
      if (!isOp(v)) fail();
      i++;
    };

    function orTest() {
      const items = [andTest()];
      while (isKw("or")) {
        i++;
        items.push(andTest());
      }
      return items.length === 1 ? items[0] : { t: "or", items };
    }
    function andTest() {
      const items = [notTest()];
      while (isKw("and")) {
        i++;
        items.push(notTest());
      }
      return items.length === 1 ? items[0] : { t: "and", items };
    }
    function notTest() {
      if (isKw("not")) {
        i++;
        return { t: "not", e: notTest() };
      }
      return comparison();
    }
    function comparison() {
      const first = bitOr();
      const ops = [];
      const rest = [];
      while (peek() && peek().t === "op" && CMP[peek().v]) {
        ops.push(peek().v);
        i++;
        rest.push(bitOr());
      }
      return ops.length ? { t: "cmp", first, ops, rest } : first;
    }
    function bin(next, opsList) {
      return function () {
        let left = next();
        while (peek() && peek().t === "op" && opsList.includes(peek().v)) {
          const op = peek().v;
          i++;
          left = { t: "bin", op, l: left, r: next() };
        }
        return left;
      };
    }
    const factor = () => {
      if (peek() && peek().t === "op" && ["+", "-", "~"].includes(peek().v)) {
        const op = peek().v;
        i++;
        return { t: "un", op, e: factor() };
      }
      return power();
    };
    function power() {
      const base = atom();
      if (isOp("**")) {
        i++;
        return { t: "bin", op: "**", l: base, r: factor() };
      }
      return base;
    }
    const term = bin(factor, ["*", "/", "//", "%"]);
    const arithExpr = bin(term, ["+", "-"]);
    const bitAnd = bin(arithExpr, ["&"]);
    const bitXor = bin(bitAnd, ["^"]);
    const bitOr = bin(bitXor, ["|"]);

    function atom() {
      const tk = peek();
      if (!tk) fail();
      if (tk.t === "num") {
        i++;
        return { t: "num", v: tk.v, float: tk.float };
      }
      if (tk.t === "name") {
        if (["and", "or", "not"].includes(tk.v)) fail();
        i++;
        if (isOp("(")) {
          i++;
          const args = [];
          const kwargs = {};
          if (!isOp(")")) {
            for (;;) {
              if (peek() && peek().t === "name" && toks[i + 1] && toks[i + 1].v === "=") {
                const key = peek().v;
                i += 2;
                kwargs[key] = orTest();
              } else {
                args.push(orTest());
              }
              if (isOp(",")) {
                i++;
                continue;
              }
              break;
            }
          }
          expect(")");
          return { t: "call", name: tk.v, args, kwargs };
        }
        return { t: "name", v: tk.v };
      }
      if (isOp("(")) {
        i++;
        const e = orTest();
        expect(")");
        return e;
      }
      return fail();
    }

    if (!toks.length) fail();
    const tree = orTest();
    if (i < toks.length) fail();
    return tree;
  }

  /* ------------------------------ evaluator ------------------------------ */
  const unavailable = (name) =>
    new NumpyError(
      "NotInThisLab",
      `${name} is not available in this lab. A mask only needs comparisons, & | ~, np.any and np.all.`,
    );
  function evaluateTree(node, env) {
    const ev = (n) => evaluateTree(n, env);
    switch (node.t) {
      case "num":
        return scalarOf(node.v, node.float ? "float" : "int");
      case "name":
        if (node.v === "A") return env.A;
        if (node.v === "True") return scalarOf(1, "bool");
        if (node.v === "False") return scalarOf(0, "bool");
        if (node.v.startsWith("np.")) throw unavailable(node.v);
        throw new NumpyError("NameError", `name '${node.v}' is not defined`);
      case "un":
        return node.op === "~" ? invert(ev(node.e)) : node.op === "-" ? negate(ev(node.e)) : ev(node.e);
      case "bin": {
        const a = ev(node.l);
        const b = ev(node.r);
        return ["&", "|", "^"].includes(node.op) ? bitwise(node.op, a, b) : arith(node.op, a, b);
      }
      case "cmp": {
        let left = ev(node.first);
        let res = null;
        for (let k = 0; k < node.ops.length; k++) {
          const right = ev(node.rest[k]);
          res = compare(node.ops[k], left, right);
          if (k < node.ops.length - 1 && !truth(res)) return res;
          left = right;
        }
        return res;
      }
      case "not":
        return scalarOf(truth(ev(node.e)) ? 0 : 1, "bool");
      case "and": {
        let v = null;
        for (const item of node.items) {
          v = ev(item);
          if (!truth(v)) return v;
        }
        return v;
      }
      case "or": {
        let v = null;
        for (const item of node.items) {
          v = ev(item);
          if (truth(v)) return v;
        }
        return v;
      }
      case "call": {
        if (node.name !== "np.any" && node.name !== "np.all") {
          if (node.name.startsWith("np.")) throw unavailable(node.name);
          throw new NumpyError("NameError", `name '${node.name}' is not defined`);
        }
        if (node.args.length < 1 || node.args.length > 2) {
          throw new NumpyError("TypeError", `${node.name}() takes an array and an optional axis`);
        }
        const x = ev(node.args[0]);
        let axisNode = node.args[1] || node.kwargs.axis;
        let axis = null;
        if (axisNode) {
          if (axisNode.t === "name" && axisNode.v === "None") axis = null;
          else {
            const a = ev(axisNode);
            if (a.shape.length !== 0 || a.dtype !== "int") {
              throw new NumpyError("TypeError", "axis must be an integer");
            }
            axis = a.data[0];
          }
        }
        return reduce(node.name.slice(3), x, axis);
      }
      default:
        throw new NumpyError("SyntaxError", "invalid syntax");
    }
  }

  function evaluate(text, A) {
    return evaluateTree(parse(text), { A });
  }

  /* ---------------------- what the lab needs on top ---------------------- */
  function parseArray(text) {
    let value;
    try {
      value = JSON.parse(text);
    } catch (e) {
      throw new NumpyError("ValueError", "Write the array as nested lists of numbers, e.g. [[1, 2], [3, 4]].");
    }
    if (!Array.isArray(value) || value.length === 0) {
      throw new NumpyError("ValueError", "Write the array as nested lists of numbers, e.g. [[1, 2], [3, 4]].");
    }
    const twoD = Array.isArray(value[0]);
    const rows = twoD ? value : [value];
    const cols = rows[0].length;
    const ok = rows.every(
      (row) => Array.isArray(row) && row.length === cols && row.every((v) => typeof v === "number" && Number.isFinite(v)),
    );
    if (!ok || cols === 0) {
      throw new NumpyError("ValueError", "Use a 1D or 2D array of numbers with equal row lengths.");
    }
    if (rows.length * cols > 100) {
      throw new NumpyError("ValueError", "Use at most 100 values.");
    }
    const data = rows.flat();
    const dtype = /[.eE]/.test(text) ? "float" : data.every(Number.isInteger) ? "int" : "float";
    return make(twoD ? [rows.length, cols] : [cols], data, dtype);
  }

  /* Decide how a boolean result can be used to index A. */
  function classifyMask(mask, A) {
    if (mask.dtype !== "bool") {
      throw new NumpyError(
        "TypeError",
        "The mask must contain True and False. Build it with a comparison, for example A > 5.",
      );
    }
    if (mask.shape.length === 0) {
      throw new NumpyError("ValueError", "The mask is a single True/False. It needs one value per element, row or column.");
    }
    const same = mask.shape.length === A.shape.length && mask.shape.every((d, i) => d === A.shape[i]);
    if (same) return "cell";
    const mismatch = (axis, sizeA, sizeM) =>
      new NumpyError(
        "IndexError",
        `boolean index did not match indexed array along axis ${axis}; size of axis is ${sizeA} but size of corresponding boolean axis is ${sizeM}`,
      );
    if (A.shape.length === 2 && mask.shape.length === 1) {
      const [r, c] = A.shape;
      const m = mask.shape[0];
      if (mask.tag === "row") {
        if (m !== r) throw mismatch(0, r, m);
        return "row";
      }
      if (mask.tag === "col") {
        if (m !== c) throw mismatch(1, c, m);
        return "col";
      }
      if (m === r) return "row";
      if (m === c) return "col";
    }
    throw mismatch(0, A.shape[0], mask.shape[0]);
  }

  /* The pieces of A that the mask lets through, as a new array. */
  function select(A, mask, kind) {
    if (kind === "cell") {
      const data = A.data.filter((_, k) => mask.data[k]);
      return make([data.length], data, A.dtype);
    }
    const [r, c] = A.shape;
    if (kind === "row") {
      const rows = [];
      for (let i = 0; i < r; i++) if (mask.data[i]) rows.push(A.data.slice(i * c, (i + 1) * c));
      return make([rows.length, c], rows.flat(), A.dtype);
    }
    const keep = [];
    for (let j = 0; j < c; j++) if (mask.data[j]) keep.push(j);
    const data = [];
    for (let i = 0; i < r; i++) for (const j of keep) data.push(A.data[i * c + j]);
    return make([r, keep.length], data, A.dtype);
  }

  /* Which flat positions of A are open (True)? */
  function holes(A, mask, kind) {
    const out = new Array(A.data.length).fill(false);
    const c = A.shape.length === 2 ? A.shape[1] : A.shape[0];
    for (let k = 0; k < out.length; k++) {
      if (kind === "cell") out[k] = !!mask.data[k];
      else if (kind === "row") out[k] = !!mask.data[Math.floor(k / c)];
      else out[k] = !!mask.data[k % c];
    }
    return out;
  }

  /* A[mask] = value, with NumPy's rule: the dtype of A never changes. */
  function assign(A, mask, kind, value) {
    const open = holes(A, mask, kind);
    let v = value;
    let note = null;
    if (A.dtype === "int" && !Number.isInteger(value)) {
      v = Math.trunc(value);
      note = `A is an integer array, so ${value} was stored as ${v}.`;
    }
    return { array: make(A.shape, A.data.map((x, k) => (open[k] ? v : x)), A.dtype), note };
  }

  /* NumPy-style printing: right-aligned columns, [[...]] for 2D. */
  function formatCells(x) {
    if (x.dtype === "bool") return x.data.map((v) => (v ? "True" : "False"));
    if (x.dtype === "int") return x.data.map(String);
    return x.data.map((v) => (Number.isInteger(v) ? `${v}.` : `${parseFloat(v.toPrecision(8))}`));
  }

  function formatArray(x) {
    if (x.data.length === 0) return "[]";
    let cells = formatCells(x);
    if (x.dtype === "float") {
      const dec = cells.map((s) => (s.includes(".") ? s.length - s.indexOf(".") - 1 : 0));
      const maxDec = Math.max(...dec);
      cells = cells.map((s, k) => {
        const [intPart, frac = ""] = s.split(".");
        return `${intPart}.${frac.padEnd(maxDec, " ")}`;
      });
    }
    const w = x.dtype === "bool" ? 5 : Math.max(...cells.map((s) => s.length)); // NumPy pads booleans to the width of "False"
    const pad = (s) => s.padStart(w, " ");
    if (x.shape.length === 1) return `[${cells.map(pad).join(" ")}]`;
    const [r, c] = x.shape;
    const lines = [];
    for (let i = 0; i < r; i++) lines.push(`[${cells.slice(i * c, (i + 1) * c).map(pad).join(" ")}]`);
    return `[${lines.join("\n ")}]`;
  }

  return {
    NumpyError,
    evaluate,
    parseArray,
    classifyMask,
    select,
    holes,
    assign,
    formatArray,
    fmtShape,
    make,
  };
});
