# Community claim tracker revision response

October 9, 2026. Response to the [owner-supplied review summary](review.md) of the initial specification at `7c768a431d94d8dc0c4f0649a759a1a4db6a127a`. The five reported blockers have written changes in [v1.md](v1.md). Follow-up review and runtime acceptance checks remain pending. The detailed ten-criteria annotations referenced in the summary were not supplied; the acceptance edits below are our responses to the available findings, not a reconstruction of that missing report.

## Changes responding to the five blockers

| Finding | Written revision | Acceptance criteria |
| --- | --- | --- |
| Unassessed publication and narrowed claims | Accepted intake stays private until first completed assessment. Require as circulating, assessed assertion, and scope note; a narrower/historical fact cannot determine a supported label for a broader/current rumor. Preserve privacy when representing circulating wording. | A1, A6, A12 |
| Unbounded automatic intake and correction priority | Manual-only first release with 20 open unassessed claims and two open submissions per member. Corrections have reserved capacity and may displace all new work. Later imports have per-source and global admission limits, expiry, pauses, and visible coverage gaps. | A2, A3, A12 |
| Undefined detection and removal authority | Member reports and manual due-date checks supply first-release detection. Give removal administration a separate permission; reviewers cannot erase history. Audit emergency hides and administrator removals, including historical and follower payloads. | A5, A8, A10 |
| Private duplicate disclosure | Members match only against authorized published summaries. Private matches, identities, counts, and distinguishable inaccessible-ID responses are prohibited. Reviewer matching remains role-restricted. | A1, A4, A5 |
| No declined allegation retention limit | Purge declined/expired private payloads within seven days; keep only safe disposition events. Daily retention jobs, restricted backups with 30-day expiry, and deletion before restore access are launch requirements. | A10, A11 |

## Clarified release stages

The lean first release has one niche, 10 to 20 invited participants, one or two reviewers, and a designated removal administrator. It includes manual claims and evidence, first-assessment publication, corrections, following, review reminders, and retention. Capacity settings are proposals to be validated, not measured operating performance.

Manual launch requires M portions of A1 and A4 through A12, accountable reviewers, a chosen niche, and hosting/identity/storage that implement the privacy and retention rules. A2 and A3 are later-stage L checks. The L portion of A12 also gates connectors. Automatic discovery requires one authorized live source, observed spare reviewer capacity, proven admission/expiry controls, and accurate reporting of coverage gaps. The first release promises neither live feed discovery nor automatic source-change detection.

## Follow-up checks

Ask the follow-up reviewer to trace these concrete cases through the revised requirements:

1. A member accepts a candidate for assessment; a second member searches its exact wording or probes its ID. No private record, identity, count, or existence signal should be returned.
2. "The city just banned gardens" is backed only by a 2019 sidewalk ordinance. Show the original meaning, the narrowed fact, and the resulting scope-based assessment. Supported must not silently migrate between them.
3. The new-claim queue is full while a published claim's sole source is retracted. The report enters the priority lane, displaces new work, and a reviewer-confirmed loss of support creates an unresolved revision.
4. A reviewer notices accidentally published identifying content. A temporary hide creates a safe event; only a separately authorized administrator completes redaction; prior assessment accountability survives without the sensitive payload.
5. A private-person allegation is declined. Verify the deletion deadline applies to source URLs, summaries, logs, historical and follower copies where applicable, and that restoring a backup cannot expose it again.
6. A later importer saturates its per-source or global cap, then retries and resumes. It must disclose omitted coverage and preserve correction capacity without an unbounded staging queue.

These are design and future acceptance checks. They have not been exercised against an implementation. A follow-up reviewer should distinguish a written resolution from an observed working control.
