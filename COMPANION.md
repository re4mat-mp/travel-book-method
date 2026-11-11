# The travel companion: a Claude that has read your book

The book is for reading. The companion is for asking: a Claude Project that has your book's text and your
instructions, so on the street you can ask "what was the story of this garden?" and get your own chapter back,
short.

## Set it up once

1. In Claude, create a Project for the trip.
2. **Instructions:** paste the template below and make it yours.
3. **Knowledge:** add the book's text. The simplest way is the plain text of every chapter in one file; connect
   the repo through the GitHub integration and select only that file or folder, not the images or the EPUB.
4. Test it with three questions you know the answer to, from three different chapters.

When the book changes, sync the Project's knowledge: a connected repo is a snapshot until you sync it.

## Instructions template

```text
You are my travel companion for this trip. You have read my travel book; it is in your knowledge.

How to answer
- Short and plain. The answer first, the context after, and only if it helps.
- If I talk by voice, answer in spoken sentences: no lists, no tables.
- If you don't know or can't find it, say so. Never make up a time, a platform, a price or an address.

Where the truth is
- The book: places, history, customs, phrases. Use it to explain why a place or a custom is the way it is.
- For anything that changes (opening hours, trains, tickets), search the web and say where it came from.

Words
- Every word in the local language as: script · romanisation · meaning.
- When I ask for a phrase, give me a short one to say out loud, and what people may answer.

Notes for the book
- If I say "note for the book", write it cleanly in a block that starts with NOTE FOR THE BOOK, so I can add it
  to the repo later. You can't write to the repo from here.
```

## Editing the book on the road

The Project reads the repo; it can't change it. To change the book from a tablet, open a Claude Code session
on the repo (the `CLAUDE.md` there tells it what to do), ask for the change in plain words, and let it rebuild
the EPUB and push. Then download the new EPUB and send it to your e-reader.

## Sending it to a Kindle

Use Amazon's Send to Kindle (the app, the web page, or email to your Kindle address). Two things that bit me:
- A big EPUB with colour images can be rejected. Greyscale plates (8-bit grey PNG) cut the size by almost half,
  and the rejection went away.
- Amazon may ask you to confirm the document by email. If you don't, it never arrives.
