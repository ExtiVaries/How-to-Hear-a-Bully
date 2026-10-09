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
        if tag == "link" and attrs.get("rel") == "stylesheet":
            self.links.append(attrs["href"])
        if tag == "h1":
            self.h1s += 1
        if tag == "main":
            self.mains += 1
        if tag == "h2":
            self.headings.append(attrs.get("id"))


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
                      "sitemap_matches": True}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
