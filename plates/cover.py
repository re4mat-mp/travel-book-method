"""The cover: a seal, the title, the three places, and a band of waves (seigaiha)."""
import pathlib
from common import svg, text, SERIF, SANS, JP

W, H = 800, 1280
out = []
a = out.append

# the seal: 旅 (tabi, a journey) in a square
a(f'<rect x="{W/2-60}" y="150" width="120" height="120" rx="10" class="acc"/>')
a(text(W / 2, 236, "旅", 84, "bg", JP))

a(text(W / 2, 470, "Three days", 104, "ink", SERIF))
a(f'<line x1="{W/2-50}" y1="515" x2="{W/2+50}" y2="515" class="acc-s" stroke-width="3"/>')
a(text(W / 2, 585, "A sample travel book", 40, "mid", SERIF, extra='font-style="italic"'))
a(text(W / 2, 690, "KANAZAWA · KYOTO · NAOSHIMA", 24, "mid", SANS, extra='letter-spacing="5"'))

# seigaiha: rows of concentric half-circles, each row offset by half a wave
r, top = 56, 900
a(f'<clipPath id="band"><rect x="0" y="{top}" width="{W}" height="{4*r}"/></clipPath><g clip-path="url(#band)">')
for row in range(7):
    y = top + row * r * 0.5
    off = (row % 2) * r
    for i in range(-1, W // (2 * r) + 2):
        cx = i * 2 * r + off
        for k, rr in enumerate((r, r * 0.72, r * 0.44)):
            cls = "light" if k == 1 else "bg"
            a(f'<circle cx="{cx}" cy="{y + r}" r="{rr}" class="{cls if k else "cloth"}"/>')
a('</g>')

pathlib.Path(__file__).with_suffix(".svg").write_text(svg(W, H, "".join(out)))
