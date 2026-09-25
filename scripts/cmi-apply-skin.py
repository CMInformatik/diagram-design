#!/usr/bin/env python3
"""Swap the upstream skin (typefaces and palette) for the CMI skin across the plugin.

Upstream ships Instrument Serif (title/callout), Geist (sans) and Geist Mono.
CMI uses Arial with the metric-compatible Google font Arimo for every text
role, and Roboto Mono for technical values. Upstream palette tokens in the
templates, examples and code snippets are mapped to the CMI palette from
references/style-guide.md. Run this again after every upstream sync; it is
idempotent.

    python scripts/cmi-apply-skin.py
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SUFFIXES = {".html", ".md", ".svg"}  # Python checkers stay upstream
SKIP = {"cmi-apply-skin.py", "CMI.md", "THIRD_PARTY_LICENSES.md", "LICENSE"}

RULES = [
    # Google Fonts links: serif + sans + mono triple, with & or &amp;
    (re.compile(r"family=Instrument\+Serif(?::ital@0;1)?(&amp;|&)family=Geist:wght@[0-9;]+\1family=Geist\+Mono:wght@[0-9;]+"),
     r"family=Arimo:ital,wght@0,400;0,700;1,400\1family=Roboto+Mono:wght@400;500;600"),
    (re.compile(r"family=Geist\+Mono:wght@[0-9;]+"), "family=Roboto+Mono:wght@400;500;600;700"),
    (re.compile(r"family=Geist:wght@[0-9;]+"), "family=Arimo:ital,wght@0,400;0,700;1,400"),
    (re.compile(r"family=Instrument\+Serif(?::ital@0;1)?(&amp;|&)"), ""),
    # Mono first, so "Geist" below never touches it
    (re.compile(r"Geist Mono"), "Roboto Mono"),
    # Quoted families in CSS, SVG attributes and Python string literals
    (re.compile(r"(\\?['\"])(?:Geist|Instrument Serif)\1"), r"\1Arial\1, \1Arimo\1"),
    # Unquoted families inside a font stack: font-family="Geist, sans-serif"
    (re.compile(r"\b(?:Geist|Instrument Serif)(?=\s*,)"), "Arial, Arimo"),
    # Remaining prose mentions
    (re.compile(r"\bInstrument Serif\b"), "Arial"),
    (re.compile(r"\bGeist\b"), "Arial"),
    # Tidy prose that distinguished the old sans from the old serif
    (re.compile(r"\bArial \(sans\)"), "Arial"),
    (re.compile(r"\bArial sans\b"), "Arial"),
    (re.compile(r"\bArial and Arial\b"), "Arial"),
    # CMI title is Arial 700; upstream sets the serif h1 in 400
    (re.compile(r"(h1\s*\{[^}]*?font-weight:\s*)400"), r"\g<1>700"),
    (re.compile(r"(h1\s*\{[^}]*?font:\s*)400(\s)"), r"\g<1>700\2"),
]


# Upstream token -> CMI token, light and dark columns of the style guide.
PALETTE = {
    "#f5f5f5": "#f7f9fa", "#ececec": "#ebebed", "#2d3142": "#1d3849",
    "#111111": "#000000", "#4f5d75": "#4a6272", "#7a8399": "#7a8e9b",
    "#bfc0c0": "#b7c4ce", "#eb6c36": "#009fe3", "#2e5aa8": "#1a808c",
    "#393e53": "#24455a", "#8e98ac": "#8da0ad", "#f08a59": "#33b5ec",
    "#6a95d8": "#4fb3be",
    "rgba(45,49,66,": "rgba(29,56,73,", "rgba(235,108,54,": "rgba(0,159,227,",
    "rgba(245,245,245,": "rgba(247,249,250,", "rgba(191,192,192,": "rgba(183,196,206,",
    "rgba(240,138,89,": "rgba(51,181,236,",
}
PALETTE_RE = re.compile(
    "|".join(re.escape(k) for k in sorted(PALETTE, key=len, reverse=True)) + r"(?![0-9a-fA-F])",
    re.IGNORECASE,
)
# The palette swap skips the style guide (already CMI) and the files that
# describe the pristine upstream defaults for gate and profile detection.
PALETTE_SKIP = {"style-guide.md", "onboarding.md", "profiles.md"}
GATE_LINE = "If they are still the shipped defaults"


def swap_palette(text: str) -> str:
    lines = text.split("\n")
    return "\n".join(
        line if GATE_LINE in line else PALETTE_RE.sub(lambda m: PALETTE[m.group(0).lower()], line)
        for line in lines
    )


def main() -> None:
    changed = 0
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or path.suffix not in SUFFIXES or path.name in SKIP:
            continue
        text = path.read_bytes().decode("utf-8")
        new = text
        for pattern, repl in RULES:
            new = pattern.sub(repl, new)
        if path.name not in PALETTE_SKIP:
            new = swap_palette(new)
        if new != text:
            path.write_bytes(new.encode("utf-8"))
            changed += 1
    print(f"{changed} files updated")


if __name__ == "__main__":
    main()
