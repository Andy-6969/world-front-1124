"""Flat SVG drawings, one per story picture. Each function takes the box width and height (in CSS px) and
returns SVG markup for that box. The scene sits on the left; the right side is kept calm so the big
number drawn over it (in HTML) stays readable. Everything is drawn from plain shapes: no photos, no logos."""

NAVY = "#14213d"
SEA = "#1d4e89"
INK = "#1b1b1b"
RED = "#c62828"
ORANGE = "#f08a24"
YELLOW = "#ffd23f"
GREEN = "#2e7d32"


def svg(w, h, body, bg):
    return (f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="{w}" height="{h}" fill="{bg}"/>{body}</svg>')


def smoke(x, y, r):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#4b5563" opacity=".7"/>'
            f'<circle cx="{x + r * 0.8}" cy="{y - r * 0.6}" r="{r * 0.75}" fill="#6b7280" opacity=".65"/>')


def probe(w, h):
    """A pillared hall under a red star, with a magnifying glass held over it."""
    hall = (f'<rect x="{h * 0.1}" y="{h * 0.8}" width="{h * 1.3}" height="{h * 0.08}" fill="#7f1d1d"/>'
            f'<path d="M{h * 0.08} {h * 0.36} L{h * 0.75} {h * 0.16} L{h * 1.42} {h * 0.36} Z" fill="#991b1b"/>'
            + "".join(f'<rect x="{h * (0.2 + i * 0.22)}" y="{h * 0.38}" width="{h * 0.1}" height="{h * 0.42}" fill="#e7d9c4"/>'
                      for i in range(5))
            + f'<rect x="{h * 0.1}" y="{h * 0.36}" width="{h * 1.3}" height="{h * 0.04}" fill="#7f1d1d"/>')
    star = (f'<path d="M{h * 0.75} {h * 0.02} l{h * 0.035} {h * 0.07} l{h * 0.075} {h * 0.008} l{-h * 0.057} {h * 0.05} '
            f'l{h * 0.018} {h * 0.075} l{-h * 0.07} {-h * 0.04} l{-h * 0.07} {h * 0.04} l{h * 0.018} {-h * 0.075} '
            f'l{-h * 0.057} {-h * 0.05} l{h * 0.075} {-h * 0.008} Z" fill="{YELLOW}"/>')
    glass = (f'<circle cx="{h * 1.42}" cy="{h * 0.46}" r="{h * 0.23}" fill="#ffffff" fill-opacity=".35" '
             f'stroke="{INK}" stroke-width="{h * 0.06}"/>'
             f'<path d="M{h * 1.58} {h * 0.63} L{h * 1.85} {h * 0.92}" stroke="{INK}" stroke-width="{h * 0.1}" '
             f'stroke-linecap="round"/>')
    return svg(w, h, hall + star + glass, "#f6e3d3")


def verdict(w, h):
    """A courthouse front and a gavel coming down on its block."""
    court = (f'<path d="M{h * 0.06} {h * 0.34} L{h * 0.55} {h * 0.1} L{h * 1.04} {h * 0.34} Z" fill="#64748b"/>'
             + "".join(f'<rect x="{h * (0.14 + i * 0.2)}" y="{h * 0.38}" width="{h * 0.09}" height="{h * 0.44}" fill="#cbd5e1"/>'
                       for i in range(5))
             + f'<rect x="{h * 0.06}" y="{h * 0.82}" width="{h * 0.98}" height="{h * 0.08}" fill="#64748b"/>')
    gavel = (f'<g transform="rotate(-32 {h * 1.45} {h * 0.42})">'
             f'<rect x="{h * 1.18}" y="{h * 0.26}" width="{h * 0.52}" height="{h * 0.24}" rx="4" fill="#7c4a1e"/>'
             f'<rect x="{h * 1.4}" y="{h * 0.5}" width="{h * 0.08}" height="{h * 0.48}" fill="#a16207"/></g>'
             f'<rect x="{h * 1.12}" y="{h * 0.8}" width="{h * 0.5}" height="{h * 0.1}" fill="#7c4a1e"/>'
             f'<path d="M{h * 1.1} {h * 0.66} l{-h * 0.08} {-h * 0.06} M{h * 1.08} {h * 0.75} l{-h * 0.1} 0" '
             f'stroke="{INK}" stroke-width="2"/>')
    return svg(w, h, court + gavel, "#e8edf3")


def apartment(w, h):
    """A five-storey block with a blown-out corner, smoke and fire, at dawn."""
    x0, bw = h * 0.25, h * 0.95
    floors = []
    for f in range(5):
        for c in range(5):
            if f >= 3 and c >= 3:
                continue  # the missing corner
            lit = "#fde68a" if (f + c) % 3 == 0 else "#1f2937"
            floors.append(f'<rect x="{x0 + h * 0.07 + c * h * 0.18}" y="{h * 0.28 + (4 - f) * h * 0.12}" '
                          f'width="{h * 0.1}" height="{h * 0.07}" fill="{lit}"/>')
    body = (f'<rect y="{h * 0.88}" width="{w}" height="{h * 0.12}" fill="#3f3f46"/>'
            f'<path d="M{x0} {h * 0.88} L{x0} {h * 0.24} L{x0 + bw * 0.55} {h * 0.24} L{x0 + bw * 0.62} {h * 0.4} '
            f'L{x0 + bw * 0.8} {h * 0.36} L{x0 + bw} {h * 0.52} L{x0 + bw} {h * 0.88} Z" fill="#94a3b8"/>'
            + "".join(floors)
            + smoke(x0 + bw * 0.78, h * 0.22, h * 0.14)
            + f'<path d="M{x0 + bw * 0.66} {h * 0.48} q{h * 0.05} {-h * 0.16} {h * 0.1} {-h * 0.04} '
              f'q{h * 0.04} {-h * 0.14} {h * 0.09} 0 q{h * 0.03} {-h * 0.1} {h * 0.06} {h * 0.06} Z" fill="{ORANGE}"/>')
    return svg(w, h, body, "#f4c9a8")


def chipdown(w, h):
    """A GPU chip and a share line that leaps up, then falls."""
    s = h * 0.56
    x, y = h * 0.12, h * 0.22
    pins = "".join(
        f'<rect x="{x + s * (0.12 + i * 0.16)}" y="{y - s * 0.12}" width="{s * 0.06}" height="{s * 0.12}" fill="#9aa4b2"/>'
        f'<rect x="{x + s * (0.12 + i * 0.16)}" y="{y + s}" width="{s * 0.06}" height="{s * 0.12}" fill="#9aa4b2"/>'
        for i in range(5))
    chip = (pins + f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="4" fill="#1f2937"/>'
            f'<rect x="{x + s * 0.2}" y="{y + s * 0.2}" width="{s * 0.6}" height="{s * 0.6}" fill="#76b900"/>'
            f'<text x="{x + s / 2}" y="{y + s * 0.6}" font-family="Bahnschrift,Arial" font-weight="700" '
            f'font-size="{s * 0.22}" text-anchor="middle" fill="#0b1d05">GPU</text>')
    pts = [(h * 0.85, h * 0.85), (h * 1.05, h * 0.78), (h * 1.2, h * 0.2), (h * 1.42, h * 0.32), (h * 1.62, h * 0.62)]
    line = " ".join(f"{a:.1f},{b:.1f}" for a, b in pts)
    body = (chip + f'<polyline points="{line}" fill="none" stroke="{RED}" stroke-width="4" stroke-linejoin="round"/>'
            f'<path d="M{h * 1.54} {h * 0.7} L{h * 1.72} {h * 0.74} L{h * 1.66} {h * 0.54} Z" fill="{RED}"/>')
    return svg(w, h, body, "#eef2f7")


def pill(w, h):
    """A two-tone capsule and a pair of lungs."""
    cap = (f'<g transform="rotate(-28 {h * 0.6} {h * 0.5})">'
           f'<rect x="{h * 0.18}" y="{h * 0.36}" width="{h * 0.44}" height="{h * 0.3}" rx="{h * 0.15}" fill="#2563eb"/>'
           f'<rect x="{h * 0.48}" y="{h * 0.36}" width="{h * 0.5}" height="{h * 0.3}" rx="{h * 0.15}" fill="#f8fafc" '
           f'stroke="#cbd5e1"/>'
           f'<rect x="{h * 0.48}" y="{h * 0.36}" width="{h * 0.14}" height="{h * 0.3}" fill="#2563eb"/></g>')
    lungs = (f'<path d="M{h * 1.28} {h * 0.18} L{h * 1.28} {h * 0.42}" stroke="#9f1239" stroke-width="3"/>'
             f'<path d="M{h * 1.25} {h * 0.4} q{-h * 0.3} {-h * 0.04} {-h * 0.26} {h * 0.42} q{h * 0.14} {h * 0.04} {h * 0.26} -{h * 0.06} Z" '
             f'fill="#fb7185"/>'
             f'<path d="M{h * 1.31} {h * 0.4} q{h * 0.3} {-h * 0.04} {h * 0.26} {h * 0.42} q{-h * 0.14} {h * 0.04} {-h * 0.26} -{h * 0.06} Z" '
             f'fill="#fb7185"/>')
    return svg(w, h, cap + lungs, "#e6eefc")


def trophy(w, h):
    """Senegal's flag behind a gold cup."""
    flag = (f'<rect x="{h * 0.08}" y="{h * 0.14}" width="{h * 0.26}" height="{h * 0.62}" fill="#00853f"/>'
            f'<rect x="{h * 0.34}" y="{h * 0.14}" width="{h * 0.26}" height="{h * 0.62}" fill="#fdef42"/>'
            f'<rect x="{h * 0.6}" y="{h * 0.14}" width="{h * 0.26}" height="{h * 0.62}" fill="#e31b23"/>'
            f'<circle cx="{h * 0.47}" cy="{h * 0.45}" r="{h * 0.07}" fill="#00853f"/>')
    cup = (f'<path d="M{h * 1.0} {h * 0.12} L{h * 1.44} {h * 0.12} Q{h * 1.42} {h * 0.56} {h * 1.22} {h * 0.58} '
           f'Q{h * 1.02} {h * 0.56} {h * 1.0} {h * 0.12} Z" fill="#d4a017"/>'
           f'<path d="M{h * 1.0} {h * 0.18} q{-h * 0.14} 0 {-h * 0.1} {h * 0.14} q{h * 0.04} {h * 0.1} {h * 0.14} {h * 0.1}" '
           f'fill="none" stroke="#d4a017" stroke-width="3"/>'
           f'<path d="M{h * 1.44} {h * 0.18} q{h * 0.14} 0 {h * 0.1} {h * 0.14} q{-h * 0.04} {h * 0.1} {-h * 0.14} {h * 0.1}" '
           f'fill="none" stroke="#d4a017" stroke-width="3"/>'
           f'<rect x="{h * 1.18}" y="{h * 0.58}" width="{h * 0.08}" height="{h * 0.16}" fill="#b8860b"/>'
           f'<rect x="{h * 1.06}" y="{h * 0.74}" width="{h * 0.32}" height="{h * 0.14}" fill="#8b6b12"/>')
    return svg(w, h, flag + cup, "#eaf3e6")


def tower(w, h):
    """A glass tower struck high up by a small drone, smoke trailing."""
    t = (f'<rect y="{h * 0.9}" width="{w}" height="{h * 0.1}" fill="#c8b48a"/>'
         f'<path d="M{h * 0.4} {h * 0.9} L{h * 0.46} {h * 0.08} L{h * 0.7} {h * 0.08} L{h * 0.76} {h * 0.9} Z" fill="#3b82a6"/>'
         + "".join(f'<rect x="{h * 0.45}" y="{h * (0.14 + i * 0.1)}" width="{h * 0.26}" height="1.5" fill="#bfdbfe"/>'
                   for i in range(8))
         + f'<rect x="{h * 0.12}" y="{h * 0.55}" width="{h * 0.22}" height="{h * 0.35}" fill="#a8a29e"/>'
         f'<rect x="{h * 0.82}" y="{h * 0.62}" width="{h * 0.24}" height="{h * 0.28}" fill="#a8a29e"/>'
         f'<circle cx="{h * 0.7}" cy="{h * 0.26}" r="{h * 0.07}" fill="{ORANGE}"/>'
         + smoke(h * 0.8, h * 0.2, h * 0.09))
    drone = (f'<g transform="translate({h * 1.18},{h * 0.3})">'
             f'<path d="M0 0 L{h * 0.16} {-h * 0.05} L{h * 0.16} {h * 0.05} Z" fill="{INK}"/>'
             f'<rect x="{h * 0.06}" y="{-h * 0.12}" width="{h * 0.04}" height="{h * 0.24}" fill="{INK}"/></g>'
             f'<path d="M{h * 1.16} {h * 0.3} L{h * 0.8} {h * 0.27}" stroke="{INK}" stroke-dasharray="4 3" stroke-width="1.6"/>')
    return svg(w, h, t + drone, "#f3e9d6")


def jets(w, h):
    """An island in a dark sea, three jets passing close and a siren."""
    sea = f'<rect y="{h * 0.66}" width="{w}" height="{h * 0.34}" fill="{SEA}"/>'
    island = (f'<path d="M{h * 0.1} {h * 0.7} Q{h * 0.35} {h * 0.3} {h * 0.7} {h * 0.7} Z" fill="#4d7c0f"/>'
              f'<path d="M{h * 0.25} {h * 0.6} l{h * 0.06} {-h * 0.06} l{h * 0.06} {h * 0.06} Z" fill="#fef3c7"/>')
    jet = ""
    for i, (x, y) in enumerate(((h * 0.9, h * 0.18), (h * 1.25, h * 0.32), (h * 0.95, h * 0.44))):
        jet += (f'<g transform="translate({x},{y})">'
                f'<path d="M0 0 L{h * 0.3} {-h * 0.035} L{h * 0.3} {h * 0.035} Z" fill="#374151"/>'
                f'<path d="M{h * 0.1} 0 L{h * 0.2} {-h * 0.13} L{h * 0.24} {-h * 0.13} L{h * 0.19} 0 Z" fill="#374151"/>'
                f'<path d="M{h * 0.1} 0 L{h * 0.2} {h * 0.13} L{h * 0.24} {h * 0.13} L{h * 0.19} 0 Z" fill="#374151"/></g>')
    siren = (f'<path d="M{h * 0.22} {h * 0.18} a{h * 0.1} {h * 0.1} 0 0 1 {h * 0.2} 0 l0 {h * 0.08} l{-h * 0.2} 0 Z" fill="{RED}"/>'
             f'<path d="M{h * 0.12} {h * 0.12} l{-h * 0.06} {-h * 0.04} M{h * 0.52} {h * 0.12} l{h * 0.06} {-h * 0.04}" '
             f'stroke="{RED}" stroke-width="2.5"/>')
    return svg(w, h, sea + island + jet + siren, "#c7d7ea")


def gaza(w, h):
    """Flattened blocks, dust, and a drone overhead."""
    body = (f'<rect y="{h * 0.84}" width="{w}" height="{h * 0.16}" fill="#a8a29e"/>'
            f'<path d="M{h * 0.08} {h * 0.84} L{h * 0.1} {h * 0.46} L{h * 0.3} {h * 0.56} L{h * 0.36} {h * 0.84} Z" fill="#78716c"/>'
            f'<path d="M{h * 0.42} {h * 0.84} L{h * 0.48} {h * 0.34} L{h * 0.62} {h * 0.3} L{h * 0.7} {h * 0.62} L{h * 0.8} {h * 0.84} Z" '
            f'fill="#d6d3d1"/>'
            f'<path d="M{h * 0.86} {h * 0.84} q{h * 0.2} {-h * 0.22} {h * 0.44} 0 Z" fill="#57534e"/>'
            + "".join(f'<rect x="{h * (0.5 + (i % 2) * 0.08)}" y="{h * (0.42 + (i // 2) * 0.12)}" width="{h * 0.05}" '
                      f'height="{h * 0.06}" fill="#44403c"/>' for i in range(4))
            + smoke(h * 1.05, h * 0.56, h * 0.12)
            + f'<g transform="translate({h * 0.95},{h * 0.12})"><rect x="0" y="{h * 0.04}" width="{h * 0.3}" height="{h * 0.06}" fill="{INK}"/>'
              f'<rect x="{-h * 0.05}" y="0" width="{h * 0.14}" height="{h * 0.03}" fill="{INK}"/>'
              f'<rect x="{h * 0.21}" y="0" width="{h * 0.14}" height="{h * 0.03}" fill="{INK}"/></g>')
    return svg(w, h, body, "#eadfce")


def thermo(w, h):
    """A blazing sun and a thermometer in the red."""
    rays = "".join(
        f'<rect x="{h * 0.43}" y="{h * 0.02}" width="{h * 0.04}" height="{h * 0.14}" fill="{ORANGE}" '
        f'transform="rotate({k * 45} {h * 0.45} {h * 0.42})"/>' for k in range(8))
    body = (rays + f'<circle cx="{h * 0.45}" cy="{h * 0.42}" r="{h * 0.2}" fill="#f59e0b"/>'
            f'<rect x="{h * 1.0}" y="{h * 0.08}" width="{h * 0.16}" height="{h * 0.62}" rx="{h * 0.08}" fill="#fff" stroke="{INK}" stroke-width="2"/>'
            f'<rect x="{h * 1.05}" y="{h * 0.22}" width="{h * 0.06}" height="{h * 0.52}" fill="{RED}"/>'
            f'<circle cx="{h * 1.08}" cy="{h * 0.78}" r="{h * 0.14}" fill="{RED}" stroke="{INK}" stroke-width="2"/>')
    return svg(w, h, body, "#fde7cf")


def bus(w, h):
    """A coach run into the back of a lorry on a desert highway."""
    road = (f'<rect y="{h * 0.78}" width="{w}" height="{h * 0.22}" fill="#52525b"/>'
            f'<rect y="{h * 0.88}" width="{w}" height="3" fill="#fde047"/>')
    truck = (f'<rect x="{h * 0.1}" y="{h * 0.3}" width="{h * 0.66}" height="{h * 0.42}" fill="#f97316"/>'
             f'<circle cx="{h * 0.24}" cy="{h * 0.76}" r="{h * 0.07}" fill="{INK}"/>'
             f'<circle cx="{h * 0.62}" cy="{h * 0.76}" r="{h * 0.07}" fill="{INK}"/>')
    coach = (f'<g transform="rotate(-6 {h * 1.1} {h * 0.6})">'
             f'<rect x="{h * 0.72}" y="{h * 0.36}" width="{h * 0.9}" height="{h * 0.38}" rx="5" fill="#e5e7eb" stroke="#475569"/>'
             + "".join(f'<rect x="{h * (0.82 + i * 0.18)}" y="{h * 0.42}" width="{h * 0.12}" height="{h * 0.12}" fill="#60a5fa"/>'
                       for i in range(4))
             + f'<circle cx="{h * 0.92}" cy="{h * 0.76}" r="{h * 0.07}" fill="{INK}"/>'
               f'<circle cx="{h * 1.42}" cy="{h * 0.76}" r="{h * 0.07}" fill="{INK}"/></g>'
               f'<path d="M{h * 0.7} {h * 0.3} l{h * 0.05} {-h * 0.12} l{h * 0.03} {h * 0.1} l{h * 0.06} {-h * 0.08}" '
               f'stroke="{RED}" stroke-width="3" fill="none"/>')
    return svg(w, h, road + truck + coach, "#f5e6c8")


def derrick(w, h):
    """An oil derrick and a storage tank on dry ground, a gas flare burning."""
    body = (f'<rect y="{h * 0.82}" width="{w}" height="{h * 0.18}" fill="#c8a978"/>'
            f'<path d="M{h * 0.2} {h * 0.82} L{h * 0.4} {h * 0.08} L{h * 0.6} {h * 0.82}" fill="none" stroke="{INK}" stroke-width="3"/>'
            f'<path d="M{h * 0.27} {h * 0.56} L{h * 0.53} {h * 0.56} M{h * 0.32} {h * 0.34} L{h * 0.48} {h * 0.34} '
            f'M{h * 0.27} {h * 0.56} L{h * 0.48} {h * 0.34} M{h * 0.53} {h * 0.56} L{h * 0.32} {h * 0.34}" '
            f'stroke="{INK}" stroke-width="1.6"/>'
            f'<rect x="{h * 0.72}" y="{h * 0.5}" width="{h * 0.42}" height="{h * 0.32}" rx="3" fill="#94a3b8"/>'
            f'<rect x="{h * 0.72}" y="{h * 0.58}" width="{h * 0.42}" height="{h * 0.05}" fill="#64748b"/>'
            f'<rect x="{h * 1.3}" y="{h * 0.3}" width="{h * 0.05}" height="{h * 0.52}" fill="#475569"/>'
            f'<path d="M{h * 1.325} {h * 0.3} q{-h * 0.1} {-h * 0.12} 0 {-h * 0.26} q{h * 0.1} {h * 0.14} 0 {h * 0.26} Z" fill="{ORANGE}"/>')
    return svg(w, h, body, "#f5e8cc")


def blast(w, h):
    """A ground-floor shopfront blown out under a block of flats, a burst of flame and debris."""
    body = (f'<rect y="{h * 0.88}" width="{w}" height="{h * 0.12}" fill="#57534e"/>'
            f'<rect x="{h * 0.12}" y="{h * 0.1}" width="{h * 0.9}" height="{h * 0.78}" fill="#d6d3d1"/>'
            + "".join(f'<rect x="{h * (0.2 + c * 0.22)}" y="{h * (0.16 + r * 0.16)}" width="{h * 0.12}" height="{h * 0.09}" '
                      f'fill="#64748b"/>' for r in range(3) for c in range(4))
            + f'<rect x="{h * 0.12}" y="{h * 0.64}" width="{h * 0.9}" height="{h * 0.24}" fill="#292524"/>'
            f'<path d="M{h * 0.57} {h * 0.5} l{h * 0.08} {h * 0.12} l{h * 0.14} -{h * 0.04} l-{h * 0.06} {h * 0.12} '
            f'l{h * 0.14} {h * 0.08} l-{h * 0.16} {h * 0.02} l{h * 0.02} {h * 0.12} l-{h * 0.12} -{h * 0.08} '
            f'l-{h * 0.12} {h * 0.08} l{h * 0.02} -{h * 0.12} l-{h * 0.16} -{h * 0.02} l{h * 0.14} -{h * 0.08} '
            f'l-{h * 0.06} -{h * 0.12} l{h * 0.14} {h * 0.04} Z" fill="{ORANGE}"/>'
            f'<circle cx="{h * 0.57}" cy="{h * 0.74}" r="{h * 0.07}" fill="{YELLOW}"/>'
            + "".join(f'<rect x="{h * x}" y="{h * y}" width="{h * 0.05}" height="{h * 0.04}" fill="#78716c" '
                      f'transform="rotate(30 {h * x} {h * y})"/>'
                      for x, y in ((1.1, 0.7), (1.2, 0.8), (1.05, 0.58), (0.0, 0.8))))
    return svg(w, h, body, "#efe6da")


DRAW = dict(probe=probe, verdict=verdict, apartment=apartment, chipdown=chipdown, pill=pill, trophy=trophy,
            tower=tower, jets=jets, gaza=gaza, thermo=thermo, bus=bus, derrick=derrick, blast=blast)
