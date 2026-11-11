This repo is a travel book. Answer short.

## Editing the book (also from a tablet, in a Claude Code session)
- The text lives in `book/OEBPS/`, one `.xhtml` per chapter. A new chapter also goes into `content.opf`
  (manifest and spine), `nav.xhtml` and `toc.ncx`.
- Read `STYLE.md` before writing a single line. The skeleton of the trip is in `SKELETON.md` (private, not in
  git); use it to know which day is where, and never copy a date, booking or name from it into the book.
- A plate is a Python file in `plates/` that writes an SVG. Render it with `bash plates/render.sh <name>`
  and look at the PNG before using it.
- A new day also gets its line in `02-the-days.xhtml` (the index readers touch).
- After any change, run `bash scripts/build-epub.sh` (and `bash scripts/build-pages.sh` if the web page should
  follow), commit and push to `main`, and say in one line what changed and that the EPUB is ready.
- Book rules, short: no times, prices or bookings; every foreign word as script · romanisation · meaning; every
  fact with its source at the end of the chapter.
