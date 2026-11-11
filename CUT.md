# What's in this repo, and what I left out

This repo comes from a real travel book I wrote with Claude for one trip. That book stays private: it carries a
real trip. What's here is the method, shown on an invented trip so every part of it can be opened, built and changed.

## In

| What | Why it's here |
|---|---|
| `book/` | A complete sample book: an invented three-day trip (Kanazawa, Kyoto, Naoshima), seven chapters and a cover, built the same way as the real one |
| `plates/` | Three drawings as code (the cover and two plates), with the two-edition styles and the renderer. Same technique as the real book's plates; new drawings |
| `scripts/` | The EPUB build and the Pages build |
| `STYLE.md`, `CLAUDE.md` | The real book's rules, translated and made general: chapter order, tone, the three-way words, no times or prices, sources |
| `SKELETON.example.md` | The shape of the private trip file, filled with the invented trip |
| `prompts/` | Two briefs for a session: write a day, draw a plate |
| `COMPANION.md` | How the travel companion (a Claude Project that has read the book) was set up, as a template |
| `docs/` | The page GitHub Pages serves: turn the sample's pages and see what's underneath each one. Has a text version for people and for AI |
| `assets/book.gif` | The animation at the top of the README: the sample book, nothing from the real one |

## Out

| What | Why it's out |
|---|---|
| The real book: its chapters, drawings and cover | It describes a real trip. The method is the part worth sharing |
| The real skeleton: dates, bookings, flights, hotels, who travelled | Private by definition. That file never entered the book either: that's rule one of the method |
| The companion's real instructions | They name accounts, people and places. `COMPANION.md` keeps the structure and drops all of that |
| The real book's git history | It belongs to the private repo. This repo starts clean |

## How it was checked

- Every file was read for names of people, places of stay, dates, booking codes, accounts and email addresses
  before publishing. The sample trip has no dates at all.
- The facts in the sample chapters each have a source at the end of the chapter; tourism and commercial
  sources are marked as such, and where a fact is uncertain the text says so.
- A secret scanner (gitleaks) on the files and on the git history, and a pattern search for keys and tokens.
- A separate reviewer agent read the whole repo, file by file, looking for anything private.
- The EPUB builds with `scripts/build-epub.sh`, and the page was opened and its pages turned before publishing.
