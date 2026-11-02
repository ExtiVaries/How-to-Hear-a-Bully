#!/usr/bin/env python3
"""Render the full Complain or Constrain? guide and source notes as static HTML."""
from html import escape
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://extivaries.github.io/How-to-Hear-a-Bully/"
SOURCE = ROOT / "docs/complain-guide"
DATE = "2026-11-02"


def render(source_name, target, notes=False):
    text = (SOURCE / source_name).read_text(encoding="utf-8")
    title, text = text.split("\n", 1)
    title = title.removeprefix("# ")
    if notes:
        text = re.sub(r'^<a id="(n\d+)"></a>\n### (.+)$', r'## \2 {#\1}', text, flags=re.M)
    body = subprocess.run(["pandoc", "--from=markdown-smart", "--to=html5", "--wrap=none"],
                          input=text, text=True, capture_output=True, check=True).stdout
    links = {"complain-or-constrain-notes.md": "notes.html", "complain-or-constrain.md": "index.html",
             "kmk-case-study.md": "kmk.html", "editorial-note.md": "../docs/complain-guide/editorial-note.md",
             "DOCKET-RECHECK-2026-10-13.md": "../docs/complain-guide/DOCKET-RECHECK-2026-10-13.md",
             "PUBLICATION-2026-11-02.md": "../docs/complain-guide/PUBLICATION-2026-11-02.md"}
    for old, new in links.items():
        body = body.replace('href="' + old, 'href="' + new)
    if notes:
        body = re.sub(r'(<h2 id="n(\d+)">.*?</h2>)(.*?)(?=<h2\b|\Z)',
                      lambda m: m[1] + m[3] + f'<p><a href="index.html#r{m[2]}">Return to citation {m[2]} in the guide</a></p>\n',
                      body, flags=re.S)
    else:
        for number in range(1, 14):
            old = f'<a href="notes.html#n{number}">'
            if body.count(old) != 1:
                raise ValueError(f"Expected exactly one citation {number}")
            body = body.replace(old, f'<a id="r{number}" href="notes.html#n{number}" aria-label="Source note {number}">')
    headings = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body)
    toc = '<details class="pg-toc"><summary>On this page</summary><ol>'
    toc += ''.join(f'<li><a href="#{anchor}">{label}</a></li>' for anchor, label in headings)
    toc += '</ol></details>\n'
    first = body.find('<h2 ')
    body = body[:first] + toc + body[first:] if first >= 0 else toc + body
    source_url = BASE + "docs/complain-guide/" + source_name
    url = BASE + target.removesuffix("index.html")
    description = ("Thirteen source notes, evidence limits and review history for Complain or Constrain?."
                   if notes else "Take reported harm seriously and examine the remedy independently: six practical questions, historical cases and source notes.")
    schema = {"@context": "https://schema.org", "@type": "Article", "@id": url + "#article",
              "name": title, "headline": title, "url": url, "mainEntityOfPage": url,
              "description": description, "inLanguage": "en", "isAccessibleForFree": True,
              "datePublished": DATE, "dateModified": DATE,
              "encoding": {"@type": "MediaObject", "encodingFormat": "text/markdown", "contentUrl": source_url}}
    guide_url, notes_url = BASE + "complain/", BASE + "complain/notes.html"
    if notes:
        schema["isPartOf"] = {"@type": "Article", "@id": guide_url + "#article", "url": guide_url, "name": "Complain or Constrain?"}
    else:
        schema["isPartOf"] = {"@type": "CollectionPage", "url": BASE + "practical-guides/", "name": "Practical Guides"}
        schema["hasPart"] = {"@type": "Article", "@id": notes_url + "#article", "url": notes_url, "name": "Source Notes"}
        schema["citation"] = notes_url
    endlinks = ('<a href="./">Back to the guide</a>' if notes else '<a href="notes.html">All 13 source notes</a>')
    endlinks += f' · <a href="{source_url}">Markdown text</a> · <a href="kmk.html">K.M.K. companion case study</a>'
    html = f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>{escape(title)} | Practical Guides</title>
<meta name="description" content="{escape(description, quote=True)}">
<link rel="canonical" href="{url}"><link rel="sitemap" type="application/xml" href="{BASE}sitemap.xml">
<link rel="alternate" type="text/markdown" href="{source_url}">
<meta property="og:type" content="article"><meta property="og:title" content="{escape(title, quote=True)}">
<meta property="og:description" content="{escape(description, quote=True)}"><meta property="og:url" content="{url}">
<meta property="og:site_name" content="Practical Guides"><meta name="twitter:card" content="summary">
<link rel="stylesheet" href="../assets/practical-guides.css">
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
</head><body class="pg-page">
<a class="suite-skip" href="#main-content">Skip to content</a>
<nav class="suite-nav" aria-label="Main navigation"><a class="suite-brand" href="../practical-guides/">Practical Guides</a><div class="suite-links"><a href="../practical-guides/">All guides</a><a href="../practical-guides/methods.html">How we check our work</a></div></nav>
<div class="pg-shell"><main id="main-content" class="pg-reading{' pg-notes' if notes else ''}">
<header><p class="pg-eyebrow">Protection, remedies and equal standing</p><h1>{escape(title)}</h1><p class="pg-meta">First web edition: 2 November 2026 · Original editorial review: 9 October 2026</p></header>
<article aria-label="{escape(title, quote=True)}">{body}</article>
<p class="pg-endlinks">{endlinks}</p>
</main><footer class="suite-footer"><p>Practical Guides · Free public resources</p>
<p><a href="../practical-guides/">All guides</a> · <a href="../practical-guides/methods.html">Methods and limits</a> · <a href="https://github.com/ExtiVaries/How-to-Hear-a-Bully/issues">Report a correction</a></p>
<p>Civic education, not legal advice. Independent qualified legal review has not been obtained. Publication is owner-authorized, not legal certification. No new reuse license is assigned to this guide or its notes.</p>
</footer></div></body></html>
'''
    dest = ROOT / target
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html, encoding="utf-8")


def build():
    render("complain-or-constrain.md", "complain/index.html")
    render("complain-or-constrain-notes.md", "complain/notes.html", notes=True)


if __name__ == "__main__":
    build()
