#!/usr/bin/env bash
# Render a plate's SVG to PNG with headless Chrome, in two editions:
#   bash plates/render.sh rock-garden   -> book/OEBPS/img/rock-garden.png       (grey, 1x, for e-ink)
#                                          book/OEBPS/img-color/rock-garden.png (colour, 2x, for tablets)
#   bash plates/render.sh cover         -> book/OEBPS/cover.png                 (+ img-color/cover.png)
#
# Why these flags: --disable-lcd-text and --disable-font-subpixel-positioning stop
# Chrome from drawing coloured fringes on letter edges, which look like dirt on e-ink.
# The grey edition is saved as an 8-bit greyscale PNG: much smaller, so the EPUB stays
# small enough for Send to Kindle. Needs python3, ffmpeg, any Chrome or Chromium, and a Japanese font
# (Noto CJK on Linux), or the kanji come out as empty boxes.
set -euo pipefail
cd "$(dirname "$0")"
NAME="${1:?usage: render.sh <plate-name>}"
OEBPS="../book/OEBPS"

# Any Chrome, Chromium or chrome-headless-shell works. Set CHROME to its path if it isn't found.
if [ -z "${CHROME:-}" ]; then
  MAC_APP="/Applications/Google Chrome"   # + ".app/Contents/MacOS/Google Chrome" on a Mac
  for c in chrome-headless-shell google-chrome chromium chromium-browser "$MAC_APP.app/Contents/MacOS/${MAC_APP##*/}"; do
    if command -v "$c" >/dev/null 2>&1; then CHROME="$c"; break; fi
  done
fi
: "${CHROME:?no Chrome found: set CHROME=/path/to/chrome}"

python3 "$NAME.py"
SVG="$(cat "$NAME.svg")"
W=$(grep -o 'width="[0-9]*"' "$NAME.svg" | head -1 | tr -dc 0-9)
H=$(grep -o 'height="[0-9]*"' "$NAME.svg" | head -1 | tr -dc 0-9)
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT

shot() {  # $1 = svg markup, $2 = scale, $3 = out.png
  printf '<html><body style="margin:0;background:#fff">%s</body></html>' "$1" > "$TMP/p.html"
  "$CHROME" --headless --disable-gpu --hide-scrollbars --disable-lcd-text \
    --disable-font-subpixel-positioning --force-device-scale-factor="$2" \
    --window-size="$W,$H" --screenshot="$3" "file://$TMP/p.html" >/dev/null 2>&1
}

mkdir -p "$OEBPS/img" "$OEBPS/img-color"
GREY="$OEBPS/img/$NAME.png"; [ "$NAME" = cover ] && GREY="$OEBPS/cover.png"
shot "$SVG" 1 "$TMP/grey.png"
ffmpeg -loglevel error -y -i "$TMP/grey.png" -pix_fmt gray "$GREY"
rm -f "$OEBPS/img-color/$NAME.png"   # so a Chrome that fails quietly can't leave an old one looking new
shot "${SVG/<svg /<svg class=\"color\" }" 2 "$OEBPS/img-color/$NAME.png"
[ -s "$OEBPS/img-color/$NAME.png" ] || { echo "render: Chrome wrote no colour PNG" >&2; exit 1; }
echo "render: $GREY ($(du -h "$GREY" | cut -f1)) and img-color/$NAME.png ($(du -h "$OEBPS/img-color/$NAME.png" | cut -f1))"
