# What Actually Changed? — draft review

Research cutoff: **9 October 2026**. Prepared against `057e3a0fb77728be2cfddcd8f17b9742b137be91` on the site's current Pages branch, `claude/project-thread-i83pmv`. Review branch: `codex/what-changed`. A separate assessment of draft commit `e02455c` returned **ready with bounded corrections**; the response below records those corrections.

## Delivered and bounded

The standalone guide teaches six questions without requiring another guide first. Eight entries follow four histories: FEC capacity, Title IX, Arizona birth certificates, and NYC youth-care procurement. They include a substantiated institutional constraint, temporary restoration, and announcements that overstate an immediate change when separated from their baseline. Coverage begins in August 2019; this is a curated selection, not a national assessment.

One JSON record generates static HTML, a Markdown reading edition, and public JSON. Entries separate event precision, first recording, substantive revision, complete source comparison, effective date, jurisdiction, action, procedural status, and observed effects. Full previous entries are retained for later substantive revisions. Search and history filtering enhance an otherwise usable static page.

The existing Bully, Crisis, Trust, and Complain manuscripts remain unchanged. Original Bully HTML receives navigation only; it is still maintained separately from Markdown. Pending Tennessee material has no new web route, sitemap entry, or publication. New material has no assigned reuse license.

## Adversarial editorial review

Independent AI review examined headlines, allegation-versus-finding language, holdings versus interpretation, scope, immediate effect, lived consequences, political reversals, and inconvenient later developments. This is a challenged draft, not independent factual certification or human reader testing.

| History | Result and remaining evidence limits |
| --- | --- |
| NYC procurement | The headline names a proposal, not available appointments. The notice establishes an intended purchasing step, scope, and proposed terms. Conflicting term/date and response-time statements remain explicit. Award, registration, payment, staffing, and usable appointments have not been established. |
| Arizona | The October decision is read alongside the April stay. It rejects the facial challenge and recognizes a court-order route; that does not certify easy access or a newly effective closure of a functioning administrative route. Prior refusals are attributed to plaintiffs' testimony with the opinion's “apparently denied” qualification. A current mandate, later orders, and registrar practice remain unverified. |
| Title IX | January vacatur and September recodification are separate events. The latter changes published regulations against a rule already vacated, with exceptions identified in the final rule. The Department reports that the Tennessee appeal was dismissed with prejudice in May 2026; the entry attributes that account. Court text was read in a public reproduction; the original agency directive and full appellate docket were not independently retrieved. Neither source availability nor agency characterization supplies the missing docket check. |
| FEC | A quorum loss restricts specified decisions without eliminating reporting obligations or all staff work. Restoration uses the oath date, not confirmation, and is linked to subsequent losses. Agency output after restoration is described without claiming that restoration alone caused every outcome. Current membership is sourced to the agency roster. |

Four entries have complete source checks; four display incomplete checks and their missing evidence. Stronger current-access or operative-status claims require the missing records above. Bounded entries can be reviewed as written. Recheck active topics if publication occurs after the cutoff. Shield-law requests and school-investigation leads were not included: relief, remedy, and implementation records would require additional research. Their omission implies neither dismissal nor confirmation of the underlying concerns.

## Response to the separate assessment

All bounded findings were considered and the supported corrections applied:

- Removed the unsupported September 28 announcement date. The cited final rule establishes September 29 publication and effectiveness.
- Added the Department's attributed May 2026 appeal-dismissal account and its description of finality, without claiming an independently checked appellate docket.
- Restored the Arizona opinion's “apparently denied” qualification. NYC's entry identifies the notice title “Gender Affirming Care” and uses its care terminology while preserving the procurement-versus-access distinction.
- Clarified the FEC locator: continuing functions are in printed p. 4, footnote 3, which is PDF viewer page 5. The surrounding printed pp. 3–4 describe the other capacity limits. This resolves the page-number distinction in the assessment.
- Fixed the empty Markdown history line and doubled terminal punctuation; removed the extra test-file EOF blank line. A renderer regression checks both editions.
- Described the guide's exercises as adapted teaching examples, not wholly invented accounts.
- Kept seven-day review intervals and overdue warnings. Both reading editions disclose that no recurring check is active and label dates as suggested manual reviews. A date simulation checks that stale active topics remain overdue without changing their source-check dates.

The earlier whitespace-check claim was too broad: a tracked-file check missed newly added files, including the generated Markdown. The corrected full proposed tree is checked against the base using a temporary index that includes all intended new files. This does not alter the checkout's actual staging area.

Five real event corrections preserve their full prior review-draft entries and reasons in the public revision history. They precede first site deployment; no event was added merely to announce an editorial correction. The guide and presentation fixes are recorded here and in the Git diff. The unrelated *Tennessee v. Ward* publication condition for Complain remains open; these Title IX entries concern *Tennessee v. Cardona*.

## Research backend and schedule audit

The private registry's current publication pointers were resolved rather than relying on an old tracker. The documentation describes separate Security/Rights/Traveler assessments, saved releases, historical records, recovery, predecessor checks, and six-hour updates. Release and ledger records support that pattern, but the actual scheduler configuration, timezone, and next run could not be independently inspected with available access. Do not describe the scheduler as operationally verified.

The private Verified field compares a saved release to its intended payload; it is not certification of facts. Selected baselines can be older than selection dates. Categorical labels can flatten pending proceedings into apparent implementation. Security probabilities lack an audited calibration for this project, and the five-state panel is a research sample. None of those scores, private links, personal details, or operational ledgers is imported into the public timeline.

Keep the existing Notion process as the single research backend for now, and curate underlying public evidence into repository review branches. Moving research into the repository is a later migration requiring retention, recovery, access, and activation tests. The existing automation has not been changed.

The proposed task checks daily at 09:00 America/New_York, **unconfirmed**. Daily curation reduces churn relative to six-hour research while allowing a requested urgent check. [Exact prompt](schedule-prompt.txt), [proposed configuration](schedule.json), [record format](SCHEMA.md), and [operator workflow](WORKFLOW.md) are included. They do not create a task.

## Demonstrated cycle and checks

An isolated small copy of the real record demonstrated an Arizona wording correction: raw candidate → validation and review hash → baseline-guarded application → rendered prior wording in the revision history → exact rerun without another write. A partial source report retained the incomplete topic check. The real initial edition remained unchanged by that fixture; no fictional public correction was inserted.

The subsequent correction cycle used the same guarded CLI on the actual record: five reviewed proposals applied against their exact baselines, each repeated without another write. Eight stable event IDs and first-recorded dates were preserved; five genuine prior-entry snapshots were appended. Revised FEC capacity and Title IX recodification claims were compared with all four required public documents and exact retrieved byte hashes. Their complete checks were restored only after those comparisons. Other topics were not refreshed.

Automated tests cover exact and identity deduplication, exclusive writers, lock replacement, baseline conflict, reviewed reruns, visible correction snapshots, late discovery/date precision, partial failures, amendment hashes, malformed input, private URL rejection, stale comparison dates, and preservation of the last good canonical record. Build generation stages all rendered pages before writing; deployment remains gated on a complete successful check. The writer lock is cooperative, and supplied comparison notes/hashes still need truthful editorial review.

Validation results:

- All 15 timeline update and renderer tests passed.
- Site build and reproducibility checks passed: 11 pages, 355 internal links, 16 reciprocal note links, stable event/source and correction anchors, matching public JSON, sitemap, metadata, and no Complain publication route.
- Browser checks passed in 24 layouts across 320, 390, and 1280 px, light/dark modes, four routes, keyboard skip navigation, search, history filtering, empty-state clearing, source deep links, and no-JavaScript reading/details. No overflow or resource errors were found. Mobile screenshots were inspected. This is focused accessibility QA, not a WCAG certification or screen-reader audit.
- All 13 distinct public source URLs were requested again: 10 returned HTTP 200; two court reproductions returned 429 after earlier research access, and the agency directive returned 403. Those results are access checks, not proof of factual freshness. The incomplete topic checks remain incomplete.
- Full proposed-tree `git diff --cached --check HEAD` passed against the base, including added Markdown and tests. The remote committed diff is also checked against that base after pushing. Existing manuscripts and publication conditions were preserved.

## Publication and activation conditions

Implementation and testing are complete for a reviewable draft. An authenticated review-branch push demonstrates interactive GitHub writing; it does not prove unattended authentication. Draft PR creation remains an explicit final step: no PR was created in this demonstration. The local GitHub CLI credential was unavailable; the connected GitHub tool is the branch-writing path tested here. No Pages merge/deployment, indexing notification, recurring public writer, or schedule activation is part of this assignment.

Before deployment, review the exact PR, current active-topic evidence, unresolved source limits, and reuse decision. Then follow the existing publication workflow, verify the deployed routes and JSON, and send discovery notifications only for an actual release.

Before creating a schedule, confirm timezone/cadence and approve its prompt and editorial policy. Test the correct repository checkout, build dependencies, unattended least-privilege branch/PR access, failure delivery, safe refresh, one-writer locking, and last-good recovery on the actual scheduler host. An unrelated project must never become the writer's destination. All repository updates remain review-gated. Any future automatic check-only policy needs separate approval; new events, contradictions, ambiguous legal effects, amendments, corrections, and reinterpretations always require editorial review. Preserve Notion until a replacement has passed comparison/recovery tests and activation is approved.
