"""Ryoan-ji from above: fifteen stones in five groups, and why you never see all of them.

A sketch, not a survey: the group sizes (5, 2, 3, 2, 3) are the commonly given ones; the
positions are drawn to read clearly, not to scale.
"""
import pathlib
from common import svg, text, SERIF, SANS, JP

W, H = 1200, 760
out = []
a = out.append

# the gravel rectangle, with raked lines
gx, gy, gw, gh = 90, 110, 1020, 440
a(f'<rect x="{gx-14}" y="{gy-14}" width="{gw+28}" height="{gh+14}" class="wood"/>')  # clay wall, top and sides
a(f'<rect x="{gx}" y="{gy}" width="{gw}" height="{gh}" class="paper"/>')
for y in range(gy + 14, gy + gh, 14):
    a(f'<line x1="{gx}" y1="{y}" x2="{gx+gw}" y2="{y}" class="light-s" stroke-width="2"/>')

# five groups: (centre x, centre y, [(dx, dy, rx, ry), ...])
groups = [
    (230, 300, [(-40, -10, 34, 24), (5, 15, 26, 18), (40, -18, 22, 16), (-5, -42, 16, 12), (55, 22, 14, 10)]),
    (430, 235, [(-14, 0, 26, 18), (24, 10, 16, 12)]),
    (600, 360, [(-24, 0, 30, 20), (20, -12, 18, 13), (-22, -34, 13, 9)]),
    (790, 250, [(-12, 0, 22, 16), (22, 12, 14, 10)]),
    (960, 340, [(-26, -6, 28, 19), (12, 14, 18, 13), (34, -14, 13, 9)]),
]
hidden = (2, 2)   # group 3, third stone: right behind the big one, on the viewer's line of sight
for gi, (cx, cy, stones) in enumerate(groups):
    # rake rings around the group
    for k in (1, 2):
        a(f'<ellipse cx="{cx}" cy="{cy}" rx="{70 + 22*k}" ry="{48 + 16*k}" fill="none" class="light-s" stroke-width="3"/>')
    a(f'<ellipse cx="{cx}" cy="{cy}" rx="68" ry="46" class="moss" opacity="0.55"/>')
    for si, (dx, dy, rx, ry) in enumerate(stones):
        cls = "light" if (gi, si) == hidden else "ink"
        a(f'<ellipse cx="{cx+dx}" cy="{cy+dy}" rx="{rx}" ry="{ry}" class="{cls}"/>')
        if (gi, si) == hidden:
            a(f'<ellipse cx="{cx+dx}" cy="{cy+dy}" rx="{rx}" ry="{ry}" fill="none" class="acc-s" stroke-width="3" stroke-dasharray="6 5"/>')
    a(text(cx, cy - 92, str(len(stones)), 30, "mid", SANS, extra='font-weight="700"'))

# the veranda and the viewer
vy = gy + gh + 30
a(f'<rect x="{gx-14}" y="{vy}" width="{gw+28}" height="46" class="wood"/>')
for x in range(gx, gx + gw, 60):
    a(f'<line x1="{x}" y1="{vy}" x2="{x}" y2="{vy+46}" class="wood-s" stroke-width="2"/>')
ex, ey = 560, vy + 23
a(f'<circle cx="{ex}" cy="{ey}" r="15" class="acc"/>')
# line of sight through the front stone of group 3 to the hidden one
g = groups[2]
fx, fy = g[0] + g[2][0][0], g[1] + g[2][0][1]
hx, hy = g[0] + g[2][2][0], g[1] + g[2][2][1]
a(f'<line x1="{ex}" y1="{ey}" x2="{hx}" y2="{hy}" class="acc-s" stroke-width="3" stroke-dasharray="10 8"/>')

a(text(W / 2, 62, "Fifteen stones, never all at once", 40, "ink", SERIF))
a(text(hx + 40, hy - 30, "hidden from here", 24, "acc", SANS, anchor="start", extra='font-weight="700"'))
a(text(W / 2, H - 40, "From above: 5 + 2 + 3 + 2 + 3 = 15.  From the veranda: fourteen at most.", 26, "mid", SANS))
a(text(ex + 26, ey + 9, "you", 24, "ink", SANS, anchor="start", extra='font-weight="700"'))

pathlib.Path(__file__).with_suffix(".svg").write_text(svg(W, H, "".join(out)))
