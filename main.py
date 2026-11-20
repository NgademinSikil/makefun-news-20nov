#!/usr/bin/env python3
"""news-image-20261120: deliver the finished front page.

The graded program, Python 3.13 standard library only. It takes the
front page drawn at build time (entry.png, beside this file) and
writes it to $MAKEFUN_OUTPUT_DIR/entry.png, or /output/entry.png
when that variable is unset. No network, no drawing at grade time:
every run writes the same bytes.

Run:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil


def run():
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out, exist_ok=True)
    shutil.copy(os.path.join(here, "entry.png"),
                os.path.join(out, "entry.png"))


run()
