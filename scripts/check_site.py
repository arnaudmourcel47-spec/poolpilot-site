#!/usr/bin/env python3
"""Check generated Pages files and internal navigation without external packages."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
PAGES = [ROOT.joinpath(*(parts + ["index.html"])) for parts in
         ([], ["privacy"], ["support"], ["legal"], ["en"], ["en", "privacy"],
          ["en", "support"], ["en", "legal"], ["es"], ["es", "privacy"],
          ["es", "support"], ["es", "legal"])]


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links: list[str] = []
        self.lang = ""
        self.mains = 0
        self.h1s = 0
        self.navs = 0
        self.title = False
        self.remote_assets: list[str] = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == "html":
            self.lang = values.get("lang", "")
        if tag == "main":
            self.mains += 1
        if tag == "h1":
            self.h1s += 1
        if tag == "nav":
            self.navs += 1
        if tag == "title":
            self.title = True
        for attribute in ("href", "src"):
            if attribute in values:
                value = values[attribute]
                if value.startswith(("http://", "https://", "//")) and tag in ("script", "link", "img"):
                    self.remote_assets.append(value)
                if attribute == "href" and tag in ("a", "link"):
                    self.links.append(value)


def main():
    for page in PAGES:
        assert page.is_file(), f"Missing page: {page}"
        parser = PageParser()
        parser.feed(page.read_text(encoding="utf-8"))
        expected_lang = page.relative_to(ROOT).parts[0]
        expected_lang = expected_lang if expected_lang in ("en", "es") else "fr"
        assert parser.lang == expected_lang, f"Wrong lang: {page}"
        assert parser.mains == parser.h1s == 1 and parser.navs == 2 and parser.title, f"Missing landmarks: {page}"
        assert not parser.remote_assets, f"Remote runtime asset: {page}: {parser.remote_assets}"
        for href in parser.links:
            parsed = urlsplit(href)
            if parsed.scheme or parsed.netloc or href.startswith("#"):
                continue
            target = (page.parent / parsed.path).resolve()
            if target.is_dir():
                target /= "index.html"
            assert target.is_file(), f"Broken link: {page} -> {href}"
    for suffix in ("FR", "EN", "ES"):
        assert (ROOT / "content" / f"PRIVACY_POLICY_{suffix}.md").is_file()
        assert (ROOT / "content" / f"LEGAL_{suffix}.md").is_file()
    prohibited = [p for p in ROOT.rglob("*") if p.suffix.lower() in (".ipa", ".swift", ".sqlite", ".db", ".xcarchive", ".xcodeproj")]
    assert not prohibited, f"Application artifact in site: {prohibited}"
    print("OK: 12 localized pages, semantic landmarks, internal links, local assets, no iOS artifacts.")


if __name__ == "__main__":
    main()
