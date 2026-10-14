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



ROSE, ROSE_BG = "#b42318", "#fde8e6"


def lines(x, y, rows, size=14, fill=INK, weight=400, anchor="start", lh=None):
    lh = lh or size * 1.35
    return "".join(text(x, y + i * lh, r, size, fill, weight if i == 0 else 400, anchor) for i, r in enumerate(rows))


# --------------------------------------------------------------------------- hosting
def hosting() -> str:
    W, H = 1000, 640
    b = ""
    qs = [
        (["Is it one classic web app,", "not packaged in containers?"], "PaaS web app", "ops effort: low"),
        (["Is it mostly small functions", "triggered by events?"], "Serverless functions", "ops effort: lowest"),
        (["Do you need Kubernetes itself: operators,", "GPU node pools, a platform team?"], "Managed Kubernetes", "ops effort: high"),
        (["Does it need a full operating system", "that you manage yourself?"], "Virtual machines", "ops effort: very high"),
    ]
    y0, step, qh = 32, 118, 76
    for i, (q, opt, eff) in enumerate(qs):
        y = y0 + i * step
        b += box(40, y, 520, qh, BAND, SLATE, rx=12)
        b += text(60, y + 32, f"{i + 1}", 18, SLATE, 700)
        b += lines(88, y + 32, q, 16, INK, 600, lh=22)
        b += arrow(562, y + qh / 2, 646, y + qh / 2)
        b += text(604, y + qh / 2 - 8, "Yes", 13.5, MUTED, 600, "middle")
        b += box(648, y + 4, 312, qh - 8, PAPER, SLATE, rx=12)
        b += text(804, y + 34, opt, 17, INK, 700, "middle")
        b += text(804, y + 56, eff, 13.5, MUTED, 400, "middle")
        ny = y + step if i < 3 else 504
        b += arrow(300, y + qh, 300, ny - 2)
        b += text(312, y + qh + 26, "No", 13.5, MUTED, 600)
    b += f'<rect x="40" y="504" width="920" height="108" rx="14" fill="{TEAL_BG}" stroke="{TEAL}" stroke-width="2.5"/>\n'
    b += text(500, 540, "★  Managed container platform  (the default)", 19, TEAL, 700, "middle")
    b += text(500, 566, "Runs your containers, scales to zero, low ops effort", 15, INK, 400, "middle")
    b += text(500, 592, "Azure Container Apps · AWS ECS on Fargate · Google Cloud Run", 14, MUTED, 400, "middle")
    return svg(W, H, b, "Where does my code run?",
               "Four yes-or-no questions lead to PaaS web app, serverless functions, managed Kubernetes "
               "or virtual machines. If every answer is no, use the default: a managed container platform.")


# --------------------------------------------------------------------------- AI inside the app
def ai_in_app() -> str:
    W, H = 1000, 590
    b = ""
    left, gap, w, h = 32, 24, 168, 64
    xs = [left + i * (w + gap) for i in range(5)]

    def n(col, y, title, sub, fill=VIOLET_BG, stroke=VIOLET):
        x = xs[col]
        return box(x, y, w, h, fill, stroke, rx=10) + text(x + w / 2, y + 28, title, 15, INK, 700, "middle") + \
            text(x + w / 2, y + 48, sub, 13, MUTED, 400, "middle")

    ya, yb, yc = 64, 214, 346
    b += text(left, ya - 14, "INDEX", 13.5, VIOLET, 700, spacing=1.2) + text(left + 62, ya - 14, "once per document, in a worker", 14, MUTED)
    b += n(0, ya, "Documents", "PDFs, pages, notes", PAPER, VIOLET)
    b += n(1, ya, "Chunks", "a few hundred words")
    b += n(2, ya, "Embedding model", "text → vector")
    b += n(3, ya, "Vector database", "chunks + vectors", AMBER_BG, AMBER)
    for c in range(3):
        b += arrow(xs[c] + w + 1, ya + h / 2, xs[c + 1] - 1, ya + h / 2)

    b += text(left, yb - 14, "ANSWER", 13.5, VIOLET, 700, spacing=1.2) + text(left + 76, yb - 14, "every question, in the API", 14, MUTED)
    b += n(0, yb, "Question", "from the user", PAPER, VIOLET)
    b += n(2, yb, "Embedding model", "the same one")
    b += n(3, yb, "Search", "filtered by user")
    b += n(4, yb, "Language model", "answer from passages")
    b += arrow(xs[0] + w + 1, yb + h / 2, xs[2] - 1, yb + h / 2)
    b += arrow(xs[2] + w + 1, yb + h / 2, xs[3] - 1, yb + h / 2)
    b += arrow(xs[3] + w + 1, yb + h / 2, xs[4] - 1, yb + h / 2)
    # same model link and search to vector db
    b += (f'<line x1="{xs[2] + w / 2}" y1="{ya + h}" x2="{xs[2] + w / 2}" y2="{yb}" stroke="{VIOLET}" '
          f'stroke-width="1.8" stroke-dasharray="5 4"/>\n')
    b += text(xs[2] + w / 2 - 8, (ya + h + yb) / 2 + 5, "same model, same version", 13, VIOLET, 600, "end")
    b += arrow(xs[3] + w / 2, yb - 1, xs[3] + w / 2, ya + h + 1, both=True)
    b += text(xs[3] + w / 2 + 8, (ya + h + yb) / 2 + 5, "nearest passages", 13, MUTED)
    # outcomes
    b += n(4, yc, "Cited answer", "with links to sources", TEAL_BG, TEAL)
    b += arrow(xs[4] + w / 2, yb + h + 1, xs[4] + w / 2, yc - 1)
    b += n(3, yc, "“I don't know”", "when nothing matches", ROSE_BG, ROSE)
    b += arrow(xs[3] + w / 2, yb + h + 1, xs[3] + w / 2, yc - 1)
    b += text(xs[3] + w / 2 - 8, yb + h + 30, "no good match", 13, MUTED, 400, "end")
    # bottom cards
    cw = (936 - 24) / 2
    for j, (title, rows) in enumerate([
        ("Evaluation", ["Fixed test questions run in CI:", "right passage found? answer faithful? cost?"]),
        ("Model serving", ["Managed model API or your own container:", "pinned versions, timeouts, token limits"]),
    ]):
        x = left + j * (cw + 24)
        b += box(x, 450, cw, 108, BAND, SLATE, rx=12)
        b += text(x + 20, 480, title, 16, SLATE, 700)
        b += lines(x + 20, 506, rows, 14.5, MUTED, 400, lh=21)
    return svg(W, H, b, "AI inside the app",
               "Retrieval-augmented generation. Once per document a worker splits text into chunks, embeds "
               "them and stores the vectors. For each question the API embeds it with the same model, "
               "searches with a user filter, and the language model answers from the passages with "
               "citations, or says it doesn't know. Evaluation and model serving sit underneath.")


# --------------------------------------------------------------------------- AI agents
def ai_agents() -> str:
    W, H = 1000, 520
    b = ""
    lx, x0, right = 32, 168, 968
    lanes = [("HUMAN", "decides", 70, INDIGO), ("AI AGENT", "types", 200, VIOLET)]
    for name, verb, y, col in lanes:
        b += box(lx, y - 14, right - lx, 112, BAND, LINE, rx=12)
        b += text(lx + 18, y + 34, name, 14, col, 700, spacing=1.2)
        b += text(lx + 18, y + 56, verb, 14, MUTED)
    steps = [
        (0, ["Issue + spec", "goal · limits · done"]),
        (1, ["Plan", "after reading rules"]),
        (0, ["✓ Approve", "the plan"]),
        (1, ["Code + tests", "on a branch"]),
        (1, ["CI checks", "tests · lint · eval"]),
        (0, ["✓ Review", "and merge"]),
    ]
    gap = 16
    w = (right - 16 - x0 - gap * 5) / 6
    pts = []
    for i, (lane, rows) in enumerate(steps):
        x = x0 + i * (w + gap)
        y = lanes[lane][2]
        ci = i == 4
        fill, stroke = (TEAL_BG, TEAL) if ci else (INDIGO_BG, INDIGO) if lane == 0 else (VIOLET_BG, VIOLET)
        b += box(x, y, w, 84, fill, stroke, rx=10)
        b += text(x + w / 2, y + 36, rows[0], 15, INK, 700, "middle")
        b += text(x + w / 2, y + 58, rows[1], 12.5, MUTED, 400, "middle")
        pts.append((x, y, w))
    for (x1, y1, w1), (x2, y2, _) in zip(pts, pts[1:]):
        if y1 == y2:
            b += arrow(x1 + w1 + 1, y1 + 42, x2 - 1, y2 + 42)
        else:
            b += arrow(x1 + w1 + 1, y1 + (64 if y2 > y1 else 20), x2 - 1, y2 + (20 if y2 > y1 else 64))
    b += box(lx, 330, right - lx, 64, VIOLET_BG, VIOLET, rx=12)
    b += text(lx + 18, 357, "Every task starts from an instruction file", 15, VIOLET, 700)
    b += text(lx + 18, 380, "CLAUDE.md or AGENTS.md: project rules, how to run and test, hard limits", 14, INK)
    b += box(lx, 410, right - lx, 82, ROSE_BG, ROSE, rx=12)
    b += text(lx + 18, 438, "Always a human", 15, ROSE, 700)
    b += text(lx + 18, 462, "production deploys · infrastructure apply and destroy · deleting data · changing access ·", 14, INK)
    b += text(lx + 18, 481, "anything that bills", 14, INK)
    return svg(W, H, b, "Building with AI agents",
               "Two lanes. The human writes the issue and spec, approves the agent's plan, and reviews and "
               "merges. The agent proposes the plan, codes with tests on a branch, and CI checks it. An "
               "instruction file sets the rules; irreversible actions always stay with a human.")


# --------------------------------------------------------------------------- going live
def going_live() -> str:
    W, H = 1000, 560
    b = ""
    groups = [
        ("DELIVERY", INDIGO, INDIGO_BG, ["Reviewed PRs + CI", "One image per version", "Migrations first", "Rollback in minutes"],
         ["on every change", "built by CI", "run before each deploy", "tested at least once"]),
        ("RUNTIME AND DATA", TEAL, TEAL_BG, ["HTTPS everywhere", "No data on disk", "Managed database", "A restore tested"],
         ["with health checks", "files in object storage", "automatic backups", "at least once"]),
        ("SECURITY AND OPERATIONS", SLATE, SLATE_BG, ["No secrets in code", "Infrastructure in code", "An alert to a person", "Budget alert + tags"],
         ["identities, not passwords", "rebuilt from scratch once", "logs, metrics, traces", "on every resource"]),
    ]
    left, gap = 32, 16
    w = (936 - gap * 3) / 4
    y = 40
    for name, col, bg, titles, subs in groups:
        b += text(left, y, name, 13.5, col, 700, spacing=1.2)
        for i, (t1, t2) in enumerate(zip(titles, subs)):
            x = left + i * (w + gap)
            b += box(x, y + 12, w, 82, bg, col, rx=12)
            b += f'<circle cx="{x + 26}" cy="{y + 53}" r="12" fill="{col}"/>\n'
            b += (f'<path d="M{x + 20},{y + 53} l4,4 l8,-9" fill="none" stroke="#fff" stroke-width="2.4" '
                  f'stroke-linecap="round" stroke-linejoin="round"/>\n')
            b += text(x + 48, y + 49, t1, 14.5, INK, 700)
            b += text(x + 48, y + 70, t2, 13.5, MUTED)
        y += 126
    b += box(left, y - 8, 936, 96, VIOLET_BG, VIOLET, rx=12)
    b += text(left + 20, y + 22, "IF THE APP USES AI", 13.5, VIOLET, 700, spacing=1.2)
    b += text(left + 20, y + 48, "Pinned model versions · timeouts and token limits · same embedding model everywhere ·", 14.5, INK)
    b += text(left + 20, y + 70, "retrieval filtered by user · evaluation set in CI that blocks regressions", 14.5, INK)
    return svg(W, H, b, "Going live: the minimum",
               "Twelve must-haves in three groups: delivery, runtime and data, security and operations, "
               "plus five extra checks when the app uses AI.")


# --------------------------------------------------------------------------- cost
def cost() -> str:
    W, H = 1000, 560
    b = ""
    cols = [
        ("Bills while it runs", ORANGE, ORANGE_BG, ["Servers and databases left on", "A minimum of 1 replica", "Container registries", "Log storage"]),
        ("Bills when it is used", TEAL, TEAL_BG, ["Apps that scale to zero", "Model calls (tokens)", "Storage you actually fill", ""]),
        ("Easy to miss", ROSE, ROSE_BG, ["Free credit that ends quietly", "Paid add-ons in setup wizards", "Untagged leftovers", ""]),
    ]
    left, gap = 32, 18
    w = (936 - gap * 2) / 3
    for i, (title, col, bg, items) in enumerate(cols):
        x = left + i * (w + gap)
        b += box(x, 32, w, 196, bg, col, rx=14)
        b += text(x + 20, 64, title, 17, col, 700)
        for k, it in enumerate([i for i in items if i]):
            b += f'<circle cx="{x + 26}" cy="{96 + k * 32}" r="4" fill="{col}"/>\n'
            b += text(x + 40, 101 + k * 32, it, 15, INK)
    b += text(left, 276, "SIX BRAKES, IN ORDER", 13.5, SLATE, 700, spacing=1.2)
    brakes = [("Budget first", "alerts at 50·80·100%"), ("Estimate", "before creating"), ("Scale to zero", "where idle is fine"),
              ("Tag everything", "review monthly"), ("Cap logs", "daily limit"), ("Tear down", "when finished")]
    gap = 14
    w = (936 - gap * 5) / 6
    for i, (t1, t2) in enumerate(brakes):
        x = left + i * (w + gap)
        b += box(x, 292, w, 104, SLATE_BG, SLATE, rx=12)
        b += f'<circle cx="{x + w / 2}" cy="{322}" r="15" fill="{SLATE}"/>\n'
        b += text(x + w / 2, 327, str(i + 1), 14, "#ffffff", 700, "middle")
        b += text(x + w / 2, 362, t1, 15, INK, 700, "middle")
        b += text(x + w / 2, 382, t2, 13, MUTED, 400, "middle")
        if i < 5:
            b += arrow(x + w + 1, 344, x + w + gap - 1, 344)
    b += box(left, 426, 936, 104, AMBER_BG, AMBER, rx=14)
    b += text(500, 466, "A budget alerts. It does not stop spending.", 20, AMBER, 700, "middle")
    b += text(500, 496, "Stopping takes an action you set up yourself, or a teardown.", 15, INK, 400, "middle")
    return svg(W, H, b, "Cost guardrails",
               "What bills while it runs, what bills when used, and what is easy to miss; then six brakes in "
               "order: budget first, estimate, scale to zero, tag everything, cap logs, tear down. A budget "
               "alerts but does not stop spending.")



# --------------------------------------------------------------------------- banner and social preview
def banner(W: int = 1200, H: int = 340) -> str:
    """Title banner for the README; at 1280x640 it doubles as the GitHub social preview.

    Content is drawn on a 1200x340 canvas and scaled to fit, centred, on a full-size background.
    """
    s = min(W / 1200, H / 340)
    ox, oy = (W - 1200 * s) / 2, (H - 340 * s) / 2
    bg = (
        '<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#2f2a8f"/><stop offset="0.55" stop-color="#4b3cc4"/>'
        '<stop offset="1" stop-color="#7b3fd1"/></linearGradient></defs>\n'
        f'<rect x="0" y="0" width="{W}" height="{H}" rx="22" fill="url(#g)"/>\n'
        f'<circle cx="{W - 120}" cy="-40" r="{H * 0.55:.0f}" fill="#ffffff" opacity="0.05"/>\n'
        f'<circle cx="80" cy="{H + 60}" r="{H * 0.6:.0f}" fill="#ffffff" opacity="0.05"/>\n'
    )
    b = ""
    x = 60
    b += text(x, 78, "OPEN PLAYBOOK · FREE TO REUSE", 15, "#cfc9ff", 700, spacing=2)
    b += text(x, 150, "AI App Playbook", 66, "#ffffff", 800)
    b += text(x, 196, "Architect, build, deploy and run AI-powered apps,", 23, "#ece9ff")
    b += text(x, 228, "one clear step at a time.", 23, "#ece9ff")
    cx = x
    for c in ["Architecture", "Delivery loop", "AI in the app", "AI agents", "Any cloud · Azure examples"]:
        w = len(c) * 8.6 + 34
        b += (f'<rect x="{cx:.1f}" y="262" width="{w:.1f}" height="36" rx="18" fill="#ffffff" '
              f'fill-opacity="0.14" stroke="#ffffff" stroke-opacity="0.35"/>\n')
        b += text(cx + w / 2, 286, c, 15, "#ffffff", 600, "middle")
        cx += w + 10
    rcx, rcy, rr = 1010, 170, 112
    b += (f'<circle cx="{rcx}" cy="{rcy}" r="{rr}" fill="none" stroke="#ffffff" stroke-opacity="0.45" '
          'stroke-width="2.5" stroke-dasharray="6 6"/>\n')
    for i in range(8):
        a = math.radians(-90 + i * 45)
        nx, ny = rcx + rr * math.cos(a), rcy + rr * math.sin(a)
        fill = "#c9cdfd" if i < 4 else "#ffd2b8"
        b += f'<circle cx="{nx:.1f}" cy="{ny:.1f}" r="20" fill="{fill}" stroke="#ffffff" stroke-width="2"/>\n'
        b += text(nx, ny + 6, str(i + 1), 16, "#2f2a8f", 800, "middle")
    b += text(rcx, rcy - 4, "plan → monitor", 15, "#ffffff", 700, "middle")
    b += text(rcx, rcy + 18, "every change,", 13.5, "#e3e0ff", 400, "middle")
    b += text(rcx, rcy + 36, "the same way", 13.5, "#e3e0ff", 400, "middle")
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
        f'role="img" aria-labelledby="t" {FONT}>\n<title id="t">AI App Playbook: architect, build, deploy '
        f'and run AI-powered apps, one clear step at a time</title>\n{bg}'
        f'<g transform="translate({ox:.1f},{oy:.1f}) scale({s:.4f})">\n{b}</g>\n</svg>\n'
    )


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for name, fn in [("playbook", overview), ("architecture", architecture), ("delivery-loop", delivery_loop),
                     ("hosting", hosting), ("ai-in-app", ai_in_app), ("ai-agents", ai_agents),
                     ("going-live", going_live), ("cost", cost)]:
        (OUT / f"{name}.svg").write_text(fn(), encoding="utf-8")
        print("wrote", OUT / f"{name}.svg")
    (OUT.parent / "banner.svg").write_text(banner(), encoding="utf-8")
    (OUT.parent / "social-preview.svg").write_text(banner(1280, 640), encoding="utf-8")
    print("wrote banner.svg and social-preview.svg (convert the latter to PNG for GitHub)")
