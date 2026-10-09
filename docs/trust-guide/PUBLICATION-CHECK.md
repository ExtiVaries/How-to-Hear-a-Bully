# Trust guide website check

9 October 2026. This records the website checks for the Trust guide addition. The [final manuscript check](FINAL-CHECK.md) records the editorial verdict and research limits; rebuilding the website does not renew that review.

## Publication scope

The guide and seven notes are rendered at [`trust/`](https://extivaries.github.io/How-to-Hear-a-Bully/trust/) and [`trust/notes.html`](https://extivaries.github.io/How-to-Hear-a-Bully/trust/notes.html). The collection has four primary resources and keeps Plant Climate Map as a separate related tool. The desktop collection uses two columns for the four cards; narrow screens use one.

The approved Trust guide and notes remain byte-for-byte identical to commit `795b56eb84532a5ca6600b3b562fc803ea877f49`. The guide is 1,924 readable words. The existing Bully and Crisis manuscripts and reading-page HTML also remain unchanged. The shared stylesheet's only change is the collection card grid.

## Build and discovery checks

- `python3 scripts/check_site.py` passes for eight pages, 230 internal links, and 16 reciprocal citations: nine Crisis notes and seven Trust notes.
- The Trust guide and notes article text matches the approved Markdown word for word after excluding the added navigation.
- Rebuilding all six generated pages produces identical HTML. Each page has one main landmark and one H1, unique IDs, the correct canonical URL, a Markdown alternative, and a sitemap link.
- The collection's four listed resources and related Plant Climate Map link match the visible links. Trust's article metadata connects its guide and notes; it assigns no reuse license or expert-review certification.
- The sitemap includes the two new Trust routes, and the text index links both HTML and Markdown editions. The new pages contain visible static HTML without a JavaScript rendering dependency.
- Updated README, collection, methods, and Trust README Markdown links resolve locally. Existing Google, Bing and IndexNow verification files are unchanged.

## Browser checks

Chromium/Playwright checked the Trust guide, Trust notes, collection homepage and methods page at 320, 390 and 1280 pixels in light and dark modes: 24 page/layout combinations. All returned HTTP 200, with no horizontal overflow, failed resources or JavaScript errors. Each retained one H1 and main landmark.

All seven Trust citations were followed to their notes and back to the originating passage. The keyboard skip link and expandable contents navigation also passed. These are local browser checks; the release step separately verifies the deployed files.

## Limits retained

The 2022 classroom study's allocation method remains unverified, and the notes describe source-access limits. The guide's questions are an untested teaching aid. Trust's reuse terms remain undecided. Website tests do not constitute reader testing, scholarly peer review, a new source review, or proof of search indexing.
