# Making Practical Guides discoverable

The collection address is https://extivaries.github.io/How-to-Hear-a-Bully/practical-guides/. Bully remains at https://extivaries.github.io/How-to-Hear-a-Bully/, Crisis uses https://extivaries.github.io/How-to-Hear-a-Bully/crisis/, and Trust uses https://extivaries.github.io/How-to-Hear-a-Bully/trust/. The eight pages are ordinary HTML with visible text and stable section anchors. Every page advertises its Markdown alternative and sitemap. The collection metadata identifies its four primary projects and a related Plant Climate Map link; article metadata connects each guide to its notes without claiming expert certification. Middleman and Plant Climate Map retain their own hosting and discovery configuration.

These features help services identify and retrieve the material. They do not guarantee indexing, ranking, inclusion in an AI answer, or an assessment that the guide is impartial. Google says its AI search features use ordinary Search requirements and do not require special AI files or special schema: [Google's AI features guidance](https://developers.google.com/search/docs/appearance/ai-features).

## Existing Google and Bing setup

Keep the existing Google HTML verification file and Bing XML file in place. The owner previously completed the account-verification steps; rebuilding the collection does not require adding a new property or changing those tokens.

The shared sitemap is https://extivaries.github.io/How-to-Hear-a-Bully/sitemap.xml and lists all eight HTML reading pages. In the existing **URL-prefix property** `https://extivaries.github.io/How-to-Hear-a-Bully/`:

1. In [Google Search Console](https://search.google.com/search-console/), confirm that this sitemap remains submitted. Use URL Inspection for the collection, methods, Crisis guide and notes, and Trust guide and notes if their indexing status needs checking. Request indexing for a newly published page when appropriate; repeated requests do not speed it up. See [Google's recrawl guidance](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl).
2. In [Bing Webmaster Tools](https://www.bing.com/webmasters/), confirm the same sitemap is registered. [Bing's sitemap guidance](https://blogs.bing.com/webmaster/2025/7/Keeping-Content-Discoverable-with-Sitemaps-in-AI-Powered-Search/) explains its role in discovery.

A public HTTP check can establish that pages and verification files are reachable. It cannot establish an account's current verification state, sitemap-submission status or indexing reports. No account report was accessible during this setup. Publication and a working sitemap are not proof of indexing.

## Notify participating engines after changes

[IndexNow](https://www.indexnow.org/documentation) lets the site notify participating engines about changed URLs. Its ownership file, `indexnow-key.txt`, is served inside this GitHub Pages project. The script uses the explicit `keyLocation` option, so its scope is `/How-to-Hear-a-Bully/`, not other projects on the host. No search-account credential is used.

After the changed pages are deployed:

```sh
# Preview the eight sitemap URLs without sending a request.
python3 scripts/submit_indexnow.py

# Notify engines once for a changed page (repeat --url if needed).
python3 scripts/submit_indexnow.py --submit --url https://extivaries.github.io/How-to-Hear-a-Bully/trust/
```

`--submit` without `--url` sends all eight sitemap pages. The script checks the live ownership file and that the submitted pages return HTTP 200 before sending. It reports the actual response: 200 means received; 202 means received with key validation pending. Neither means indexed. Submit real changes, not repeated unchanged URLs. IndexNow does not replace the sitemap and Google Search Console workflow.

## Search crawling and AI training are separate

OpenAI documents `OAI-SearchBot` for ChatGPT search and `GPTBot` for possible model training. Search visibility does not require opting into training: [OpenAI crawler documentation](https://developers.openai.com/api/docs/bots). Bully alone is licensed under CC BY 4.0 with an extra author permission (see the README); Crisis, Trust and collection reuse terms remain undecided. These discovery changes do not change licenses or make a separate choice about training permissions.

Crawler rules for this host belong at `https://extivaries.github.io/robots.txt`. A file at `/How-to-Hear-a-Bully/robots.txt` would not control crawling. If host-wide rules are added later, check that they allow the desired search crawlers to reach all guide and collection pages and their supporting files. See [Google's robots.txt location rules](https://developers.google.com/crawling/docs/robots-txt/create-robots-txt).

The existing `llms.txt` is an optional link index for tools that choose to read it. It is not an access-control mechanism, an instruction to endorse the guide, or a requirement for Google or OpenAI search inclusion.

## Maintain a source people can evaluate

- Keep the author, edition, source notes, uncertainty statements, and correction history visible. Do not claim independent scholarly peer review or institutional endorsement without evidence.
- Keep the guide and notes linked in both HTML and Markdown. Preserve existing section and note anchors when possible so citations keep working.
- When an edition changes, update the HTML metadata and the sitemap's `lastmod` only to reflect a real page change. Preserve the original publication date. Do not refresh dates just to look recent.
- Update the Markdown source and its HTML counterpart together. Metadata belongs to the corresponding page: the notes page must retain its own title, canonical URL, and structured-data identity.
- If sharing the guide with educators, libraries, or media-literacy groups, describe its purpose and invite source-based corrections. Recommendations and links should reflect their own judgment; avoid mass posting or manufactured endorsements.
- Use Search Console and Bing's reports to check indexing and discovery over time. No analytics or tracking scripts are required by these repository changes.

The source and correction practices follow [Google's people-first content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content). The sitemap follows [Google's sitemap guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap).

## Collection, Crisis and Trust pages

The same sitemap also lists `practical-guides/`, `practical-guides/methods.html`, `crisis/`, `crisis/notes.html`, `trust/`, and `trust/notes.html`. The collection uses `CollectionPage` structured data with a list matching its four primary project links and a `relatedLink` matching the visible Plant Climate Map link. Crisis, Trust and their notes use `Article`; the methods page uses `WebPage`. Metadata connects the sources and canonical pages, without invented authorship, an assigned Crisis or Trust license, expert-review claims or a new research-review date. The existing Google and Bing verification files are retained unchanged. The `llms.txt` index describes the collection and related tool, with links to sources, limits and correction routes.
