# Community claim tracker revision response

October 9, 2026. The [initial summary](review.md) describes `7c768a4`. The [full original report](review-detailed.md) and [historical follow-up](FOLLOWUP.md) were subsequently supplied on `claude/project-thread-68owll` and are copied unchanged into this packet. The follow-up reviewed `1adb5a3` and found the five initial blockers resolved in writing, with three remaining edits and additional before-pilot requirements. Its verdict remains **ready after specified revisions**; it is not an approval of the latest spec.

The current [specification](v1.md) addresses those remaining findings. A targeted internal consistency check found no blocking contradictions in the written changes. Verification by the follow-up reviewer, implementation, runtime acceptance checks, and launch remain pending.

## Initial five blockers

| Finding | Written revision | Acceptance criteria |
| --- | --- | --- |
| Unassessed publication and narrowed claims | Accepted intake stays private until first completed assessment. Require as circulating, assessed assertion, and scope note; a narrower/historical fact cannot determine Supported for a broader/current rumor. | A1, A6, A12 |
| Unbounded automatic intake and correction priority | Manual-only first release, two open new submissions/member, 20 hard ceiling, age-based intake pause. Specific reviewer-triaged corrections have priority; later imports have caps, expiry, and coverage gaps. | A2, A3, A10, A12 |
| Undefined detection and removal authority | Specific reports and dated manual checks supply detection. Separate removal permission, listed bases, safe immutable revision metadata, and audit apply to hides and redactions. | A5, A8, A10 |
| Private duplicate disclosure | Members match only authorized published summaries; no private counts, identities, or distinguishable inaccessible-ID responses. | A1, A4, A5 |
| Declined allegation retention | Seven-day maximum for terminal private payloads, daily retention, 30-day restricted backup expiry, and deletion before restored access. | A10, A11 |

## Latest changes responding to the follow-up

| Finding | Written change | Check or gate |
| --- | --- | --- |
| N1: public doubt and unbounded reports | Evidence-change reports identify cited evidence and concrete change; assessment corrections identify the revision and specific error. Private specificity triage precedes banner and substantive reassessment. Two open correction reports/member from receipt to disposition; third refused, duplicates coalesced, dismissals explained. Confidential privacy escalation remains available without automatic publication or hiding power. | A10, A12 |
| N2: removal can erase accountability | Closed bases: Private-person data, Legal request, Platform-required deletion, Copyright. Remove only restricted spans, with `[removed: basis]`. Revision label, dates, and stable non-identifying reviewer handle remain visible, including during a hide. Label overlapping roles and removal by the reviewing author. | A5, A8, A10 |
| N3: accepted private records never end | First-assessment deadline within three working days of acceptance; Expired after three-calendar-day grace without publication. No edit/reassignment clock reset. Purge within seven days of expiry; unpublished archive/merge also triggers purge. Published dated assessments do not expire. | A11 |
| F11: lead-only conclusive labels | Explicit Lead disposition for screenshots/transcriptions, unverifiable quotations, and anonymous allegations. Supported, Contradicted, and Misleading require reviewed non-lead evidence establishing the relevant point. Explained Unresolved may cite leads. | A6 |
| F13: revision type | Required Initial assessment for first publication only; later types: Correction of our error, New development, Evidence lost or changed, Scope or wording edit. History/inbox show type; a development preserves the earlier dated assessment without calling it corrected solely because the world changed. | A8 |
| N4/F18: inbox and materiality | Exactly one durable event per active follower at commit, including retries. Label/material evidence changes and merge/archive notify; other revisions need an explicit notify decision/reason. | A9 |
| N4/F9: attribution privacy | Member-supplied community context is private unless explicitly opted into publication; reviewer public sightings are separately attributed. | A11 |
| N4: capacity limits | Age pause and correction priority govern first; 20 is a ceiling, not a target. Proposed capacity is not measured performance. | A12; pilot evaluation |
| Participation notice/F18 | Before inviting members, notice explains data, visibility, attribution, retention/backups, removal, correction, stable reviewer handles, and contribution terms. Contribution/reuse terms must be decided before opening. Member exports are deferred; tracked operator copies remain subject to removal/retention. | Manual launch prerequisite |
| F15: evaluation limits | Private pilot tests reviewer workflow and invited-member understanding; it cannot demonstrate wider community reach or impact. | Pilot evaluation |
| F16: later import edge cases | Run leases use fencing; stale writes/cursors fail. Edits create dated versions under stable item IDs; required platform deletions use the audited removal path. | A3, before any connector |

## Release stages and deferred decisions

Manual launch requires M checks A1 and A4 through A12, a chosen niche, accountable reviewers and weekly spot checks, a removal administrator, hosting/identity/storage meeting retention rules, and the participation notice with contribution terms. No connector, publisher feed, automated verdict, popularity count, or automatic evidence-change detection is promised in this release.

A2, A3, and A12's L portion gate later discovery. Enable one authorized live source only after permissions, measured spare capacity, admission/expiry controls, fenced retries, edit/deletion handling, and coverage reporting are verified.

The follow-up permits these refinements after the pilot: F10 assessed-merge reconciliation, F12 authoritative negative-search evidence, F14 selection audits/external sampling, and F17 reviewer conflicts/second sign-off. These are tracked future work, not claimed fixes. Existing safeguards against changing material scope, transferring mismatched assessments, and losing merge associations still apply. Any implementation exposing an unresolved unsafe operation must keep it unavailable until its rule is settled. General absence of evidence does not become Contradicted while F12 is deferred. Single-reviewer publication remains the documented pilot choice, with weekly assessment spot checks; second-person sign-off is not implied.

## Next verification cases

1. Submit a vague source-change report: no public banner, safe dismissal reason. A specific cited-evidence report gets a banner only after specificity triage; its truth still awaits review. Refuse the member's third open report.
2. Reject an unlisted removal basis. With dual-role credentials, redact only restricted text and preserve each revision's label, dates, author handle, marker, and same-reviewer disclosure through pages and inbox.
3. Let an accepted record miss its first-assessment deadline plus grace; verify Expired and seven-day purge. Archive/merge an unpublished record and verify it cannot evade that rule; a restored backup must apply deletion before access.
4. Reject all three conclusive labels with only Lead evidence; allow an explained Unresolved. Reject a revision without a valid change type; show a development's prior dated assessment without a false correction label.
5. Retry a material publication with active followers: exactly one durable inbox event each, and none after committed unfollow. Verify private community context stays absent unless opted in.
6. At full new-intake capacity, admit a specific correction within the member cap after triage, prioritize it, and publish Unresolved immediately when a reviewer confirms sole decisive support was invalidated.
7. Before inviting participants, inspect the notice, agreed contribution terms, reviewer handles/roles, retention-capable host, and passed M checks. These launch dependencies cannot be satisfied by prose alone.
8. Before L, expire an import lease while its process continues, edit a source post, then require deletion: stale writes fail, versions remain correctly attributed, and prohibited wording is removed.

These are written design requirements and future acceptance cases, not reproduced runtime successes.
