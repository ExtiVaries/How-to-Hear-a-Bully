#!/usr/bin/env python3
"""Build the dated K.M.K. companion, without assigning a new reuse license."""
import argparse
from html import escape
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://extivaries.github.io/How-to-Hear-a-Bully/"
SOURCE = "docs/complain-guide/kmk-case-study.md"
TARGET = "complain/kmk.html"


def render():
    title, text = (ROOT / SOURCE).read_text(encoding="utf-8").split("\n", 1)
    title = title.removeprefix("# ")
    body = subprocess.run(
        ["pandoc", "--from=markdown-smart", "--to=html5", "--wrap=none"],
        input=text, text=True, capture_output=True, check=True,
    ).stdout
    headings = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body)
    toc = '<details class="pg-toc"><summary>On this page</summary><ol>'
    toc += ''.join(f'<li><a href="#{anchor}">{label}</a></li>' for anchor, label in headings)
    toc += '</ol></details>\n'
    pos = body.find('<h2 ')
    body = body[:pos] + toc + body[pos:] if pos >= 0 else toc + body
    description = "A dated case study separating a student's reported harm, requested wrestling accommodations, effects on other students, and unresolved court proceedings."
    url = BASE + TARGET
    schema = {
        "@context": "https://schema.org", "@type": "Article",
        "@id": url + "#article", "name": title, "headline": title,
        "url": url, "mainEntityOfPage": url, "description": description,
        "inLanguage": "en", "isAccessibleForFree": True,
        "datePublished": "2026-11-02", "dateModified": "2026-11-02",
        "encoding": {"@type": "MediaObject", "encodingFormat": "text/markdown", "contentUrl": BASE + SOURCE},
        "isPartOf": {"@type": "CollectionPage", "name": "Practical Guides", "url": BASE + "practical-guides/"},
    }
    return f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>{escape(title)} | Practical Guides</title>
<meta name="description" content="{escape(description, quote=True)}">
<link rel="canonical" href="{url}">
<link rel="sitemap" type="application/xml" href="{BASE}sitemap.xml">
<link rel="alternate" type="text/markdown" href="{BASE + SOURCE}">
<meta property="og:type" content="article">
<meta property="og:title" content="{escape(title, quote=True)}">
<meta property="og:description" content="{escape(description, quote=True)}">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary">
<link rel="stylesheet" href="../assets/practical-guides.css">
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
</head><body class="pg-page">
<a class="suite-skip" href="#main-content">Skip to content</a>
<nav class="suite-nav" aria-label="Main navigation"><a class="suite-brand" href="../practical-guides/">Practical Guides</a><div class="suite-links"><a href="../practical-guides/">All guides</a><a href="../practical-guides/methods.html">How we check our work</a></div></nav>
<div class="pg-shell">
<main id="main-content" class="pg-reading">
<header><p class="pg-eyebrow">Complain or Constrain? · Case study</p><h1>{escape(title)}</h1><p class="pg-meta">Published 2 November 2026 · Dated snapshot, not live coverage</p></header>
<article aria-label="{escape(title, quote=True)}">
{body}</article>
<p class="pg-endlinks"><a href="../{SOURCE}">Markdown text</a> · <a href="#sources">Sources and limits</a> · <a href="#publication">Publication and reuse</a></p>
</main>
<footer class="suite-footer"><p>Practical Guides · Free public resources</p><p><a href="../practical-guides/">All guides</a> · <a href="../practical-guides/methods.html">Methods and limits</a> · <a href="https://github.com/ExtiVaries/How-to-Hear-a-Bully/issues">Report a correction</a></p><p>Reuse terms for this case study have not been assigned. <a href="#publication">Read the publication note</a>.</p></footer>
</div></body></html>
'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify output without writing")
    args = parser.parse_args()
    output = render()
    target = ROOT / TARGET
    if args.check:
        if not target.exists() or target.read_text(encoding="utf-8") != output:
            raise SystemExit("K.M.K. case page is missing or stale")
        print("K.M.K. case page: reproducible")
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(output, encoding="utf-8")


if __name__ == "__main__":
    main()
