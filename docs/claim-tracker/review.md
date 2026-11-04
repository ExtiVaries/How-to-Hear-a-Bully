# Community claim tracker review summary

Review supplied by the project owner on October 9, 2026, concerning the initial specification at commit `7c768a431d94d8dc0c4f0649a759a1a4db6a127a` on `codex/claim-tracker-v1`, PR #6. The verdict was **ready after specified revisions**. This is the summary pasted into the task, not the full detailed review. The supplied attachment named `independent-review_md.md` reviews **Complain or Constrain?** and is unrelated to this tracker; it is not reproduced here.

At the time this summary was recorded, the detailed sections were unavailable. The owner subsequently supplied the [full original report](review-detailed.md) and [follow-up review](FOLLOWUP.md) on `claude/project-thread-68owll`; both are now copied unchanged into this packet. The [revision response](REVISIONS.md) distinguishes initial changes from the latest responses. The pasted summary below remains unchanged. Neither historical report approves the latest edits; no runtime checks or expert certification are represented by this record.

## Supplied tracker review

My verdict is **ready after specified revisions**. I don't think it needs a redesign. The spec already handles several of the 16 scenarios well: official documents that prove only an announcement, prompt injection and unsafe URLs, concurrent edits, and labeling connectors honestly. Five places still need fixing before anyone builds from it.

**The three most consequential changes:**

1. **Unassessed claims are published, and what people are actually saying stays private.** "Accepted" currently means visible to every participant, so the backlog becomes a list of unchecked allegations. Also, because submitted wording is private, a reviewer can narrow "the city just banned gardens" to a true 2019 ordinance and label it Supported, while the version people repeat is misleading. The fix is a required "as circulating" field with a scope note. I'd also show a claim to other participants only after its first assessment.
2. **Automatic discovery feeds an unbounded human queue.** Every imported post becomes a candidate someone has to triage, and capacity is five assessments a day. Corrections also get no priority over popular new claims. I'd make the manual-only pilot the first release, and add per-source caps, expiry and a priority lane for corrections before any connector.
3. **Evidence-change detection and removal authority are undefined.** The spec requires flagging cited sources that change or disappear (A10), but it also forbids the server from fetching them, so nothing can notice. Removal of history isn't in the permission table either, which means a reviewer could use it to erase an earlier assessment.

Two other blockers: the duplicate matcher can reveal other members' private submissions, and declined allegations about private people have no retention limit. The review also covers clarifications for 10 of the 12 acceptance criteria, the leanest credible pilot, and what blocks which stage.

## Recording status

The owner provided this summary after the initial handoff requested authorization to commit a review. The summary has now been recorded alongside the revised specification. This recording does not constitute approval of the revised design, a follow-up review verdict, authorization to merge PR #6, or authorization to deploy a service.

Subsequent recording: the original and follow-up reports are now available alongside this summary. The follow-up at `1adb5a3` found the initial blockers resolved in writing and specified remaining edits; the latest specification implements those written changes. Verification of the latest revision and all implementation checks remain pending.
