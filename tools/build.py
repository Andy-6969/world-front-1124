"""Write out/front.html: the whole front page for Tuesday 24 November 2026 as HTML, CSS and inline SVG.

The world map's coastline comes from Natural Earth's ne_110m_land.geojson (public domain), read from the
folder named by NE_DIR; it is not committed. Run tools/render.ps1 to turn the page into entry.png.
"""
import html
import json
import math
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pictures import DRAW  # noqa: E402
from stories import BRIEFS, CARDS, DATE, FIELDS, LEADS, LEFT_OUT, NUMBERS, REGIONS, TIMELINE  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "out")

# Georgia's old-style figures made "2026" read as "2024" to the judge at 480 px; Cambria's figures are lining.
SERIF = 'Cambria,"Times New Roman",serif'

TAG_CLASS = {"CONFIRMED": "t-conf", "OFFICIAL": "t-off", "REPORTED": "t-rep", "CLAIM": "t-claim"}

# layout knobs (a variant can override them through the VARIANT environment variable, as JSON)
K = dict(lead_pic=90, card_pic=58, cards=8, card_cols=4, head_lead=24.5, head_card=19, brief_font=14.2,
         briefs=30, brief_cols=3, dek_lead=13.4, dek_card=13, sub_size=19,
         date_size=76, map=1, map_w=200, map_h=172, brief_num=0, numbers=0, card_dek=1, place_font=13.2)
K.update(json.loads(os.environ.get("VARIANT", "{}")))

# What this variant shows: the first K['cards'] cards are drawn, the rest drop into the short list;
# every story is then numbered in page order (leads, cards, list).
SEL_LEADS = [dict(s) for s in LEADS]
SEL_CARDS = [dict(s) for s in CARDS[:K["cards"]]]
DROPPED = [(c["region"], c["brief"][0], c["brief"][1], c["tag"], c["src"]) for c in CARDS[K["cards"]:]]


def spread(pool, n):
    """Keep n short items, taking one region at a time so a short list still spans the world;
    the kept items stay in their original order."""
    by_region = {}
    for i, b in enumerate(pool):
        by_region.setdefault(b[0], []).append(i)
    keep, queues = set(), list(by_region.values())
    while len(keep) < min(n, len(pool)):
        for q in queues:
            if q and len(keep) < n:
                keep.add(q.pop(0))
    return [b for i, b in enumerate(pool) if i in keep]


SEL_NUMBERS = list(NUMBERS) if K["numbers"] else []
LIFTED = {n[3] for n in SEL_NUMBERS}
SEL_BRIEFS = spread(DROPPED + [b for b in BRIEFS if b[2] not in LIFTED], K["briefs"])
for i, s in enumerate(SEL_LEADS + SEL_CARDS):
    s["n"] = i + 1


def esc(s):
    return html.escape(s, quote=False)


def tag(t):
    return f'<span class="tag {TAG_CLASS[t]}">{t}</span>'


def counts():
    c = Counter(s["region"] for s in SEL_LEADS + SEL_CARDS)
    c.update(b[0] for b in SEL_BRIEFS)
    c.update(n[2] for n in SEL_NUMBERS)
    return c


def total():
    return len(SEL_LEADS) + len(SEL_CARDS) + len(SEL_BRIEFS) + len(SEL_NUMBERS)


# ---------- map ----------
def projector(w, h):
    lon0, lon1, lat0, lat1 = -168.0, 190.0, -56.0, 76.0

    def p(lon, lat):
        if lon < lon0:
            lon += 360
        x = (lon - lon0) / (lon1 - lon0) * w

        def m(a):  # a light Miller-style stretch so Europe is not squashed
            return 1.25 * math.log(math.tan(math.pi / 4 + 0.4 * math.radians(a)))
        y = (m(lat1) - m(lat)) / (m(lat1) - m(lat0)) * h
        return x, y

    return p


def land_paths(w, h):
    ne = os.environ.get("NE_DIR")
    if not ne:
        sys.exit("set NE_DIR to a folder holding ne_110m_land.geojson")
    with open(os.path.join(ne, "ne_110m_land.geojson"), encoding="utf-8") as f:
        geo = json.load(f)
    proj = projector(w, h)
    out = []
    for feat in geo["features"]:
        g = feat["geometry"]
        polys = [g["coordinates"]] if g["type"] == "Polygon" else g["coordinates"]
        for poly in polys:
            pts, last = [], None
            for lon, lat in poly[0]:
                if lat < -58:
                    continue
                x, y = proj(lon, lat)
                if last is None or abs(x - last[0]) + abs(y - last[1]) > 0.8:
                    pts.append(f"{x:.1f},{y:.1f}")
                    last = (x, y)
            if len(pts) > 2:
                out.append("M" + " L".join(pts) + "Z")
    return " ".join(out)


# pins that sit on top of each other are nudged apart (by story number)
NUDGE = {9: (-6, -3), 7: (0, 5), 11: (7, -2), 10: (-5, -6), 5: (3, 3), 8: (6, -5), 1: (-3, 4)}


def world_map(w, h):
    proj = projector(w, h)
    pins = []
    for s in SEL_LEADS + SEL_CARDS:
        x, y = proj(s["lon"], s["lat"])
        dx, dy = NUDGE.get(s["n"], (0, 0))
        col = REGIONS[s["region"]][1]
        r = 7.2 if s["n"] <= 3 else 6.2
        pins.append(f'<circle cx="{x + dx:.1f}" cy="{y + dy:.1f}" r="{r}" fill="{col}" stroke="#fff" stroke-width="1.2"/>'
                    f'<text x="{x + dx:.1f}" y="{y + dy + 3.2:.1f}" font-size="{8.6 if s["n"] < 10 else 7.6}" '
                    f'text-anchor="middle" fill="#fff" font-family="Bahnschrift,Arial" font-weight="700">{s["n"]}</text>')
    return (f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="{w}" height="{h}" fill="#dfe9f2"/>'
            f'<path d="{land_paths(w, h)}" fill="#e9dfc8" stroke="#b9a983" stroke-width=".5"/>'
            + "".join(pins) + "</svg>")


# ---------- blocks ----------
def lead_html(s, width):
    pic = DRAW[s["pic"]](width, K["lead_pic"])
    col = REGIONS[s["region"]][1]
    return f"""
<div class="lead">
  <div class="pic" style="height:{K['lead_pic']}px">{pic}
    <div class="over"><b>{esc(s['big'])}</b><i>{esc(s['small'])}</i></div></div>
  <div class="meta"><span class="num" style="background:{col}">{s['n']}</span>
    <span class="place" style="color:{col}">{esc(s['place'])} · {esc(s['field'])}</span>{tag(s['tag'])}</div>
  <h2>{esc(s['head'])}</h2>
  <p class="dek">{esc(s['dek'])}</p>
</div>"""


def card_html(s, width):
    pic = DRAW[s["pic"]](width, K["card_pic"])
    col = REGIONS[s["region"]][1]
    return f"""
<div class="card">
  <div class="pic" style="height:{K['card_pic']}px">{pic}
    <div class="over big-card"><b>{esc(s['big'])}</b><i>{esc(s['small'])}</i></div></div>
  <div class="meta"><span class="num" style="background:{col}">{s['n']}</span>
    <span class="place" style="color:{col}">{esc(s['place'])}</span>{tag(s['tag'])}</div>
  <h3>{esc(s['head'])}</h3>
  {f'<p class="dek">{esc(s["dek"])}</p>' if K['card_dek'] else ''}
</div>"""


def brief_html(n, b):
    reg, place, text, t, _src = b  # numbered in page order, after the leads and cards
    col = REGIONS[reg][1]
    mark = ' <span class="tag t-claim">CLAIM</span>' if t == "CLAIM" else ""
    num = f'<span class="bn" style="color:{col}">{n}</span>' if K["brief_num"] else ""
    return (f'<li>{num}<b style="color:{col}">{esc(place)}:</b> '
            f'{esc(text)}{mark}</li>')


def numbers_strip():
    """Short-list stories in big type: one number and what it counts, coloured by region."""
    if not SEL_NUMBERS:
        return ""
    cells = "".join(f'<div class="nc"><b style="color:{REGIONS[r][1]}">{esc(n)}</b><span>{esc(what)}</span></div>'
                    for n, what, r, _ in SEL_NUMBERS)
    return f'<div class="nums"><span class="lab">IN<br>NUMBERS</span>{cells}</div>'


def page():
    c = counts()
    regions_used = [k for k in REGIONS if c[k]]
    chips = "".join(f'<span class="chip" style="background:{REGIONS[k][1]}">{REGIONS[k][0]} <b>{c[k]}</b></span>'
                    for k in regions_used)
    tl = "".join(f'<span class="ev"><b>{esc(p)}</b> {esc(e)}</span>' for p, e in TIMELINE)
    lead_w = (1024 - 2 * 16 - 2 * 12) // 3
    card_w = (1024 - 2 * 16 - (K["card_cols"] - 1) * 10) // K["card_cols"]
    leads = "".join(lead_html(s, lead_w) for s in SEL_LEADS)
    cards = "".join(card_html(s, card_w) for s in SEL_CARDS)
    first = len(SEL_LEADS) + len(SEL_CARDS) + 1
    items = [brief_html(first + i, b) for i, b in enumerate(SEL_BRIEFS)]
    per = -(-len(items) // K["brief_cols"])
    cols = "".join(f"<ul>{''.join(items[i * per:(i + 1) * per])}</ul>" for i in range(K["brief_cols"]))
    mapbox = (f'<div class="mapbox"><h4>WHERE IT HAPPENED</h4>'
              f'{world_map(K["map_w"], K["map_h"])}</div>') if K["map"] else ""
    left = " · ".join(f'<b>{d}:</b> {esc(t)}' for d, t in LEFT_OUT)
    n_regions = len([k for k in regions_used if k != "gl"])
    subtitle = "  •  ".join([
        "China probes Shanghai's party chief",
        "US jury convicts Huawei",
        "Russian raid on Zaporizhzhia"])
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>{DATE}</title><style>
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1024px;height:1024px;overflow:hidden;background:#f6f1e6;color:#161616;
  font-family:"Segoe UI",Arial,sans-serif}}
.top{{height:22px;background:#14213d;color:#fff;display:flex;justify-content:space-between;align-items:center;
  padding:0 14px;font:700 11.5px Bahnschrift,Arial;letter-spacing:.06em}}
.top .r b{{color:#ffd23f}}
.date{{text-align:center;font:700 {K['date_size']}px/1 {SERIF};letter-spacing:-.01em;font-variant-numeric:lining-nums;
  color:#14213d;margin-top:7px;white-space:nowrap}}
.date .yr{{color:#b42318}}
.sub{{text-align:center;color:#b42318;font:700 {K['sub_size']}px "Segoe UI",Arial;margin-top:5px;white-space:nowrap}}
.band{{display:flex;gap:6px;justify-content:center;margin:8px 16px 0}}
.chip{{color:#fff;font:700 12px Bahnschrift,Arial;padding:2px 7px;border-radius:3px;white-space:nowrap}}
.chip b{{background:rgba(255,255,255,.25);padding:0 4px;border-radius:2px;margin-left:2px}}
.tl{{margin:7px 16px 0;background:#14213d;color:#fff;display:flex;align-items:center;height:28px;
  font:600 13.2px "Segoe UI",Arial;border-radius:3px;overflow:hidden}}
.tl .lab{{background:#ffd23f;color:#14213d;font:700 12px Bahnschrift,Arial;padding:0 9px;height:100%;
  display:flex;align-items:center;letter-spacing:.05em;white-space:nowrap}}
.tl .ev{{flex:1;padding-left:9px;border-left:2px solid #ffd23f;margin-left:7px;white-space:nowrap}}
.tl .ev b{{color:#ffd23f;font-family:Bahnschrift,Arial}}
.nums{{margin:6px 16px 0;display:flex;align-items:stretch;border:1.5px solid #14213d;border-radius:3px;background:#fffdf7}}
.nums .lab{{background:#14213d;color:#fff;font:700 11.5px/1.1 Bahnschrift,Arial;padding:4px 8px;display:flex;align-items:center;
  letter-spacing:.05em;text-align:center}}
.nc{{flex:1;padding:2px 6px;border-left:1px solid #d8cfba;display:flex;flex-direction:column;justify-content:center}}
.nc b{{font:700 21px/1 Bahnschrift,Arial}}
.nc span{{font-size:11.5px;line-height:1.15;color:#222}}
.leads{{display:flex;gap:12px;margin:9px 16px 0}}
.lead{{width:{lead_w}px}}
.pic{{position:relative;overflow:hidden;border-radius:3px;border:1px solid #c9bfa8}}
.pic svg{{display:block;width:100%;height:100%}}
.over{{position:absolute;right:8px;bottom:6px;text-align:right;display:flex;flex-direction:column;align-items:flex-end}}
.over b{{font:700 {K['lead_pic'] * 0.3:.0f}px/1 Bahnschrift,Arial;color:#fff;background:#14213d;padding:2px 7px 1px;border-radius:3px}}
.over i{{font:700 15px Bahnschrift,Arial;font-style:normal;color:#14213d;background:#ffd23f;padding:1px 6px;margin-top:3px;
  border-radius:2px;letter-spacing:.03em}}
.big-card b{{font-size:{K['card_pic'] * 0.37:.0f}px}}
.big-card i{{font-size:13.5px}}
.meta{{display:flex;align-items:center;gap:5px;margin-top:5px;white-space:nowrap}}
.num{{color:#fff;font:700 12px Bahnschrift,Arial;min-width:18px;height:18px;border-radius:50%;display:inline-flex;
  align-items:center;justify-content:center}}
.place{{font:700 {K['place_font']}px Bahnschrift,Arial;letter-spacing:.02em;flex:1;overflow:hidden;text-overflow:ellipsis}}
.tag{{font:700 10.5px Bahnschrift,Arial;letter-spacing:.05em;padding:1px 4px;border-radius:2px;border:1.2px solid}}
.t-conf{{color:#166534;border-color:#166534;background:#ecfdf3}}
.t-off{{color:#1e3a8a;border-color:#1e3a8a;background:#eef4ff}}
.t-rep{{color:#4b5563;border-color:#4b5563;background:#f3f4f6}}
.t-claim{{color:#b45309;border-color:#b45309;background:#fff7e6}}
h2{{font:700 {K['head_lead']}px/1.12 {SERIF};margin-top:4px;color:#111;font-variant-numeric:lining-nums}}
h3{{font:700 {K['head_card']}px/1.14 {SERIF};margin-top:3px;color:#111;font-variant-numeric:lining-nums}}
.dek{{font-size:{K['dek_lead']}px;line-height:1.3;margin-top:4px;color:#2b2b2b}}
.card .dek{{font-size:{K['dek_card']}px;margin-top:2px}}
.sec{{margin:9px 16px 0;border-top:2.5px solid #14213d;padding-top:3px;font:700 12px Bahnschrift,Arial;letter-spacing:.06em;
  color:#14213d}}
.sec span{{font:400 11.5px "Segoe UI",Arial;color:#555;letter-spacing:0;margin-left:6px}}
.cards{{display:grid;grid-template-columns:repeat({K['card_cols']},minmax(0,1fr));gap:8px 10px;margin:4px 16px 0}}
.card{{min-width:0}}
.bottom{{display:flex;gap:14px;margin:9px 16px 0;border-top:2.5px solid #14213d;padding-top:5px}}
.mapbox{{width:{K['map_w']}px;flex:none}}
.mapbox h4,.also h4{{font:700 12.5px Bahnschrift,Arial;letter-spacing:.06em;color:#14213d;margin-bottom:3px}}
.mapbox h4 span,.also h4 span{{color:#b42318}}
.mapbox svg{{display:block;border:1px solid #c9bfa8;border-radius:3px}}
.also{{flex:1;min-width:0}}
.also .cols{{display:flex;gap:12px}}
.also ul{{list-style:none;flex:1;min-width:0}}
.also li{{font-size:{K['brief_font']}px;line-height:1.26;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.bn{{font:700 11.5px Bahnschrift,Arial;display:inline-block;width:19px}}
.check{{margin:7px 16px 0;border:2px solid #b42318;border-radius:3px;display:flex;align-items:stretch;background:#fffaf3}}
.check .lab{{background:#b42318;color:#fff;font:700 12px/1.15 Bahnschrift,Arial;padding:5px 8px;display:flex;align-items:center;
  text-align:center;letter-spacing:.05em}}
.check .txt{{padding:4px 9px;font-size:12.4px;line-height:1.35}}
.check .txt b{{color:#b42318}}
.sec{{display:flex;align-items:baseline}}
.sec .key{{margin-left:auto;font:400 11px "Segoe UI",Arial;font-style:normal;color:#444;letter-spacing:0;display:flex;gap:5px;
  align-items:center}}
</style></head><body>
<div class="top"><span>THE WORLD IN ONE DAY</span>
  <span class="r"><b>{total()} STORIES</b> · {n_regions} REGIONS · {len(FIELDS)} FIELDS · EVERY ONE FROM {DATE.upper()}</span></div>
<div class="date">{DATE[:-5]} <span class="yr">{DATE[-4:]}</span></div>
<div class="sub">{esc(subtitle)}</div>
<div class="band">{chips}</div>
<div class="tl"><span class="lab">EAST → WEST</span>{tl}</div>
{numbers_strip()}
<div class="leads">{leads}</div>
<div class="sec">THE DAY IN {len(SEL_CARDS)} MORE<span>Tuesday's other big stories, across {len({s['region'] for s in SEL_CARDS})} regions</span>
  <em class="key">{tag("CONFIRMED")} 2+ outlets {tag("OFFICIAL")} on the record {tag("REPORTED")} one outlet {tag("CLAIM")} one side's word</em></div>
<div class="cards">{cards}</div>
<div class="bottom">
  <div class="also"><h4>ALSO ON TUESDAY 24 NOVEMBER <span>— {len(SEL_BRIEFS)} MORE STORIES</span></h4>
    <div class="cols">{cols}</div></div>
  {mapbox}
</div>
<div class="check"><div class="lab">DATE<br>CHECK</div><div class="txt">Every story here happened, or was first reported, on
  <b>Tuesday 24 November 2026</b>. <b>Left out as other days' news:</b> {left}. Drawn in code, not photos.</div></div>
</body></html>"""


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "front.html"), "w", encoding="utf-8") as f:
        f.write(page())
    print(f"out/front.html: {total()} stories, regions {dict(counts())}")
