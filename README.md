# How to Hear a Bully

**Recognizing the Language of Power and Manipulation** is a free, plain-language civic guide. It teaches readers to spot misleading accusations and labels in politics, to separate evidence from impression, and to apply the same standards to leaders they admire as to leaders they oppose.

## Read it

- [The guide](how-to-hear-a-bully.md) (second edition, October 2026)
- [Notes and verification](how-to-hear-a-bully-notes.md), with source notes, case-by-case verification records and the revision ledger
- [Read the guide online](https://extivaries.github.io/How-to-Hear-a-Bully/) or [open its sources and verification records](https://extivaries.github.io/How-to-Hear-a-Bully/notes.html).

## Practical Guides collection

This branch adds a small collection hub, a methods page, and the reviewed crisis guide. The existing Bully reading address stays the same. The original crisis homepage copy is retained as an editorial draft; the current web copy is in `docs/practical-guides/homepage.md`.

- [Collection homepage source](docs/practical-guides/homepage.md)
- [How we check our work](docs/practical-guides/methods.md)
- [Why Does Everything Feel Like a Crisis?](docs/crisis-guide/why-does-everything-feel-like-a-crisis.md) and [source notes](docs/crisis-guide/why-does-everything-feel-like-a-crisis-notes.md)
- [Editorial review record](docs/crisis-guide/FINAL-CHECK.md)
- [Website checks and release steps](docs/practical-guides/PUBLICATION-CHECK.md)

The new web routes are `practical-guides/`, `practical-guides/methods.html`, `crisis/`, and `crisis/notes.html`. They become public when these changes are merged into the GitHub Pages branch, `claude/project-thread-i83pmv`.

### Build and preview

The site is static HTML, served without a build step by GitHub Pages. To update the collection or Crisis pages, edit the Markdown in `docs/practical-guides/` or `docs/crisis-guide/`, then run:

```sh
# Python 3.9+ and Pandoc 3 are required to regenerate the four new pages.
python3 scripts/build_suite.py
python3 scripts/check_site.py
python3 -m http.server 8765
```

Open `http://localhost:8765/practical-guides/`. Commit the generated HTML alongside source changes. The builder deliberately does not regenerate the existing Bully pages; keep their HTML and Markdown synchronized when editing their prose. The shared navigation styling lives in `assets/practical-guides.css`.

The new pages have no client-side JavaScript, analytics, external fonts, or form backend. The JSON-LD script blocks contain metadata only. A link to GitHub issues is the correction route; it requires a GitHub account and posts publicly. Research dates are editorial dates, not link-check or build dates.

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

The guide is meant to practice the discipline it teaches. If you find a misquotation, a broken link or missing context, please [open an issue](https://github.com/ExtiVaries/How-to-Hear-a-Bully/issues) with the original source.

## License

Copyright 2026 Exti. *How to Hear a Bully* and its notes are licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). The full text is in [LICENSE](LICENSE).

**Extra permission from the author:** if your use is not commercial, you don't need to credit me. Share it, copy it, translate it, adapt it, or teach from it freely. Commercial use, meaning anything you sell or use to make money, is also allowed, but it must credit the work as "How to Hear a Bully, by Exti" with a link to https://extivaries.github.io/How-to-Hear-a-Bully/ and say whether you changed it.

Quotations and translations of other people's words (Thucydides, Confucius, Orwell, politicians, journalists and others) belong to their own authors or translators and are not covered by this license. They are quoted here for commentary and education.

Reuse terms for the crisis guide and new collection material have not been chosen. The Bully license and extra permission above apply only to *How to Hear a Bully* and its notes; they do not extend to the new material, Middleman, or linked sources.
