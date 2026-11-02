# K.M.K. companion publication record — 2 November 2026

## Authorization and scope

The owner instructed: “Ok great, let’s publish and stop the watch.” The scoped release is the K.M.K. case study at `complain/kmk.html`, with canonical Markdown at `docs/complain-guide/kmk-case-study.md`. The associated daily wrestling-case automation was disabled successfully. Other monitoring tasks were not changed.

The complete Complain or Constrain? guide and Tennessee section are not included in this release. The accepted manuscript, existing source notes and independent legal-review requirement remain unchanged. No new reuse license is assigned. Publication approval is not professional legal clearance.

Baseline: publishing branch `claude/project-thread-i83pmv`, commit `e7be1adaa3d8c1689ba056da92d9d5f938ce2c25`, tree `d79a91c8e8b9c0ca68b6c7ae8279409bcaddf065`. The release is additive apart from bounded discovery/checker updates and this folder’s README addendum. Existing unrelated drafts are not merged.

## Evidence and editorial checks

The official Supreme Court docket was checked on November 2 and still ended with the October 15 reply. The application and appended lower-court orders, district and WIAA oppositions, and applicants’ reply were inspected. Relevant PDF pages were also visually inspected. The case study links those sources with document-page references.

The text distinguishes the reported assault from established facts; records the district’s investigation account as of its October 13 filing; does not equate a charging declination with a finding that the allegation is false; describes the individualized request and withdrawal alternatives; and separates the applicants’ and respondents’ positions from interim court findings. It does not describe the immediate requested injunction as a nationwide ban or infer the student’s motives. Neither the full trial record nor private investigative records were reviewed.

The published page is explicitly dated and is not live coverage. It directs readers to the official docket for current status and warns against submitting private information about minors to the public correction tracker.

## Validation actually performed

- Pandoc 3.1.11.1 rendered the case source; `build_kmk_case.py --check` confirmed byte-for-byte reproducibility.
- Python syntax checks passed for the case builder and modified site checker.
- The new case page has one H1, one main landmark, unique IDs, 28 valid same-page fragment links, five source anchors, canonical URL, Markdown alternative and consistent structured metadata. No new license is asserted in its metadata.
- The homepage’s complete visible content was compared with Pandoc output from its source using the existing builder’s section/link rules. Four primary guide cards remain; the case is a supporting link, not a claim that the complete guide is published.
- The sitemap contains ten unique URLs matching the checker’s publication-page list. Existing unrelated dates were preserved.
- Chromium rendered the case and collection at 320, 390 and 1280 pixels in light and dark modes. No horizontal overflow was detected. Keyboard skip links worked; the case contents menu and source-return navigation worked. Mobile and desktop screenshots were inspected.

Browser tests used in-memory HTML and the exact shared CSS because the environment blocked local file/HTTP navigation. They are rendering/interaction checks, not a test of deployed network routing. A full-repository `check_site.py` run was NOT performed: the complete checkout was unavailable in the execution environment. Existing baselines for copied files were checked against their Git blob hashes before bounded edits. The CSS was not modified.

Deployment and public-route verification are separate from these premerge checks and must be reported from actual GitHub Pages/public-page evidence, not inferred from a commit or this record.
