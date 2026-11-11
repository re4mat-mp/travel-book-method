"""The noren: the split curtain over a shop door. Out means open; taken in means closed."""
import pathlib
from common import svg, text, SERIF, SANS, JP

W, H = 1200, 700
out = []
a = out.append


def front(x0, open_):
    # roof, posts, a lattice door
    a(f'<polygon points="{x0-30},170 {x0+470},170 {x0+440},120 {x0},120" class="ink"/>')
    a(f'<rect x="{x0}" y="170" width="440" height="380" class="paper"/>')
    a(f'<rect x="{x0}" y="170" width="24" height="380" class="wood"/>')
    a(f'<rect x="{x0+416}" y="170" width="24" height="380" class="wood"/>')
    for x in range(x0 + 70, x0 + 380, 18):
        a(f'<line x1="{x}" y1="230" x2="{x}" y2="550" class="wood-s" stroke-width="3"/>')
    a(f'<rect x="{x0+60}" y="230" width="320" height="320" fill="none" class="wood-s" stroke-width="5"/>')
    a(f'<rect x="{x0-40}" y="550" width="520" height="16" class="ink"/>')
    if open_:
        # the rod and three panels, with a crest across the middle panel
        a(f'<rect x="{x0+40}" y="184" width="360" height="8" class="ink"/>')
        for i in range(3):
            px = x0 + 46 + i * 118
            a(f'<rect x="{px}" y="192" width="112" height="200" class="cloth"/>')
        a(f'<circle cx="{x0+220}" cy="280" r="46" class="bg"/>')
        a(text(x0 + 220, 300, "錦", 56, "cloth", JP))
    else:
        # the curtain rolled up and leaning inside the door
        a(f'<rect x="{x0+330}" y="300" width="18" height="240" rx="9" class="cloth" transform="rotate(8 {x0+339} 540)"/>')


front(90, True)
front(670, False)
a(text(310, 620, "Out: open", 34, "ink", SERIF))
a(text(890, 620, "Taken in: closed for the day", 34, "ink", SERIF))
a(text(W / 2, 72, "暖簾 · noren · the curtain over the door", 38, "ink", JP))
a(text(W / 2, 672, "The crest on the cloth is the shop's sign. (The character here, 錦, is nishiki: brocade.)", 22, "mid", SANS))

pathlib.Path(__file__).with_suffix(".svg").write_text(svg(W, H, "".join(out)))
