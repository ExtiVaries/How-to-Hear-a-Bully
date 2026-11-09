# TENT court-source recheck — November 2, 2026

Scope: bounded correction to existing draft PR #18. Publication hold remains; no merge or deployment authorized.

## Primary records inspected

- [October 30 published orders](https://www.txcourts.gov/supreme/orders-opinions/2026/october/october-30-2026/): case 26-1246, In re Texas Transgender Student Union LLC, from Travis County; administrative stay; mandamus petition and temporary-relief motion pending; Justice Sullivan not participating.
- [Official case docket](https://search.txcourts.gov/Case.aspx?cn=26-1246&coa=cossup), inspected through the public Case Search interface: October 29 petition, emergency motion, and mandamus record; October 30 court order. No later event or response filing was displayed. TENT is the real party in interest, distinct from the LLC relator. Trial case D-1-GN-26-010559, 345th District Court, Travis County.
- [One-page October 30 order](https://search.txcourts.gov/SearchMedia.aspx?MediaVersionID=c31f6085-6d37-4d83-9d07-709f81721cef&coa=cossup&DT=ORDER%20ISSUED&MediaID=37d54909-208f-4bc8-a072-43762184f154), read visually in the official PDF viewer: administratively pauses the October 28 order for the LLC corporate representative's pre-suit oral deposition without reaching the merits; requires the real party's response by 10 a.m. Monday, November 2; leaves the petition and temporary-relief motion pending.
- The companion clerk letter confirms the administrative stay and Sullivan's nonparticipation. The emergency motion's cover and docket entry were inspected, but its substantive arguments were not assessed. Neither the full petition nor the mandamus record was substantively reviewed.

The Case Search interface warns that data refresh nightly. Absence of a displayed response or newer order is an observation about the available record, not proof that nothing has been filed or issued. The published orders index still listed October 30 as its most recent release when inspected. A fresh docket check is required before eventual publication.

## Comparison with PR #18 at 103892400ed667d2bdcd52b554aa09051d491b8b

| Draft claim or limitation | Result and correction |
| --- | --- |
| Temporary block on questioning, sourced to reporting | Supported and narrowed to the specific October 28 deposition order; add official identifier and direct order citation. |
| Court gave no explanation | Order supplies procedural terms but no substantive rationale; distinguish those terms from speculation about motive. |
| November 2, 10 a.m. response deadline | Confirmed directly by the order; add Central context and historical tense. It is neither a ruling date nor a stated automatic stay expiration. |
| Full order and motion not independently inspected | Superseded for the one-page order. Retain the limit on substantive motion review. |
| Text attribution, denials, and unproven mailer connection | Preserve attribution to the October 30 Tribune report. The inspected court records do not establish printed-mailer sponsorship or liability. |
| Possible procedural explanations and election effects | Retain as editorial possibilities; neither the stay nor election timing establishes motive or resolves the underlying dispute. |

The dated October 29 account remains historical. Existing TENT anchors remain stable. Both Markdown and HTML carry the corrected update and explicit source limits.

## Validation

- `python3 scripts/check_site.py`: PASS — 9 pages, 265 local links, 16 reciprocal citation pairs, generated output current, sitemap and structured-data checks passed.
- Targeted updated-section Markdown/HTML text and link parity: PASS (Pandoc conversion compared with HTMLParser extraction).
- Rhetoric HTML unique IDs, preserved TENT anchors, and all 7 local links/anchors: PASS, resolving the project URL prefix.
- `git diff --check`: PASS.
- Bounded editorial review checked merits/pending distinction, separate identities, dated evidence limits, denials, and motive language. No independent expert certification or browser layout review claimed.
