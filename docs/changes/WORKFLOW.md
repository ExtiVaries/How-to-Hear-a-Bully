# Curated timeline: operator workflow

This is a proposed, review-gated workflow. No schedule or unattended public publication is enabled by these files. A draft PR is reviewable work, not a deployed release. The existing Notion research automation stays in place.

## One research process, one public history

Keep Notion as the research backend for now, with the repository as the durable curated public record. The existing research process resolves registry pointers and produces its assessments; a bounded editorial export checks underlying public documents for selected timeline topics. It does not generate a competing assessment of the country. This lets us test public-history preservation before moving the research system itself.

Moving all structured research into the repository could eventually reduce dependency on private publication pointers and make provenance easier to review. It also requires migration of immutable releases, private operational state, retention and recovery, scheduler authentication, and publication policy. The present public selection is neither a replacement for Security/Rights/Traveler assessments nor permission to expose private ledgers. Test that migration separately, approve activation, then retire the former destination only after recovery and comparison tests succeed. Do not run two independent researchers rewriting the same history.

## Distinct responsibilities

- **Scheduler:** wakes the task; it does not prove tool access, GitHub authentication, branch permissions, or unattended execution.
- **Research:** uses current registry pointers and release baselines, checks primary public documents, and marks partial access honestly. The private Verified comparison field does not certify underlying facts.
- **Validation:** enforces IDs, dates, source references, immutable history, no deletion, and complete candidate integrity. Editorial review establishes wording and interpretation; neither JSON validation nor HTTP 200 does that.
- **Repository update:** applies an exact reviewed candidate against a known baseline under an exclusive writer lock, then builds and checks the entire site. The task produces a draft PR on a branch distinct from the current Pages branch.
- **Deployment:** follows separate release approval and existing site publication conditions. No automatic merge or deployment is included.

Recommend one daily editorial check at 09:00 **America/New_York**, proposed and unconfirmed. Existing six-hour research need not force four public rewrites a day. Daily curated checks reduce churn while permitting a manually requested urgent check. Active matters use a seven-day due interval by default; settled history uses 30 days. An entry's interval is configurable from one to 365 days. Staleness is computed per topic from its last complete source comparison; a partial check does not make an old topic look current. Selection and coverage dates describe the record's bounds, not comprehensive national surveillance. Confirm the timezone before creating any actual schedule.

## Record and candidate contract

`timeline.json` is the canonical source for HTML and public machine-readable data. IDs stay stable, series connects related steps, event-date precision remains explicit, and related IDs must exist. The identity guard rejects the same series/date/action/source set under a different ID; editors must additionally examine near duplicates with different sources. No fuzzy deduplication can establish whether two legal steps are the same event.

First-recorded dates are immutable. An old event discovered today keeps its historical event date and gets today's first-recorded date. Existing entries cannot disappear. A correction or substantive development appends the complete previous event, a stable history ID, date, kind, and editorial reason to `history`; the renderer links the old record and the current event. Existing history must preserve identical parsed content. Amended source documents and changed interpretations are substantive changes, even when the URL remains unchanged. Preserve the prior document/version explanation in the snapshot; source bytes are not retained in the public repository. A substantive amendment clears the current entry's complete-check date: the old date remains in its historical snapshot and cannot imply that revised claims have been checked.

Successful checks require a source-by-source report with a calendar date, content SHA256, and a note explaining the comparison. The engine retains each source's `content_sha256` and `evidence_note`. The initial record may lack a hash; its first reported full comparison establishes a baseline. A later differing hash rejects the check-only path and requires an amended-source candidate and editorial review. Dynamic page bytes can change without changing their substantive evidence; that still needs a reviewer to establish what changed. These values are operator-supplied evidence, not independent certification or automatic fetching. A fabricated hash or comparison note cannot be discovered by format validation alone. A failed fetch, an index snippet, or HTTP success alone is insufficient. A partial report can advance the source that was actually compared, but retains the topic's last complete check. No outcome creates a new event automatically.

Example check report (use actual public document evidence, never these placeholders):

```json
{"us-example": {"s1": {"result": "success", "date": "2026-10-09", "content_sha256": "<64 lowercase hex characters>", "evidence_note": "Compared operative paragraphs and publication version"}, "s2": {"result": "failed"}}}
```

An `amended` result or a changed previously stored hash rejects the check-only path. Prepare a substantive candidate instead. A failure leaves the canonical file untouched. Never treat unlisted sources as checked. Recorded and successful-check dates cannot exceed the update's actual date, and check dates cannot move backward. A complete check must be backed by full-access sources with individual successful dates at least as recent. Every changed candidate requires an editorial reason, including check-only metadata changes. Private IP addresses, loopback and local hostnames, credential-bearing URLs, and Notion evidence URLs are rejected, but the editor must also inspect prose and URLs for private information before a PR. URL syntax checks do not establish a public domain's access permissions or resolve its DNS; the research process must verify that the actual document is public and safely accessible.

## Complete local update cycle

Use short temporary paths. A full fixture path such as this checkout plus `scripts/.test-xxxxxxxx/record.json` remains well below 180 characters. Tests copy only tiny JSON fixtures. Do not copy dependencies, source trees, profiles, or private research into evidence.

1. Confirm Git root, branch, status, writer ownership, and the current canonical SHA256. Work on a non-Pages branch. Refresh the baseline before every proposal.
2. Write a raw candidate JSON outside the canonical path, preserving history. For check-only work, prepare a bounded source report.
3. Validate and prepare the candidate:

```sh
python scripts/update_timeline.py validate
python scripts/update_timeline.py propose --candidate /short/raw.json --output /short/review.json --reason "Explain the supported change" --kind development --date 2026-10-09
# Or, for a bounded check-only candidate:
python scripts/update_timeline.py checks --report /short/report.json --output /short/review.json
```

4. Review the candidate, sources, headline, immutable history, and diff. The printed SHA256 identifies the exact candidate reviewed. Apply locally only after that review; pass the printed baseline and candidate hashes. Use the same reason, kind, and date used when preparing a substantive proposal:

```sh
python scripts/update_timeline.py apply --candidate /short/review.json --baseline <canonical-sha256> --review-sha256 <candidate-sha256> --reason "Explain the supported change" --kind development --date 2026-10-09
python scripts/test_timeline.py
python scripts/build_suite.py
python scripts/check_site.py
git diff --check
```

5. Inspect regenerated HTML, public JSON, internal anchors, mobile and keyboard operation, sources, and corrections. Stage only the intended files. Commit and push the review branch using the approved authenticated GitHub tool, then create a **draft** PR containing the validation results and unresolved claims. Link and attach the created PR to the task. Do not merge it or push directly to the Pages branch.

The Python engine intentionally has no GitHub credentials, network fetching, deployment, or automatic commit logic. A demonstrated authenticated branch push and draft PR proves that interactive workflow only. Unattended operation still requires a tested scheduler host with least-privilege repository/PR write access, build dependencies, safe checkout refresh, and operator failure delivery. Do not infer those from the task's existence or from interactive access.

A successful source report cannot predate the entry's last substantive revision, and a complete-check date must be on or after that revision. Old comparison evidence therefore cannot restore freshness after changed claims; compare the revised entry against its sources again.

## Recovery, overlap, and publication policy

The engine creates `<record>.lock` exclusively and records its PID, UTC start time, and unique ownership token. A second writer fails; it never steals the lock. Cleanup checks the token and retains an altered replacement lock. After a crash, an operator checks that exact PID, host and task ownership, current baseline, and incomplete work before removing the abandoned lock. The lock protects engine writers only: editors and other tools must respect the one-writer contract. Under the lock, baseline and candidate hashes are computed from the exact bytes that are parsed, avoiding an independent hash/read race. SHA256 baseline comparison rejects a changed record. Repeating an already-applied exact reviewed candidate acknowledges no change even with its original baseline. Candidate validation completes before same-directory atomic replacement; invalid input never replaces the last good canonical file. Build failure must prevent PR completion or merge; it does not justify replacing deployed output. Keep failure details in operator/task records, not the public timeline.

Currently **all repository updates need review**, including successful check-only candidates. A future approved policy could permit machine-validated check-only updates when every listed source was fully compared, no source changed, no claim or date interpretation changed, and full site checks passed. It must still use an audited authenticated writer and clear failure notification. New events, corrections, amended documents, ambiguous legal effects, contradictions, unsupported claims, changed scope, and substantive reinterpretations always need editorial review. A global rebuild timestamp must never stand in for topic freshness.

The exact proposed prompt is `schedule-prompt.txt`; its proposed configuration is `schedule.json`. Neither creates a scheduler task. Activation requires timezone confirmation, explicit policy approval, an unattended authentication/permissions test, and a recovery rehearsal. Preserve the existing automation until a replacement passes those checks and its activation is approved.
