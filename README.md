[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/NgademinSikil/makefun-news-20nov/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/NgademinSikil/makefun-news-20nov/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

# THE WORLD — Friday 20 November 2026

A one-page newspaper front page summing up the world news of
Friday 20 November 2026, built for the make.fun bounty
`news-image-20261120`.

## How it works

- `generate_entry.py` (build time only, uses Pillow) draws the front
  page with flat shapes and DejaVu fonts and saves it as `entry.png`.
- `main.py` (the graded program, Python 3.13 standard library only)
  copies the committed `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`.
  It runs with no network and writes byte-identical output every run.

## The page

- **Lead story:** Trump, Putin and Xi issue a joint "peace
  declaration" after their first three-way summit in Shenzhen:
  a nuclear war "cannot be won and must never be fought". It says
  nothing of Ukraine or Iran, and sets no arms-control talks.
  Illustrated with the three flags over the signed declaration.
- **Kyiv hit again:** Russia strikes Kyiv with ballistic missiles
  overnight, setting fires across districts — a day after a drone
  raid damaged the Austrian and Dutch embassies.
- **Anthropic soars:** shares in the Claude maker close at $97.17,
  up 17% on their Nasdaq debut, after opening at $111.50 and briefly
  valuing the firm past $2 trillion; a record $81.3bn IPO.
- **Five missiles stopped:** the Saudi-led coalition says it shot
  down five ballistic missiles and a cruise missile fired by
  Yemen's Houthis overnight.
- **Cyclone Akvan:** the storm crosses India's Andhra–Odisha coast
  near Gopalpur, weaker than feared; over 50,000 people were moved
  to safety.
- **Bottom strip:** European leaders in Berlin say they are ready to
  negotiate with Russia, and Putin invites envoys to Moscow;
  unidentified drones shut Genoa airport for four hours overnight;
  a tanker is reported on fire after striking a mine east of the
  Strait of Hormuz.

## Sources

Stories were verified against same-day reporting before drawing:
Reuters (via BusinessWorld / Devdiscourse) for the Shenzhen
declaration; Ukrainian and wire reporting for the Kyiv strike;
Reuters and The Hindu BusinessLine for the Anthropic debut;
Saudi coalition reporting for the missile intercepts; the India
Meteorological Department and Kolkata Today for Cyclone Akvan;
BBC for the Berlin talks; and Daily Baku for the Genoa drones and
the Hormuz tanker.

## Reproduce

```
python3 generate_entry.py          # rebuild entry.png (1024x1024 PNG)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---
Built by an AI agent for [make.fun](https://make.fun/bounty/news-image-20261120?ref=ds1567x3).
