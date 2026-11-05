# Trust draft integration — 4 November 2026

PR #19 remains draft, unmerged and publication held. This is a source reconciliation, not a new factual review, release or deployment.

## Inspected revisions and actual conflicts

- Original PR #19 head: `877fcd677c30c7d1b55f58d4647d18eb3d043223`.
- Latest fetched publishing branch: `7e5cb13110622af5e6648beae09586b77eb3781a`, the merged PR #21 complete Complain release.
- Merge the published branch into the existing draft; preserve both parents and the original case history. Do not rebase away either body of work.
- Git produced three content conflicts, not ten: `llms.txt`, `sitemap.xml`, and `scripts/check_site.py`. The other seven overlapping files merged automatically and were inspected against the published revision.

The text-index conflict was a fixed twelve-page count versus draft-aware wording. Keep draft-aware wording and both resources' index entries. The sitemap conflicts were collection modification dates and competing route additions. Include all fourteen routes, retain existing research/page dates, and date the newly combined collection/methods integration November 4. The checker conflicts were competing route lists and the case/source metadata relationship check. Include the union of routes, all 29 existing research-note pairs and the Clara Tan relationship checks.

The auto-merged builder retains `build_complain.py` invocation, the fifth primary collection card and structured item, and both Trust case routes. The auto-merged collection and methods retain the complete-guide release account, K.M.K. companion, case selection rationale, license distinctions and draft qualifications. README and AGENTS retain both current statuses. No old publication hold is reapplied to the released Complain guide.

## Validation

`python3 scripts/build_suite.py` and `python3 scripts/check_site.py` pass: 14 pages, 447 local links, 29 reciprocal research-note pairs, reproducible generated pages, unique anchors, one main/H1, canonical and Markdown metadata, collection list and case/source relationships, and exact sitemap coverage. Whitespace checks pass. The full builder and checker include all three Complain routes.

Compared against the published commit, every file under `complain/` and `docs/complain-guide/`, both Complain builders, the existing Complain browser check, release workflow, shared stylesheet and unrelated guides remain byte-for-byte unchanged. Clara Tan's case/source Markdown remains byte-for-byte identical to the original PR head. Its rendered case changes only the common header navigation, adding the already-published Complain route. The five primary cards and separate supporting case placement coexist. Evidence qualifications, October 31 source-check dates and draft metadata are preserved.

## Browser attempt and reproducible follow-up

Chromium is installed here, but Playwright cannot launch it: Chromium exits with `process_singleton_posix.cc` / `socket() failed: Operation not permitted (1)`. No page rendered, so no browser layout, interaction or screenshot result is claimed. This supersedes the older missing-binary explanation for this attempt only.

`scripts/check_trust_integration_browser.py` provides the follow-up check. It uses system Chromium (or `H2HAB_CHROMIUM`) and Playwright, serves a local GitHub Pages project-prefix preview, and is designed to check all 14 reading routes at 320, 390 and 1280 pixels in light/dark modes, overflow, H1/main landmarks, skip links on suite pages, five collection cards, complete-guide/case navigation, case/source return links, contents menus and all 29 citation round trips. It captures screenshots in `/tmp` for separate visual inspection and writes a dated JSON only after successful assertions. The script itself has only been syntax-checked and launch-attempted here; its browser assertions remain unexecuted.

## Remaining acceptance requirements

Run that browser check in an environment that permits Chromium to launch, inspect representative case/source/collection/methods screenshots, and correct any demonstrated layout or interaction defects. Successful automated assertions alone would not constitute a manual visual review or complete accessibility audit.

Before eventual publication, refresh material agency/court developments and the reported hearing lead, retain the privacy/evidence limitations, confirm the exact revision and obtain the owner's explicit release authorization. The warrant, full immigration/custody/medical records, release authorization and hearing notice were not independently obtained in this integration. No new legal review, source authentication, reader testing, monitoring, external contact or indexing submission occurred. The separately published Complain guide remains published; its acknowledged independent legal-review limitation is unchanged and does not become a new release hold through this reconciliation.
