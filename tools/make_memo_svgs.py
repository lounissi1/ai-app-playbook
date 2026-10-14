"""Generate the memo infographics in docs/assets/memos/.

Run from the repository root:  python tools/make_memo_svgs.py
Edit the data at the top of each function, not the generated SVG files.
"""

from __future__ import annotations

import math
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path("docs/assets/memos")

FONT = "font-family=\"Inter, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif\""
INK, MUTED, LINE, PAPER, BAND = "#1f2937", "#5b6472", "#d9dee5", "#ffffff", "#f6f8fb"
TEAL, TEAL_BG = "#0f766e", "#d5f5ef"
AMBER, AMBER_BG = "#a15c07", "#fdf0d5"
INDIGO, INDIGO_BG = "#3f3cbb", "#e3e5fc"
ORANGE, ORANGE_BG = "#b4480e", "#fde4d3"
VIOLET, VIOLET_BG = "#6d32c9", "#eee5fd"
SLATE, SLATE_BG = "#334155", "#e6eaf0"


def svg(width: int, height: int, body: str, title: str, desc: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" role="img" aria-labelledby="t d" {FONT}>\n'
        f"<title id=\"t\">{escape(title)}</title>\n<desc id=\"d\">{escape(desc)}</desc>\n"
        "<defs>"
        f'<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        f'<path d="M0,0 L10,5 L0,10 z" fill="{MUTED}"/></marker>'
        "</defs>\n"
        f'<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="16" fill="{PAPER}" stroke="{LINE}"/>\n'
        f"{body}</svg>\n"
    )


def text(x, y, s, size=14, fill=INK, weight=400, anchor="start", spacing=0):
    ls = f' letter-spacing="{spacing}"' if spacing else ""
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{weight}" fill="{fill}" '
        f'text-anchor="{anchor}"{ls}>{escape(s)}</text>\n'
    )


def box(x, y, w, h, fill, stroke, rx=10):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>\n'


def arrow(x1, y1, x2, y2, both=False, dashed=False):
    start = ' marker-start="url(#arrow)"' if both else ""
    dash = ' stroke-dasharray="5 4"' if dashed else ""
    return (
        f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{MUTED}" '
        f'stroke-width="1.6" marker-end="url(#arrow)"{start}{dash}/>\n'
    )


def header(x, y, label, color, note):
    return text(x, y, label, 14, color, 700, spacing=1.2) + text(x + 10 * len(label) + 20, y, note, 15, MUTED)


def swatch(x, y, fill, stroke, label):
    return box(x, y - 12, 15, 15, fill, stroke, rx=3) + text(x + 21, y, label, 13.5, MUTED)


# --------------------------------------------------------------------------- overview
def overview() -> str:
    W, H = 1000, 520
    b = ""
    left, right = 32, 968
    span = right - left

    # 1 · Architecture
    b += header(left, 40, "ARCHITECTURE", TEAL, "what the app is made of")
    b += swatch(744, 40, TEAL_BG, TEAL, "stateless") + swatch(842, 40, AMBER_BG, AMBER, "holds data")
    parts = [("Frontend", 0), ("API", 0), ("Queue + workers", 0), ("Cache", 0),
             ("Database", 1), ("Object storage", 1), ("AI services", 0)]
    gap = 10
    w = (span - gap * (len(parts) - 1)) / len(parts)
    for i, (name, state) in enumerate(parts):
        x = left + i * (w + gap)
        fill, stroke = (AMBER_BG, AMBER) if state else (TEAL_BG, TEAL)
        b += box(x, 56, w, 46, fill, stroke)
        b += text(x + w / 2, 85, name, 14 if len(name) > 12 else 15, INK, 600, "middle")

    # 2 · Delivery loop
    b += header(left, 146, "DELIVERY LOOP", INDIGO, "how every change reaches users")
    b += swatch(744, 146, INDIGO_BG, INDIGO, "build it") + swatch(842, 146, ORANGE_BG, ORANGE, "run it")
    stages = ["Plan", "Code", "Build", "Test", "Release", "Deploy", "Operate", "Monitor"]
    gap = 18
    w = (span - gap * 7) / 8
    for i, s in enumerate(stages):
        x = left + i * (w + gap)
        fill, stroke = (INDIGO_BG, INDIGO) if i < 4 else (ORANGE_BG, ORANGE)
        b += box(x, 162, w, 46, fill, stroke, rx=23)
        b += text(x + w / 2, 191, f"{i + 1}  {s}", 15, INK, 600, "middle")
        if i < 7:
            b += arrow(x + w + 2, 185, x + w + gap - 2, 185)
    # return path
    y = 232
    b += (f'<path d="M{right - w / 2:.1f},208 V{y} H{left + w / 2:.1f} V212" fill="none" '
          f'stroke="{MUTED}" stroke-width="1.6" stroke-dasharray="5 4" marker-end="url(#arrow)"/>\n')
    b += f'<rect x="{500 - 150}" y="{y - 11}" width="300" height="22" fill="{PAPER}"/>\n'
    b += text(500, y + 5, "what you learn becomes the next plan", 14, MUTED, 400, "middle")

    # 3 · AI
    b += header(left, 280, "AI", VIOLET, "two different jobs")
    cw = (span - 24) / 2
    flows = [
        ("Inside the app", ["Question", "Retrieve", "Generate", "Cited answer"],
         "Retrieve = embeddings + vector search · checked by evaluation"),
        ("Building the app", ["Spec", "Plan ✓", "Code", "Review ✓"],
         "An AI agent types · a human approves the ✓ steps"),
    ]
    for j, (title, steps, foot) in enumerate(flows):
        x0 = left + j * (cw + 24)
        b += box(x0, 294, cw, 118, VIOLET_BG, VIOLET, rx=12)
        b += text(x0 + 16, 318, title, 15, VIOLET, 700)
        sg = 14
        sw = (cw - 32 - sg * 3) / 4
        for k, s in enumerate(steps):
            sx = x0 + 16 + k * (sw + sg)
            b += box(sx, 332, sw, 38, PAPER, VIOLET, rx=8)
            b += text(sx + sw / 2, 356, s, 13.5 if len(s) > 10 else 14.5, INK, 600, "middle")
            if k < 3:
                b += arrow(sx + sw + 1, 351, sx + sw + sg - 1, 351)
        b += text(x0 + 16, 397, foot, 13.5, MUTED)

    # 4 · Foundation
    b += header(left, 452, "FOUNDATION", SLATE, "under every stage")
    tiles = ["Infrastructure as code", "Identity & secrets", "Managed data & backups", "Cost guardrails"]
    gap = 12
    w = (span - gap * 3) / 4
    for i, s in enumerate(tiles):
        x = left + i * (w + gap)
        b += box(x, 466, w, 38, SLATE_BG, SLATE, rx=8)
        b += text(x + w / 2, 491, s, 15, INK, 600, "middle")

    return svg(W, H, b, "The AI App Playbook in one picture",
               "Four layers: the architecture of the app, the eight-stage delivery loop, the two "
               "jobs of AI (inside the app and building the app), and the foundation under every stage.")


# --------------------------------------------------------------------------- architecture
def architecture() -> str:
    W, H = 1000, 600
    b = ""

    def node(x, y, w, h, title, sub, fill=TEAL_BG, stroke=TEAL):
        out = box(x, y, w, h, fill, stroke, rx=12)
        out += text(x + w / 2, y + h / 2 - 3, title, 17, INK, 700, "middle")
        out += text(x + w / 2, y + h / 2 + 18, sub, 14.5, MUTED, 400, "middle")
        return out

    # users
    b += box(420, 24, 160, 36, BAND, LINE, rx=18) + text(500, 47, "Users", 14, INK, 600, "middle")
    b += arrow(500, 60, 500, 92)
    b += node(380, 94, 240, 66, "Web frontend", "pages and screens")
    b += arrow(500, 160, 500, 208)
    b += text(510, 189, "HTTPS + JSON", 12.5, MUTED)
    b += node(380, 210, 240, 74, "API", "fast answers, under a second")
    b += node(70, 214, 220, 66, "Cache", "hot results in memory")
    b += arrow(292, 247, 378, 247, both=True)
    b += node(710, 214, 220, 66, "AI services", "LLM · embeddings", VIOLET_BG, VIOLET)
    b += arrow(622, 247, 708, 247)
    # slow path
    b += node(440, 322, 160, 56, "Queue", "slow work waits")
    b += arrow(520, 284, 520, 320)
    b += node(710, 316, 220, 66, "Workers", "slow and heavy jobs")
    b += arrow(602, 350, 708, 350)
    b += arrow(820, 316, 820, 282)
    # state band
    b += box(60, 430, 880, 136, AMBER_BG, AMBER, rx=14)
    b += text(80, 454, "STATE LIVES ONLY HERE", 12.5, AMBER, 700, spacing=1.2)
    b += node(200, 470, 260, 74, "Database", "records · vectors · maps", PAPER, AMBER)
    b += node(540, 470, 260, 74, "Object storage", "files · images · models", PAPER, AMBER)
    b += arrow(410, 284, 410, 468)
    b += text(400, 410, "read / write", 12.5, MUTED, 400, "end")
    b += arrow(780, 382, 780, 468)
    b += arrow(740, 382, 440, 468)
    # legend
    b += swatch(70, 410 - 290, TEAL_BG, TEAL, "stateless: safe to restart or copy")
    b += swatch(70, 142, AMBER_BG, AMBER, "holds data: back it up")
    b += swatch(70, 164, VIOLET_BG, VIOLET, "AI: managed API or own service")
    return svg(W, H, b, "Reference app architecture",
               "Users reach a web frontend, which calls the API. The API reads a cache, calls AI "
               "services, and sends slow work to a queue for workers. Only the database and object "
               "storage hold data; everything else is stateless.")


# --------------------------------------------------------------------------- delivery loop
def delivery_loop() -> str:
    W, H = 1000, 640
    cx, cy, R, r = 500, 330, 205, 40
    stages = [
        ("Plan", "Small issues with", "a clear finish line"),
        ("Code", "Branch, pull request,", "human review"),
        ("Build", "CI makes one image", "per commit"),
        ("Test", "Tests, lint and scans", "on every change"),
        ("Release", "The tested image", "becomes a version"),
        ("Deploy", "Migrate, switch traffic,", "roll back if needed"),
        ("Operate", "Scale, schedule, back up,", "control cost"),
        ("Monitor", "Logs, metrics, alerts", "feed the next plan"),
    ]
    b = ""
    # ring arcs with arrows
    for i in range(8):
        a1 = math.radians(-90 + i * 45)
        a2 = math.radians(-90 + (i + 1) * 45)
        pad = math.asin((r + 6) / R)
        s, e = a1 + pad, a2 - pad
        x1, y1 = cx + R * math.cos(s), cy + R * math.sin(s)
        x2, y2 = cx + R * math.cos(e), cy + R * math.sin(e)
        b += (f'<path d="M{x1:.1f},{y1:.1f} A{R},{R} 0 0 1 {x2:.1f},{y2:.1f}" fill="none" '
              f'stroke="{MUTED}" stroke-width="1.8" marker-end="url(#arrow)"/>\n')
    # nodes and labels
    for i, (name, l1, l2) in enumerate(stages):
        a = math.radians(-90 + i * 45)
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        fill, stroke = (INDIGO_BG, INDIGO) if i < 4 else (ORANGE_BG, ORANGE)
        b += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>\n'
        b += text(x, y - 6, str(i + 1), 13, stroke, 700, "middle")
        b += text(x, y + 14, name, 15.5, INK, 700, "middle")
        lx, ly = cx + (R + r + 22) * math.cos(a), cy + (R + r + 22) * math.sin(a)
        c = math.cos(a)
        anchor = "start" if c > 0.3 else "end" if c < -0.3 else "middle"
        if anchor == "middle":
            ly = ly - 22 if math.sin(a) < 0 else ly + 8
        b += text(lx, ly, l1, 15, MUTED, 400, anchor)
        b += text(lx, ly + 19, l2, 15, MUTED, 400, anchor)
    # centre
    b += text(cx, cy - 18, "Every change,", 20, INK, 700, "middle")
    b += text(cx, cy + 8, "the same way", 20, INK, 700, "middle")
    b += text(cx, cy + 36, "small · reviewed · automated · reversible", 14, MUTED, 400, "middle")
    # corner labels
    b += swatch(36, 40, INDIGO_BG, INDIGO, "1–4  DEV: build it right")
    b += swatch(36, 64, ORANGE_BG, ORANGE, "5–8  OPS: run it well")
    return svg(W, H, b, "The delivery loop",
               "Eight stages in a circle: plan, code, build, test (building it right), then release, "
               "deploy, operate, monitor (running it well). Monitoring feeds the next plan.")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for name, fn in [("playbook", overview), ("architecture", architecture), ("delivery-loop", delivery_loop)]:
        (OUT / f"{name}.svg").write_text(fn(), encoding="utf-8")
        print("wrote", OUT / f"{name}.svg")
