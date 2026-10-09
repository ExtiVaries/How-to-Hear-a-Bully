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
SUITE = ROOT / "docs/practical-guides"


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
<p><a href="{prefix}practical-guides/">All guides</a> · <a href="{prefix}practical-guides/methods.html">Methods and limits</a> · <a href="{ISSUES}">Report a correction</a></p>
<p>Sources and reuse terms belong to each project. <a href="{prefix}practical-guides/methods.html#reading-and-reuse">Read about reuse</a>.</p>
</footer>'''


def page(path, title, description, body, current="", schema_type="WebPage"):
    url = BASE + (path.removesuffix("index.html"))
    schema = {"@context": "https://schema.org", "@type": schema_type,
              "name": title, "url": url, "description": description, "inLanguage": "en"}
    doc = f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>{escape(title)} | Practical Guides</title>
<meta name="description" content="{escape(description, quote=True)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{escape(title, quote=True)}">
<meta property="og:description" content="{escape(description, quote=True)}">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="Practical Guides">
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
    intro, *rest = source.split("\n### ")
    last_card, methods = rest[-1].split("\n---\n", 1)
    rest[-1] = last_card
    hub_links = {"../../how-to-hear-a-bully.md": "../", "../crisis-guide/why-does-everything-feel-like-a-crisis.md": "../crisis/", "methods.md": "methods.html"}
    intro = markdown(intro, hub_links)
    intro = intro.replace("<p>", '<p class="pg-lede">', 1)
    labels = ["Official routes", "Language and power", "Information and action"]
    cards = []
    for label, card in zip(labels, rest):
        cards.append(f'<section class="pg-card"><span class="pg-label">{label}</span>{markdown("## " + card, hub_links)}</section>')
    body = f'''<main id="main-content">
<header class="pg-hero"><p class="pg-eyebrow">Free public resources</p>{intro}</header>
<div class="pg-grid">{''.join(cards)}</div>
<section class="pg-methods-link">{markdown(methods, hub_links)}</section>
</main>'''
    page("practical-guides/index.html", "What would help right now?",
         "Find official service routes, examine manipulative language, and judge alarming information. Free guides with sources, limits, and practical next steps.",
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
    reading("practical-guides/methods.html", SUITE / "methods.md",
            "What each Practical Guides project covers, how evidence and limits are recorded, what review dates mean, and how to report a correction.",
            "Methods and limits", '<a href="./">All guides</a>',
            {"homepage.md": "./", "../../how-to-hear-a-bully-notes.md": "../notes.html",
             "../../how-to-hear-a-bully.md": "../",
             "../crisis-guide/why-does-everything-feel-like-a-crisis-notes.md": "../crisis/notes.html",
             "../crisis-guide/why-does-everything-feel-like-a-crisis.md": "../crisis/"})


if __name__ == "__main__":
    build()
