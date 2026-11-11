#!/usr/bin/env bash
# Refresh what GitHub Pages serves from docs/: a copy of the book for the reader page,
# and the two EPUBs to download. Run it after changing the book, then commit docs/.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
rm -rf "$ROOT/docs/book" && mkdir -p "$ROOT/docs/book"
cp -R "$ROOT/book/OEBPS" "$ROOT/docs/book/OEBPS"
bash "$ROOT/scripts/build-epub.sh" >/dev/null && mv "$ROOT/sample.epub" "$ROOT/docs/sample.epub"
bash "$ROOT/scripts/build-epub.sh" color >/dev/null && mv "$ROOT/sample-color.epub" "$ROOT/docs/sample-color.epub"
echo "build-pages: docs/book/ refreshed, docs/sample.epub and docs/sample-color.epub built"
