# Brief: draw a plate

```text
Draw the plate "<name>" for the chapter <chapter>: <what it has to explain, in one sentence>.

- Write plates/<name>.py using plates/common.py, so it outputs plates/<name>.svg.
- Grey by default, colours only under `svg.color` (see common.py). Same drawing, two editions.
- Text big enough to read on a 6-inch e-reader: nothing under ~22 px at 1200 px wide.
- Every number or name on the plate must be in the chapter's sources. If it's a sketch, say "not to scale".
- Render with `bash plates/render.sh <name>`, then LOOK at both PNGs before wiring it in. Fix what's
  overlapping, cut off or wrong, and look again.
- Done = both PNGs looked at, the figure wired into the chapter with alt text and a caption, the EPUB builds.
```
