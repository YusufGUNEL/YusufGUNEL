import html

TPL = '''<svg width="440" height="200" viewBox="0 0 440 200" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bd" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{accent}"/>
      <stop offset="0.5" stop-color="#30363D"/>
      <stop offset="1" stop-color="{accent}"/>
      <animateTransform attributeName="gradientTransform" type="rotate" from="0 0.5 0.5" to="360 0.5 0.5" dur="7s" repeatCount="indefinite"/>
    </linearGradient>
    <radialGradient id="gl" cx="100%" cy="0%" r="80%">
      <stop offset="0%" stop-color="{accent}" stop-opacity="0.10"/>
      <stop offset="100%" stop-color="{accent}" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect x="1" y="1" width="438" height="198" rx="14" fill="#0D1117"/>
  <rect x="1" y="1" width="438" height="198" rx="14" fill="url(#gl)"/>
  <rect x="1" y="1" width="438" height="198" rx="14" stroke="url(#bd)" stroke-width="1.6"/>

  <rect x="26" y="30" width="4" height="18" rx="2" fill="{accent}"/>
  <text x="40" y="45" font-family="Segoe UI, Ubuntu, Helvetica, Arial, sans-serif" font-size="21" font-weight="700" fill="#E6EDF3">{title}</text>
  <text x="26" y="68" font-family="Consolas, 'Courier New', monospace" font-size="12.5" font-weight="600" fill="{accent}" letter-spacing="1">{subtitle}</text>
  <rect x="26" y="78" width="52" height="2.5" rx="1.25" fill="{accent}">
    <animate attributeName="width" values="52;110;52" dur="4s" repeatCount="indefinite"/>
  </rect>

  <text x="26" y="106" font-family="Segoe UI, Ubuntu, Helvetica, Arial, sans-serif" font-size="13.5" fill="#8B949E">{line1}</text>
  <text x="26" y="126" font-family="Segoe UI, Ubuntu, Helvetica, Arial, sans-serif" font-size="13.5" fill="#8B949E">{line2}</text>

  {chips}
  {extra}
</svg>
'''

MONO = "Consolas, 'Courier New', monospace"

def chips(items, accent, y=152):
    out, x = [], 26
    for label in items:
        w = int(len(label) * 7.2) + 22
        out.append(f'<g><rect x="{x}" y="{y}" width="{w}" height="26" rx="13" fill="{accent}" fill-opacity="0.10" stroke="{accent}" stroke-opacity="0.45"/>'
                   f'<text x="{x + w/2}" y="{y+17}" text-anchor="middle" font-family="{MONO}" font-size="12" fill="{accent}">{label}</text></g>')
        x += w + 10
    return "\n  ".join(out)

def wavebars(accent):
    bars = []
    for i, (h, d) in enumerate([(14,'0s'),(26,'-0.3s'),(38,'-0.6s'),(22,'-0.9s'),(32,'-1.2s'),(16,'-1.5s')]):
        x = 340 + i*14
        h2 = max(8, 46-h)
        bars.append(f'<rect x="{x}" y="{60-h/2}" width="7" rx="3.5" height="{h}" fill="{accent}" opacity="0.75">'
                    f'<animate attributeName="height" values="{h};{h2};{h}" dur="1.4s" begin="{d}" repeatCount="indefinite"/>'
                    f'<animate attributeName="y" values="{60-h/2};{60-h2/2};{60-h/2}" dur="1.4s" begin="{d}" repeatCount="indefinite"/></rect>')
    return "\n  ".join(bars)

def radar(accent):
    return (f'<g opacity="0.8"><circle cx="382" cy="58" r="30" stroke="{accent}" stroke-opacity="0.3" fill="none"/>'
            f'<circle cx="382" cy="58" r="19" stroke="{accent}" stroke-opacity="0.3" fill="none"/>'
            f'<circle cx="382" cy="58" r="8" stroke="{accent}" stroke-opacity="0.3" fill="none"/>'
            f'<line x1="382" y1="58" x2="382" y2="28" stroke="{accent}" stroke-width="2">'
            f'<animateTransform attributeName="transform" type="rotate" from="0 382 58" to="360 382 58" dur="4s" repeatCount="indefinite"/></line>'
            f'<circle cx="395" cy="45" r="3" fill="{accent}"><animate attributeName="opacity" values="0;1;0" dur="4s" repeatCount="indefinite"/></circle></g>')

def pulse(accent):
    return (f'<path d="M330 58 h18 l7 -16 l12 32 l9 -22 l6 6 h28" stroke="{accent}" stroke-width="2.5" fill="none" '
            f'stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="130" stroke-dashoffset="130">'
            f'<animate attributeName="stroke-dashoffset" values="130;0;0;-130" keyTimes="0;0.4;0.7;1" dur="3s" repeatCount="indefinite"/></path>')

def nodes(accent):
    return (f'<g><circle cx="355" cy="40" r="4" fill="{accent}"><animate attributeName="opacity" values="0.3;1;0.3" dur="2s" repeatCount="indefinite"/></circle>'
            f'<circle cx="400" cy="55" r="4" fill="{accent}"><animate attributeName="opacity" values="0.3;1;0.3" dur="2s" begin="-0.7s" repeatCount="indefinite"/></circle>'
            f'<circle cx="365" cy="78" r="4" fill="{accent}"><animate attributeName="opacity" values="0.3;1;0.3" dur="2s" begin="-1.4s" repeatCount="indefinite"/></circle>'
            f'<line x1="355" y1="40" x2="400" y2="55" stroke="{accent}" stroke-opacity="0.4"/>'
            f'<line x1="400" y1="55" x2="365" y2="78" stroke="{accent}" stroke-opacity="0.4"/>'
            f'<line x1="355" y1="40" x2="365" y2="78" stroke="{accent}" stroke-opacity="0.4"/></g>')

def eye(accent):
    return (f'<g><path d="M345 58 q37 -26 74 0 q-37 26 -74 0 Z" stroke="{accent}" stroke-width="2" fill="none"/>'
            f'<circle cx="382" cy="58" r="9" fill="{accent}" fill-opacity="0.25" stroke="{accent}" stroke-width="2">'
            f'<animate attributeName="cx" values="382;390;374;382" dur="4s" repeatCount="indefinite"/></circle></g>')

def spark(accent):
    return (f'<g><rect x="350" y="40" width="60" height="38" rx="6" stroke="{accent}" stroke-width="2" fill="{accent}" fill-opacity="0.08"/>'
            f'<line x1="350" y1="52" x2="410" y2="52" stroke="{accent}" stroke-width="2"/>'
            f'<rect x="358" y="60" width="20" height="8" rx="2" fill="{accent}" opacity="0.7">'
            f'<animate attributeName="opacity" values="0.4;1;0.4" dur="2.5s" repeatCount="indefinite"/></rect></g>')

def orbit(accent):
    return (f'<g><circle cx="382" cy="58" r="26" stroke="{accent}" stroke-opacity="0.35" stroke-dasharray="5 6" fill="none">'
            f'<animateTransform attributeName="transform" type="rotate" from="0 382 58" to="360 382 58" dur="10s" repeatCount="indefinite"/></circle>'
            f'<circle cx="382" cy="58" r="7" fill="{accent}" fill-opacity="0.3" stroke="{accent}" stroke-width="2"/>'
            f'<circle cx="408" cy="58" r="4" fill="{accent}">'
            f'<animateTransform attributeName="transform" type="rotate" from="0 382 58" to="360 382 58" dur="5s" repeatCount="indefinite"/></circle></g>')

cards = [
 dict(file="medos", accent="#F472B6", emoji="", title="MedOS Stroke Detection",
      subtitle="MEDICAL AI · BRAIN CT SEGMENTATION",
      line1="Segments ischemic stroke lesions on brain CT with an ensemble of",
      line2="DeepLabV3+, Attention U-Net and YOLO11-seg, plus a risk score.",
      tech=["PyTorch","Flask","Healthcare"], extra="pulse"),
 dict(file="freesweep", accent="#34D399", emoji="", title="FreeSweep",
      subtitle="MEDICAL IMAGING · 3D ULTRASOUND",
      line1="Sensorless freehand 3D ultrasound reconstruction (TUS-REC):",
      line2="drift cut from 86.9 mm to 14.4 mm, 83% below the baseline.",
      tech=["PyTorch","6D rotation","Research"], extra="wave"),
 dict(file="geoanchor", accent="#22D3EE", emoji="", title="GeoAnchor",
      subtitle="GNSS-DENIED UAV LOCALIZATION",
      line1="Locates a UAV without GPS by fusing visual odometry with",
      line2="satellite-map matching in a particle filter — knows when it fails.",
      tech=["DINOv2","LoFTR","OpenCV"], extra="radar"),
 dict(file="novex", accent="#818CF8", emoji="", title="Novex",
      subtitle="HEALTH TECH · CLINIC HACKATHON",
      line1="Guided 5-angle photo capture after hair transplant, Gemini",
      line2="pre-analysis and a doctor panel for approval and follow-up.",
      tech=["Flutter","Firebase","ML Kit"], extra="spark"),
 dict(file="pys", accent="#60A5FA", emoji="", title="PYS Project Management",
      subtitle="FULL-STACK · .NET 10 WEB API",
      line1="Projects, staff, documents and petitions for a municipal",
      line2="software unit — JWT, SignalR chat, MinIO, PostgreSQL.",
      tech=["ASP.NET Core","EF Core","SignalR"], extra="nodes"),
 dict(file="pys-angular", accent="#EF4444", emoji="", title="PYS Angular",
      subtitle="FRONTEND · ANGULAR 21 SPA",
      line1="Standalone components and signals, real-time chat, role guards;",
      line2="104 unit tests and a CI pipeline (format, lint, test, build).",
      tech=["Angular","PrimeNG","Vitest"], extra="orbit"),
 dict(file="brailletr", accent="#F97316", emoji="", title="BrailleTR",
      subtitle="ACCESSIBILITY · IN DEVELOPMENT",
      line1="Reads embossed Turkish Braille from a phone photo and speaks it;",
      line2="new dot-detection engine with no trained model, license-clean.",
      tech=["OpenCV","FastAPI","PWA"], extra="braille"),
 dict(file="officeguardian", accent="#FBBF24", emoji="", title="OfficeGuardian",
      subtitle="REAL-TIME CV · WORKPLACE HEALTH",
      line1="Posture and attention tracking through a standard webcam;",
      line2="images stay on the PC, only metrics reach the live dashboard.",
      tech=["Django","MediaPipe","OpenCV"], extra="eye"),
]

def braille(accent):
    out = []
    for i, (cx, cy, on) in enumerate([(362,36,1),(382,36,0),(362,58,1),(382,58,1),(362,80,0),(382,80,1),
                                       (404,36,1),(424,36,1),(404,58,0),(424,58,1),(404,80,1),(424,80,0)]):
        if on:
            out.append(f'<circle cx="{cx-12}" cy="{cy}" r="6" fill="{accent}"><animate attributeName="opacity" '
                       f'values="0.35;1;0.35" dur="2.4s" begin="-{i*0.2:.1f}s" repeatCount="indefinite"/></circle>')
        else:
            out.append(f'<circle cx="{cx-12}" cy="{cy}" r="6" fill="none" stroke="{accent}" stroke-opacity="0.35"/>')
    return "<g>" + "".join(out) + "</g>"

extras = dict(braille=braille, wave=wavebars, radar=radar, pulse=pulse, nodes=nodes, eye=eye, spark=spark, orbit=orbit)

for c in cards:
    svg = TPL.format(accent=c["accent"], emoji=c["emoji"], title=html.escape(c["title"]),
                     subtitle=html.escape(c["subtitle"]), line1=html.escape(c["line1"]), line2=html.escape(c["line2"]),
                     chips=chips(c["tech"], c["accent"]), extra=extras[c["extra"]](c["accent"]))
    with open(f'assets/cards/{c["file"]}.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print("wrote", c["file"])
