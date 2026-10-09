# Community claim tracker: follow-up review

Reviewed: `v1.md`, `review.md`, `REVISIONS.md` and `claude.md` on `codex/claim-tracker-v1` at commit `1adb5a3` (draft PR #6), October 9, 2026. This follow-up compares that revision with the [initial review](review-detailed.md) of `7c768a4`.

This is an AI-assisted review of a written specification. It is not independent expert certification, and no implementation exists, so every "resolved" below means resolved in writing. The platform terms the specification cites were not rechecked.

## Verdict

**Ready after specified revisions. The remaining revisions are small.** All five blockers in the summary are resolved in writing, and several fixes go further than the initial review asked. For example, the headline assessment now answers the as-circulating claim rather than only carrying a scope note. The revision introduced one new problem (N1). It also left the removal path from the initial review partly open (N2), and the end of an accepted claim's life undefined (N3). These three are short edits. Once they are made, I would call the manual pilot ready for implementation.

`review.md` is an accurate copy of the summary I posted. It also states correctly that it is not the full report. That full report is now in [review-detailed.md](review-detailed.md). Its items F8 to F18 were not part of the summary, so they are triaged under "Carried over" below rather than counted against this revision.

## The five blockers

| Blocker | Status | Where |
| --- | --- | --- |
| Unassessed publication and narrowed claims | **Resolved.** Claims stay private until a first completed assessment. As circulating, assessed assertion and scope note are required and published atomically. The headline answers the circulating claim, and a narrower fact cannot lend it Supported. | Pilot scope; Manual submission; assessment rules after the assessment table; A1, A6, A12 |
| Unbounded intake and correction priority | **Resolved.** The first release is manual-only, with per-member and global caps, expiry, a pause rule and a reserved correction lane. Connectors are gated behind admission caps and coverage-gap reporting. | Review capacity and priority; Later stage automatic discovery; A3, A12 |
| Evidence-change detection and removal authority | **Detection resolved**: manual checks and member reports, with no promise of automatic detection. **Removal partially resolved**: see N2. | Claim identity and corrections, final paragraph; Removal authority and retention; A5, A8, A10 |
| Private duplicate disclosure | **Resolved.** Members match only against published records. Unknown and inaccessible IDs give the same response, and counts are not exposed. | Manual submission, third paragraph; A1, A4, A5 |
| Retention of declined allegations | **Resolved.** A seven-day purge with content-free disposition events and no hashes. Backups expire, and a deletion manifest is applied before a restore. A provider that cannot do this blocks launch. | Removal authority and retention; A11 |

## New or remaining findings

### N1. Any member can put a doubt banner on any assessment and consume the correction lane (medium, design risk)

Where: "A member's report immediately opens a priority review task and displays 'Evidence change reported; review pending' on the published record." Also, under Review capacity: corrections "may displace all new work".

Hypothetical sequence: A member who dislikes a Contradicted assessment files a vague "the source changed" report. The banner appears at once, and the report takes a priority slot. Three such reports a day fill the correction lane and pause new intake. New submissions are capped at two per member, but correction reports have no cap, so the lane meant to protect accuracy becomes the cheapest way to cast doubt or stall the tracker.

Smallest revision:
- A report must name the cited evidence record and say what changed.
- The banner appears only after a reviewer confirms the report is specific, not that it is true. That triage should be a quick step and may use one priority slot.
- Cap open correction reports per member, for example at two, matching submissions.
- A dismissed report gives the reporter a reason.

Acceptance check: An unspecific report shows no banner and is dismissed with a reason. A member's third open report is refused. A specific report shows the banner only after reviewer triage.

### N2. Removal reasons are open-ended, and one person may hold every role (medium, missing requirement)

Where: Participants table ("One pilot operator may hold multiple roles"); Removal authority ("reason category" is not enumerated).

Hypothetical sequence: In a pilot with one reviewer, that reviewer is also the removal administrator. They remove the wording of an earlier assessment they now regret, under a broad reason such as "restricted content". The audit event survives, but the accountability the history was meant to provide is gone. This was the erasure path in the initial review's F6.

Smallest revision:
- Enumerate the removal bases: private-person data, legal request, platform-required deletion, copyright.
- A revision's label, date and author are never removable. Only the specific personal or restricted text is removable, replaced with a visible "[removed: basis]" marker.
- When the same person holds reviewer and removal-administrator roles, the removal event says so.

Acceptance check: A removal without a listed basis is rejected. After any removal, the revision still shows its label, date, author and marker. A same-person removal is labeled as such.

### N3. Accepted claims have a deadline but no defined end (low to medium, specification gap)

Where: Accepted records "cannot remain an indefinite private backlog". Yet only queued and needs-context records can expire, accepted claims may only be merged or archived, and the seven-day purge covers only declined or expired payloads.

Consequence: The specification does not say what happens to an accepted claim whose review deadline passes. An accepted claim that is never published keeps its submitter's wording indefinitely.

Smallest revision: Allow Accepted to move to Expired (or archive it with a reason) after a stated overdue period. Apply the seven-day payload rule to accepted records that were never published.

Acceptance check: An accepted record past its deadline plus the grace period moves to Expired, and its payload is purged on schedule.

### N4. Smaller items

- **A9** still says "at most one event per follower", so an inbox that never fires passes. It should say exactly one per active follower. Also, "material" is undefined; a label change should always count as material.
- **Capacity numbers.** Five reviews a day minus two reserved slots leaves about three new assessments a day. The three-working-day pause therefore triggers at around nine to twelve open claims, well before the cap of 20. This is not harmful, but the 20 will rarely bind. Say which limit is the operative one.
- **Community context on published claims.** In a 10 to 20 person pilot, "member-supplied: [small forum]" can identify the submitter (initial review F9). Show the community only when the submitter opts in.

## Carried over from the full review

These items were in the full review but not in the summary, so the revision could not address them. Two of them should be done before the pilot opens:

- **F11. A "lead" (screenshot, transcription, anonymous claim) must not be the sole basis for Supported, Contradicted or Misleading.** One sentence in Evidence plus an A6 check.
- **F13. Every revision needs a required change type**: correction, new development, evidence lost or changed, or wording edit. A new-development revision keeps the earlier dated assessment visible as accurate for its date.

Also before the pilot opens: a participation notice covering what is stored, who sees it, retention, and how to request removal. The spec now supplies most of the content.

These can wait until after the pilot:
- **F10:** reconciling merges of claims whose assessments conflict.
- **F12:** documented negative searches as evidence.
- **F14:** a per-community selection audit.
- **F15:** stating that a private pilot tests the reviewer workflow, not community reach.
- **F17:** no self-assessment, and second sign-off on Contradicted and Misleading.

**F16** (import lease fencing, and source-post edits and deletions) belongs with the L-stage checks, before any connector.

## Acceptance criteria and stages

The M/L split is correct. A2, A3 and the L half of A12 depend on a live connector. Everything else can and should be tested in the manual release. Adjustments:

| ID | Change |
| --- | --- |
| A5 | Add the N2 checks for removal basis and same-person labeling. |
| A6 | Add the F11 lead-only rejection. |
| A8 | Add the F13 required change type. |
| A9 | "At most one" becomes exactly one per active follower. |
| A10 | Add the N1 report specificity, banner timing and per-member cap. |
| A11 | Extend the purge to accepted records that were never published (N3). |

## Pilot and launch dependencies

The revised manual pilot matches the leanest credible pilot from the initial review. Its launch dependencies are named honestly: niche, reviewers, removal administrator, a host that can meet the retention rule, and passed M checks. The retention rule is the dependency most likely to narrow hosting choices, since it requires deletion from operational copies within seven days and a deletion manifest applied on restore. Confirm that before choosing a provider. Connector launch correctly requires its own permissions, spare capacity measured in the pilot, and the L checks.
