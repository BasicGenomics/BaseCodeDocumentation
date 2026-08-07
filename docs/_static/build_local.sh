#!/usr/bin/env bash
# Build the site locally the same way Read the Docs does.
#
# `jupyter-book build` wipes _build/html, and MyST does not copy the standalone
# demo pages that the iframes point at. .readthedocs.yaml copies them in a
# separate step, so a plain local build leaves the interactive pages blank.
# This wrapper keeps the two in sync.

set -euo pipefail

DOCS="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$DOCS"

jupyter-book build --html

mkdir -p _build/html/demo
cp _static/demo/*.html _build/html/demo/

echo "copied $(ls -1 _build/html/demo/*.html | wc -l) demo page(s) into _build/html/demo/"
