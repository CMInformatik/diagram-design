#!/usr/bin/env python3
"""Swap the upstream typefaces for the CMI stack across the whole plugin.

Upstream ships Instrument Serif (title/callout), Geist (sans) and Geist Mono.
CMI uses Arial with the metric-compatible Google font Arimo for every text
role, and Roboto Mono for technical values. Run this again after every
upstream sync; it is idempotent.

    python scripts/cmi-apply-fonts.py
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SUFFIXES = {".html", ".md", ".svg"}  # Python checkers stay upstream
SKIP = {"cmi-apply-fonts.py", "CMI.md", "THIRD_PARTY_LICENSES.md", "LICENSE"}

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
]


def main() -> None:
    changed = 0
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or path.suffix not in SUFFIXES or path.name in SKIP:
            continue
        text = path.read_bytes().decode("utf-8")
        new = text
        for pattern, repl in RULES:
            new = pattern.sub(repl, new)
        if new != text:
            path.write_bytes(new.encode("utf-8"))
            changed += 1
    print(f"{changed} files updated")


if __name__ == "__main__":
    main()
