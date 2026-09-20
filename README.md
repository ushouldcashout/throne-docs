# throne. docs

Public documentation for the THRONE desk: docs.throne.network (GitHub Pages, this repo's root).

- Write in `content/<slug>.md`. Page order and titles live in `NAV` in `build.py`.
- Build: `pip install markdown` once, then `python3 build.py`. Commit the generated `*.html`.
- Styling: `assets/docs.css` uses the same tokens as the desk and the site (see the brand kit).
- Rules for what goes in here: standard trader vocabulary; one headline fee (4.5 bps taker / 0 maker), nothing about how it is split underneath; nothing about the Court's mechanics beyond "priority access"; no yield or APY language; no team names.
