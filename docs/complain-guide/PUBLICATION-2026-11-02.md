# Complete Complain or Constrain? web edition — 2 November 2026

## Owner instruction and scope

After the K.M.K. companion release, the owner explicitly instructed: “Post the complete complaint or constrain guide.” This release covers the complete accepted Complain or Constrain? manuscript and all thirteen source notes, not only the companion. That current instruction supersedes the earlier editorial publication hold for this guide. Independent qualified legal review, including review of the Tennessee section, has not been obtained. Publication does not represent professional certification. Other project holds are unchanged.

The guide is at `complain/`; the notes are at `complain/notes.html`; the dated case study remains at `complain/kmk.html`. The case watch remains stopped. No new reuse license is assigned. Existing grants for the other named resources are unchanged.

## Source and manuscript preservation

Baseline: commit `4c41db0aafc31a9db73a8d04280ee779a9c2276b` on `claude/project-thread-i83pmv`.

The complete substantive manuscript is preserved. The preparation script verifies exact equality with the accepted baseline after only two replacements: the opening draft/publication label and the Tennessee docket-check date. The source notes retain original research dates and access limitations. The October 13 publication-gate paragraph is labeled historical, and a separate dated November 2 publication/source-check note records the owner’s instruction without claiming legal clearance.

The [official Tennessee appellate display](https://pch.tncourts.gov/CaseDetails.aspx?Number=True&id=92346) was inspected on November 2. It identifies W2025-01186-CCA-R3-CD, shows the October 5 opinion as the latest event, lists Reverse, and leaves Supreme Court appeal-date and closed-date fields blank. Those observations do not exclude unrecorded or trial-court activity. The [judicial text hosted by Justia](https://law.justia.com/cases/tennessee/court-of-criminal-appeals/2026/w2025-01186-cca-r3-cd.html) was consulted to confirm that the reversal/new-trial order and rejection of the insufficiency challenge address different questions. No new complete trial-record review or independent legal review is claimed.

The [Supreme Court docket for 26A458](https://www.supremecourt.gov/docket/docketfiles/html/public/26A458.html) was also inspected on November 2 and still ended with the October 15 reply. This was a publication check, not a restart of the discontinued watch. The companion’s case narrative stays unchanged; only the publication-scope paragraph is reconciled with the complete-guide release.

## Build and validation plan

`scripts/build_suite.py` invokes the new static builder `scripts/build_complain.py`. It renders the canonical Markdown without client-side content loading, preserves the accepted body, and adds accessible navigation, stable citation IDs and thirteen return links. The collection has a fifth primary guide card, and the sitemap, text index, methods and handoff identify the full edition. No analytics, new backend or new reuse grant is introduced.

The release-preparation workflow is scoped only to `release/complain-full-2026-11-02`; it is a build/check workflow, not a recurring case watch. It runs the complete repository checker and Chromium tests before committing generated pages to the release branch. Successful results, if produced, appear in `SITE-CHECK-2026-11-02.json` and `BROWSER-CHECK-2026-11-02.json` and the GitHub Actions run. The browser tests cover 320/390/1280 widths, light/dark modes, skip links, table of contents, collection navigation and all thirteen guide-note round trips. Screenshots are captured but are not described as manually inspected without separate evidence.

This initial record does not claim tests passed, a merge occurred, or public deployment succeeded. Those states must be established from the actual workflow outputs, merged commit and GitHub Pages/public-route checks. A successful build is not independent legal review, reader testing, comprehensive accessibility certification or proof of search indexing.
