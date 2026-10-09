# Editorial note — Complain or Constrain?

*Prepared 9 October 2026. Review draft only.*

**Repository handoff:** the user subsequently accepted the text and authorized pushing the packet to GitHub. The manuscript and notes are preserved unchanged from the text-ready ZIP. The preparation history below records earlier authorization and publication status; it is not a statement that the later GitHub push was unauthorized. The Tennessee docket check and legal review remain open before website publication.

## What is ready for review

- [Standalone article](complain-or-constrain.md): approximately 3,500 words; requested title, subtitle, structure, six questions, five possible outcomes, and closing principle.
- [Sources and verification](complain-or-constrain-notes.md): thirteen linked notes, case-specific evidence and limitations, alternative interpretations, and explicit access boundaries.

The six historical/legal examples are Plessy/Brown, Bob Jones University, Japanese American wartime exclusion, Snyder, Holt, and Lukumi. Holt is the deliberate case where requiring others to change is justified protection. Snyder is the deliberate case where real suffering coexists with a remedy the Court held impermissible; Alito’s contrary reasoning is included to avoid pretending that the moral judgment is uncontested.

Bob Jones University is a qualified substitute for the proposed “loss of advantage described as persecution” category: the actual constitutional burden claim is verified, but no unsupported persecution quotation is supplied. The article does not infer dishonesty from religious sincerity or from losing a case.

## Further verification and publication limits

The six included cases have source support for the claims made. None is identified here as awaiting verification of its basic identity or holding. The research does not represent a comprehensive check of subsequent doctrine across every relevant jurisdiction; publication as current legal guidance would need a separate legal review. The article presents historical decisions and civic reasoning.

The empirical paragraph is deliberately narrow. Mutz’s study was inspected, not replicated or treated as the consensus of an exhaustive literature review. Berlin and Pettit are explained through scholarly secondary sources, which are identified in the notes. Du Bois was considered but omitted; additional historical material can be added only if it improves the guide rather than becoming a list of names.

The opening and other unnamed scenarios are labeled as invented. The framework has not been tested with readers. AI review is not independent legal, historical, or psychological certification.

## Tennessee case: verified opinion, limited inclusion

The original judicial opinion in *State v. Samuel Ward, Jr.*, No. W2025-01186-CCA-R3-CD, filed 5 October 2026, was located and read through Justia’s hosted PDF after initial retrieval failures. The article includes a short complication after the six main cases. [Note 13](complain-or-constrain-notes.md#n13) records the sources, individual evidence, competing arguments, actual holding, and access limits.

The decision orders a new trial and separately rejects the insufficiency challenge; it does not acquit Ward or find the killing justified. The article recognizes his procedural rights while questioning what group-based inferences can establish about an individual. It does not infer discriminatory intent by judges.

**Further checks before publication:** confirm subsequent docket developments; obtain the official consolidated evidence rules if independently citing their current versions; complete legal review of the Tennessee section before it goes live. The article uses Rules 401 and 403 as quoted and applied in the opinion. The official court PDF and rule pages returned browser challenges; the judicial PDF was inspected through a public legal archive. The full trial record and unredacted exhibits were not reviewed. No conclusion is offered about guilt on retrial.

## Repository context and proposed links

Initial reference checkout: `https://github.com/ExtiVaries/How-to-Hear-a-Bully`, commit `8dd59ac9d7605fbd42f5f5ed8dd375effe5aeab9`. During corrections, the remote branch was fetched and its current tree inspected at `8f5322ff0d9a3042b79cf42429666eeb95bec472`, including [AGENTS.md](https://github.com/ExtiVaries/How-to-Hear-a-Bully/blob/8f5322ff0d9a3042b79cf42429666eeb95bec472/AGENTS.md). No checked-out repository source file was changed.

The repository contains the root guide `how-to-hear-a-bully.md` and a `docs/crisis-guide/` and `docs/trust-guide/` pattern for companion drafts. A matching proposed home for these new files is:

```text
docs/complain-guide/complain-or-constrain.md
docs/complain-guide/complain-or-constrain-notes.md
docs/complain-guide/editorial-note.md
```

These are suggestions, not paths created in the repository. With that placement, an optional related-reading line in the new article would be:

```markdown
Related reading: [How to Hear a Bully](../../how-to-hear-a-bully.md) examines manipulative uses of language, including accusations and labels. This guide asks whether a proposed remedy is justified. Either can be read on its own.
```

For later approval, a reciprocal line in the existing root guide would be:

```markdown
Related reading: [Complain or Constrain?](docs/complain-guide/complain-or-constrain.md) distinguishes genuine harm from unjustified remedies—and explains how both can occur together.
```

The article-to-notes and notes-to-article links already work when the new files remain together. The suggested reciprocal links were not inserted into the existing guide. No new public website route is assumed or claimed to exist. A Markdown link added to the root Bully guide will not appear on the website automatically: `index.html` is maintained separately and is not regenerated by the current builder. A future web edition would need its own route and corresponding HTML navigation, collection and methods entries, `sitemap.xml`, and `llms.txt` updates. Those are publication tasks, not changes made in this draft packet.

No existing repository files were changed, and nothing was committed, pushed, published, or sent to another person. A temporary clone was used only for reading. No license was assigned to the new material: the repository explicitly says the Bully license does not automatically extend to new guides.

## Production roles

The primary assistant prepared the prose and source notes. Astra was assigned the requested research and adversarial-review role. Claude was not available in this session; this draft must not be represented as Claude-authored. Final editorial responsibility remains with the project owner.

## Adversarial review and changes

Astra reviewed the full draft and found no evident critical factual error in the six case summaries; that was a critical reading, not independent re-verification of every source. Two suggestions were incorporated: Bob Jones now refers precisely to withdrawal of a tax benefit for discriminatory conduct, rather than implying a special religious privilege; question A expressly includes credible risks requiring prevention. Snyder’s legal/moral distinction and the dissent were preserved. Astra suggested a more general closing, but the user’s requested memorable closing was retained, supported by the article’s repeated acknowledgment that some restrictions are justified.

All thirteen article citations resolve to notes anchors, and the delivered files’ local cross-links were checked. The read-only reference checkout remained clean.

Astra also checked the added Ward section against the original opinion PDF. Its two refinements were incorporated: the State’s account of Ward’s prior knowledge, and explicit acknowledgment that the appellate court endorsed the evidence’s relevance rather than leaving that question open.

## Independent-review corrections — 9 October 2026

The supplied independent review was checked against the existing source cache and additional bibliographic evidence. The bounded corrections preserve the article’s structure and successful sections:

- Corrected the State’s relationship-length averment to “at least two years,” and stated both sides’ acceptance of Ward’s prior knowledge.
- Made the trial judge’s irrelevance ruling explicit; added the appellate court’s “misled the jury” reasoning and its finding that the error was not harmless; quoted its statement that a detailed discussion of physiological differences was unnecessary.
- Added an as-of date. Reattempted the official docket search, but did not retrieve a case history. Subsequent filings remain unconfirmed; the article does not claim the ruling is final or that no review has been sought.
- Corrected “mostly American” to “all American,” clarified Bob Jones using the Court’s actual formulation, and corrected Wollstonecraft’s chapter from V to IV.
- Added Morgan’s published challenge and Mutz’s reply to the research note, with source-access limits.
- Clarified that Markdown links alone do not update the website.

The user’s original closing was compared word for word and is unchanged: **“You can believe someone is hurting without agreeing that someone else must lose their freedom to make it stop.”**

The user clarified that quality takes priority over a word target. The repository’s instruction to preserve successful sections during bounded corrections is followed; no philosophy section or useful example was removed to force a shorter guide. The reviewer’s preference for legal review before publishing the Tennessee section is recorded as an editorial recommendation. No professional legal review has been obtained, and no publication was requested in this revision.

## Text acceptance and final polish — 9 October 2026

The user supplied a second independent review accepting all bounded corrections and confirming the text is ready. Two optional touch-ups were applied: Rule 403 now uses “probative value,” and straight apostrophes in the prose were standardized to curly apostrophes. No other article wording changed; its closing line and all thirteen citations remain intact. This copy edit does not renew source-research dates.

Two items remain open before the Tennessee section goes live: a successful check of subsequent docket developments and legal review of the section. Neither is marked complete. No website or repository publication is authorized or performed by this text-acceptance record.
