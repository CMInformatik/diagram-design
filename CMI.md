# CMI-Variante von diagram-design

Fork von [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) (MIT),
Basis-Commit `dc1ace47b99a419e42d01a03cb6ace5346efa8ae` (v2.6.33). Eingebunden über den
CMI-Marketplace `cmi-claude-infrastructure`.

## Was anders ist

- **Farben:** `skills/diagram-design/references/style-guide.md` enthält das CMI-Skin aus dem
  Brandbook (Skill `allgemein:cmi-ci-dokumente`): Dunkelblau `#1D3849`, CMI-Cyan `#009FE3`,
  Hellblau `#DFF2FD`, Hellgrau `#EBEBED`, Petrol `#1A808C`. CMI-Cyan nie als Textfarbe (Kontrast 2.97:1).
- **Schrift:** Arial mit Arimo als freiem Ersatz (gleiche Laufweite) für alle Texte, Roboto Mono
  für technische Werte. Keine Serifenschrift, Titel in Arial 700.
- **Vorlagen, Beispiele, Code-Snippets:** Schriften und Upstream-Farbtokens in `.html`/`.md`
  mit `scripts/cmi-apply-skin.py` auf CMI umgestellt, Titel in Arial 700. Ausgenommen sind die
  Stellen, die die Upstream-Standardwerte zur Erkennung brauchen (Gate-Zeile im `SKILL.md`,
  `onboarding.md`, `profiles.md`). «Coral» bleibt als Name der Akzent-Rolle stehen.
- **Onboarding-Gate** entfällt (Hinweis im `SKILL.md`, Abschnitt 0).

Die Python-Prüfskripte unter `scripts/` bleiben unverändert. Die Upstream-Entwickler-Checks
(`lint-skin.py`, `verify-docs-sync.py` u.a.) melden deshalb Abweichungen bei Farben und Schriften;
für die Nutzung relevant ist nur `skills/diagram-design/scripts/self_check.py`.

## Upstream nachziehen

```bash
git remote add upstream https://github.com/cathrynlavery/diagram-design.git   # einmalig
git fetch upstream && git merge upstream/main
# Konflikte in style-guide.md: CMI-Version behalten, neue Abschnitte von Upstream übernehmen
python scripts/cmi-apply-skin.py
for f in skills/diagram-design/assets/{example-,template}*.html; do python skills/diagram-design/scripts/self_check.py "$f" || echo "FAIL $f"; done
```

Danach Version in `.claude-plugin/plugin.json` auf `<upstream>-cmi.1` setzen und im
CMI-Marketplace den `sha` nachführen.
