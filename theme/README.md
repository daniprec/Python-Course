# Course theme (IE University)

The site uses the IE School of Science & Technology palette (design.ie.edu, Brand basics > Colors) and IE's fonts, with a light and a dark mode.
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

The variable names (`ie-oceanblue`, `ie-seablue`, ...) are kept from the old blue theme so that
existing pages keep working; the values are the Scitech colours.

| Variable | Hex | Scitech name | Used for |
|---|---|---|---|
| `ie-oceanblue`, `ie-electricblue` | `#1F3700` | Green Olive | Headings, links, primary buttons (light) |
| `ie-seablue` | `#6DC201` (light), `#D8FFA5` text on dark | Tech Green / light green | Accents and rules. **Never as text on white** |
| `ie-lightblue` | `#D8FFA5` | Light green | Surfaces, headings and links in dark mode |
| `ie-iceblue` | `#EFEFEF` | Grey | Soft surfaces, inline code background |
| `ie-techblack` | `#000024` | Tech Black | Text colour on light surfaces, dark-mode background |
| Tech Green | `#6DC201` | | "Stay", tips, wins (fills only on white) |
| VIG Red | `#E2000F` | | Doors, "important" callouts |

Text/background pairs keep the 4.5:1 WCAG 2.1 AA contrast in both modes.

## Rule of thumb

Change a colour in the palette (`ie-*.scss` defaults / `ie-tokens.css`),
not in components. Components only read the semantic `--ie-*` variables.
