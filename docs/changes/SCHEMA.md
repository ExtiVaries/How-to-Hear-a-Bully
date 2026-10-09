# Public timeline record, version 1

Canonical file: `docs/changes/timeline.json`. HTML, public `changes/timeline.json`, and the Markdown reading edition are generated from it. The update script validates it before a proposal or write. Prose is plain text and is escaped in HTML.

| Field | Type and meaning |
| --- | --- |
| `schema_version` | Integer `1` |
| `coverage` | `start`, `end` ISO dates; `description` and `selection` prose. Bounds of this curated record, not a national completeness claim |
| `events` | Array of events, each with a stable unique `us-…` ID |
| `history` | Append-only substantive revisions with `id`, `event_id`, `date`, `kind`, `reason`, and full `before` event |

Each event has these distinct fields:

| Field | Type and meaning |
| --- | --- |
| `id`, `series`, `related_events` | Stable slug, history grouping, array of existing IDs. Do not change an ID when a headline changes |
| `title`, `what_happened` | Headline and specific institutional act |
| `event_date` | `{value, precision}`; day `YYYY-MM-DD`, month `YYYY-MM`, or year `YYYY`. Never invent day precision |
| `first_recorded` | ISO date first entered in this history; immutable |
| `last_substantive_revision` | ISO date claim, interpretation, scope, or document version last changed |
| `last_successful_source_check` | ISO date or null; full successful comparison for this entry, separate from individual source access |
| `effective_date` | Date object or null. Do not put a proposed service start here as an established effective date |
| `jurisdiction`, `scope` | Array of named jurisdictions and prose identifying affected people/institutions |
| `action_type` | Specific institutional act, such as proposal, ruling, regulation, or institutional-capacity change |
| `legal_status`, `applies_now` | Procedural position and what is established now; separate from the act and its consequences |
| `previous_position`, `what_changed` | Baseline and incremental change |
| `practical_effects` | Array of `{kind, text, source_ids}`. Kind: documented, reported, measured, inference, forecast. Empty means none established here, not no harm |
| `uncertainty`, `update_trigger` | Known gaps and evidence that justifies another update |
| `sources` | Public HTTPS sources with local unique IDs, title, publisher, locator, supports, date, access, and version note |
| `check_note`, `check_interval_days` | Check coverage/limits and topic-specific review interval, 1–365 days |

Sources distinguish `last_checked` from `document_date`; either may be null. Access is `full`, `indexed`, or `blocked`. Optional `content_sha256` and `evidence_note` identify compared byte versions and the comparison performed. A first stored hash establishes a comparison baseline; a changed hash requires review, including benign page changes. A hash does not establish truth. Current docket or implementation gaps belong in the event's uncertainty and check note even when listed documents load successfully.

New events require editorial review and deduplication. The engine rejects duplicate IDs and exact identities defined by series/date/action/source URLs; near duplicates with different sources need editorial comparison. All updates currently remain review-gated. No database, network-fetching agent, or public scheduler is hidden in this format.
