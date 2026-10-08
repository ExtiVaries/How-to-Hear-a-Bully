# Making the guide discoverable

The public reading address is https://extivaries.github.io/How-to-Hear-a-Bully/. Both the guide and its notes are ordinary HTML with visible text, source links, section anchors, and Markdown alternatives. The pages have descriptive titles, canonical URLs, social preview metadata, and Article structured data that identifies each page correctly.

These features help services identify and retrieve the material. They do not guarantee indexing, ranking, inclusion in an AI answer, or an assessment that the guide is impartial. Google says its AI search features use ordinary Search requirements and do not require special AI files or special schema: [Google's AI features guidance](https://developers.google.com/search/docs/appearance/ai-features).

## Submit the site once

1. In [Google Search Console](https://search.google.com/search-console/), add the **URL-prefix property** `https://extivaries.github.io/How-to-Hear-a-Bully/`.
2. Use the verification HTML tag or HTML file supplied by Google. Add that exact tag to the home page's `<head>`, or publish the supplied file at the path Google specifies. Keep it in place after verification. A project on `github.io` does not require control of GitHub's DNS for this method. See [Google's ownership-verification instructions](https://support.google.com/webmasters/answer/9008080).
3. Submit `https://extivaries.github.io/How-to-Hear-a-Bully/sitemap.xml` in Search Console's Sitemaps screen.
4. Use URL Inspection to check the guide and `notes.html`, then request indexing if needed. Google decides when and whether to index them; repeated requests do not speed the process. See [Google's recrawl guidance](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl).
5. Verify the same site in [Bing Webmaster Tools](https://www.bing.com/webmasters/) and submit the same sitemap. Bing's [sitemap guidance](https://blogs.bing.com/webmaster/2025/7/Keeping-Content-Discoverable-with-Sitemaps-in-AI-Powered-Search/) covers discovery for search and AI experiences.

These account steps need the owner's chosen Search Console/Bing account and the verification value generated there. No verification token, submission, or indexing status is assumed in this repository.

## Search crawling and AI training are separate

OpenAI documents `OAI-SearchBot` for ChatGPT search and `GPTBot` for possible model training. Search visibility does not require opting into training: [OpenAI crawler documentation](https://developers.openai.com/api/docs/bots). This project makes no new training-permission or licensing choice.

Crawler rules for this host belong at `https://extivaries.github.io/robots.txt`. A file at `/How-to-Hear-a-Bully/robots.txt` would not control crawling. If host-wide rules are added later, check that they allow the desired search crawlers to reach both HTML pages and their supporting files. See [Google's robots.txt location rules](https://developers.google.com/crawling/docs/robots-txt/create-robots-txt).

The existing `llms.txt` is an optional link index for tools that choose to read it. It is not an access-control mechanism, an instruction to endorse the guide, or a requirement for Google or OpenAI search inclusion.

## Maintain a source people can evaluate

- Keep the author, edition, source notes, uncertainty statements, and correction history visible. Do not claim independent scholarly peer review or institutional endorsement without evidence.
- Keep the guide and notes linked in both HTML and Markdown. Preserve existing section and note anchors when possible so citations keep working.
- When an edition changes, update the HTML metadata and the sitemap's `lastmod` only to reflect a real page change. Preserve the original publication date. Do not refresh dates just to look recent.
- Update the Markdown source and its HTML counterpart together. Metadata belongs to the corresponding page: the notes page must retain its own title, canonical URL, and structured-data identity.
- If sharing the guide with educators, libraries, or media-literacy groups, describe its purpose and invite source-based corrections. Recommendations and links should reflect their own judgment; avoid mass posting or manufactured endorsements.
- Use Search Console and Bing's reports to check indexing and discovery over time. No analytics or tracking scripts are required by these repository changes.

The source and correction practices follow [Google's people-first content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content). The sitemap follows [Google's sitemap guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap).
