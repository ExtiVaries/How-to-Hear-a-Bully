#!/usr/bin/env python3
"""Preview or submit changed, published URLs to participating IndexNow engines."""
import argparse
import json
from pathlib import Path
import re
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://extivaries.github.io/How-to-Hear-a-Bully/"
ENDPOINT = "https://api.indexnow.org/indexnow"
KEY_URL = BASE + "indexnow-key.txt"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", action="append", dest="urls", help="Changed canonical URL; repeat for multiple URLs. Defaults to all sitemap pages.")
    parser.add_argument("--submit", action="store_true", help="Send the notification after checking the live ownership file and pages.")
    args = parser.parse_args()
    key = (ROOT / "indexnow-key.txt").read_text().strip()
    if not re.fullmatch(r"[A-Za-z0-9-]{8,128}", key):
        parser.error("Invalid IndexNow ownership key")
    urls = list(dict.fromkeys(args.urls or [node.text for node in ET.parse(ROOT / "sitemap.xml").iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]))
    for url in urls:
        parts = urlsplit(url)
        if not url.startswith(BASE) or parts.fragment or parts.query or "/../" in parts.path or "%" in parts.path:
            parser.error(f"Use a canonical URL within this project: {url}")
    payload = {"host": urlsplit(BASE).netloc, "key": key, "keyLocation": KEY_URL, "urlList": urls}
    if not args.submit:
        print(json.dumps({"mode": "preview", "endpoint": ENDPOINT, "keyLocation": KEY_URL, "urls": urls}, indent=2))
        print("No request sent. After publication, add --submit to notify participating engines.")
        return 0
    try:
        headers = {"User-Agent": "PracticalGuides-IndexNow/1.0", "Cache-Control": "no-cache"}
        with urlopen(Request(KEY_URL, headers=headers), timeout=20) as response:
            if response.read().decode("utf-8").strip() != key:
                raise ValueError("The live ownership file does not match this checkout")
        for url in urls:
            with urlopen(Request(url, headers=headers), timeout=20) as response:
                if response.status != 200:
                    raise ValueError(f"The changed page is not published: {url}")
        request = Request(ENDPOINT, data=json.dumps(payload).encode(),
                          headers={"Content-Type": "application/json; charset=utf-8", "User-Agent": "PracticalGuides-IndexNow/1.0"}, method="POST")
        with urlopen(request, timeout=30) as response:
            status = response.status
        meanings = {200: "Notification received; indexing is not guaranteed.",
                    202: "Notification received; ownership-key validation is pending."}
        print(json.dumps({"endpoint": ENDPOINT, "status": status, "urls": urls,
                          "meaning": meanings.get(status, "Unexpected response; inspect before retrying.")}, indent=2))
        return 0 if status in meanings else 1
    except (HTTPError, URLError, ValueError) as error:
        print(f"Notification not confirmed: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
