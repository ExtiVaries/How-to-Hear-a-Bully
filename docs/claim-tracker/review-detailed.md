# Community claim tracker v1: adversarial specification review

Reviewed: `docs/claim-tracker/v1.md` and `docs/claim-tracker/claude.md` on branch `codex/claim-tracker-v1` at commit `7c768a4` (draft PR #6). Review date: October 9, 2026.

This is the full report behind the [owner-supplied summary](review.md). It describes the initial specification, not the revision at `1adb5a3`; see [FOLLOWUP.md](FOLLOWUP.md) for what that revision resolved.

This is an AI-assisted adversarial review of a written specification. It is not independent expert certification. No implementation exists, so nothing below is a reproduced runtime failure; each finding is labeled as a specification contradiction, missing requirement, design risk, external dependency, or product decision. Platform terms cited in the specification (Reddit, Truth Social) were not independently rechecked here; the specification's own "checked October 9, 2026" note stands and the recheck-before-enable rule should remain.

## Verdict up front

**Ready after specified revisions.** The specification is unusually careful on the things most claim trackers get wrong: it separates intake from endorsement, awaiting from unresolved, repetition from corroboration, and corrections from new developments, and it already handles several of the sixteen scenarios well (see "Scenarios already handled"). It is not yet ready to guide implementation because five requirements are either internally contradictory or untestable as written, and one of them sits directly on the central promise.

The three most consequential changes:

1. **Decide what an accepted but unassessed claim looks like, and require the published record to show how the scoped assertion differs from what people are actually saying.** Today "Accepted" means published, and the submitted wording stays private, so the tracker can both list unchecked allegations and attach a "Supported" label to a narrowed version of a claim that is circulating in a misleading form (F1, F2).
2. **Shrink the first pilot to manual intake and bound the candidate queue.** Every imported post becomes a private candidate a human must triage, against a stated capacity of five assessments a day. Corrections have no priority over new intake (F3, F4).
3. **Specify how evidence changes are detected and who may remove history.** The specification forbids fetching submitted URLs yet requires flagging cited sources that change or disappear (A10), and the removal path that protects privacy is not in the permission table, so it is also an unguarded way to erase an assessment (F5, F6).

## Release blockers

### F1. Accepted claims are published before anyone has assessed them

- **Severity:** High. The tracker can become an index of unchecked allegations visible to every participant, which is the amplification the project is meant to counter.
- **Type:** Product decision, with a design risk.
- **Where:** Intake table, "Accepted: Specific, relevant, and suitable to publish within the pilot"; Pilot scope, "'Published' means visible to pilot participants"; Assessment table, "Awaiting assessment"; Screens 1, "Search accepted claims; filter by assessment".
- **Sequence (hypothetical):** A reviewer accepts "The state is ending its e-bike rebate on November 1" because it is specific and in scope. Capacity is five assessments a day and the backlog grows. The claim sits on the Tracker as "Awaiting assessment" for nine days, searchable, followable, with an observed count beside it. Participants read a list of claims the tracker hosts, and the label that matters is the one they skim least.
- **Consequence:** Breaks "what the evidence supports so far" for every claim in the backlog. The acceptance copy ("Acceptance is not evidentiary endorsement") is correct but does not survive a list view.
- **Smallest revision:** Choose one and write it into the spec. (a) Publish only once a first assessment exists, including Unresolved; before that, the claim is visible only to its submitters, followers who attached to it, and reviewers. Or (b) publish awaiting claims, but render them as questions ("Being checked: is the state ending…?"), exclude them from the default Tracker view, show no observed counts on them, and show how long they have been waiting. I recommend (a) for the pilot because it is simpler and costs nothing in a 20-30 person group.
- **Acceptance check:** With one assessed and one accepted-but-unassessed claim, a member who did not submit or follow the second claim cannot find it in Tracker search or filters (option a), or sees it only under a "being checked" filter, phrased as a question, without counts (option b).

### F2. The scoped assertion can be "Supported" while the circulating claim is misleading

- **Severity:** High. This is the most direct path to a misleading answer under the central promise.
- **Type:** Missing requirement, partly a contradiction between privacy and "see what people are claiming".
- **Where:** Manual submission, "Preserve submitted wording separately from the reviewer's precise assertion"; Claim identity, "Attaching a private candidate… keeps that candidate's wording and member identity private"; Assessment, "Supported: …this exact scoped assertion".
- **Sequence (R3, hypothetical):** Members submit "The city just banned front-yard vegetable gardens." The reviewer correctly scopes it to the verifiable fact: "In 2019, the city council passed an ordinance restricting front-yard structures over 4 feet, including raised beds." That scoped assertion is Supported. The submitted wording is private, so the published record shows only a correct statement with a green-reading label. A member who arrives asking "is the ban true?" sees "Supported."
- **Consequence:** Scoping, which is good practice, becomes a laundering step. The Misleading label exists but nothing requires the reviewer to apply it to the version people are actually repeating.
- **Smallest revision:** Add a required, reviewer-written, non-identifying "As circulating" field to every accepted claim (a paraphrase, not a member's wording), and a required "Scope note" whenever the scoped assertion drops or changes a time, place, quantity, or quantifier ("all", "some") present in the circulating version. When the scope note is non-empty, the reviewer must state an assessment of the circulating version too, which will usually be Misleading. Show both on the claim detail and in the Tracker list.
- **Acceptance check:** Publishing a Supported assessment on a claim whose scoped assertion adds or removes a date, place, quantity, or quantifier relative to the "As circulating" text is rejected unless a scope note and a circulating-version assessment are present; both render above the evidence on claim detail.

### F3. Automatic discovery feeds an unbounded human queue

- **Severity:** High. It fails R13 by construction and is the largest source of complexity in v1.
- **Type:** Design risk and product decision.
- **Where:** Automatic discovery, "Each run reads at most 50 new items per source"; "Imports create private source-post candidates. The reviewer selects the atomic claim"; Pilot scope, "up to five new claims per day"; developing-story feeds, "Match incoming articles… as evidence suggestions".
- **Sequence:** Five modest community sources producing 60 posts a day each yield 300 candidates a day. Most are not checkable claims. Two reviewers who can assess five claims a day now also triage 300 candidates, plus publisher-feed evidence suggestions for every active claim. The 50-item cap limits each run, not the day (48 runs a day). Nothing expires candidates, filters them, or caps the daily total.
- **Consequence:** Reviewer time goes to triage instead of assessments and corrections; the queue grows without bound; timeliness claims fail.
- **Smallest revision:** Make the manual-only pilot the default first release (the spec already permits it in the A2/A3 note). When a connector is added, require: a daily per-source candidate cap; an operator-set filter (keywords, flair, or minimum thread activity) applied before a candidate is created; automatic expiry of untriaged candidates after a stated period, recorded as an event rather than silently deleted; and bulk dismiss. Defer publisher-feed matching until after the pilot; the spec does not say how matching works without an LLM, and keyword matching will mostly add noise.
- **Acceptance check:** With a fixture source producing more items than the daily cap, the reviewer queue receives no more than the cap; the excess is counted on the Sources screen as "not queued"; candidates older than the expiry are marked expired with an event.

### F4. Corrections have no guaranteed priority over new intake

- **Severity:** High for credibility. A tracker that is slow to correct itself under load is the failure the collection's methods page warns against.
- **Type:** Missing requirement.
- **Where:** Screens 5, "Reviewer queue: Private candidates, duplicate proposals, evidence suggestions, correction requests, and overdue reviews"; "Reviewers prioritize relevance, timeliness, unanswered questions, and overdue corrections"; Product purpose, "Popularity affects discovery and investigation priority."
- **Sequence (R13, R1):** A viral, low-value story draws twenty submissions. Because popularity affects investigation priority, it outranks a week-old correction request showing that a published "Contradicted" relied on a misread table. The correction waits.
- **Consequence:** A known-wrong assessment stays live while the queue serves attention.
- **Smallest revision:** Define queue order: (1) evidence-invalidation flags and correction requests on published assessments, (2) overdue reviews, (3) everything else. Popularity may order only within the third tier. Show participants the age of the oldest open correction request on the Tracker page.
- **Acceptance check:** With a correction request and twenty duplicate submissions on another claim, the correction request appears first in the reviewer queue; the Tracker shows the oldest open correction's age.

### F5. Evidence changes must be flagged, but nothing is allowed to notice them

- **Severity:** High. A10 cannot pass as written, and R9's protection depends on it.
- **Type:** Specification contradiction.
- **Where:** Corrections, "If cited evidence is corrected, withdrawn, materially edited, or inaccessible, flag it and request reassessment"; Records, "do not fetch arbitrary submitted URLs on the server"; A10, "Source correction/removal triggers review".
- **Sequence (R9, hypothetical):** The only supporting article for a "Supported" claim is quietly updated to retract its key figure. No member notices. The server may not fetch the URL. The next-review date is seven days out, and the review reminder does not require re-opening each cited source. The assessment stays live with no warning.
- **Consequence:** "What changed" silently fails for the most important kind of change. Also, "materially edited" cannot be determined later without knowing what the source said at citation time.
- **Smallest revision:** Name the detection paths: (a) member correction requests, which already exist; (b) a required checklist item at every scheduled review to re-open each cited source and record "unchanged / changed / unavailable"; (c) optionally, a link checker limited to the operator's allowlist of publisher hosts, with the redirect, size, time, and private-network limits the spec already lists for any future fetcher. At citation time, store the permitted excerpt plus an archive reference (for example a Wayback Machine capture URL) so "materially edited" can be judged.
- **Acceptance check:** A scheduled review cannot be closed until every cited evidence record has a recheck result dated that day; an evidence record marked "changed" or "unavailable" puts "Evidence under review" on the claim detail.

### F6. The removal path is not in the permission table, so it can erase history

- **Severity:** High. It is the bypass for R8 ("a reviewer attempts to erase prior wording").
- **Type:** Missing requirement.
- **Where:** Corrections, "Audit history preserves accountability subject to required deletion and redaction… without the removed payload"; Participants table, which lists no removal or moderation permission; Records, "Review event: … moderation, or removal".
- **Sequence:** A reviewer regrets an earlier "Contradicted" wording. Ordinary revisions cannot erase it, so they mark the old revision for removal as "restricted content." The payload disappears; only a removal event remains.
- **Consequence:** The protection against concealment depends on a permission the spec never assigns.
- **Smallest revision:** Add removal to the permission table, restricted to the operator, with a required basis from a closed list (personal data of a private person, legal request, platform-required deletion, copyright). Reviewer-authored assessment wording is not removable except for the specific personal or restricted text, which is replaced with a visible "[removed: basis]" marker in that revision rather than deleting the revision.
- **Acceptance check:** A reviewer account cannot remove any revision content; an operator removal without a listed basis is rejected; after a removal, the revision still exists with its label, date, author, and a removal marker, and the removed text appears in no revision, inbox entry, search index, or export.

### F7. Duplicate matching is an indirect read path into private submissions

- **Severity:** High for a small invited group, where a match can identify a neighbor or colleague.
- **Type:** Missing requirement.
- **Where:** Manual submission, "Before creating another claim, show possible existing matches"; Screens 2, "inspect potential matches"; A5, "cannot… read private submissions from another member".
- **Sequence (R6, R11):** Member B types the name of a coworker into "Check a claim." The matcher, searching all claims and candidates, shows that a similar private submission already exists, or shows its text. B now knows someone else has made an allegation about that person.
- **Consequence:** Cross-account exposure of exactly the material the pilot excludes, through a feature that A5 does not test.
- **Smallest revision:** Restrict match suggestions to records the submitter could already read: published claims and their own submissions. Reviewer-only matching may use private candidates.
- **Acceptance check:** With a private submission from member A, member B's matcher returns no indication of it for an identical query, including no change in result count or timing class visible in the UI.

## Other findings

### F8. Declined and private submissions have no retention limit

- **Severity:** Medium. Identifying allegations about private people (R6) are excluded from publication but kept indefinitely in the database, logs, and backups.
- **Type:** Missing requirement.
- **Where:** "A declined submission includes a reason and remains private"; Archived, "Retained where permitted".
- **Revision:** Set a retention period for declined and expired candidates (for example 30 days), after which wording is purged and a reason-only event remains. Allow immediate reviewer purge for declined private-person allegations. Keep source-post text out of application logs.
- **Acceptance check:** A declined private-person allegation purged by a reviewer is absent from the record, search index, and logs; only the declined event and reason category remain.

### F9. "Observed in community X" can identify a submitter in a 25-person pilot

- **Severity:** Medium.
- **Type:** Design risk.
- **Where:** Screens 3, "observed communities"; Screens/attribution, "First observed by this tracker in…"; Manual submission, optional "community name".
- **Sequence:** Only one participant belongs to a small hobby forum. Their manual submission names it. The claim detail now says "first observed in [forum], Oct 3."
- **Revision:** Only imported source observations and reviewer-recorded sightings contribute to public community attribution. A member's community field is reviewer context unless the member opts in.
- **Acceptance check:** A manual submission with a community name produces no public community attribution unless the opt-in is set.

### F10. A merge of two assessed claims has no reconciliation rule, and undo can strand citations

- **Severity:** Medium.
- **Type:** Missing requirement.
- **Where:** Claim identity, "A merge never automatically transfers an assessment to a materially different assertion"; "Undo restores original associations; records added after the merge require explicit reassignment".
- **Sequence (R14, hypothetical):** Claims A (Supported) and B (Contradicted) are judged equivalent and merged into B. If they truly are equivalent, the two labels cannot both be right, but the spec does not say what the destination shows. Later, after undo, B's newer revision still cites evidence that has returned to A.
- **Revision:** Merging two claims with different published assessments requires a destination assessment revision in the same operation that explains both prior assessments. Undo flags any destination revision that cites evidence leaving with the undone claim as "Evidence under review." A merged-away claim's assessment history remains readable at its redirect.
- **Acceptance check:** A merge of two claims with conflicting assessments without a new destination revision is rejected; after undo, a destination revision citing moved evidence shows "Evidence under review."

### F11. Leads can still be the only basis for a conclusive label

- **Severity:** Medium.
- **Type:** Missing requirement.
- **Where:** Evidence, "A screenshot, anonymous allegation, or unverifiable quotation is a lead whose limitations remain visible"; A6.
- **Sequence (R4):** A transcription of a screenshot is the only support; the original post is deleted. The reviewer records it with visible limitations and publishes Supported. Nothing forbids that.
- **Revision:** Make "lead" a review disposition that cannot by itself satisfy the evidence requirement for Supported, Contradicted, or Misleading.
- **Acceptance check:** Publishing a conclusive assessment whose only cited evidence is lead-disposition is rejected; Unresolved citing it is allowed.

### F12. A documented negative search is sometimes real evidence

- **Severity:** Low to medium.
- **Type:** Specification clarification.
- **Where:** "Missing evidence never defaults to contradicted."
- **Sequence (R15):** "The council passed Ordinance 24-117 banning X." A search of the council's complete public ordinance register finds no such ordinance. That is a reasoned basis for Contradicted, not mere absence.
- **Revision:** Allow an evidence type "documented search of an authoritative record," requiring the record searched, why it would be complete for this question, query terms, and date. A general "we found nothing" stays insufficient. Add a reason code to Unresolved (insufficient, conflicting, not yet knowable) so the list view does not flatten R15's two cases.
- **Acceptance check:** Contradicted citing only a documented-search record with all fields is accepted; one missing the completeness rationale is rejected.

### F13. Every revision needs an explicit change type

- **Severity:** Medium.
- **Type:** Missing requirement.
- **Where:** "Distinguish correction of an earlier mistake from a new development in the world"; "A material claim change requires a new linked claim."
- **Sequence (R16):** "The city bans sidewalk gardens" is Contradicted in January. In March the council passes the ban. If the assertion has no period, is this a new claim or a revision? Either path is permitted, and the follower inbox can show "assessment changed" without saying the earlier assessment was right at the time.
- **Revision:** Present-tense claims carry an implicit "as of [assessment date]". Each revision carries a required change type: correction of our error, new development, evidence lost or changed, scope or wording edit. A new-development revision keeps the earlier dated assessment visible as accurate for its date. The inbox shows the change type.
- **Acceptance check:** A revision cannot be published without a change type; a new-development revision renders the prior label with its date and without "corrected."

### F14. Fair scrutiny depends on selection, which the spec does not record

- **Severity:** Medium. With one or two reviewers and three to five communities, bias enters through which communities are monitored and which claims get accepted or assessed first, not through the label rules.
- **Type:** Missing requirement and product decision.
- **Where:** "Apply the same evidence criteria to every community and viewpoint"; Launch, "named communities with permitted access".
- **Revision:** Record and show participants a short rationale for each monitored community. In the pilot evaluation, report per community: candidates, accepted, declined (by reason), assessed, and label distribution, and have someone other than the reviewer sample declined items. Recruit invited participants from the range of viewpoints present in the niche, since only invitees can contribute contrary evidence.
- **Acceptance check:** The Sources screen shows each community's selection rationale; the pilot report includes the per-community table.

### F15. The pilot can test the reviewer workflow, not the community use case

- **Severity:** Medium. This affects what the pilot can honestly claim.
- **Type:** Product decision.
- **Where:** Pilot scope, invitation-only; Delivery order and pilot evaluation.
- **Analysis:** Members of the monitored communities are not participants, cannot see assessments, and cannot contribute contrary evidence. A four-week private pilot can test whether invited people understand scoped claims, uncertainty, and updates, and whether reviewers can sustain the workflow. It cannot test whether assessments reach the people who saw the claim or whether communities engage with them.
- **Revision:** Say so in the evaluation section, and do not report pilot results as evidence of community impact.

### F16. Import idempotency is nearly complete; three edge cases remain

- **Severity:** Medium.
- **Type:** Missing requirement.
- **Where:** Automatic discovery, cursor and overlap rules; "Import a source item once using a stable source-item identity."
- **Sequence (R10):** A run times out, its lock expires, a second run starts, and the first run is still writing (overlap despite the rule). Separately, a source post is edited after import and its later wording is never captured; or its author deletes it, and the platform's terms may require the stored copy to be deleted too (to be verified per platform).
- **Revision:** Use a run lease with a fencing token so a stale run's writes and cursor updates are rejected. Define behavior for source-item edits (record a new observed version or ignore, stated) and deletions (honor where required, using the F6 removal path with "platform-required deletion" as basis).
- **Acceptance check:** A3 extended: with an expired lease, the stale run's cursor update is rejected and no duplicate observation exists; a fixture deletion event removes the stored wording.

### F17. Single-reviewer publication and reviewer conflicts

- **Severity:** Medium.
- **Type:** Product decision.
- **Where:** Participants table; "a designated reviewer for each active task".
- **Analysis:** One reviewer can define the claim, choose the evidence, write the rationale, and publish with no second look, including on claims they submitted themselves. A two-person rule would roughly halve throughput at the stated capacity.
- **Recommendation:** Disallow assessing a claim one submitted; for the pilot, require a second reviewer's sign-off only for Contradicted and Misleading, and spot-check a weekly sample of Supported.

### F18. Smaller items

- A9 says "at most one follower event" per material revision. A broken inbox that produces zero passes. Change to exactly one per active follower. "Material" is undefined; make a label change always material and require a recorded "notify followers" decision for other revisions.
- Observed counts and "popularity affects investigation priority" invite sockpuppet attention in any later public version (R1). For the pilot, show no counts and dedupe manual submissions by member if counts are ever shown.
- "Exports" are mentioned only in A10 and the removal section. Either define the export feature or drop it from the checks.
- Whether the publishing reviewer's name is shown to participants is undecided. It trades accountability against harassment risk; decide before launch.
- Next-review reminders do not need a scheduler in a manual-only pilot: compute "overdue" when the queue is read.
- The two platform examples (Reddit and Truth Social) should follow the niche choice. If the niche is products or technology, the likely sources (public forums, RSS, project discussion boards) each still need their own terms check.
- A participation notice is a launch dependency: what is stored, who sees it, retention, how to request removal, and the terms for member contributions, since reuse terms are undecided.

## Scenarios already handled adequately

- **R5** (official document proves an announcement, not an outcome): explicitly covered in "Evidence and source independence".
- **R7** (prompt injection, unsafe URLs, redirects to private addresses): covered by text-only rendering, HTTP/HTTPS validation, no server fetch of submitted URLs, approved connector hosts, and the AI-has-no-authority rule. Only addition: render outbound links with `rel="noopener noreferrer nofollow ugc"` and show the destination host.
- **R8** concurrency: revision checks, stale-write rejection, and atomic audit events are specified. The erasure half of R8 is F6.
- **R2** near-identical claims: the claim identity rule ("assertion, entities, jurisdiction, relevant period, quantities, and material qualifiers") and A4 are sound.
- **R9** after detection: "immediately publish an unresolved revision" when sole decisive support is invalidated is the right rule. Detection is F5.
- **R12** connector honesty: "enabled" requires verified end-to-end import, fixtures are labeled test data, and A12 covers labeling.
- **R1** repetition as corroboration: underlying-source groups and A7 cover the evidence side. Note that A7 can test display and counting only; whether reviewers group sources correctly is a judgment to audit in the pilot.
- **Separation from the static guides:** the specification keeps the tracker as a separate resource without backend dependencies for the published guides, and does not extend Bully's license. No change needed.

## Acceptance criteria needing clarification

| ID | Clarification |
| --- | --- |
| A1 | Replace "correct privacy and role access" with the enumerated visibility rules for submitter, other member, reviewer, operator. |
| A3 | Add expired-lease overlap, source-item edit, and deletion cases (F16). |
| A4 | Add conflicting-assessment merges and undo after post-merge revisions (F10). |
| A5 | Add the duplicate-matcher leak (F7). |
| A6 | Add lead-only evidence rejection and documented-search acceptance (F11, F12). |
| A7 | State that it tests display and counting, not grouping accuracy. |
| A8 | Add removal permission and basis (F6). |
| A9 | "At most one" becomes "exactly one per active follower"; define material. |
| A10 | Specify the detection path it tests (F5). |
| A11 | Every record already needs reviewer acceptance, so the private-person clause passes trivially; test retention and purge instead (F8). |

New criteria to add: scoped-versus-circulating disclosure (F2), queue order and candidate cap (F3, F4), and awaiting-claim visibility (F1).

## Leanest credible pilot

Manual intake only, invite-only, one niche, one reviewer plus a second for the sign-offs in F17, no connectors, no publisher feeds, no counts. Reviewers record sightings by hand ("seen by reviewer in [community] on [date], link"), which tests whether community discovery adds value before anyone builds a connector. Claims become visible to others only when first assessed (F1). Keep the in-product inbox, corrections, and revision history, since those are the product's distinctive promise. Run four weeks, measure as the spec proposes plus the per-community table from F14, then add one authorized connector with the F3 caps.

## Launch dependencies that cannot be assumed

- A chosen niche and named communities, with a recorded selection rationale.
- Platform permission for any connector, rechecked against current terms at enable time.
- Accountable reviewers with enough time for the stated capacity, and a named operator for removals.
- An identity provider and a host with durable server storage and a scheduler (scheduler not needed for a manual-only pilot).
- A participation notice and contribution terms (reuse terms remain undecided).

## Blockers versus improvements that can wait

- **Before implementation starts:** F1, F2, F5, F6, F7 (they change the data model or permission table).
- **Before any connector is enabled:** F3, F16.
- **Before the pilot opens:** F4, F8, F11, F13, the participation notice.
- **Can wait until after the pilot:** F9 (if no manual community field is shown), F12, F14's external sampling, F17's second-reviewer rule if one reviewer is used with weekly spot checks, and the smaller items in F18.
