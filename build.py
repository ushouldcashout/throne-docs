#!/usr/bin/env python3
"""THRONE docs builder. Markdown in content/ → static HTML at the repo root.

    pip install markdown   (once)
    python3 build.py

Page order and titles come from NAV below. Each content/<slug>.md becomes <slug>.html
(index.md → index.html). Commit the generated HTML; GitHub Pages serves the repo root.
"""
import re, pathlib, datetime
import markdown

ROOT = pathlib.Path(__file__).parent
NAV = [
    ("start here", [("index", "start here"), ("how-it-works", "how the desk works")]),
    ("trading", [("markets", "markets and hours"), ("orders-and-margin", "orders, margin, leverage"),
                 ("funding-and-liquidation", "funding and liquidation"), ("fees", "fees")]),
    ("account", [("deposits-and-withdrawals", "deposits and withdrawals"), ("account-and-security", "account and security")]),
    ("programs", [("referrals", "referrals"), ("points", "points and season zero"), ("the-court", "the court and $THRONE.")]),
    ("fine print", [("risks", "risks"), ("support", "support and links")]),
]
SITE = "https://docs.throne.network"
DESK = "https://trade.throne.network"
HOME = "https://throne.network"

md = markdown.Markdown(extensions=["tables", "toc", "fenced_code", "attr_list", "sane_lists"], extension_configs={"toc": {"toc_depth": "2-3"}})

def nav_html(active):
    out = []
    for group, pages in NAV:
        out.append(f'<div class="grp">{group}</div>')
        for slug, title in pages:
            cls = ' class="on"' if slug == active else ""
            out.append(f'<a href="{slug}.html"{cls}>{title}</a>')
    return "\n".join(out)

TEMPLATE = open(ROOT / "template.html", encoding="utf-8").read()

def build():
    stamp = datetime.date.today().strftime("%d %b %Y").lower()
    for group, pages in NAV:
        for slug, title in pages:
            src = ROOT / "content" / f"{slug}.md"
            if not src.exists():
                print("missing", src); continue
            text = src.read_text(encoding="utf-8")
            text = re.sub(r"\n(\{:\s*\.[\w-]+\})", r"\n\n\1", text)  # marker line must not join the table
            md.reset()
            body = md.convert(text)
            # `{: .cls}` on the line after a table → class on that table (attr_list doesn't do tables)
            body = re.sub(r"<table>(.*?)</table>\s*<p>\{:\s*\.([\w-]+)\}</p>", r'<table class="\2">\1</table>', body, flags=re.S)
            h1 = re.search(r"<h1[^>]*>(.*?)</h1>", body)
            page_title = re.sub("<[^>]+>", "", h1.group(1)) if h1 else title
            toc = md.toc if "<li>" in md.toc else ""
            html = (TEMPLATE.replace("{{title}}", page_title).replace("{{nav}}", nav_html(slug))
                    .replace("{{body}}", body).replace("{{toc}}", toc).replace("{{stamp}}", stamp)
                    .replace("{{desk}}", DESK).replace("{{home}}", HOME).replace("{{slug}}", slug))
            (ROOT / f"{slug}.html").write_text(html, encoding="utf-8")
            print("built", slug)

if __name__ == "__main__":
    build()
