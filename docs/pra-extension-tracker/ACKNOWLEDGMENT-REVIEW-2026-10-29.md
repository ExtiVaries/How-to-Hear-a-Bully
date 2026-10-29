# NARA acknowledgment verification — October 29, 2026

This is a bounded correction to the research-request status in the Presidential Records Release & Extension Tracker. It does not refresh the October 27 case research snapshot or change either notification-level extension confirmation.

## Evidence checked

- The editor-held request sent October 27, 2026, at 16:28 UTC seeks existing 2016–2026 extension registers, written statements and formal acknowledgments for PA 2026-099 and LW 2024-084, and current extension-tracking procedures.
- NARA's Operational FOIA Division acknowledgment is dated October 28, 2026. Its message timestamp is October 28 at 19:10 UTC. It confirms receipt on October 27, assigns **NGC27-065**, and instructs the requester to use that number in future case correspondence.
- The acknowledgment thread and subsequent relevant NARA correspondence were checked on October 29. No later substantive processing determination or responsive records for NGC27-065 were found. This describes the inspected correspondence, not all NARA systems or a public status portal.
- [PR #13](https://github.com/ExtiVaries/How-to-Hear-a-Bully/pull/13) merged October 28 at 15:48 UTC, before the acknowledgment arrived. Its pending-verification language reflected the earlier check. The current tracker replaces that language and retains a dated correction explaining the sequence.

The correspondence is held by the editor and is not publicly posted. This note publishes a factual summary without private mailbox links, message headers, personal contact details, or an unredacted copy of the correspondence.

## Evidentiary limits

Receipt and case assignment do not establish that responsive records exist, that NARA maintains a centralized register, that the public-interest fee waiver was approved, or that records have been produced. The acknowledgment supplies no new evidence of another PRA review extension, an executive-privilege claim, or delivery or public posting of the underlying presidential or vice-presidential records.

The request's public-interest fee-waiver request and prohibition on billable fees without separate written approval are retained as the requester's terms, not a NARA fee determination. Later processing decisions and record production require separate verification.

## Change boundaries

The correction starts from publishing-branch commit `97071b9e56a3337557d778fd7191c0396268fc74`. The already merged historical pilots remain intact. The separate historical-comparisons work in [PR #14](https://github.com/ExtiVaries/How-to-Hear-a-Bully/pull/14) is outside this correction.

Only the tracker Markdown, synchronized HTML, tracker modification dates, and this verification note change. The original October 27 case research date, request scope, case narratives, two-row case register, and December 2 **proposed** opening-date distinction are retained. `events.csv` remains byte-for-byte unchanged; its Git blob is `2fa383e896665e3382cdeffde5a37429af9372c6`.

## Validation record

- `python3 scripts/build_suite.py` completed successfully with Pandoc 3.1.3.
- After regeneration, `python3 scripts/check_site.py` passed for 9 pages, 264 local links, 16 reciprocal notes, metadata, sitemap, and generated-page consistency.
- A clean worktree at the starting commit reproduces one pre-existing reproducibility warning: Pandoc 3.1.3 adds `header`, `odd`, and `even` classes to three rows in the unrelated methods-page table. No text or links change. Those generated formatting changes were restored before committing this correction. A fresh check with this Pandoc version will flag the same baseline difference; the after-regeneration pass is not a claim that the committed methods page reproduces byte-for-byte in this environment.
- Targeted checks passed for full tracker Markdown/HTML main-text, link, and heading parity; stable section anchors; a single acknowledgment entry; unchanged case narratives and dates outside the stated correction; and byte-for-byte preservation of the event register. No personal contact information or private mailbox links were found in the additions.
- Whitespace and four-file change-scope checks passed. Browser verification was attempted but could not run because this environment has no installed Chromium executable; no new browser-validation claim is made. The correction changes prose and modification metadata, with no layout or stylesheet changes.

AI-assisted review is not independent expert certification. The pull request records the reviewed commit and remote read-back checks; deployment must be verified separately after integration.
