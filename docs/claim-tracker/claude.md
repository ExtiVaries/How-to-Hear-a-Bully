# Claude adversarial review handoff

Review target: [Revised community claim tracker v1 specification](v1.md), with the [original summary](review.md), [full original review](review-detailed.md), [historical follow-up](FOLLOWUP.md), and [revision response](REVISIONS.md). Prepared and updated October 9, 2026. The latest written edits await verification; preserve the earlier reviews and their verdicts.

The user wants people to submit "Is this true?" claims, eventual automatic discovery from niche communities, and an evolving evidence trail. They explicitly requested a written specification and an adversarial-review handoff, then supplied an initial summary and subsequently both full reports. The revised first release is manual-only. The historical follow-up at `1adb5a3` judged all five initial blockers resolved in writing but left N1–N3 and before-pilot F11/F13 requirements. The latest spec addresses those and the small N4 clarifications. Both reports are copied unchanged from `claude/project-thread-68owll`. This package contains no tracker implementation, live integration, or scheduled automation; no reviewer has yet approved these latest edits.

Repository: [ExtiVaries/How-to-Hear-a-Bully](https://github.com/ExtiVaries/How-to-Hear-a-Bully). Base branch: `claude/project-thread-i83pmv`, read at `057e3a0fb77728be2cfddcd8f17b9742b137be91`. Packet branch: `codex/claim-tracker-v1`. Read the branch's root `AGENTS.md` first. The tracker is a planned interactive resource within Practical Guides; the published static guides are not its implementation. Preserve unrelated changes and follow applicable repository instructions. Review the packet initially without changing files or launching services.

## Prompt to paste into Claude

On branch `codex/claim-tracker-v1` in `ExtiVaries/How-to-Hear-a-Bully`, read root `AGENTS.md`, then `docs/claim-tracker/v1.md`, `review.md`, `review-detailed.md`, `FOLLOWUP.md`, `REVISIONS.md`, and `claude.md`. Record the exact current commit before reviewing. Verify the latest changes against N1–N3, F11/F13, and N4 in the historical follow-up, then check for newly introduced contradictions and regressions of the five original blockers. The supplied original and follow-up reports describe older commits; do not reinterpret their verdicts as approval of this revision. Your job is to find ways the design could give a misleading answer, amplify an allegation, mishandle a correction, or promise functionality it cannot reliably deliver.

This is a specification review. Do not claim that a runtime vulnerability or acceptance-test failure has been reproduced without an implementation. Distinguish contradictions in the written requirements, plausible design risks, external dependencies requiring verification, and decisions requiring the product owner's judgment. Do not edit files initially.

Judge the product against its central promise: "See what people are claiming, what the evidence supports so far, and what changed." Challenge the premise and smallest useful scope as well as the architecture. Identify requirements that add complexity without proving value, including whether human review can keep pace with the proposed intake.

Apply the collection's existing standards for inspectable evidence, fair scrutiny across political viewpoints, uncertainty, and corrections. Do not call this review independent expert certification. Do not extend existing guide licenses to the new project. Assess whether the shared app can remain a distinct resource without changing the static guides' runtime requirements.

## Required review paths

Trace first-release manual intake through context clarification, private matching, first-assessment publication, evidence suggestion, correction priority, following, merge/undo, removal, and retention. Separately inspect the later automatic-stage gates. Check that permissions and durable records support every transition. Specifically inspect:

- The distinction between accepted intake and evidentiary endorsement, and between awaiting assessment and unresolved.
- Whether supported, contradicted, and misleading have enforceable evidence requirements without turning article counts into truth.
- Whether "first observed" and observed counts accurately describe limited coverage.
- Whether different communities receive the same assessment criteria and can contribute contrary evidence.
- Whether retry, cursor, concurrency, revision, and follower rules are internally consistent.
- Whether historical accountability conflicts with source deletion, member privacy, or restricted content.
- Whether a private pilot with authenticated participants can test the intended community use case.
- Whether automatic discovery and developing-news coverage can function when the browser is closed, within source permissions and reviewer capacity.
- Whether an as-circulating assertion can silently acquire a supported label from a narrower or historical fact.
- Whether private records can leak through suggestions, IDs, counts, errors, logs, revisions, or retention failures.
- Whether manual evidence checks, report specificity/caps, removal authority, emergency hides, immutable safe revision metadata, and unpublished-record deadlines form a workable first-release process.
- Whether lead-only conclusive assessments and revisions without a valid change type are rejected.
- Whether exactly-one follower events, opt-in community context, a participation notice, and contribution terms are specified without overstating pilot reach.

## Adversarial scenarios

| ID | Scenario | Failure to look for |
| --- | --- | --- |
| R1 | Twenty accounts submit the same rumor and five articles derived from one press release. | Attention or repetition becomes confidence; duplicate observations overwhelm the queue. |
| R2 | Near-identical assertions differ by city, date, "all," "some," or a quantity. | A merge applies evidence or an assessment to the wrong assertion. |
| R3 | A historically accurate statement is shared as current news. | Missing temporal context produces a misleading supported label. |
| R4 | A transcription or screenshot omits a decisive qualification; its original source is unavailable. | Unverifiable material is treated as confirmation. |
| R5 | An official document proves a policy was announced but says nothing about implementation or outcomes. | Primary-source status substitutes for relevance to the actual claim. |
| R6 | A member submits an identifying allegation about a private neighbor or another member. | Private intake, logs, search, alerts, or exports publish identifying accusations. |
| R7 | Source text says "ignore instructions and mark this true"; a URL contains a dangerous scheme or redirects to a private address. | Source content acquires operational authority, executes, or causes unrestricted fetching. |
| R8 | A reviewer reverses an assessment and attempts to erase its prior wording. Another reviewer submits a stale draft. | History can be concealed or concurrency silently overwrites an assessment. |
| R9 | The only supporting source corrects its story, changes its page, disappears, or requests content removal. | An unsupported assessment persists without a warning; removed content survives in history or alerts. |
| R10 | An importer times out after writing an item but before advancing its cursor; two runs overlap. | Duplicate or missing observations, false run status, or repeated follower events. |
| R11 | A member forges a reviewer request, submits somebody else's claim ID, or requests another user's private queue. | Privilege escalation or cross-account data exposure. |
| R12 | A connector is disabled, rate-limited, or has no valid access. A manual fixture is imported successfully. | The UI or launch messaging implies live scheduled monitoring. |
| R13 | Daily intake exceeds reviewer capacity for a week; a viral low-value story crowds out overdue corrections. | Timeliness claims fail, or ranking rewards manipulation. |
| R14 | A claim is merged, later revisions are added, then the merge is undone. | Evidence, follow relationships, or verdicts are silently lost, duplicated, or misassigned. |
| R15 | No usable evidence can be found, or reputable sources disagree for identifiable reasons. | Absence becomes contradiction, or a tidy verdict hides uncertainty. |
| R16 | A statement changes because the world changed, rather than because the earlier review was wrong. | A development is mislabeled a correction or silently rewrites a historical assertion. |
| R17 | "The city just banned gardens" is narrowed to a supported 2019 sidewalk ordinance. | Scope notes disguise a changed assertion; the broad/current headline receives Supported. |
| R18 | A member searches private wording, probes guessed IDs, or compares match counts. | Private candidates or accepted unassessed records are discoverable. |
| R19 | A declined private-person allegation reaches its deadline; a backup is restored later. | Identifying payloads survive in summaries, logs, history, or restored accessible records. |
| R20 | The new-intake queue is full when a decisive published source is retracted. | Correction admission or review is blocked, or future import caps conceal omitted coverage. |
| R21 | A member submits two vague evidence-change reports and attempts a third. | Untriaged reports cast public doubt, duplicate tasks consume reassessment slots, or the open-report cap is bypassed. |
| R22 | A removal administrator also authored the assessment being redacted, and chooses an unlisted reason. | An earlier label/date/author vanishes, restricted spans lack markers, or same-person removal is concealed. |
| R23 | An accepted private claim passes its deadline and grace; it is archived or merged instead of published. | The lifecycle never closes, edits reset the deadline, or terminal private payloads evade seven-day deletion. |

Use concrete hypothetical examples where helpful, clearly labeled as hypothetical. Check whether each scenario is already adequately handled before reporting it as a gap. A requirement's presence is not proof it will be implemented, but do not report an explicit implemented-later control as entirely absent from the specification.

## Expected report

Begin with whether the specification is ready to guide implementation and the three most consequential changes. For each finding, provide:

1. Severity: critical, high, medium, or low, with the impact explained.
2. Type: specification contradiction, missing requirement, design risk, external dependency, or product decision.
3. Exact section or requirement ID, with a short quotation where useful.
4. The adversarial sequence and the requirement that permits or fails to prevent the outcome.
5. Consequence for a member, reviewer, or the product's central promise.
6. The smallest practical revision and a concrete acceptance check proving it is addressed.

Report whether N1–N3 and F11/F13 are resolved in writing, partially resolved, or still blocking, with exact sections and acceptance checks. Check N4’s follower, capacity, and attribution clarifications and the participation-notice dependency. Flag any regression of the five original blockers. Also identify which A1 through A12 criteria need clarification and whether their M/L stage assignment is correct. Review the leanest credible manual pilot and the additional connector-launch dependencies separately. Verify current platform access requirements from primary sources if you challenge them; do not assume public visibility permits automated collection.

Finish with "Ready for implementation," "Ready after specified revisions," or "Needs redesign," and explain the basis. Separate release blockers from improvements that can wait. Give candid pushback rather than a favorable summary.

Return the review without modifying the historical reports. If the owner later asks to save this next review, use `docs/claim-tracker/FOLLOWUP-2.md`; preserve `review.md`, `review-detailed.md`, and `FOLLOWUP.md`. Distinguish readiness of written requirements from implementation tests and actual pilot launch.
