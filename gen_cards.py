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
 dict(file="belediyeai", accent="#22D3EE", emoji="🏛️", title="BelediyeAI",
      subtitle="TURKISH NLP · COMPLAINT TRIAGE",
      line1="Classifies municipal complaints into 10 categories and 4 priority",
      line2="levels — smart routing to the right department, end to end.",
      tech=["Python","scikit-learn","NLP"], extra="nodes"),
 dict(file="medos", accent="#F472B6", emoji="🧠", title="MedOS Stroke Detection",
      subtitle="MEDICAL AI · NEURO-DIAGNOSTICS",
      line1="Deep learning system detecting stroke from brain imaging,",
      line2="wrapped in a clinical-style diagnostic interface.",
      tech=["Deep Learning","CV","Healthcare"], extra="pulse"),
 dict(file="speechquest", accent="#34D399", emoji="🎙️", title="SpeechQuest",
      subtitle="OFFLINE STT · QUESTION GENERATION",
      line1="Fully offline speech-to-text and automatic question generation —",
      line2="audio, YouTube links and live microphone. Zero external APIs.",
      tech=["Python","NLP","React"], extra="wave"),
 dict(file="officeguardian", accent="#FBBF24", emoji="👁️", title="OfficeGuardian",
      subtitle="REAL-TIME CV · WORKPLACE HEALTH",
      line1="Posture and attention analysis through a standard webcam —",
      line2="no wearable sensors, role-based health dashboards.",
      tech=["Django","OpenCV","Python"], extra="eye"),
 dict(file="tanktespit", accent="#EF4444", emoji="🎯", title="TankTespit",
      subtitle="OBJECT DETECTION · YOLOV8",
      line1="Military vehicle detection trained on a custom dataset —",
      line2="end-to-end YOLOv8 data prep and training pipeline.",
      tech=["YOLOv8","PyTorch","CV"], extra="radar"),
 dict(file="vera", accent="#818CF8", emoji="💳", title="Vera",
      subtitle="AI-NATIVE FINTECH · BTK HACKATHON",
      line1="Next-gen mobile finance OS prototype powered by Gemini AI —",
      line2="Android, iOS, Web and Desktop from one codebase.",
      tech=["Flutter","Gemini AI","Riverpod"], extra="spark"),
 dict(file="handspeak", accent="#F97316", emoji="🤟", title="HandSpeak",
      subtitle="ACCESSIBILITY · SIGN LANGUAGE",
      line1="Sign language translation and learning — interactive lessons,",
      line2="video practice tools and personalized profiles.",
      tech=["Flutter","Firebase","Dart"], extra="orbit"),
 dict(file="travel", accent="#60A5FA", emoji="✈️", title="Travel Orchestration",
      subtitle="MICROSERVICES · RESILIENT APIS",
      line1="Distributed booking system with Circuit Breaker patterns",
      line2="and composite endpoints — NestJS microservices on Docker.",
      tech=["NestJS","Docker","Microservices"], extra="orbit"),
]

extras = dict(wave=wavebars, radar=radar, pulse=pulse, nodes=nodes, eye=eye, spark=spark, orbit=orbit)

for c in cards:
    svg = TPL.format(accent=c["accent"], emoji=c["emoji"], title=html.escape(c["title"]),
                     subtitle=html.escape(c["subtitle"]), line1=html.escape(c["line1"]), line2=html.escape(c["line2"]),
                     chips=chips(c["tech"], c["accent"]), extra=extras[c["extra"]](c["accent"]))
    with open(f'assets/cards/{c["file"]}.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print("wrote", c["file"])
