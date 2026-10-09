# Collection publication check

9 October 2026 · Prepared for draft pull-request review

The collection hub, methods page, crisis guide and source notes are implemented as static GitHub Pages files. The existing Bully guide remains at its original address. This record closes the implementation and live-link dependencies left open in the earlier [editorial check](../crisis-guide/FINAL-CHECK.md); that document remains a record of the earlier review.

## What was checked

- The reviewed Crisis guide and notes are byte-for-byte unchanged from the uploaded editorial files. The HTML conversion preserves their text and nine citation/return anchors. Note headings become semantic HTML headings; source Markdown is retained.
- The existing Bully guide and notes retain their complete article contents. Changes add collection navigation, a skip link and a main-content landmark. Search verification files and `.nojekyll` remain unchanged.
- `python3 scripts/check_site.py` passes: six pages, 156 local links, nine reciprocal note links, unique IDs, canonical URLs and sitemap coverage. Rebuilding the four new pages produces identical HTML.
- Chromium/Playwright checked all six pages at 320, 390, 768 and 1280 pixels, in light and dark mode: 48 page/layout combinations, with no horizontal overflow or failed local resources. Screenshots of the hub, crisis guide and notes were inspected at phone and desktop widths. The legacy pages were checked with their built-in font fallback.
- Keyboard navigation reaches the skip link; its destination works. The hub-to-guide path, citation-to-note-and-back path, contents links and print layout work. These checks do not constitute a full accessibility certification or human reader testing.
- Both existing public homepages, the Bully notes and Middleman's About page returned HTTP 200. Bully's correction link is visible. Middleman's About page shows its correction route, privacy/response limits and a content-check date. No test message was sent, and delivery or response is not promised.
- The methods page distinguishes Bully's edition date, Middleman's entry-specific verification information and Crisis's editorial review date. It discloses AI assistance and separates the projects' reuse permissions. No license was assigned to the new material.

## Publication routes

These routes become live after the changes are merged into the existing Pages branch, `claude/project-thread-i83pmv`:

- `practical-guides/` — collection hub
- `practical-guides/methods.html` — methods, limits and corrections
- `crisis/` — crisis guide
- `crisis/notes.html` — nine source notes

The existing Bully routes `/How-to-Hear-a-Bully/` and `/How-to-Hear-a-Bully/notes.html` are preserved. Middleman stays at its existing external address.

## Remaining release step

Review and merge the draft pull request, then confirm the four new routes and reciprocal citations on the deployed Pages site. The sitemap includes the new routes. Search indexing and AI discovery are not guaranteed, and the new pages have not undergone human reader testing.
