"""Shared bits for the plates: one drawing, two editions.

Every plate uses these classes. Without class="color" on the root <svg> the plate
is grey (for e-ink); render.sh adds class="color" for the colour edition, and the
`svg.color` rules below take over. Nothing else changes between the two.
"""
SERIF = "'Iowan Old Style', 'Palatino', 'Georgia', serif"
SANS = "'Helvetica Neue', 'Arial', sans-serif"
JP = "'Hiragino Mincho ProN', 'Noto Serif CJK JP', 'Yu Mincho', serif"

STYLE = """<style>
  .bg { fill:#fff }  .ink { fill:#111 }  .ink-s { stroke:#111 }  .mid { fill:#777 }  .mid-s { stroke:#777 }
  .light { fill:#d6d6d6 }  .light-s { stroke:#bdbdbd }  .paper { fill:#f2f2f2 }  .acc { fill:#444 }  .acc-s { stroke:#444 }
  .moss { fill:#9a9a9a }   .cloth { fill:#3a3a3a }  .wood { fill:#8c8c8c }  .wood-s { stroke:#555 }
  svg.color .bg { fill:#f6f1e7 }  svg.color .ink { fill:#1d2733 }  svg.color .ink-s { stroke:#1d2733 }
  svg.color .mid { fill:#5d6b7a }  svg.color .mid-s { stroke:#5d6b7a }  svg.color .light { fill:#e8dcc4 }
  svg.color .light-s { stroke:#cdbb96 }  svg.color .paper { fill:#efe6d3 }  svg.color .acc { fill:#b23a2b }
  svg.color .acc-s { stroke:#b23a2b }  svg.color .moss { fill:#6f8f4e }  svg.color .cloth { fill:#2b4a6f }
  svg.color .wood { fill:#a0744a }  svg.color .wood-s { stroke:#6b4a2c }
</style>"""


def svg(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f'{STYLE}<rect class="bg" width="{w}" height="{h}"/>{body}</svg>\n')


def text(x, y, s, size, cls="ink", family=SERIF, anchor="middle", extra=""):
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" class="{cls}" '
            f'text-anchor="{anchor}" {extra}>{s}</text>')
