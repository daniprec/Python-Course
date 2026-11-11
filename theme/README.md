# Course theme (IE University)

The site uses IE's official colours and fonts, with a light and a dark mode.
Readers switch with the toggle at the top of the sidebar; the choice is
remembered and shared with the interactive pages (e.g. the Monty Hall simulator).

| File | What it holds |
|---|---|
| `ie-light.scss` | Light theme: IE palette → Bootstrap/Quarto variables + `--ie-*` CSS variables |
| `ie-dark.scss`  | Dark theme: same structure, Tech Black background, Sea Blue accents |
| `ie.css`        | Shared component rules (fonts, headings, sidebar, buttons, focus). Uses only `--ie-*` variables |
| `ie-tokens.css` | Raw palette as CSS variables, for standalone HTML pages (Monty Hall) |
| `fonts.html`    | Google Fonts include: Montserrat (UI/headings), PT Serif (reading text), JetBrains Mono (code) |

## Palette

| Name | Hex | Used for |
|---|---|---|
| IE Ocean Blue | `#000066` | Headings, primary buttons (light) |
| IE Electric Blue | `#0000DB` | Links, "Switch" (light) |
| IE Sea Blue | `#47BFFF` | Accents; headings and buttons in dark mode. **Never as text on white** (2.1:1) |
| Tech Green | `#6DC201` | "Stay", tips, wins (fills only on white) |
| Tech Green (New) | `#1F3700` | Green text on light backgrounds |
| Tech Black | `#000024` | Dark-mode background |
| VIG Red | `#E2000F` | Doors, "important" callouts |

All text/background pairs pass WCAG 2.1 AA (4.5:1) in both modes.

## Rule of thumb

Change a colour in the palette (`ie-*.scss` defaults / `ie-tokens.css`),
not in components. Components only read the semantic `--ie-*` variables.
