#!/usr/bin/env python3
"""Build one PDF per module from the rendered Quarto site (``_site``).

Run ``quarto render`` first, then::

    python tools/build_module_pdfs.py                 # all modules -> pdf/
    python tools/build_module_pdfs.py --modules 3     # only Module 3
    python tools/build_module_pdfs.py --no-side-projects

What it does
------------
* Reads the sidebar of ``_quarto.yml`` to know which pages belong to each module
  and in which order (module index, lessons, homework, optionally side projects).
* Merges the rendered HTML pages of a module into a single document: a cover with a
  table of contents (with page numbers), then each page starting on a new sheet.
* Opens every collapsed callout ("Solution" dropdowns) and every ``<details>``.
* Adds print rules so that pages do not break in awkward places (see PRINT_CSS and
  the measuring step in ``PREPARE_JS``).
* Prints with headless Chromium (Playwright), adds PDF bookmarks with pypdf.

Requirements: ``pip install playwright pypdf beautifulsoup4 lxml pyyaml`` and
``playwright install chromium``.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

import yaml
from bs4 import BeautifulSoup
from pypdf import PdfReader, PdfWriter

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"
SITE_URL = "https://daniprec.github.io/Python-Course/"
COURSE = "Computer Programming I (Python)"

PRINT_CSS = r"""
@page { size: A4; margin: 20mm 16mm 18mm 16mm; }
html { font-size: 13px; }
body { background: #fff !important; }
* { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
#quarto-document-content { max-width: none !important; margin: 0 !important; padding: 0 !important; }

/* Every page of the site starts on a new sheet */
.pdf-lesson { break-before: page; }
.pdf-cover { break-after: page; }
.pdf-lesson > header#title-block-header { margin-bottom: 1.2rem; }
.pdf-marker { position: absolute; color: #fff; font-size: 1px; line-height: 1px; }

/* Things that only make sense on screen */
.quarto-title-breadcrumbs, .quarto-code-tools, .code-copy-button, .code-tools-button,
.callout-btn-toggle, .quarto-alternate-formats, .page-navigation, .nav-footer,
.hw-filter, .no-pdf, .anchorjs-link, .quarto-title-meta:empty { display: none !important; }
a { color: inherit; text-decoration: none; }
#quarto-document-content a[href] { text-decoration: underline; text-decoration-color: rgba(0,0,0,.35); }

/* ---- Where pages may (not) break ---------------------------------------- */
h1, h2, h3, h4, h5, h6 { break-after: avoid; break-inside: avoid; }
p, li { orphans: 3; widows: 3; }
/* a lead-in sentence stays with what it introduces */
p:has(+ .cell), p:has(+ div.sourceCode), p:has(+ pre), p:has(+ .callout),
p:has(+ figure), p:has(+ table), p:has(+ ul), p:has(+ ol), p:has(+ .math.display) { break-after: avoid; }
div.sourceCode, pre, figure, img, table, .cell-output, .cell-output-display,
blockquote, .math.display { break-inside: avoid; }
tr { break-inside: avoid; }
details, details > summary { break-inside: avoid; }
details > summary { break-after: avoid; }
thead { display: table-header-group; }
img { max-width: 100%; max-height: 235mm; object-fit: contain; }
/* long lines wrap instead of being cut off */
pre, pre code, div.sourceCode pre { white-space: pre-wrap !important; word-break: break-word; overflow: visible !important; }
/* JS adds these after measuring (see PREPARE_JS) */
.keep-together { break-inside: avoid; }
.keep-with-next { break-after: avoid; }
.callout-collapse { height: auto !important; }
.callout-body-container, .callout-body { overflow: visible !important; }
.callout { margin-top: 0.4rem; margin-bottom: 0.9rem; }

/* ---- Cover and table of contents ---------------------------------------- */
.pdf-cover h1.pdf-title { font-size: 2.3rem; font-weight: 700; margin: 0 0 .3rem; border: 0; }
.pdf-cover .pdf-course { font-size: 1.1rem; margin: 0; opacity: .8; }
.pdf-cover .pdf-date { font-size: .85rem; margin: .2rem 0 2rem; opacity: .65; }
.pdf-toc { list-style: none; padding: 0; margin: 0; }
.pdf-toc li { display: flex; align-items: baseline; gap: .5rem; padding: .22rem 0; break-inside: avoid; }
.pdf-toc li .dots { flex: 1; border-bottom: 1px dotted #888; transform: translateY(-.2em); }
.pdf-toc li .pg { min-width: 2.2em; text-align: right; font-variant-numeric: tabular-nums; }
.pdf-toc li.part { font-weight: 700; margin-top: .8rem; }
.pdf-toc a { text-decoration: none !important; }
"""

# Runs in the browser, in print layout, right before printing.
PREPARE_JS = r"""
() => {
  const PAGE_H = 259 / 25.4 * 96;           // usable height of a sheet in CSS px
  const main = document.getElementById("quarto-document-content");

  // 1. Keep a callout in one piece when it is smaller than most of a sheet.
  main.querySelectorAll(".callout").forEach(c => {
    if (c.closest(".callout") !== c) return;
    if (c.getBoundingClientRect().height < PAGE_H * 0.8) c.classList.add("keep-together");
  });

  // 2. Keep an exercise (blue box) with its solution (collapsed box) when the pair fits a sheet.
  main.querySelectorAll(".callout-note").forEach(q => {
    const s = q.nextElementSibling;
    if (!s || !s.classList.contains("callout-tip")) return;
    const h = s.getBoundingClientRect().bottom - q.getBoundingClientRect().top;
    if (h < PAGE_H * 0.85) q.classList.add("keep-with-next");
  });
  return main.querySelectorAll(".callout").length;
}
"""


def sidebar_modules(cfg: dict) -> list[dict]:
    """Return [{'title', 'pages': [(href, title, is_side_project)]}] for each module."""
    contents = cfg["website"]["sidebar"]["contents"]
    modules = []
    for sec in contents:
        title = sec.get("section", "")
        if not title.startswith("Module"):
            continue
        pages: list[tuple[str, str, bool]] = []
        if sec.get("href"):
            pages.append((sec["href"], "Overview", False))

        def walk(items, side=False):
            for it in items:
                if "section" in it:
                    is_side = side or "side project" in it["section"].lower()
                    if it.get("href"):
                        pages.append((it["href"], it["section"], is_side))
                    walk(it.get("contents", []), is_side)
                else:
                    pages.append((it["href"], it["text"], side))

        walk(sec.get("contents", []))
        modules.append({"title": title, "pages": pages})
    return modules


def slug(href: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "-", Path(href).with_suffix("").as_posix()).strip("-")


def load_page(href: str):
    path = SITE / Path(href).with_suffix(".html")
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "lxml")
    return path, soup


def clean_lesson(soup: BeautifulSoup, path: Path, prefix: str, known: dict[str, str]) -> BeautifulSoup:
    """Take <main> of a rendered page and make it printable and self-contained."""
    main = soup.select_one("main#quarto-document-content")
    for sel in ["script", ".quarto-title-breadcrumbs", ".quarto-code-tools", ".code-copy-button",
                ".quarto-alternate-formats", "nav.page-navigation", ".hw-filter"]:
        for el in main.select(sel):
            el.decompose()

    # Open every collapsed callout
    for body in main.select(".callout-collapse"):
        body["class"] = [c for c in body.get("class", []) if c != "collapse"] + ["show"]
    for head in main.select(".callout-header"):
        for attr in ("data-bs-toggle", "data-bs-target", "aria-controls", "aria-expanded", "aria-label"):
            head.attrs.pop(attr, None)
        head["class"] = [c for c in head.get("class", []) if c != "collapsed"]
    for toggle in main.select(".callout-btn-toggle"):
        toggle.decompose()
    # Open every <details> (code-fold and friends)
    for det in main.select("details"):
        det["open"] = ""

    # Make ids unique across the merged document and re-point in-page links
    for el in main.select("[id]"):
        el["id"] = f"{prefix}-{el['id']}"
    for a in main.select("a[href]"):
        href = a["href"]
        if href.startswith("#"):
            a["href"] = f"#{prefix}-{href[1:]}"
        elif not re.match(r"^[a-z]+:", href):  # relative link to another page
            target = (path.parent / urlparse(href).path).resolve()
            frag = urlparse(href).fragment
            try:
                rel = target.relative_to(SITE.resolve()).as_posix()
            except ValueError:
                continue
            if rel in known:
                a["href"] = f"#{known[rel]}" + (f"-{frag}" if frag else "")
            else:
                a["href"] = SITE_URL + rel + (f"#{frag}" if frag else "")
    return main


def build_module_html(mod: dict, include_side: bool, out_html: Path, page_numbers: dict[str, int] | None):
    pages = [p for p in mod["pages"] if include_side or not p[2]]
    # skip duplicated hrefs and files that do not exist
    seen, keep = set(), []
    for href, title, side in pages:
        f = SITE / Path(href).with_suffix(".html")
        if href in seen or not f.exists():
            continue
        seen.add(href)
        keep.append((href, title, side))

    known = {Path(h).with_suffix(".html").as_posix(): f"pg-{slug(h)}" for h, _, _ in keep}
    known = {k: v for k, v in known.items()}
    # keys in `known` are relative to _site, like "modules/numpy/arithmetics.html"
    lessons, head_soup = [], None
    for href, title, side in keep:
        path, soup = load_page(href)
        if head_soup is None:
            head_soup = soup
        rel = Path(href).with_suffix(".html").as_posix()
        main = clean_lesson(soup, path, known[rel], known)
        real_title = soup.select_one("h1.title")
        lessons.append({
            "href": href,
            "id": known[rel],
            "title": real_title.get_text(" ", strip=True) if real_title else title,
            "side": side,
            "main": main,
        })

    # ---- <head>: keep only the light theme + MathJax -----------------------------------
    head = head_soup.head
    for el in list(head.find_all(["script", "link"])):
        if el.name == "script":
            if "mathjax" not in (el.get("src") or "").lower():
                el.decompose()
        else:
            rel_attr = " ".join(el.get("rel", []))
            if el.get("data-mode") == "dark" or "quarto-color-alternate" in el.get("class", []) or rel_attr in ("prefetch", "preconnect"):
                el.decompose()
    for el in head.find_all("meta"):
        if el.get("name") in ("quarto:offset",):
            el.decompose()
    # MathJax is always needed: the first page of a module may have no formulas itself
    mj = head_soup.new_tag("script", src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml-full.js")
    head.append(mj)
    style = head_soup.new_tag("style")
    style.string = PRINT_CSS
    head.append(style)
    title_tag = head.find("title")
    if title_tag:
        title_tag.string = f"{mod['title']} – {COURSE}"

    # ---- cover + TOC -----------------------------------------------------------------
    today = dt.date.today().strftime("%d %B %Y")
    toc_items, last_part = [], None
    for l in lessons:
        part = "Side Projects" if l["side"] else None
        if part and part != last_part and l["title"] != "Side Projects":
            toc_items.append('<li class="part"><span>Side Projects</span></li>')
        last_part = part
        if l["title"] == "Side Projects":
            toc_items.append(
                f'<li class="part"><a href="#{l["id"]}">Side Projects</a><span class="dots"></span>'
                f'<span class="pg">{(page_numbers or {}).get(l["id"]) or "00"}</span></li>'
            )
            continue
        pg = (page_numbers or {}).get(l["id"])
        toc_items.append(
            f'<li><a href="#{l["id"]}">{html.escape(l["title"])}</a><span class="dots"></span>'
            f'<span class="pg">{pg if pg else "00"}</span></li>'
        )
    cover = f"""
<section class="pdf-cover">
  <h1 class="pdf-title">{html.escape(mod['title'])}</h1>
  <p class="pdf-course">{COURSE}</p>
  <p class="pdf-date">Generated on {today} · {SITE_URL}</p>
  <h2>Contents</h2>
  <ol class="pdf-toc">{''.join(toc_items)}</ol>
</section>"""

    body_parts = []
    for l in lessons:
        inner = l["main"].decode_contents()
        body_parts.append(
            f'<section class="pdf-lesson" id="{l["id"]}"><span class="pdf-marker">zzpg-{l["id"]}-zz</span>{inner}</section>'
        )

    doc = (
        "<!DOCTYPE html>\n<html lang=\"en\">" + str(head) +
        '<body class="quarto-light fullcontent"><main class="content" id="quarto-document-content">'
        + cover + "".join(body_parts) + "</main></body></html>"
    )
    out_html.write_text(doc, encoding="utf-8")
    return lessons


def print_pdf(html_path: Path, pdf_path: Path, header_title: str):
    from playwright.sync_api import sync_playwright

    header = (
        '<div style="width:100%;font-size:8px;font-family:Montserrat,Arial,sans-serif;color:#555;'
        'padding:0 16mm;display:flex;justify-content:space-between;">'
        f'<span>{html.escape(header_title)}</span><span>{html.escape(COURSE)}</span></div>'
    )
    footer = (
        '<div style="width:100%;font-size:8px;font-family:Montserrat,Arial,sans-serif;color:#555;'
        'padding:0 16mm;text-align:center;"><span class="pageNumber"></span> / <span class="totalPages"></span></div>'
    )
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 673, "height": 1000})  # 178 mm text width
        page.emulate_media(media="print")
        page.goto(html_path.as_uri(), wait_until="networkidle", timeout=120_000)
        page.evaluate("document.fonts.ready")
        page.evaluate("window.MathJax && MathJax.startup ? MathJax.startup.promise : null")
        page.wait_for_timeout(500)
        # make sure lazy images are loaded
        page.evaluate("Array.from(document.images).forEach(i => i.loading = 'eager')")
        page.evaluate("Promise.all(Array.from(document.images).map(i => i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; })))")
        n = page.evaluate(PREPARE_JS)
        print(f"   {n} callouts prepared")
        page.pdf(
            path=str(pdf_path), format="A4", print_background=True, prefer_css_page_size=True,
            display_header_footer=True, header_template=header, footer_template=footer,
            margin={"top": "20mm", "bottom": "18mm", "left": "16mm", "right": "16mm"},
            tagged=True,
        )
        browser.close()


def find_page_numbers(pdf_path: Path, lessons: list[dict]) -> dict[str, int]:
    reader = PdfReader(str(pdf_path))
    found: dict[str, int] = {}
    for i, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        for l in lessons:
            if l["id"] not in found and f"zzpg-{l['id']}-zz" in text.replace(" ", "").replace("\n", ""):
                found[l["id"]] = i
    return found


def add_bookmarks(pdf_path: Path, lessons: list[dict], numbers: dict[str, int], title: str):
    reader = PdfReader(str(pdf_path))
    writer = PdfWriter(clone_from=reader)
    writer.add_outline_item("Contents", 0)
    side_parent = None
    for l in lessons:
        if l["id"] not in numbers:
            continue
        if l["title"] == "Side Projects":
            side_parent = writer.add_outline_item("Side Projects", numbers[l["id"]] - 1)
            continue
        if l["side"] and side_parent is None:
            side_parent = writer.add_outline_item("Side Projects", numbers[l["id"]] - 1)
        writer.add_outline_item(l["title"], numbers[l["id"]] - 1, parent=side_parent if l["side"] else None)
    writer.add_metadata({"/Title": f"{title} – {COURSE}", "/Author": "IE University", "/Subject": COURSE})
    writer.page_mode = "/UseOutlines"
    with open(pdf_path, "wb") as fh:
        writer.write(fh)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--modules", nargs="*", type=int, help="module numbers to build (default: all)")
    ap.add_argument("--no-side-projects", action="store_true", help="leave the Side Projects out")
    ap.add_argument("--out", default=str(ROOT / "pdf"), help="output folder")
    args = ap.parse_args()

    cfg = yaml.safe_load((ROOT / "_quarto.yml").read_text(encoding="utf-8"))
    modules = sidebar_modules(cfg)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    for idx, mod in enumerate(modules, start=1):
        if args.modules and idx not in args.modules:
            continue
        name = re.sub(r"[^a-z0-9]+", "_", mod["title"].lower()).strip("_")
        print(f"== {mod['title']}")
        first_dir = SITE / Path(mod["pages"][0][0]).parent
        tmp_html = first_dir / f"_pdf_{name}.html"  # same folder as the pages: relative paths keep working
        pdf_path = out_dir / f"{name}.pdf"
        try:
            lessons = build_module_html(mod, not args.no_side_projects, tmp_html, None)
            print_pdf(tmp_html, pdf_path, mod["title"])                      # pass 1: find page numbers
            numbers = find_page_numbers(pdf_path, lessons)
            build_module_html(mod, not args.no_side_projects, tmp_html, numbers)
            print_pdf(tmp_html, pdf_path, mod["title"])                      # pass 2: TOC with numbers
            numbers2 = find_page_numbers(pdf_path, lessons)
            if numbers2 != numbers:
                print("   page numbers moved between passes, rebuilding once more")
                build_module_html(mod, not args.no_side_projects, tmp_html, numbers2)
                print_pdf(tmp_html, pdf_path, mod["title"])
                numbers = find_page_numbers(pdf_path, lessons)
            add_bookmarks(pdf_path, lessons, numbers, mod["title"])
            print(f"   {len(PdfReader(str(pdf_path)).pages)} pages -> {pdf_path}")
        finally:
            tmp_html.unlink(missing_ok=True)


if __name__ == "__main__":
    sys.exit(main())
