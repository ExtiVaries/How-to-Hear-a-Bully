#!/usr/bin/env python3
"""Check publication routes, anchors, metadata and reproducible generated pages."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import json
import subprocess
import sys
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://extivaries.github.io/How-to-Hear-a-Bully/"
PAGES = ["index.html", "notes.html", "practical-guides/index.html",
         "practical-guides/methods.html", "crisis/index.html", "crisis/notes.html"]


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids, self.links, self.canonicals, self.headings = [], [], [], []
        self.alternates, self.schemas, self.sitemaps = [], [], []
        self._jsonld = None
        self.indexing_blocked = False
        self.h1s = self.mains = 0
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonicals.append(attrs["href"])
        if tag == "link" and attrs.get("rel") in ("stylesheet", "alternate", "sitemap"):
            self.links.append(attrs["href"])
        if tag == "link" and attrs.get("rel") == "alternate" and attrs.get("type") == "text/markdown":
            self.alternates.append(attrs["href"])
        if tag == "link" and attrs.get("rel") == "sitemap":
            self.sitemaps.append(attrs["href"])
        if tag == "script" and attrs.get("type") == "application/ld+json":
            self._jsonld = ""
        if tag == "meta" and attrs.get("name", "").lower() in ("robots", "googlebot", "bingbot"):
            self.indexing_blocked |= "noindex" in attrs.get("content", "").lower()
        if tag == "h1":
            self.h1s += 1
        if tag == "main":
            self.mains += 1
        if tag == "h2":
            self.headings.append(attrs.get("id"))

    def handle_data(self, data):
        if self._jsonld is not None:
            self._jsonld += data

    def handle_endtag(self, tag):
        if tag == "script" and self._jsonld is not None:
            self.schemas.append(json.loads(self._jsonld))
            self._jsonld = None


def main():
    failures = []
    before = {name: (ROOT / name).read_bytes() for name in PAGES[2:]}
    subprocess.run([sys.executable, str(ROOT / "scripts/build_suite.py")], check=True)
    for name, content in before.items():
        if (ROOT / name).read_bytes() != content:
            failures.append(f"{name}: generated page was stale; rebuilt it, rerun check")

    docs = {name: Document((ROOT / name).read_text()) for name in PAGES}
    links_checked = 0
    for name, doc in docs.items():
        duplicates = [key for key, count in Counter(doc.ids).items() if count > 1]
        if duplicates:
            failures.append(f"{name}: duplicate IDs {duplicates}")
        if doc.h1s != 1 or doc.mains != 1:
            failures.append(f"{name}: expected one H1 and one main landmark")
        expected = BASE + name.removesuffix("index.html")
        if doc.canonicals != [expected]:
            failures.append(f"{name}: incorrect canonical URL")
        if doc.indexing_blocked:
            failures.append(f"{name}: indexing is blocked by a meta tag")
        if len(doc.alternates) != 1 or doc.sitemaps != [BASE + "sitemap.xml"]:
            failures.append(f"{name}: missing Markdown alternative or sitemap discovery link")
        if len(doc.schemas) != 1:
            failures.append(f"{name}: expected one structured-data record")
        else:
            schema = doc.schemas[0]
            if schema.get("url") != expected or schema.get("isAccessibleForFree") is not True:
                failures.append(f"{name}: structured data has the wrong page identity or access status")
            if schema.get("encoding", {}).get("contentUrl") not in doc.alternates:
                failures.append(f"{name}: structured data and Markdown alternative differ")
            if name.startswith(("crisis/", "practical-guides/")) and "license" in schema:
                failures.append(f"{name}: new material has no assigned reuse license")
        for href in doc.links:
            resolved = urlsplit(urljoin(BASE + name, href))
            if resolved.netloc != urlsplit(BASE).netloc:
                continue
            prefix = urlsplit(BASE).path
            if not resolved.path.startswith(prefix):
                failures.append(f"{name}: local link escapes the project prefix: {href}")
                continue
            relative = unquote(resolved.path[len(prefix):])
            if not relative or relative.endswith("/"):
                relative += "index.html"
            target = ROOT / relative
            if not target.is_file():
                failures.append(f"{name}: missing destination {href}")
            elif resolved.fragment and target.suffix == ".html":
                target_doc = docs.get(relative) or Document(target.read_text())
                if unquote(resolved.fragment) not in target_doc.ids:
                    failures.append(f"{name}: missing fragment {href}")
            links_checked += 1

    guide, notes = docs["crisis/index.html"], docs["crisis/notes.html"]
    collection = docs["practical-guides/index.html"].schemas[0]
    listed = [item["item"]["url"] for item in collection["mainEntity"]["itemListElement"]]
    visible_targets = {urljoin(BASE + "practical-guides/", href) for href in docs["practical-guides/index.html"].links}
    if len(listed) != 3 or any(url not in visible_targets for url in listed):
        failures.append("Collection structured data must describe the three visible project links")
    if guide.schemas[0].get("hasPart", {}).get("url") != BASE + "crisis/notes.html" or notes.schemas[0].get("isPartOf", {}).get("url") != BASE + "crisis/":
        failures.append("Crisis guide/notes structured relationships differ from their visible links")
    for number in range(1, 10):
        if f"n{number}" not in notes.headings:
            failures.append(f"Note {number} is not a semantic heading")
        if f"notes.html#n{number}" not in guide.links or f"index.html#r{number}" not in notes.links:
            failures.append(f"Note {number} is missing its citation or return link")

    sitemap = ET.parse(ROOT / "sitemap.xml")
    locations = [element.text for element in sitemap.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    expected = [BASE + name.removesuffix("index.html") for name in PAGES]
    if sorted(locations) != sorted(expected):
        failures.append("Sitemap does not match the six publication pages")

    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print(json.dumps({"pages": len(PAGES), "local_links_checked": links_checked,
                      "reciprocal_notes": 9, "generated_pages_current": True,
                      "sitemap_matches": True, "structured_data_and_markdown": True}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
