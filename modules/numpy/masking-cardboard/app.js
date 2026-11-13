"use strict";

const M = window.MaskExpr;
const $ = (sel) => document.querySelector(sel);

const el = {
  array: $("#array-input"),
  expr: $("#mask-input"),
  presets: $("#presets"),
  load: $("#load"),
  message: $("#message"),
  title: $("#board-title"),
  prev: $("#prev"),
  next: $("#next"),
  steps: [...document.querySelectorAll("#steps li")],
  board: $("#board"),
  stats: $("#stats"),
  select: $("#select"),
  assign: $("#assign"),
  value: $("#value"),
  reset: $("#reset"),
  toggles: $("#toggles"),
  togglesHint: $("#toggles-hint"),
  readout: $("#readout"),
};

const PRESETS = [
  { label: "A > 5", expr: "A > 5" },
  { label: "A % 2 == 0", expr: "A % 2 == 0" },
  { label: "(A > 2) & (A < 9)", expr: "(A > 2) & (A < 9)" },
  { label: "~(A % 2 == 0)", expr: "~(A % 2 == 0)" },
  { label: "rows: np.any(A > 8, axis=1)", expr: "np.any(A > 8, axis=1)" },
  { label: "columns: np.all(A > 0, axis=0)", expr: "np.all(A > 0, axis=0)" },
  { label: "pitfall: A > 2 & A < 9", expr: "A > 2 & A < 9", pitfall: true },
];

const STEP_TITLES = [
  "Step 1 — The original array",
  "Step 2 — Put the cardboard on top",
  "Step 3 — Read or write through the holes",
];

const state = {
  original: null, // A as loaded, for Reset
  A: null,
  mask: null,
  kind: "cell", // cell | row | col
  expr: "",
  edited: false,
  stage: 0,
  ops: [], // what the student did, for the transcript
};

/* ------------------------------ helpers ------------------------------ */
const fmt = (x) => M.formatArray(x);
const rowsOf = (A) => (A.shape.length === 2 ? A.shape[0] : 1);
const colsOf = (A) => (A.shape.length === 2 ? A.shape[1] : A.shape[0]);
const cleanNumber = (v) => (Number.isInteger(v) ? String(v) : String(parseFloat(v.toPrecision(6))));

function selectCode() {
  return state.kind === "col" ? "A[:, mask]" : "A[mask]";
}

function setMessage(text, kind = "") {
  el.message.textContent = text;
  el.message.className = `message${kind ? ` message--${kind}` : ""}`;
}

/* ------------------------------ loading ------------------------------ */
function load() {
  try {
    const A = M.parseArray(el.array.value);
    const mask = M.evaluate(el.expr.value, A);
    const kind = M.classifyMask(mask, A);
    state.original = A;
    state.A = M.make(A.shape.slice(), A.data.slice(), A.dtype);
    state.mask = M.make(mask.shape.slice(), mask.data.slice(), "bool");
    state.kind = kind;
    state.expr = el.expr.value.trim();
    state.edited = false;
    state.stage = 0;
    state.ops = [];
    const open = state.mask.data.filter(Boolean).length;
    setMessage(`Loaded. The mask is ${describeKind(kind)} with ${open} True.`, "ok");
    render(false);
  } catch (e) {
    if (!(e instanceof M.NumpyError)) throw e;
    setMessage(`${e.type}: ${e.message}`, "error");
  }
}

function describeKind(kind) {
  return kind === "row" ? "a row mask" : kind === "col" ? "a column mask" : "a cell-by-cell mask";
}

/* ------------------------------ actions ------------------------------ */
function go(delta) {
  state.stage = Math.max(0, Math.min(2, state.stage + delta));
  render(delta > 0 && state.stage === 1);
}

function readThrough() {
  const picked = M.select(state.A, state.mask, state.kind);
  state.stage = 2;
  state.ops.push({ code: selectCode(), out: fmt(picked) });
  setMessage(`${selectCode()} has shape ${M.fmtShape(picked.shape)}: only what shows through the holes.`, "ok");
  render(false);
}

function writeThrough() {
  const value = parseFloat(el.value.value);
  if (!Number.isFinite(value)) {
    setMessage("Type a number to write through the holes.", "error");
    return;
  }
  const res = M.assign(state.A, state.mask, state.kind, value);
  state.A = res.array;
  state.stage = 2;
  const code = state.kind === "col" ? `A[:, mask] = ${cleanNumber(value)}` : `A[mask] = ${cleanNumber(value)}`;
  state.ops.push({ code, out: null, after: fmt(state.A) });
  setMessage(res.note || `Done: ${code}. Only the cells under the holes changed.`, res.note ? "warn" : "ok");
  render(false);
}

function resetArray() {
  if (!state.original) return;
  state.A = M.make(state.original.shape.slice(), state.original.data.slice(), state.original.dtype);
  state.ops = [];
  state.stage = 0;
  setMessage("Original array restored.", "ok");
  render(false);
}

function toggle(i) {
  state.mask.data[i] = state.mask.data[i] ? 0 : 1;
  state.edited = true;
  state.stage = Math.max(state.stage, 1);
  render(false);
}

/* ------------------------------ drawing ------------------------------ */
const CELL = 72;
const PAD = 42;
const BROWN = "#bc8c56";
const BROWN_EDGE = "#78502c";

function svgBoard(animate) {
  const A = state.A;
  const rows = rowsOf(A);
  const cols = colsOf(A);
  const w = cols * CELL + PAD + 20;
  const h = rows * CELL + PAD + 20;
  const ox = PAD;
  const oy = PAD;
  const open = M.holes(A, state.mask, state.kind);
  const covered = state.stage >= 1;

  let cells = "";
  let labels = "";
  for (let c = 0; c < cols; c++) {
    labels += `<text class="axis" x="${ox + c * CELL + CELL / 2}" y="${oy - 16}" text-anchor="middle">${c}</text>`;
  }
  for (let r = 0; r < rows; r++) {
    labels += `<text class="axis" x="${ox - 24}" y="${oy + r * CELL + CELL / 2 + 5}" text-anchor="middle">${r}</text>`;
    for (let c = 0; c < cols; c++) {
      const v = A.data[r * cols + c];
      const x = ox + c * CELL;
      const y = oy + r * CELL;
      const text = A.dtype === "float" ? cleanNumber(v) : String(v);
      cells +=
        `<rect class="cell" x="${x + 3}" y="${y + 3}" width="${CELL - 6}" height="${CELL - 6}" rx="8"/>` +
        `<text class="num" x="${x + CELL / 2}" y="${y + CELL / 2 + 8}" text-anchor="middle">${text}</text>`;
    }
  }

  // Holes: one window per open cell; a row or a column mask is one long slot.
  const holeRects = [];
  if (state.kind === "row") {
    for (let r = 0; r < rows; r++) {
      if (state.mask.data[r]) holeRects.push([ox + 4, oy + r * CELL + 4, cols * CELL - 8, CELL - 8]);
    }
  } else if (state.kind === "col") {
    for (let c = 0; c < cols; c++) {
      if (state.mask.data[c]) holeRects.push([ox + c * CELL + 4, oy + 4, CELL - 8, rows * CELL - 8]);
    }
  } else {
    for (let k = 0; k < open.length; k++) {
      if (open[k]) holeRects.push([ox + (k % cols) * CELL + 4, oy + Math.floor(k / cols) * CELL + 4, CELL - 8, CELL - 8]);
    }
  }
  const holes = holeRects.map(([x, y, hw, hh]) => `<rect x="${x}" y="${y}" width="${hw}" height="${hh}" rx="10" fill="black"/>`).join("");
  const rims = holeRects
    .map(([x, y, hw, hh]) => `<rect x="${x}" y="${y}" width="${hw}" height="${hh}" rx="10" fill="none" stroke="${BROWN_EDGE}" stroke-width="3"/>`)
    .join("");
  const rings = state.ops.length && state.stage === 2
    ? holeRects.map(([x, y, hw, hh]) => `<rect class="ring" x="${x - 2}" y="${y - 2}" width="${hw + 4}" height="${hh + 4}" rx="12"/>`).join("")
    : "";

  const board =
    `<defs><mask id="cut" maskUnits="userSpaceOnUse" x="0" y="0" width="${w}" height="${h}">` +
    `<rect width="${w}" height="${h}" fill="white"/>${holes}</mask></defs>` +
    `<rect class="bg" width="${w}" height="${h}" rx="16"/>${labels}${cells}`;

  const cardboard = covered
    ? `<g id="cardboard" class="cardboard" style="${animate ? `transform:translateY(${-(h + 40)}px);opacity:0` : "transform:translateY(0);opacity:1"}">` +
      `<g mask="url(#cut)"><rect x="${ox - 8}" y="${oy - 8}" width="${cols * CELL + 16}" height="${rows * CELL + 16}" rx="14" fill="${BROWN}" stroke="${BROWN_EDGE}" stroke-width="4"/></g>${rims}${rings}</g>`
    : "";

  el.board.setAttribute("viewBox", `0 0 ${w} ${h}`);
  el.board.setAttribute("width", w);
  el.board.setAttribute("height", h);
  el.board.innerHTML = board + cardboard;
  el.board.setAttribute(
    "aria-label",
    `Array A with ${rows} ${rows === 1 ? "row" : "rows"} and ${cols} columns. ` +
      (covered ? `Cardboard on top with ${holeRects.length} ${holeRects.length === 1 ? "hole" : "holes"}.` : "No cardboard yet."),
  );

  if (animate) {
    const g = $("#cardboard");
    requestAnimationFrame(() =>
      requestAnimationFrame(() => {
        g.style.transform = "translateY(0)";
        g.style.opacity = "1";
      }),
    );
  }
}

function renderToggles() {
  const rows = rowsOf(state.A);
  const cols = colsOf(state.A);
  el.toggles.innerHTML = "";
  let n;
  let cssCols;
  let name;
  if (state.kind === "row") {
    n = rows;
    cssCols = 1;
    name = (i) => `row ${i}`;
    el.togglesHint.textContent = "A row mask has one value per row. Press a row to switch it.";
  } else if (state.kind === "col") {
    n = cols;
    cssCols = cols;
    name = (i) => `column ${i}`;
    el.togglesHint.textContent = "A column mask has one value per column. Press a column to switch it.";
  } else {
    n = rows * cols;
    cssCols = cols;
    name = (i) => (rows > 1 ? `row ${Math.floor(i / cols)}, column ${i % cols}` : `position ${i}`);
    el.togglesHint.textContent = "Press any cell to switch it between True and False.";
  }
  el.toggles.style.gridTemplateColumns = `repeat(${cssCols}, minmax(0, 84px))`;
  for (let i = 0; i < n; i++) {
    const on = !!state.mask.data[i];
    const b = document.createElement("button");
    b.type = "button";
    b.className = `toggle${on ? " is-on" : ""}`;
    b.textContent = on ? "True" : "False";
    b.setAttribute("aria-pressed", String(on));
    b.setAttribute("aria-label", `Mask at ${name(i)}: ${on ? "True" : "False"}`);
    b.addEventListener("click", () => {
      toggle(i);
      const again = el.toggles.children[i];
      if (again) again.focus();
    });
    el.toggles.appendChild(b);
  }
}

function transcript() {
  const lines = [">>> A", fmt(state.original && state.ops.length === 0 && state.stage === 0 ? state.A : state.original)];
  if (state.stage >= 1 || state.ops.length) {
    lines.push(state.edited ? ">>> mask  # edited by hand" : `>>> mask = ${state.expr}`);
    lines.push(">>> mask", fmt(state.mask));
  }
  for (const op of state.ops) {
    lines.push(`>>> ${op.code}`);
    if (op.out) lines.push(op.out);
    if (op.after) lines.push(">>> A", op.after);
  }
  return lines.join("\n");
}

function render(animate) {
  const A = state.A;
  el.title.textContent = STEP_TITLES[state.stage];
  el.steps.forEach((li, i) => {
    li.classList.toggle("is-done", i < state.stage);
    if (i === state.stage) li.setAttribute("aria-current", "step");
    else li.removeAttribute("aria-current");
  });
  el.prev.disabled = state.stage === 0;
  el.next.disabled = state.stage === 2;
  el.select.textContent = selectCode();
  el.assign.textContent = `${selectCode()} = value`;

  svgBoard(animate);

  const open = state.mask.data.filter(Boolean).length;
  el.stats.innerHTML =
    `<b>Shape of A:</b> ${M.fmtShape(A.shape)} &nbsp;·&nbsp; <b>dtype:</b> ${A.dtype === "int" ? "int" : A.dtype === "float" ? "float" : "bool"}` +
    ` &nbsp;·&nbsp; <b>Mask:</b> ${describeKind(state.kind)}, ${open} True and ${state.mask.data.length - open} False`;

  renderToggles();
  el.readout.textContent = transcript();
  el.readout.scrollTop = el.readout.scrollHeight;
}

/* ------------------------------ wiring ------------------------------ */
PRESETS.forEach((p) => {
  const b = document.createElement("button");
  b.type = "button";
  b.className = `chip${p.pitfall ? " chip--pitfall" : ""}`;
  b.textContent = p.label;
  b.addEventListener("click", () => {
    el.expr.value = p.expr;
    load();
  });
  el.presets.appendChild(b);
});

el.load.addEventListener("click", load);
el.expr.addEventListener("keydown", (e) => {
  if (e.key === "Enter") load();
});
el.prev.addEventListener("click", () => go(-1));
el.next.addEventListener("click", () => go(1));
el.select.addEventListener("click", readThrough);
el.assign.addEventListener("click", writeThrough);
el.reset.addEventListener("click", resetArray);

/* ---------------- Light / dark theme (same as the other labs) ---------------- */
const themeToggle = $("#theme-toggle");
const ICONS = {
  moon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>',
  sun: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
};

function syncThemeToggle() {
  const dark = document.documentElement.dataset.theme === "dark";
  const next = dark ? "light" : "dark";
  themeToggle.innerHTML = dark ? ICONS.sun : ICONS.moon;
  themeToggle.setAttribute("aria-label", `Switch to ${next} theme`);
  themeToggle.title = `Switch to ${next} theme`;
}

themeToggle.addEventListener("click", () => {
  const dark = document.documentElement.dataset.theme !== "dark";
  document.documentElement.dataset.theme = dark ? "dark" : "light";
  try {
    localStorage.setItem("quarto-color-scheme", dark ? "alternate" : "default");
  } catch (e) {
    /* private mode: the choice just isn't remembered */
  }
  syncThemeToggle();
});

syncThemeToggle();
load();
setMessage("");
