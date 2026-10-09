# How to Hear a Bully

**Recognizing the Language of Power and Manipulation** is a free, plain-language civic guide. It teaches readers to spot misleading accusations and labels in politics, to separate evidence from impression, and to apply the same standards to leaders they admire as to leaders they oppose.

## Read it

- [The guide](how-to-hear-a-bully.md) (second edition, October 2026)
- [Notes and verification](how-to-hear-a-bully-notes.md), with source notes, case-by-case verification records and the revision ledger
- [Read the guide online](https://extivaries.github.io/How-to-Hear-a-Bully/) or [open its sources and verification records](https://extivaries.github.io/How-to-Hear-a-Bully/notes.html).

## Practical Guides collection

The collection includes a small hub, a methods page, and the reviewed Crisis and Trust guides. The Bully reading address stays the same. The original crisis homepage copy is retained as an editorial draft; the current web copy is in `docs/practical-guides/homepage.md`.

- [Collection homepage source](docs/practical-guides/homepage.md)
- [How we check our work](docs/practical-guides/methods.md)
- [Why Does Everything Feel Like a Crisis?](docs/crisis-guide/why-does-everything-feel-like-a-crisis.md) and [source notes](docs/crisis-guide/why-does-everything-feel-like-a-crisis-notes.md)
- [Crisis editorial review record](docs/crisis-guide/FINAL-CHECK.md)
- [Who to Trust When It All Breaks Down?](docs/trust-guide/who-to-trust-when-it-all-breaks-down.md) and [seven source notes](docs/trust-guide/who-to-trust-when-it-all-breaks-down-notes.md)
- [Trust editorial review record](docs/trust-guide/FINAL-CHECK.md)
- [What Actually Changed?](docs/changes/guide.md), [U.S. timeline](docs/changes/timeline.md), and [methods and source notes](docs/changes/methodology.md)
- [Timeline update workflow](docs/changes/WORKFLOW.md), [record format](docs/changes/SCHEMA.md), [draft review and tests](docs/changes/REVIEW.md), [proposed schedule](docs/changes/schedule.json), and [exact proposed task prompt](docs/changes/schedule-prompt.txt)
- [Original collection website checks](docs/practical-guides/PUBLICATION-CHECK.md) and [Trust website checks](docs/trust-guide/PUBLICATION-CHECK.md)

The collection's existing web routes are `practical-guides/`, `practical-guides/methods.html`, `crisis/`, `crisis/notes.html`, `trust/`, and `trust/notes.html`. This draft adds the three `changes/` routes described below. GitHub Pages publishes the site from `claude/project-thread-i83pmv`. [Open the collection](https://extivaries.github.io/How-to-Hear-a-Bully/practical-guides/), [read the Crisis guide](https://extivaries.github.io/How-to-Hear-a-Bully/crisis/), or [read the Trust guide](https://extivaries.github.io/How-to-Hear-a-Bully/trust/).

### Build and preview

The site is static HTML, served without a build step by GitHub Pages. To update the collection, Crisis, Trust, or Changes pages, edit their canonical sources in `docs/practical-guides/`, `docs/crisis-guide/`, `docs/trust-guide/`, or `docs/changes/`, then run:

```sh
# Python 3.9+ and Pandoc 3 are required to regenerate the collection and guide pages.
python3 scripts/build_suite.py
python3 scripts/check_site.py
python3 -m http.server 8765
```

Open `http://localhost:8765/practical-guides/`. Commit the generated HTML alongside source changes. The builder deliberately does not regenerate the existing Bully pages; keep their HTML and Markdown synchronized when editing their prose. The shared navigation styling lives in `assets/practical-guides.css`.

The collection, Crisis and Trust pages have no client-side JavaScript, analytics, external fonts, or form backend. The What Actually Changed? timeline adds optional local search and history filtering; all entries and sources remain readable without JavaScript. The JSON-LD script blocks contain metadata only. A link to GitHub issues is the correction route; it requires a GitHub account and posts publicly. Research dates are editorial dates, not link-check or build dates.

### What Actually Changed? draft

The new routes are `changes/`, `changes/timeline.html`, and `changes/methodology.html`. `docs/changes/timeline.json` is canonical; the builder validates it and produces `changes/timeline.json` and `docs/changes/timeline.md` alongside HTML. Run `python scripts/test_timeline.py` for the update safeguards. The builder renders all pages before writing output; a build or validation failure must block release. No recurring writer or automatic merge is enabled. The existing research process is retained. See the workflow for candidate hashes, exclusive locking, partial checks, source amendments, immutable corrections, and activation requirements.

Complain or Constrain? remains an accepted manuscript, with no website route. Its Tennessee docket check and legal-review publication conditions are unchanged. Original Bully Markdown and HTML remain separately maintained; this addition changes navigation, not their accepted article text.

### Search and AI retrieval

Each page supplies a canonical URL, structured metadata, a sitemap link and a Markdown alternative. The collection's [text index](llms.txt) points readers and tools to the guides, their sources and their limits. These features support retrieval and citation; they do not guarantee search rankings or inclusion in AI answers.

[Discovery maintenance](DISCOVERY.md) covers the existing Google/Bing setup and IndexNow notifications after publication. `python3 scripts/submit_indexnow.py` previews the URLs without sending; add `--submit` after deployment to notify participating engines of actual changes. No research date or reuse license is changed by this setup.

## Cite it

Exti. *How to Hear a Bully: Recognizing the Language of Power and Manipulation*. Second edition, October 2026. https://extivaries.github.io/How-to-Hear-a-Bully/

The guide aims to apply the same standards across political affiliations. Its notes distinguish original statements, contrary evidence, interpretations, and unresolved questions. Readers can follow those sources and the revision history when evaluating its conclusions.

## What's here

| File | Purpose |
|---|---|
| `how-to-hear-a-bully.md` | Main guide (Markdown source) |
| `how-to-hear-a-bully-notes.md` | Sources, verification appendix, revision ledger |
| `index.html`, `notes.html` | Web pages built from the Markdown files |
| `.nojekyll` | Tells GitHub Pages to serve the HTML as is |
| `sitemap.xml` | Lists the guide, notes, and collection pages for search engines |
| `llms.txt` | Optional text index of the guide and supporting material; not required for search or AI citations |
| `LICENSE` | Full text of CC BY 4.0 (see License below for the author's extra permission) |
| `DISCOVERY.md` | Site-owner instructions for search indexing and maintaining discovery metadata |

## Corrections

The guides are meant to practice the discipline they teach. If you find a misquotation, a broken link or missing context, please [open an issue](https://github.com/ExtiVaries/How-to-Hear-a-Bully/issues) with the original source.

## License

Copyright 2026 Exti. *How to Hear a Bully* and its notes are licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). The full text is in [LICENSE](LICENSE).

**Extra permission from the author:** if your use is not commercial, you don't need to credit me. Share it, copy it, translate it, adapt it, or teach from it freely. Commercial use, meaning anything you sell or use to make money, is also allowed, but it must credit the work as "How to Hear a Bully, by Exti" with a link to https://extivaries.github.io/How-to-Hear-a-Bully/ and say whether you changed it.

Quotations and translations of other people's words (Thucydides, Confucius, Orwell, politicians, journalists and others) belong to their own authors or translators and are not covered by this license. They are quoted here for commentary and education.

Reuse terms for the Crisis guide, Trust guide, What Actually Changed? guide, timeline, and collection material have not been chosen. The Bully license and extra permission above apply only to *How to Hear a Bully* and its notes; they do not extend to the new material, Middleman, or linked sources.
