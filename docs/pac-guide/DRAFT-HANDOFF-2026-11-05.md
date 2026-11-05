# PACs and Political Money Guide — Draft Handoff

**Date:** 5 November 2026  
**Status:** Draft manuscript and source notes for owner/editorial review. **Not published. No merge or deployment authorization is implied.**  
**Working title:** *Who Paid for That? PACs, Super PACs, and the Missing Donor Layer*

## Purpose

Add an evidence-first political-money section to the Practical Guides / How to Hear a Bully hub. The guide teaches readers to distinguish:

- a candidate contribution from independent spending;
- a PAC’s own money from earmarked individual contributions forwarded through a conduit;
- a super PAC from a 501(c)(4) nonprofit;
- the immediate organizational source from the ultimate human donor;
- disclosure gaps from proof of illegal or foreign funding;
- and a complaint or suspicion from an enforcement finding.

The manuscript uses AIPAC, AIPAC PAC, and United Democracy Project as a dated worked example because the three related names illustrate the legal-entity problem that prompted the owner’s request. The guide does not infer foreign funding, corruption, coordination, or illegality.

## Files

- `who-paid-for-that.md` — draft reader-facing guide.
- `who-paid-for-that-notes.md` — 18 source notes, claim boundaries, and dated financial figures.
- `DRAFT-HANDOFF-2026-11-05.md` — this status and integration plan.

## Editorial choices

1. **Behavior and transaction, not villain labels.** The guide asks what an entity did and what the record establishes.
2. **Words Have Meaning.** “Contributed,” “forwarded,” “transferred,” “spent,” and “lobbied” remain separate.
3. **No false reassurance.** The guide acknowledges that nonprofit donor opacity can prevent public verification of ultimate sources.
4. **No guilt by opacity.** A stopped public trail is not treated as proof of foreign money or unlawful conduct.
5. **No flattening of AIPAC-related entities.** Core AIPAC, AIPAC PAC, and UDP are presented as distinct legal entities with distinct records.
6. **No double counting.** The guide warns that a conduit memo and underlying individual contribution are not two contributions.
7. **Federal scope.** State campaign-finance rules are outside the present draft except for a general warning that they differ.

## Source hierarchy

Primary sources were used for the legal and reporting framework:

- FEC committee guidance, data pages, filing images, disclosure rules, and enforcement material.
- IRS 501(c)(4), Schedule B, and 2020 regulatory guidance.
- Supreme Court opinions for campaign disclosure and associational privacy.

The AIPAC Form 990 figures use ProPublica’s IRS-derived filing presentation; the notes identify that as a third-party presentation rather than an independent finding.

## Current review limits

- No independent election-law review has been obtained.
- No adversarial editorial review has been completed.
- Dynamic 2025–2026 FEC figures are checked only through the source cutoff stated in the notes.
- The guide has not been reader-tested.
- Links and internal note targets were checked in the draft text, but the repository’s Pandoc build, full-site checker, browser checks, sitemap, metadata, and generated HTML were not changed or run.
- The current open Clara Tan PR modifies the collection homepage and other shared integration files. To avoid manufacturing a conflict, this draft does not yet edit those files.

## Proposed eventual hub placement

After content review and reconciliation with open PR #19, add a supporting section to the Practical Guides homepage:

> ## Political money and influence
>
> **Who Paid for That?**
>
> Separate candidate contributions, conduit donations, super-PAC spending, nonprofit transfers, and lobbying. Learn what federal filings reveal, where the donor trail can stop, and what opacity does—and does not—prove.

Proposed public route: `political-money/`  
Proposed source directory: `docs/pac-guide/`

Eventual implementation would require:

1. owner approval of the revised manuscript;
2. adversarial factual and framing review;
3. integration into `scripts/build_suite.py` or a separate builder;
4. generated guide and notes HTML;
5. homepage, methods, README, `llms.txt`, and sitemap integration;
6. static-site, reciprocal-note, accessibility, phone/desktop, and light/dark checks;
7. explicit publication authorization after review.

## Questions for owner review

- Is the AIPAC worked example appropriately bounded, or should the public guide use an abstract example and retain AIPAC only in the source/review packet?
- Should the title emphasize “political money,” “PACs,” or “following the donor trail”?
- Should a later version add a second worked example from a different policy area, or would that create performative balance rather than improve the mechanism?
- Should this remain a short standalone guide or become the first page of a broader “Money, power, and accountability” collection?
