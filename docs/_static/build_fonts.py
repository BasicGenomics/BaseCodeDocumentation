#!/usr/bin/env python3
"""Embed Mona Sans into theme.css as base64 @font-face rules.

MyST does not copy files referenced from the custom stylesheet, and the
stylesheet is served from more than one path (`/myst-theme.css` and
`/build/theme-<hash>.css`), so a relative `url()` cannot be resolved
reliably. Embedding sidesteps both problems and keeps the font working
under Read the Docs' `/en/<version>/` prefix.

Run from the `docs/` folder after changing the font files:

    python _static/build_fonts.py

The script is idempotent: it replaces the generated block each time.
Requires fonttools and brotli (for the woff2 conversion).
"""

import base64
import os
import sys

# Shipped with the BaseCode Processing Pipeline for its PDF run report;
# reused here so the documentation matches the report typography.
SOURCES = [
    ("MonaSans-Regular.ttf", 400, "normal"),
    ("MonaSans-Bold.ttf", 700, "normal"),
]
SEARCH = [
    "/mnt/nvme/docker_BaseCodeVariant/BaseCode/workflow/resources",
    "/mnt/nvme/blazo/repos/BaseCode/workflow/resources",
]

START = "/* === GENERATED: Mona Sans @font-face, do not edit by hand === */"
END = "/* === END GENERATED === */"


def find(name):
    for d in SEARCH:
        p = os.path.join(d, name)
        if os.path.exists(p):
            return p
    sys.exit(f"could not find {name} in any of: {SEARCH}")


def to_woff2_b64(path):
    from fontTools.ttLib import TTFont
    import io

    f = TTFont(path)
    f.flavor = "woff2"
    buf = io.BytesIO()
    f.save(buf)
    return base64.b64encode(buf.getvalue()).decode("ascii")


def main():
    blocks = [START]
    for name, weight, style in SOURCES:
        src = find(name)
        b64 = to_woff2_b64(src)
        blocks.append(
            "@font-face{"
            'font-family:"Mona Sans";'
            f"font-style:{style};"
            f"font-weight:{weight};"
            "font-display:swap;"
            f"src:url(data:font/woff2;base64,{b64}) format(\"woff2\");"
            "}"
        )
        print(f"embedded {name} (weight {weight}): {len(b64):,} base64 chars")
    blocks.append(END)
    generated = "\n".join(blocks) + "\n"

    css_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "theme.css")
    css = open(css_path, encoding="utf-8").read()
    if START in css:
        head = css.split(START)[0].rstrip("\n")
        tail = css.split(END, 1)[1].lstrip("\n") if END in css else ""
        css = head + "\n\n" + generated + tail
    else:
        css = css.rstrip("\n") + "\n\n" + generated
    open(css_path, "w", encoding="utf-8").write(css)
    print(f"theme.css is now {os.path.getsize(css_path):,} B")


if __name__ == "__main__":
    main()
