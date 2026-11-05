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

## Review corrections applied on 5 November 2026

A bounded AI-assisted factual and adversarial editorial review checked the manuscript and principal sources. The revised draft:

- dates the conduit example to its July 2025 filing and attributes the October 2026 operating-change announcement without claiming implementation or PAC termination;
- distinguishes the FEC's legal authority from its dated lack of a quorum, without implying all reporting or other agencies' oversight stopped;
- clarifies the corporate-treasury prohibition, lawful-permanent-resident exception, and conduit direction/control rule;
- separates the general nonprofit-disclosure pathway from any unproven core-AIPAC-to-UDP transfer;
- preserves the previously checked financial figures and their October 14 cutoff, pins FEC links to the 2026 cycle, and links the filing example to PDF page 74.

The AIPAC example, entity distinctions, and limits on motive, coordination, foreign-money, and illegality inferences remain. This does not adopt a new hub-wide accountability standard or authorize publication.

## Validation of the corrected draft

- Pandoc 3.1.11.1 rendered both draft Markdown files successfully. All 18 guide-to-note references and 18 return links resolve to rendered anchors, with no duplicate IDs or missing targets; 37 local links were checked including the introductory Source Notes link.
- The seven precise financial figures in the notes remain unchanged. Both FEC committee links specify the 2026 cycle.
- All 33 distinct external source URLs returned successful HTTP responses on 5 November 2026. The principal sources and the added legal/date qualifications were also read for claim support; link availability alone is not factual or legal certification.
- The existing `scripts/check_site.py` passed for 12 published-site pages, 389 local links, and 29 reciprocal notes. Generated pages were current, with matching sitemap and structured metadata. This is a regression check of the existing site, not validation of a PAC web edition.
- `git diff --check` passed. Only the three existing PAC draft files are part of this revision; Clara Tan and shared integration files remain untouched.

## Current review limits

- No independent election-law review has been obtained.
- The bounded AI-assisted review above is not independent election-law expertise, scholarly peer review, or reader testing. The revised manuscript still needs owner/editorial acceptance.
- Dynamic 2025–2026 FEC figures are checked only through the source cutoff stated in the notes.
- The guide has not been reader-tested.
- Draft rendering, note targets, and the existing full-site regression check were completed as recorded above. No PAC website integration, generated PAC HTML, or PAC browser/accessibility review has been completed. Shared sitemap, metadata, homepage, and generated site files remain unchanged.
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
2. final factual and framing acceptance of the corrected draft, with the remaining review limits made explicit;
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
