#!/usr/bin/env bash
# Package book/ into sample.epub (grey plates, for a Kindle or any e-reader).
#   bash scripts/build-epub.sh          -> sample.epub
#   bash scripts/build-epub.sh color    -> sample-color.epub (colour plates, for a tablet or phone)
#
# An EPUB is a zip with two rules: the file `mimetype` goes first, and it is stored
# uncompressed. Everything else is compressed as usual. Needs `zip` and `perl`.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
MODE="${1:-grey}"
OUT="$ROOT/sample.epub"; [ "$MODE" = color ] && OUT="$ROOT/sample-color.epub"

TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
cp -R "$ROOT/book/." "$TMP/"
if [ "$MODE" = color ]; then
  # same book, the colour twin of every plate in place of the grey one
  for f in "$TMP"/OEBPS/img-color/*.png; do
    n="$(basename "$f")"
    if [ "$n" = cover.png ]; then cp "$f" "$TMP/OEBPS/cover.png"; else cp "$f" "$TMP/OEBPS/img/$n"; fi
  done
fi
rm -rf "$TMP/OEBPS/img-color"
NOW="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
perl -pi -e "s{(<meta property=\"dcterms:modified\">)[^<]*(</meta>)}{\${1}${NOW}\${2}}" "$TMP/OEBPS/content.opf"

rm -f "$OUT"
( cd "$TMP" && zip -X0 -q "$OUT" mimetype && zip -Xr9 -q "$OUT" META-INF OEBPS -x '*.DS_Store' )
echo "build-epub: $OUT ($(du -h "$OUT" | cut -f1))"
