#!/usr/bin/env python3
"""One-time, guarded publication migration authorized on 2026-11-02."""
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "docs/complain-guide"
BASELINE = "4c41db0aafc31a9db73a8d04280ee779a9c2276b"
BASE = "https://extivaries.github.io/How-to-Hear-a-Bully/"


def change(path, old, new, count=1):
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    if new in text:
        return
    if text.count(old) != count:
        raise ValueError(f"Unexpected baseline for {path}: {old[:70]!r}")
    p.write_text(text.replace(old, new), encoding="utf-8")


def append(path, marker, text):
    p = ROOT / path
    old = p.read_text(encoding="utf-8")
    if marker not in old:
        p.write_text(old.rstrip() + "\n\n" + text.strip() + "\n", encoding="utf-8")


def main():
    article = "docs/complain-guide/complain-or-constrain.md"
    notes = "docs/complain-guide/complain-or-constrain-notes.md"
    change(article, "*Draft for review. Sources and factual limits appear", "*First web edition: 2 November 2026. Sources and factual limits appear")
    change(article, "*Public docket checked October 13, 2026.", "*Public docket rechecked November 2, 2026.")
    before = subprocess.check_output(["git", "show", f"{BASELINE}:{article}"], text=True)
    expected = before.replace("*Draft for review. Sources and factual limits appear", "*First web edition: 2 November 2026. Sources and factual limits appear").replace("*Public docket checked October 13, 2026.", "*Public docket rechecked November 2, 2026.")
    if (ROOT / article).read_text(encoding="utf-8") != expected:
        raise ValueError("Accepted manuscript changed outside the two authorized publication/currency lines")
    change(notes, "Not publication approval.*", "These historical reviews are not independent legal approval. The owner authorized this web edition on 2 November 2026; qualified independent legal review has not been obtained.*")
    change(notes, "[Read the draft](complain-or-constrain.md)", "[Read the guide](complain-or-constrain.md)")
    change(notes, "**Remaining uncertainty and publication gate:**", "**Historical uncertainty and publication gate — 13 October 2026:**")
    marker = "**Publication recheck — 2 November 2026:**"
    p = ROOT / notes
    text = p.read_text(encoding="utf-8")
    if marker not in text:
        addendum = """**Publication recheck — 2 November 2026:** The [official Tennessee case history](https://pch.tncourts.gov/CaseDetails.aspx?Number=True&id=92346) was inspected again. Its displayed history still ends with the 5 October opinion; disposition is Reverse, and the Supreme Court appeal-date and closed-date fields remain blank. This is a dated observation of the available public display, not proof that no unrecorded or trial-court activity exists. The [judicial text](https://law.justia.com/cases/tennessee/court-of-criminal-appeals/2026/w2025-01186-cca-r3-cd.html) continues to support the distinction between reversal/new trial and rejection of the insufficiency challenge. This check does not renew notes 1–12 or represent independent professional legal review.

**Owner-authorized publication — 2 November 2026:** The owner explicitly requested publication of the complete guide after the separate K.M.K. companion was published. That instruction supersedes the prior editorial publication hold for this guide. It does not establish that qualified independent legal review occurred; that review remains unobtained and is disclosed on the reading pages. No new reuse license is assigned. See the [publication record](PUBLICATION-2026-11-02.md)."""
        text = text.replace("\n## Adversarial checks", "\n" + addendum + "\n\n## Adversarial checks")
        p.write_text(text, encoding="utf-8")
    homepage = "docs/practical-guides/homepage.md"
    text = (ROOT / homepage).read_text(encoding="utf-8")
    if "### Complain or Constrain?" not in text:
        card = """\n### Complain or Constrain?

Take reported harm seriously, then examine the requested remedy independently. Six questions, six historical cases and a Tennessee legal complication distinguish protection, accommodation and unjustified restrictions.

**[Read the complete Complain or Constrain? guide](../complain-guide/complain-or-constrain.md)**
"""
        text = text.replace("\n---\n", card + "\n---\n", 1)
        (ROOT / homepage).write_text(text, encoding="utf-8")
    change(homepage, "It is a standalone companion to Complain or Constrain?, not the release of the complete guide.", "It is a dated companion to the complete Complain or Constrain? guide above.")
    builder = "scripts/build_suite.py"
    change(builder, '"numberOfItems": 4', '"numberOfItems": 5')
    change(builder, '("Who to Trust When It All Breaks Down?", BASE + "trust/"),', '("Who to Trust When It All Breaks Down?", BASE + "trust/"),\n                    ("Complain or Constrain?", BASE + "complain/"),')
    change(builder, '"methods.md": "methods.html"}', '"../complain-guide/complain-or-constrain.md": "../complain/",\n                 "methods.md": "methods.html"}')
    change(builder, '"Evidence and trust"]', '"Evidence and trust", "Protection and remedies"]')
    change(builder, 'the four primary guide cards', 'the five primary guide cards')
    change(builder, 'def build():\n', 'def build():\n    from build_complain import build as build_complain\n    build_complain()\n')
    checker = "scripts/check_site.py"
    change(checker, '"complain/kmk.html"]', '"complain/kmk.html", "complain/index.html", "complain/notes.html"]')
    change(checker, 'BASE + "crisis/", BASE + "trust/"}', 'BASE + "crisis/", BASE + "trust/", BASE + "complain/"}')
    change(checker, 'len(listed) != 4', 'len(listed) != 5')
    change(checker, '.get("numberOfItems") != 4', '.get("numberOfItems") != 5')
    change(checker, 'the four visible project links', 'the five visible project links')
    change(checker, '(("crisis", 9), ("trust", 7))', '(("crisis", 9), ("trust", 7), ("complain", 13))')
    change("docs/complain-guide/kmk-case-study.md",
           "This is a standalone companion case study. It does not release the complete Complain or Constrain? guide or clear that manuscript’s separate Tennessee legal-review requirement. The accepted guide and its source notes remain unchanged.",
           "This case study was initially published as a standalone companion. The owner subsequently authorized the [complete Complain or Constrain? guide](https://extivaries.github.io/How-to-Hear-a-Bully/complain/) on 2 November 2026. Publication does not establish independent qualified legal approval; that review has not been obtained. The case facts on this page remain the dated snapshot above.")
    append("docs/practical-guides/methods.md", "## Complain or Constrain? — complete web edition", """## Complain or Constrain? — complete web edition

The [complete guide](https://extivaries.github.io/How-to-Hear-a-Bully/complain/) and [13 source notes](https://extivaries.github.io/How-to-Hear-a-Bully/complain/notes.html) were authorized for publication by the owner on 2 November 2026. The approved substantive manuscript is preserved. It distinguishes reported harm from the justification for a remedy; the six questions are an unvalidated civic teaching aid, not a universal legal test. Original research dates remain in the notes. The Tennessee public appellate display was rechecked on November 2; this does not establish finality or exclude unrecorded proceedings.

The owner’s explicit instruction supersedes the earlier editorial publication hold for this guide. Independent qualified legal review, including review of the Tennessee discussion, has not been obtained. Publication is not legal certification or advice. No new reuse license is assigned to Complain or Constrain?, its notes or the [dated K.M.K. companion](https://extivaries.github.io/How-to-Hear-a-Bully/complain/kmk.html); the grants for other named resources do not automatically extend to them. The K.M.K. watch remains stopped. This release does not lift holds on other projects.""")
    append("README.md", "## Complain or Constrain? — published web edition", """## Complain or Constrain? — published web edition

The owner authorized the complete [Complain or Constrain? guide](https://extivaries.github.io/How-to-Hear-a-Bully/complain/) and [source notes](https://extivaries.github.io/How-to-Hear-a-Bully/complain/notes.html) on 2 November 2026. The substantive manuscript is unchanged. Build with `python3 scripts/build_suite.py`; check with `python3 scripts/check_site.py`. Publication does not certify independent legal review, which has not been obtained. No additional reuse grant is assigned to this guide, its notes or the K.M.K. companion. Other resources retain their existing terms. See [the release record](docs/complain-guide/PUBLICATION-2026-11-02.md).""")
    p = D / "README.md"
    old = p.read_text(encoding="utf-8")
    if "## Current status — complete edition authorized" not in old:
        current = """## Current status — complete edition authorized, 2 November 2026

The owner explicitly instructed publication of the **complete** guide following the standalone K.M.K. release. This supersedes the publication hold described in the historical record below for this guide only. Independent qualified legal review has not been obtained and is not claimed. The approved substantive manuscript is preserved; only publication/currency lines and source-note status were updated.

- [Complete guide](https://extivaries.github.io/How-to-Hear-a-Bully/complain/)
- [All 13 source notes](https://extivaries.github.io/How-to-Hear-a-Bully/complain/notes.html)
- [Dated K.M.K. companion](https://extivaries.github.io/How-to-Hear-a-Bully/complain/kmk.html)
- [Publication record](PUBLICATION-2026-11-02.md)

No new reuse license is assigned. The wrestling-case watch remains stopped. Run `python3 scripts/build_suite.py` then `python3 scripts/check_site.py` to rebuild and validate the complete edition.

## Historical preparation and companion-release record

The following records describe earlier stages, not the current publication authorization.

"""
        p.write_text("# Complain or Constrain?\n\n" + current + old.split("\n", 1)[1].lstrip(), encoding="utf-8")
    p = ROOT / "AGENTS.md"
    text = p.read_text(encoding="utf-8")
    if "## Current Complain publication update — 2 November 2026" not in text:
        update = """## Current Complain publication update — 2 November 2026

The owner expressly requested publication of the **complete** Complain or Constrain? guide after the standalone K.M.K. release. That instruction supersedes the older Complain publication hold below; it does not lift holds on unrelated projects or claim independent legal review. The full guide and notes are served at `complain/` and `complain/notes.html`; the dated companion stays at `complain/kmk.html`. The substantive accepted manuscript remains unchanged. `scripts/build_suite.py` now invokes `scripts/build_complain.py`; the site checker includes all three Complain routes and 13 reciprocal guide-note citations. No new reuse license is assigned. The court watch remains stopped. See `docs/complain-guide/PUBLICATION-2026-11-02.md` and actual release/Pages evidence for deployment status. Earlier status snapshots below are retained as history.

"""
        text = text.replace("Status snapshot:", update + "Historical status snapshot:", 1)
        p.write_text(text, encoding="utf-8")
    index = "llms.txt"
    change(index, "the ten HTML pages", "the twelve HTML pages")
    change(index, "This standalone publication does not release the complete guide or clear its separate Tennessee legal-review requirement.", "The complete guide was subsequently authorized for publication on November 2; neither publication establishes independent legal review.")
    append(index, "## Complain or Constrain? — complete guide", """## Complain or Constrain? — complete guide

- [Full guide](https://extivaries.github.io/How-to-Hear-a-Bully/complain/): harm, discomfort, protection, accommodation and remedies; six questions, six historical examples and a Tennessee complication. The substantive approved manuscript is preserved.
- [All 13 source notes](https://extivaries.github.io/How-to-Hear-a-Bully/complain/notes.html): philosophical, empirical and judicial sources, contrary arguments, access limits and dated review history.
- [Markdown guide](https://extivaries.github.io/How-to-Hear-a-Bully/docs/complain-guide/complain-or-constrain.md) and [Markdown notes](https://extivaries.github.io/How-to-Hear-a-Bully/docs/complain-guide/complain-or-constrain-notes.md).

First web edition authorized November 2, 2026. This is civic education, not legal advice or independent professional legal certification. No new reuse license is assigned. The teaching framework has not been reader-validated. Original source dates are preserved; a publication date does not renew all research.""")
    p = ROOT / "sitemap.xml"
    text = p.read_text(encoding="utf-8")
    if BASE + "complain/</loc>" not in text:
        text = text.replace("</urlset>", f"  <url><loc>{BASE}complain/</loc><lastmod>2026-11-02</lastmod></url>\n  <url><loc>{BASE}complain/notes.html</loc><lastmod>2026-11-02</lastmod></url>\n</urlset>")
    text = re.sub(r'(<loc>https://extivaries.github.io/How-to-Hear-a-Bully/practical-guides/methods.html</loc><lastmod>)[^<]+', r'\g<1>2026-11-02', text)
    p.write_text(text, encoding="utf-8")
    print("Publication migration complete; accepted substantive manuscript preserved.")


if __name__ == "__main__":
    main()
