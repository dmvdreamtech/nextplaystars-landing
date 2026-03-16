with open(r"C:\Users\rphil\nextplaystars-landing\index.html", "r", encoding="utf-8") as f:
    html = f.read()

changes = []

# ─────────────────────────────────────────────────────────────────────────────
# 1 — Replace hero CSS
# ─────────────────────────────────────────────────────────────────────────────

OLD_CSS = """.hero { min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 120px 24px 80px; position: relative; overflow: hidden; }
    .hero-bg { position: absolute; inset: 0; background: radial-gradient(ellipse 60% 50% at 50% 42%, rgba(0,174,239,0.10) 0%, transparent 65%); pointer-events: none; }
    .hero-center { display: flex; flex-direction: column; align-items: center; text-align: center; max-width: 760px; margin: 0 auto; position: relative; z-index: 1; width: 100%; }
    .hero-badge { display: inline-flex; align-items: center; gap: 8px; padding: 7px 16px; border-radius: 100px; border: 1px solid rgba(0,174,239,0.3); background: rgba(0,174,239,0.06); font-size: 11px; font-weight: 700; letter-spacing: 1.5px; color: var(--cyan); text-transform: uppercase; margin-bottom: 32px; animation: badge-float 3s ease-in-out infinite; }
    .hero-badge-dot { width: 6px; height: 6px; border-radius: 50%; background: var(--cyan); display: inline-block; }
    .hero-orb-wrap { position: relative; margin-bottom: 28px; }
    .hero-orb-glow { position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%); width: 320px; height: 320px; border-radius: 50%; background: radial-gradient(ellipse, rgba(0,174,239,0.18) 0%, transparent 70%); pointer-events: none; }
    .hero-nikki-title { font-size: 13px; font-weight: 700; letter-spacing: 2.5px; text-transform: uppercase; color: rgba(0,174,239,0.6); margin-bottom: 6px; }
    .hero-nikki-name { font-size: clamp(36px, 5vw, 64px); font-weight: 900; letter-spacing: -2px; color: #00AEEF; text-shadow: 0 0 40px rgba(0,174,239,0.5), 0 0 80px rgba(0,174,239,0.2); margin-bottom: 8px; line-height: 1; }
    .hero-nikki-full { font-size: 12px; color: rgba(255,255,255,0.35); letter-spacing: 1px; text-transform: uppercase; margin-bottom: 28px; font-weight: 500; }
    .hero h1 { font-size: clamp(26px, 3.8vw, 46px); font-weight: 800; line-height: 1.15; margin-bottom: 18px; letter-spacing: -1px; }
    .hero h1 em { font-style: normal; background: linear-gradient(135deg, #00AEEF 0%, #a78bfa 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
    .hero-sub { font-size: 17px; color: var(--muted); line-height: 1.7; margin-bottom: 36px; max-width: 520px; }
    .hero-btns { display: flex; gap: 14px; flex-wrap: wrap; justify-content: center; }"""

NEW_CSS = """.hero { min-height: 100vh; display: flex; align-items: center; padding: 120px 40px 80px; position: relative; overflow: visible; }
    .hero-bg { position: absolute; inset: 0; background: radial-gradient(ellipse 55% 65% at 72% 50%, rgba(0,174,239,0.09) 0%, transparent 65%); pointer-events: none; overflow: hidden; }
    .hero-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: center; max-width: 1160px; margin: 0 auto; position: relative; z-index: 1; width: 100%; }
    .hero-left { display: flex; flex-direction: column; align-items: flex-start; }
    .hero-badge { display: inline-flex; align-items: center; gap: 8px; padding: 7px 16px; border-radius: 100px; border: 1px solid rgba(0,174,239,0.3); background: rgba(0,174,239,0.06); font-size: 11px; font-weight: 700; letter-spacing: 1.5px; color: var(--cyan); text-transform: uppercase; margin-bottom: 24px; animation: badge-float 3s ease-in-out infinite; }
    .hero-badge-dot { width: 6px; height: 6px; border-radius: 50%; background: var(--cyan); display: inline-block; }
    .hero-nikki-name { font-size: clamp(42px, 5.5vw, 72px); font-weight: 900; letter-spacing: -3px; color: #00AEEF; text-shadow: 0 0 40px rgba(0,174,239,0.55), 0 0 90px rgba(0,174,239,0.25); margin-bottom: 6px; line-height: 1; }
    .hero-nikki-full { font-size: 11px; color: rgba(255,255,255,0.35); letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 28px; font-weight: 500; }
    .hero h1 { font-size: clamp(28px, 3.2vw, 44px); font-weight: 800; line-height: 1.15; margin-bottom: 18px; letter-spacing: -1px; }
    .hero h1 em { font-style: normal; background: linear-gradient(135deg, #00AEEF 0%, #a78bfa 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
    .hero-sub { font-size: 17px; color: var(--muted); line-height: 1.7; margin-bottom: 36px; max-width: 480px; }
    .hero-btns { display: flex; gap: 14px; flex-wrap: wrap; }
    .hero-right { display: flex; align-items: center; justify-content: center; position: relative; }
    .hero-orb-glow { position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%); width: 500px; height: 500px; border-radius: 50%; background: radial-gradient(ellipse, rgba(0,174,239,0.13) 0%, transparent 68%); pointer-events: none; }"""

assert OLD_CSS in html, "hero CSS block not found"
html = html.replace(OLD_CSS, NEW_CSS, 1)
changes.append("Hero CSS: two-column grid layout")

# ─────────────────────────────────────────────────────────────────────────────
# 2 — Replace hero HTML
# ─────────────────────────────────────────────────────────────────────────────

HERO_SECTION_START = html.index('<!-- HERO -->')
HERO_SECTION_END   = html.index('<!-- WHAT IS NEXTPLAY')

NEW_HERO = """<!-- HERO -->
<section class="hero" id="hero">
  <div class="hero-bg"></div>
  <div class="hero-grid">

    <!-- LEFT: text -->
    <div class="hero-left fade-up">
      <div class="hero-badge"><span class="hero-badge-dot"></span> AI-Powered &nbsp;&middot;&nbsp; Athlete-Driven</div>
      <h2 class="hero-nikki-name">N.I.K.K.I.</h2>
      <p class="hero-nikki-full">Neurally Integrated Knowledge &amp; Kinetics Intelligence</p>
      <h1>Your Athlete&#8217;s Recruiting Assistant <em>is Ready.</em></h1>
      <p class="hero-sub">The AI voice assistant that handles your entire recruiting journey so you can focus on the game.</p>
      <div class="hero-btns">
        <a href="https://www.nextplayrecruiting.app/signup" class="btn btn-primary">Get Started Free &#8594;</a>
        <a href="#how" class="btn btn-outline">See How It Works</a>
      </div>
    </div>

    <!-- RIGHT: orb -->
    <div class="hero-right fade-up" style="animation-delay:0.18s">
      <div class="hero-orb-glow"></div>
      <div class="orb-wrap">
        <div class="orb-core"><div style="position:absolute;top:18%;left:20%;width:25%;height:18%;background:radial-gradient(ellipse,rgba(255,255,255,0.5),transparent);border-radius:50%;pointer-events:none;"></div></div>
        <div class="orb-ring r1"><div class="orb-ring-inner"></div></div>
        <div class="orb-ring r2"><div class="orb-ring-inner"></div></div>
        <div class="orb-ring r3"><div class="orb-ring-inner"></div></div>
        <div class="orb-ring r4"><div class="orb-ring-inner"></div></div>
      </div>
    </div>

  </div>
</section>

"""

html = html[:HERO_SECTION_START] + NEW_HERO + html[HERO_SECTION_END:]
changes.append("Hero HTML: two-column with left text + right orb")

# ─────────────────────────────────────────────────────────────────────────────
# 3 — Update mobile breakpoint for hero
# ─────────────────────────────────────────────────────────────────────────────

OLD_MOBILE = """.hero { padding: 100px 20px 60px; }
      .hero-center { padding: 0; }
      .hero-nikki-name { font-size: 40px; }
      .hero-btns { justify-content: center; }
      .hero-badge { margin: 0 auto 24px; }"""

NEW_MOBILE = """.hero { padding: 100px 20px 60px; }
      .hero-grid { grid-template-columns: 1fr; gap: 0; }
      .hero-left { align-items: center; text-align: center; order: 2; }
      .hero-right { order: 1; margin-bottom: 40px; }
      .hero-nikki-name { font-size: 48px; }
      .hero-sub { max-width: 100%; }
      .hero-btns { justify-content: center; }
      .hero-badge { margin: 0 auto 20px; }
      .hero-orb-glow { width: 360px; height: 360px; }"""

assert OLD_MOBILE in html, "mobile hero CSS not found"
html = html.replace(OLD_MOBILE, NEW_MOBILE, 1)
changes.append("Mobile: orb on top, text below, centered")

# ─────────────────────────────────────────────────────────────────────────────
# 4 — Boost the orb-core box-shadow to be brighter in hero context
#     (the orb-core CSS already has good glow; just confirm it's there)
# ─────────────────────────────────────────────────────────────────────────────
assert 'box-shadow: 0 0 60px rgba(0,174,239,0.5)' in html, "orb-core shadow not found"
changes.append("Orb-core glow confirmed present")

with open(r"C:\Users\rphil\nextplaystars-landing\index.html", "w", encoding="utf-8") as f:
    f.write(html)

import os
for c in changes:
    print("  OK:", c)
print(f"\nDone — {os.path.getsize(r'C:\Users\rphil\nextplaystars-landing\index.html') // 1024} KB")
