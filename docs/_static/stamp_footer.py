#!/usr/bin/env python3
"""Stamp docs/footer.md with the date of the commit being built.

Called from .readthedocs.yaml. This lives in a script rather than inline in
the build command because the equivalent one-liner needs shell command
substitution and several `%` escapes, which do not survive reliably.

Never fails the build: if the date cannot be determined the existing line is
left as it is.
"""

import pathlib
import re
import subprocess
import sys

FOOTER = pathlib.Path(__file__).resolve().parents[1] / "footer.md"
PATTERN = re.compile(r"^Last updated .*$", re.MULTILINE)


def commit_date():
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cd", "--date=format:%-d %B %Y"],
            capture_output=True, text=True, timeout=30,
        )
        if out.returncode == 0 and out.stdout.strip():
            return out.stdout.strip()
        sys.stderr.write("stamp_footer: git log failed: %s\n" % out.stderr.strip())
    except Exception as exc:                                  # never break the build
        sys.stderr.write("stamp_footer: %s\n" % exc)
    return None


def main():
    if not FOOTER.exists():
        sys.stderr.write("stamp_footer: %s not found, skipping\n" % FOOTER)
        return
    date = commit_date()
    if not date:
        sys.stderr.write("stamp_footer: leaving the existing date in place\n")
        return
    text = FOOTER.read_text(encoding="utf-8")
    if not PATTERN.search(text):
        sys.stderr.write("stamp_footer: no 'Last updated' line, skipping\n")
        return
    FOOTER.write_text(PATTERN.sub("Last updated " + date, text), encoding="utf-8")
    print("stamp_footer: Last updated " + date)


if __name__ == "__main__":
    main()
