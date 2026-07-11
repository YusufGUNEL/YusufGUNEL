import math

CX, CY, R = 210, 168, 108
AXES = [
    ("NLP", 0.95),
    ("Computer Vision", 0.90),
    ("Deep Learning", 0.85),
    ("Backend", 0.68),
    ("Embedded", 0.62),
    ("Mobile", 0.82),
]

def pt(i, frac):
    ang = math.radians(-90 + i * 60)
    return (CX + R * frac * math.cos(ang), CY + R * frac * math.sin(ang))

def poly(frac):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in (pt(i, frac) for i in range(6)))

rings = "\n  ".join(
    f'<polygon points="{poly(f)}" fill="none" stroke="#30363D" stroke-width="1"/>'
    for f in (0.33, 0.66, 1.0))

spokes = "\n  ".join(
    f'<line x1="{CX}" y1="{CY}" x2="{pt(i,1)[0]:.1f}" y2="{pt(i,1)[1]:.1f}" stroke="#30363D" stroke-width="1"/>'
    for i in range(6))

data_pts = [pt(i, v) for i, (_, v) in enumerate(AXES)]
data_poly = " ".join(f"{x:.1f},{y:.1f}" for x, y in data_pts)

dots = "\n  ".join(
    f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="#22D3EE">'
    f'<animate attributeName="opacity" values="0.4;1;0.4" dur="2.6s" begin="-{i*0.4}s" repeatCount="indefinite"/></circle>'
    for i, (x, y) in enumerate(data_pts))

label_pos = []
for i, (name, _) in enumerate(AXES):
    x, y = pt(i, 1.22)
    anchor = "middle"
    if x < CX - 12: anchor = "end"
    elif x > CX + 12: anchor = "start"
    label_pos.append(
        f'<text x="{x:.1f}" y="{y+4:.1f}" text-anchor="{anchor}" '
        f'font-family="Segoe UI, Ubuntu, Helvetica, Arial, sans-serif" font-size="13.5" font-weight="600" fill="#E6EDF3">{name}</text>')
labels = "\n  ".join(label_pos)

BARS = [
    ("Python", 0.95, "#22D3EE"),
    ("PyTorch / TensorFlow", 0.85, "#818CF8"),
    ("scikit-learn / OpenCV", 0.85, "#F472B6"),
    ("Flutter / Dart", 0.82, "#34D399"),
    ("C / C++ / Java", 0.70, "#FBBF24"),
    ("Django / Docker / Git", 0.66, "#60A5FA"),
]
bar_x, bar_w, bar_y0, bar_gap = 505, 330, 66, 42
bars = []
for i, (name, v, color) in enumerate(BARS):
    y = bar_y0 + i * bar_gap
    w = bar_w * v
    bars.append(
        f'<text x="{bar_x}" y="{y+4}" font-family="Segoe UI, Ubuntu, Helvetica, Arial, sans-serif" font-size="13.5" font-weight="600" fill="#E6EDF3">{name}</text>'
        f'<rect x="{bar_x}" y="{y+12}" width="{bar_w}" height="8" rx="4" fill="#21262D"/>'
        f'<rect x="{bar_x}" y="{y+12}" width="0" height="8" rx="4" fill="{color}">'
        f'<animate attributeName="width" from="0" to="{w:.0f}" dur="1.2s" begin="{0.3+i*0.15:.2f}s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/></rect>'
        f'<circle cx="{bar_x}" cy="{y+16}" r="0" fill="{color}">'
        f'<animate attributeName="cx" from="{bar_x}" to="{bar_x+w:.0f}" dur="1.2s" begin="{0.3+i*0.15:.2f}s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>'
        f'<animate attributeName="r" from="0" to="5" dur="0.3s" begin="{0.3+i*0.15:.2f}s" fill="freeze"/></circle>')
bars_svg = "\n  ".join(bars)

svg = f'''<svg width="920" height="330" viewBox="0 0 920 330" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="pg" cx="20%" cy="30%" r="80%">
      <stop offset="0%" stop-color="#22D3EE" stop-opacity="0.07"/>
      <stop offset="100%" stop-color="#22D3EE" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect x="1" y="1" width="918" height="328" rx="14" fill="#0D1117" stroke="#30363D" stroke-width="1.5"/>
  <rect x="1" y="1" width="918" height="328" rx="14" fill="url(#pg)"/>
  <line x1="460" y1="36" x2="460" y2="294" stroke="#21262D" stroke-width="1"/>

  <text x="60" y="40" font-family="Consolas, 'Courier New', monospace" font-size="13" font-weight="600" letter-spacing="2" fill="#22D3EE">DOMAINS</text>
  <text x="505" y="40" font-family="Consolas, 'Courier New', monospace" font-size="13" font-weight="600" letter-spacing="2" fill="#818CF8">TOOLBOX</text>

  {rings}
  {spokes}
  <polygon points="{data_poly}" fill="#22D3EE" fill-opacity="0.16" stroke="#22D3EE" stroke-width="2" stroke-linejoin="round">
    <animate attributeName="fill-opacity" values="0.10;0.22;0.10" dur="4s" repeatCount="indefinite"/>
  </polygon>
  {dots}
  {labels}

  {bars_svg}
</svg>
'''

with open("assets/expertise.svg", "w", encoding="utf-8") as f:
    f.write(svg)
print("wrote assets/expertise.svg")
