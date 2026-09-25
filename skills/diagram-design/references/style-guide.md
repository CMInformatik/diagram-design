# Style Guide

**The single source of truth for colors, typography, and tokens.** Every diagram draws from this — not from hex values inlined in other reference files. If you want to change the visual skin of Diagram Design, change this file.

Active skin: **CMI** (profile `cmi`) — near-white paper, Dunkelblau ink, CMI-Cyan accent, Petrol link, Arial labels. The shipped default is a cool editorial palette — white-smoke paper, jet-black ink, atomic-tangerine accent, blue-slate muted. It's designed to look good out of the box; swap these values (or run [`onboarding.md`](onboarding.md)) and every new diagram inherits the new skin without touching any type-specific logic.

To generate your own from a website URL, see [`onboarding.md`](onboarding.md).

---

## Tokens

### Semantic roles

Every token is referred to by **semantic role**, not by its hex value. Type references (`type-*.md`) and SKILL.md say `accent`, not `#f7591f`.

| Role | Purpose | Default (light) | Default (dark) |
|---|---|---|---|
| `paper` | Page background, default node fill | `#f7f9fa` (near-white, derived from CMI Weiss) | `#1d3849` (CMI Dunkelblau) |
| `paper-2` | Diagram container bg, secondary fill | `#ebebed` (CMI Hellgrau) | `#24455a` |
| `ink` | Primary text, primary stroke | `#1d3849` (CMI Dunkelblau) | `#f7f9fa` |
| `ink-strong` | High-contrast text on accent fills | `#000000` (CMI Schwarz) | `#000000` |
| `muted` | Secondary text, default arrow stroke | `#4a6272` (Dunkelblau, lighter) | `#b7c4ce` |
| `soft` | Sublabels, boundary labels | `#7a8e9b` | `#8da0ad` |
| `rule` | Hairline borders | `rgba(29,56,73,0.12)` | `rgba(247,249,250,0.12)` |
| `rule-solid` | Stronger borders, baselines | `#b7c4ce` | `rgba(183,196,206,0.25)` |
| `accent` | Focal / 1–2 max per diagram | `#009fe3` (CMI-Cyan) | `#33b5ec` |
| `accent-tint` | Fill for accent-bordered boxes | `#dff2fd` (CMI Hellblau) | `rgba(51,181,236,0.12)` |
| `link` | HTTP/API calls, external arrows | `#1a808c` (CMI Petrol) | `#4fb3be` |

> **Brand palette source:** CMI Brandbook via the installed skill `allgemein:cmi-ci-dokumente` (references/ci-guidelines.md). Brand colours used directly: CMI-Cyan `#009FE3` (accent), Dunkelblau `#1D3849` (ink / dark paper), Hellblau `#DFF2FD` (accent-tint), Hellgrau `#EBEBED` (paper-2), Schwarz `#000000` (ink-strong), Petrol `#1A808C` (link). Derived: `paper` light is a near-white instead of brand Weiss `#FFFFFF` (pure white is discouraged by this skill); `muted`, `soft`, `rule`, `rule-solid` and all dark-mode values are Dunkelblau tints. Not used: Violett `#8168B7` (tertiary), KI+ colours (product-brand only). **CMI-Cyan fails AA as text on light paper (2.97:1)** — use it for strokes, fills and markers only, never for text; text on accent fills uses `ink-strong`.

> **Note:** The pre-baked example HTML files in `assets/` were built under an earlier skin. Regenerating them against the current `style-guide.md` is a v5.1 task. New diagrams the skill produces will use the tokens above.

### Inversion rule (light → dark)

Any `rgba(29,56,73, X)` in light becomes `rgba(247,249,250, X)` in dark. Same opacities, RGB flipped. Dark paper is CMI Dunkelblau itself; the accent brightens to `#33b5ec` to reach AA on it.

### Series palette (multi-series chart types only)

A small set of desaturated, editorial-tone colors for chart types that genuinely need to distinguish multiple overlapping entities (currently: **radar**). The "1-focal" rule still holds — `accent` is reserved for the focal series; the palette below covers the rest.

| Token | Light | Dark | Notes |
|---|---|---|---|
| `series-1` | `#7c8f6f` (sage) | `#9caf8f` | Non-focal series |
| `series-2` | `#5e7a9b` (dusty-blue) | `#82a0c0` | Non-focal series |
| `series-3` | `#b8915a` (mustard) | `#d3ad7a` | Non-focal series |
| `series-4` | `#9c6b50` (rust-brown) | `#b88670` | Non-focal series |
| `series-5` | `#6e6479` (slate) | `#8d8298` | Non-focal series |

Fills sit at `0.18` opacity light, `0.22` dark; strokes use the full color. **Don't backfill these tokens to non-chart types** — architecture, swimlane, etc. continue to use muted-ink variants. The series palette is opt-in for diagrams where overlapping shapes demand distinguishable color, not a license to add color elsewhere.

### Terminal skin (opt-in alternate)

A self-contained palette for the terminal-window primitive (see [primitive-terminal.md](primitive-terminal.md)) — a CLI-chrome register for dev-tool posts and technical social cards. It does not replace the default skin above and isn't affected by onboarding; it's a second, fixed skin you opt into per-diagram.

| Token | Hex | Purpose |
|---|---|---|
| `terminal-page` | `#0a0a0a` | Page background behind the window |
| `terminal-paper` | `#141414` | Window body, node fill |
| `terminal-bar` | `#1b1b1b` | Titlebar strip |
| `terminal-border` | `#2b2b2b` | Window border, hairlines |
| `terminal-ink` | `#f5f5f5` | Primary text, primary stroke (same white-smoke as default `ink`) |
| `terminal-muted` | `#9a9a9a` | Secondary text, sublabels, ring stroke |
| `terminal-soft` | `#5c5c5c` | Tertiary — inactive dots, spokes |
| `terminal-accent` | `#ff5a36` | The one accent — focal station, prompt sign, active dot |
| `terminal-accent-tint` | `rgba(255,90,54,0.12)` | Fill for accent-bordered boxes |

**1-accent rule still holds.** Everything that isn't `terminal-ink` or `terminal-muted`/`terminal-soft` should be `terminal-accent` — never introduce a second hue.

---

## Typography

| Role | Family | Size | Weight | Usage |
|---|---|---|---|---|
| `title` | Arial (fallback for Gravur LL Condensed Black, custom-hosted) | 1.75rem | 700 | Page H1 |
| `node-name` | Arial (CMI Office font; system stack) | 12px | 700 | Human-readable labels |
| `sublabel` | Roboto Mono | 9px | 400 | Port, protocol, URL, field type |
| `eyebrow` | Roboto Mono | 7–8px | 500, tracked 0.18em, uppercase | Type tags, axis labels |
| `arrow-label` | Roboto Mono | 8px | 400, tracked 0.06em | Arrow annotations |
| `callout` | Arial *italic* | 14px | 400 | Editorial asides only |

### Font stack

CMI brand fonts: Gravur LL Condensed Black and Helvetica Neue (print/web) are licensed, custom-hosted and not on Google Fonts, so they are not used. Every text role (`title`, `node-name`, `callout`, plain labels) uses Arial, the CMI Office font, with the stack `'Arial', 'Arimo', 'Helvetica Neue', Helvetica, sans-serif`. Arial is installed on Windows and macOS; Arimo is the free, metric-compatible Google font that takes over where Arial is missing (Linux, CI, headless export). The brand defines no monospace face, so technical values (`sublabel`, `eyebrow`, `arrow-label`) use Roboto Mono (Google Fonts, Apache 2.0). Deliberate deviation from the upstream rule «keep a serif for title»: the CMI Brandbook allows only Arial in Office output, so there is no serif; the title uses Arial 700.

```html
<link href="https://fonts.googleapis.com/css2?family=Arimo:ital,wght@0,400;0,700;1,400&family=Roboto+Mono:wght@400;500;600&family=Noto+Serif:ital@0;1&family=Noto+Sans+KR:wght@400;500;600&family=Noto+Serif+KR:wght@400&family=Noto+Sans+TC:wght@400;500;600&family=Noto+Serif+TC:wght@400&display=swap" rel="stylesheet">
```

### Korean labels

Arial and Arimo carry no Hangul. A Korean `<text>` element extends its own family — never swap the skin:

```svg
<text font-family="'Arial', 'Arimo', 'Noto Sans KR', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif">결제 서비스</text>
```

Both Noto faces ship in the font link above, so the web font resolves before any locally installed one and the same file renders identically on macOS, Windows, and a reviewer's browser. The local families follow it for offline viewing. Page titles need the serif equivalent — `'Arial', 'Arimo', 'Noto Serif KR', serif` — or a mixed Latin/Korean title resolves Hangul through the platform's generic serif and the two halves disagree. Google's `css2` endpoint slices Korean by unicode-range, so a diagram with a handful of Korean labels downloads only the slices it touches. The four templates carry both faces because a new diagram may contain Hangul; the shipped Latin-only examples keep the shorter link, since a file with no Hangul has nothing to resolve.

**Width budget.** Measure per character, not per script: **every Unicode wide or full-width character costs 1em, every other character costs its face's Latin advance** (0.60em sans, 0.62em mono), and nonspacing/enclosing marks cost nothing. Sum over the string and multiply by the font size for the text width, then add padding and round the box up to the next multiple of 4. `verify-treemap.py` enforces exactly this text width for treemap cell labels; the padding and rounding are authoring convention, and no other type carries an automatic check, so on those the budget is yours to hold.

Counting by script is the trap. `주문 v2.1` is two full-width syllables and five narrow characters; a formula that tallies Hangul, Latin letters, and spaces silently drops `2`, `.`, and `1` and sizes the box for four of its seven characters. Every rendered character costs something — measure per character, never per script.

Three rules follow from Hangul metrics:

- **Sublabels stay Latin.** Ports, protocols, field types, and URLs are Latin anyway — keep `Roboto Mono` there and don't translate them. Hangul in a 9px mono sublabel is unreadable and has no mono face to fall back to.
- **Floor of 12px.** Hangul goes muddy below 12px. If a Korean name doesn't fit at 12px, cut the name — don't shrink the type.
- **Arrow labels, eyebrows, and legend text switch register.** Those slots are 7–8px Roboto Mono, uppercase and tracked, which Hangul has neither a face nor legibility for. A Korean label in one of those slots becomes 12px sans at weight 500 with no tracking and no uppercase transform, and its mask rect grows to match (16px tall, width from the budget above, still rounded to a multiple of 4). Latin labels in the same diagram keep the mono treatment.

**Load-bearing rule:** Mono is for *technical* content (ports, commands, URLs, field types). Names go in Arial. Page title is Arial. Italic Arial is reserved for annotation callouts (see [primitive-annotation.md](primitive-annotation.md)). **Never JetBrains Mono** as a blanket "dev" font.

### Traditional Chinese labels

Arial and Arimo carry no Han. A Traditional Chinese `<text>` element extends its own family — never swap the skin:

```svg
<text font-family="'Arial', 'Arimo', 'Noto Sans TC', 'PingFang TC', 'Microsoft JhengHei', sans-serif">請求項比對</text>
```

Both Noto TC faces ship in the font link above, so the web font resolves before any locally installed one and the same file renders identically on macOS, Windows, and a reviewer's browser. The local families follow it for offline viewing. Page titles need the serif equivalent — `'Arial', 'Arimo', 'Noto Serif TC', serif` — or a mixed Latin/Han title resolves Han through the platform's generic serif and the two halves disagree. Google's `css2` endpoint slices Chinese by unicode-range, so a diagram with a handful of Chinese labels downloads only the slices it touches.

**Width budget.** The per-character contract above is unchanged: every Unicode wide or full-width character costs 1em, every other character costs its face's Latin advance, and nonspacing marks cost nothing. Full-width punctuation — `（）「」，。：` — is wide and costs 1em as well, which is the part most often dropped.

Counting by script is the trap. `請求項 v2.1` is three full-width characters and five narrow ones; a formula that tallies Han and Latin letters silently drops `2`, `.`, and `1` and sizes the box for six of its nine characters.

Three rules follow from Han metrics, mirroring the Hangul ones:

- **Sublabels stay Latin.** Ports, protocols, field types, and URLs are Latin anyway — keep `Roboto Mono` there and don't translate them. Han in a 9px mono sublabel is unreadable and has no mono face to fall back to. A sublabel that is prose rather than a value may be Chinese, but it then switches register by the third rule below.
- **Floor of 12px.** Han packs more strokes than Hangul into the same em box, so the 12px floor binds at least as hard here. If a Chinese name doesn't fit at 12px, cut the name — don't shrink the type.
- **Arrow labels, eyebrows, and legend text switch register.** Those slots are 7–8px Roboto Mono, uppercase and tracked, which Han has neither a face nor legibility for. A Chinese label in one of those slots becomes 12px sans at weight 500 with no tracking and no uppercase transform, and its mask rect grows to match (16px tall, width from the budget above, still rounded to a multiple of 4). Latin labels in the same diagram keep the mono treatment.

Simplified Chinese takes the same three rules with the Simplified stack (`'Noto Sans SC'`, `'PingFang SC'`, `'Microsoft YaHei'`). That face does not ship in the link, so Simplified labels still resolve through whatever the viewer has locally.

### Cyrillic labels

Arial and Roboto Mono ship Cyrillic (`cyrillic` and `cyrillic-ext` on Google Fonts), so names, sublabels, arrow labels, eyebrows, and legend text in Bulgarian, Russian, Ukrainian, or Serbian keep the Latin treatment: same faces, sizes, tracking, and uppercase. There is no register switch: Hangul and Han switch register because Roboto Mono has no face for them, and Roboto Mono does cover Cyrillic.

Arial and Arimo cover Cyrillic, so a page title keeps its stack `'Arial', 'Arimo', sans-serif`; do not extend it with a serif, or a mixed Latin/Cyrillic title resolves Cyrillic through whatever face comes next and the two halves disagree. Noto Serif ships in the font link above, upright and italic, so an italic callout in Cyrillic takes the same stack.

**Noto Serif goes ahead of the CJK serifs.** When a stack also lists `'Noto Serif KR'` or `'Noto Serif TC'`, put `'Noto Serif'` ahead of them. Google Fonts slices Cyrillic into those faces as well, so a stack that reaches a CJK face first draws its Cyrillic from it. That is why the templates put `'Noto Serif'` between `'Arial', 'Arimo'` and `'Noto Serif KR'`; Noto Serif has no Hangul or Han, so Korean and Chinese titles pass straight through it.

**Width budget.** The per-character contract above is unchanged: every character costs its face's Latin advance (0.60em sans, 0.62em mono). It fits Roboto Mono exactly and Arial only on average. Roboto Mono is monospaced: a Cyrillic glyph advances exactly as far as a Latin one, so sublabels, arrow labels, eyebrows, legend text, and their mask rects are sized as for Latin. Arial is not. Its wide Cyrillic letters, capitals and lowercase alike (such as `Ж Ш Щ Ю Ы`, `ж ш щ ы ю`), run well past the 0.60em average: `Шкаф ODF-2` at 12px is budgeted at 72px and draws at about 76. Rounding the box up to a multiple of 4 recovers at most 3px, so it is not the remedy. Leave the overshoot in the box padding and measure a Cyrillic sans name in the browser — `verify-treemap.py` holds the budget, not the drawn width, so it will not catch the overshoot.

Counting by script is still the trap. `Шкаф ODF-2` is four Cyrillic letters, a space, three Latin letters, a hyphen, and a digit; a formula that tallies Cyrillic letters, Latin letters, and spaces silently drops `-` and `2` and sizes the box for eight of its ten characters.

**Preserve printed labels.** A label the reader matches against a physical thing — a cabinet, a splice closure, a port map — carries the exact printed string. Don't transliterate it and don't re-case it; if one has to sit in an uppercase slot such as an eyebrow, drop the transform for that label rather than re-case the printed string. `Шкаф ODF-2` stays `Шкаф ODF-2`, not `Shkaf ODF-2`.

---

## Stroke, radius, spacing

| Token | Value | Use |
|---|---|---|
| `stroke-thin` | `0.8` | Tag-box outlines, leaf nodes |
| `stroke-default` | `1` | Most strokes |
| `stroke-strong` | `1.2` | Emphasis strokes |
| `radius-sm` | `4` | Small tags |
| `radius-md` | `6` | Node boxes |
| `radius-lg` | `8` | Containers, rings |
| `grid` | `4` | Every coord, size, and gap is divisible by 4 (hard rule) |

---

## Node type → treatment

Semantic role combinations — reference these by name in type specs.

| Type | Fill | Stroke |
|---|---|---|
| `focal` (1–2 max) | `accent-tint` | `accent` |
| `backend` | `#ffffff` (white) | `ink` |
| `store` | `ink @ 0.05` | `muted` |
| `external` | `ink @ 0.03` | `ink @ 0.30` |
| `input` | `muted @ 0.10` | `soft` |
| `optional` | `ink @ 0.02` | `ink @ 0.20` dashed `4,3` |
| `security` | `accent @ 0.05` | `accent @ 0.50` dashed `4,4` |

---

## Customizing the skin

Four options:

1. **Run onboarding** — see [`onboarding.md`](onboarding.md). Drop a URL; the skill extracts the palette + fonts and rewrites this file.
2. **Edit by hand** — change the hex values in the tables above. Run the pre-output taste gate afterward to verify the accent still reads as "focal" against the new paper color.
3. **Brand handoff** — paste your existing design-token JSON into a new section here and map its tokens to the semantic roles above.
4. **Client profiles** — save and switch named skins, or bind one to a project, using [`profiles.md`](profiles.md).

### Constraints (don't break these)

- **Contrast**: `ink` must hit WCAG AA on `paper`. `muted` must hit AA on `paper` for 11px+ text.
- **One accent**: pick one color for `accent`. Two accents erases the focal signal.
- **No rainbow palette**: if your brand ships 8 colors, pick 3 (paper, ink, accent). The rest become `muted` variants.
- **Sans + mono**: two families, not more (CMI: Arial/Arimo + Roboto Mono). Hierarchy comes from size and weight, not from a serif.
- **Paper is warm-neutral, not pure white**: pure white turns the design sterile. Pick a cream, bone, or light grey with a hint of warmth.
- **Dot pattern is optional, not default**: the 22×22 dot pattern is an opt-in "dotted paper" variant (good for long-form editorial hero diagrams). The default background is a clean `paper` fill, no pattern. When the pattern is enabled, it should sit at ~10% opacity of `ink` on `paper` — visible but quiet.
- **Container is clean by default**: the diagram sits directly on the page paper, no secondary container background or border. A framed variant (`paper-2` bg + `rule` border + 8px radius + padding) is available as an opt-in for card-heavy layouts, but don't reach for it by default — the extra chrome fights the figure.
