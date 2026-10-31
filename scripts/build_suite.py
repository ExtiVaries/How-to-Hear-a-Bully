#!/usr/bin/env python3
"""Render the reviewed Markdown as static GitHub Pages pages (requires Pandoc 3)."""
from html import escape
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://extivaries.github.io/How-to-Hear-a-Bully/"
ISSUES = "https://github.com/ExtiVaries/How-to-Hear-a-Bully/issues"
CRISIS = ROOT / "docs/crisis-guide"
TRUST = ROOT / "docs/trust-guide"
SUITE = ROOT / "docs/practical-guides"
COLLECTION = BASE + "practical-guides/"
MARKDOWN_SOURCES = {
    "practical-guides/index.html": "docs/practical-guides/homepage.md",
    "practical-guides/methods.html": "docs/practical-guides/methods.md",
    "crisis/index.html": "docs/crisis-guide/why-does-everything-feel-like-a-crisis.md",
    "crisis/notes.html": "docs/crisis-guide/why-does-everything-feel-like-a-crisis-notes.md",
    "trust/index.html": "docs/trust-guide/who-to-trust-when-it-all-breaks-down.md",
    "trust/notes.html": "docs/trust-guide/who-to-trust-when-it-all-breaks-down-notes.md",
    "trust/clara-tan.html": "docs/trust-guide/cases/clara-tan.md",
    "trust/clara-tan-sources.html": "docs/trust-guide/cases/clara-tan-sources.md",
}


def markdown(text, links=None):
    result = subprocess.run(
        ["pandoc", "--from=markdown-smart", "--to=html5", "--wrap=none"],
        input=text, text=True, capture_output=True, check=True,
    ).stdout
    for source, target in (links or {}).items():
        result = result.replace(f'href="{source}', f'href="{target}')
    return result


def navigation(prefix, current=""):
    active = lambda item: ' aria-current="page"' if current == item else ""
    return f'''<a class="suite-skip" href="#main-content">Skip to content</a>
<nav class="suite-nav" aria-label="Main navigation">
  <a class="suite-brand" href="{prefix}practical-guides/">Practical Guides</a>
  <div class="suite-links"><a href="{prefix}practical-guides/"{active('hub')}>All guides</a><a href="{prefix}practical-guides/methods.html"{active('methods')}>How we check our work</a></div>
</nav>'''


def footer(prefix):
    return f'''<footer class="suite-footer">
<p>Practical Guides · Free public resources</p>
<p><a href="{prefix}practical-guides/">All guides</a> · <a href="{prefix}practical-guides/methods.html">Methods and limits</a> · <a href="{prefix}llms.txt">Text index</a> · <a href="{ISSUES}">Report a correction</a></p>
<p>Sources and reuse terms belong to each project. <a href="{prefix}practical-guides/methods.html#reading-and-reuse">Read about reuse</a>.</p>
</footer>'''


def page(path, title, description, body, current="", schema_type="WebPage"):
    url = BASE + (path.removesuffix("index.html"))
    source_url = BASE + MARKDOWN_SOURCES[path]
    schema = {"@context": "https://schema.org", "@type": schema_type,
              "@id": url + "#page", "name": title, "url": url,
              "description": description, "inLanguage": "en",
              "isAccessibleForFree": True,
              "license": "https://creativecommons.org/licenses/by/4.0/",
              "encoding": {"@type": "MediaObject", "encodingFormat": "text/markdown", "contentUrl": source_url}}
    if schema_type == "CollectionPage":
        schema["@id"] = COLLECTION + "#collection"
        schema["name"] = "Practical Guides"
        schema["relatedLink"] = "https://plantclimatemap.org/"
        schema["mainEntity"] = {
            "@type": "ItemList", "itemListOrder": "https://schema.org/ItemListUnordered",
            "numberOfItems": 4,
            "itemListElement": [
                {"@type": "ListItem", "position": index,
                 "item": {"@type": "WebPage", "name": name, "url": target}}
                for index, (name, target) in enumerate([
                    ("Don't Pay a Middleman", "https://dont-pay-a-middleman.vercel.app/"),
                    ("How to Hear a Bully", BASE),
                    ("Why Does Everything Feel Like a Crisis?", BASE + "crisis/"),
                    ("Who to Trust When It All Breaks Down?", BASE + "trust/"),
                ], 1)
            ]}
    else:
        schema["isPartOf"] = {"@type": "CollectionPage", "@id": COLLECTION + "#collection", "url": COLLECTION, "name": "Practical Guides"}
    if path in ("trust/clara-tan.html", "trust/clara-tan-sources.html"):
        case_url = BASE + "trust/clara-tan.html"
        sources_url = BASE + "trust/clara-tan-sources.html"
        schema.update({"@type": "Article", "@id": url + "#article", "headline": title,
                       "mainEntityOfPage": url, "dateCreated": "2026-10-31",
                       "dateModified": "2026-10-31", "creativeWorkStatus": "Draft; publication held"})
        if path == "trust/clara-tan.html":
            schema["hasPart"] = {"@type": "Article", "url": sources_url,
                                 "@id": sources_url + "#article", "name": "Sources and evidence limits"}
            schema["citation"] = sources_url
        else:
            schema["isPartOf"] = {"@type": "Article", "url": case_url,
                                  "@id": case_url + "#article", "name": "Clara Tan case study"}
    elif path.startswith(("crisis/", "trust/")):
        section = path.split("/", 1)[0]
        guide_title = {"crisis": "Why Does Everything Feel Like a Crisis?",
                       "trust": "Who to Trust When It All Breaks Down?"}[section]
        guide_url = BASE + section + "/"
        notes_url = guide_url + "notes.html"
        schema.update({"@type": "Article", "@id": url + "#article", "headline": title,
                       "mainEntityOfPage": url, "datePublished": "2026-10-09"})
        if path == "trust/index.html":
            schema["dateModified"] = "2026-10-31"
        if path.endswith("index.html"):
            schema["hasPart"] = {"@type": "Article", "@id": notes_url + "#article",
                                 "url": notes_url, "name": "Source Notes"}
            schema["citation"] = notes_url
        else:
            schema["isPartOf"] = {"@type": "Article", "@id": guide_url + "#article",
                                  "url": guide_url, "name": guide_title}
    search_title = "Practical Guides: Services, Language, News and Trust" if current == "hub" else f"{title} | Practical Guides"
    doc = f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>{escape(search_title)}</title>
<meta name="description" content="{escape(description, quote=True)}">
<link rel="canonical" href="{url}">
<link rel="sitemap" type="application/xml" href="{BASE}sitemap.xml">
<link rel="alternate" type="text/markdown" href="{source_url}">
<meta property="og:type" content="{'article' if path.startswith(('crisis/', 'trust/')) else 'website'}">
<meta property="og:title" content="{escape(search_title, quote=True)}">
<meta property="og:description" content="{escape(description, quote=True)}">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="Practical Guides">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{escape(search_title, quote=True)}">
<meta name="twitter:description" content="{escape(description, quote=True)}">
<link rel="stylesheet" href="../assets/practical-guides.css">
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
</head><body class="pg-page">
{navigation('../', current)}
<div class="pg-shell">
{body}
{footer('../')}
</div></body></html>
'''
    destination = ROOT / path
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(doc)


def contents(html):
    headings = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', html)
    items = "".join(f'<li><a href="#{anchor}">{label}</a></li>' for anchor, label in headings)
    return f'<details class="pg-toc"><summary>On this page</summary><ol>{items}</ol></details>'


def reading(path, source, description, eyebrow, meta, links, extra="", notes=False):
    text = source.read_text()
    title, text = text.split("\n", 1)
    title = title.removeprefix("# ")
    if notes:
        # Pandoc otherwise treats an anchor immediately before a heading as a
        # paragraph. Keep the reviewed Markdown intact and put its stable note
        # IDs on semantic headings in the web edition.
        text = re.sub(r'^<a id="(n\d+)"></a>\n### (.+)$',
                      r'## \2 {#\1}', text, flags=re.M)
    rendered = markdown(text, links)
    # Put navigation after the introduction, so the emergency callout stays first.
    first_section = re.search(r'<h2\b', rendered)
    if first_section:
        offset = first_section.start()
        rendered = rendered[:offset] + contents(rendered) + rendered[offset:]
    body = f'''<main id="main-content" class="pg-reading{' pg-notes' if notes else ''}">
<header><p class="pg-eyebrow">{eyebrow}</p><h1>{escape(title)}</h1><p class="pg-meta">{meta}</p></header>
<article aria-label="{escape(title, quote=True)}">{rendered}</article>
{extra}
</main>'''
    page(path, title, description, body, current="methods" if "methods.html" in path else "")


def build():
    source = (SUITE / "homepage.md").read_text()
    primary, supporting = source.split("\n---\n", 1)
    intro, *rest = primary.split("\n### ")
    hub_links = {"../../how-to-hear-a-bully.md": "../",
                 "../crisis-guide/why-does-everything-feel-like-a-crisis.md": "../crisis/",
                 "../trust-guide/who-to-trust-when-it-all-breaks-down.md": "../trust/",
                 "methods.md": "methods.html"}
    intro = markdown(intro, hub_links)
    intro = intro.replace("<p>", '<p class="pg-lede">', 1)
    labels = ["Official routes", "Language and power", "Information and action", "Evidence and trust"]
    if len(rest) != len(labels):
        raise ValueError("The homepage must contain the four primary guide cards")
    cards = []
    for label, card in zip(labels, rest):
        cards.append(f'<section class="pg-card"><span class="pg-label">{label}</span>{markdown("## " + card, hub_links)}</section>')
    supporting_html = "\n".join(
        f'<section class="pg-methods-link">{markdown(section, hub_links)}</section>'
        for section in supporting.split("\n---\n"))
    body = f'''<main id="main-content">
<header class="pg-hero"><p class="pg-eyebrow">Free public resources</p>{intro}</header>
<div class="pg-grid">{''.join(cards)}</div>
{supporting_html}
</main>'''
    page("practical-guides/index.html", "What would help right now?",
         "Find official service routes, examine language, judge alarming information, and weigh conflicting claims. Free guides with sources and practical next steps.",
         body, "hub", "CollectionPage")
    links = {"why-does-everything-feel-like-a-crisis-notes.md": "notes.html",
             "why-does-everything-feel-like-a-crisis.md": "index.html"}
    reading("crisis/index.html", CRISIS / "why-does-everything-feel-like-a-crisis.md",
            "A short guide to judging alarming information and choosing what to do, with five questions, fictional flood exercises, and research notes.",
            "Information and action", "Editorial review: 9 October 2026 · About 1,900 words", links,
            '<p class="pg-endlinks"><a href="notes.html">Read the source notes</a> · <a href="../docs/crisis-guide/why-does-everything-feel-like-a-crisis.md">Markdown text</a></p>')
    reading("crisis/notes.html", CRISIS / "why-does-everything-feel-like-a-crisis-notes.md",
            "Nine source notes for the crisis guide: study designs, verified findings, uncertainties, and limits of the evidence.",
            "Sources and limits", '<a href="./">Back to the guide</a> · Editorial review: 9 October 2026', links,
            '<p class="pg-endlinks"><a href="./">Back to the guide</a> · <a href="../docs/crisis-guide/why-does-everything-feel-like-a-crisis-notes.md">Markdown notes</a></p>', notes=True)
    trust_links = {"who-to-trust-when-it-all-breaks-down-notes.md": "notes.html",
                   "who-to-trust-when-it-all-breaks-down.md": "index.html"}
    reading("trust/index.html", TRUST / "who-to-trust-when-it-all-breaks-down.md",
            "A practical guide to conflicting claims, expertise, and uncertainty: five questions, a dated real case, two fictional exercises, and source notes to help decide whom to rely on and for what.",
            "Evidence and trust", "Editorial review: 9 October 2026 · Real case added: 21 October 2026 · Related case link added: 31 October 2026", trust_links,
            '<p class="pg-endlinks"><a href="notes.html">Read the source notes</a> · <a href="../docs/trust-guide/who-to-trust-when-it-all-breaks-down.md">Markdown text</a></p>')
    reading("trust/notes.html", TRUST / "who-to-trust-when-it-all-breaks-down-notes.md",
            "Seven source notes for the trust guide: lateral reading, online search, expertise, study findings, and the limits of the evidence.",
            "Sources and limits", '<a href="./">Back to the guide</a> · Editorial review: 9 October 2026', trust_links,
            '<p class="pg-endlinks"><a href="./">Back to the guide</a> · <a href="../docs/trust-guide/who-to-trust-when-it-all-breaks-down-notes.md">Markdown notes</a></p>', notes=True)
    case_links = {"clara-tan-sources.md": "clara-tan-sources.html",
                  "clara-tan.md": "clara-tan.html",
                  "../who-to-trust-when-it-all-breaks-down.md": "index.html",
                  "../../practical-guides/methods.md": "../practical-guides/methods.html"}
    reading("trust/clara-tan.html", TRUST / "cases/clara-tan.md",
            "A dated Clara Tan case study separating an acknowledged arrest, allegations about treatment, written detention rules, and unanswered accountability questions.",
            "Case study · Evidence and accountability", "Prepared and checked: 31 October 2026 · Draft; publication held", case_links,
            '<p class="pg-endlinks"><a href="clara-tan-sources.html">Sources and evidence limits</a> · <a href="./">Trust guide</a></p>')
    reading("trust/clara-tan-sources.html", TRUST / "cases/clara-tan-sources.md",
            "Sources, version differences, regulatory references, records not inspected, and update criteria for the Clara Tan case study.",
            "Case sources and limits", "Sources checked: 31 October 2026 · Draft; publication held", case_links,
            '<p class="pg-endlinks"><a href="clara-tan.html">Return to the case</a> · <a href="./">Trust guide</a></p>', notes=True)
    reading("practical-guides/methods.html", SUITE / "methods.md",
            "What each Practical Guides project covers, how evidence and limits are recorded, what review dates mean, and how to report a correction.",
            "Methods and limits", '<a href="./">All guides</a>',
            {"homepage.md": "./", "../../how-to-hear-a-bully-notes.md": "../notes.html",
             "../../how-to-hear-a-bully.md": "../",
             "../crisis-guide/why-does-everything-feel-like-a-crisis-notes.md": "../crisis/notes.html",
             "../crisis-guide/why-does-everything-feel-like-a-crisis.md": "../crisis/",
             "../trust-guide/who-to-trust-when-it-all-breaks-down-notes.md": "../trust/notes.html",
             "../trust-guide/who-to-trust-when-it-all-breaks-down.md": "../trust/"})


if __name__ == "__main__":
    build()
