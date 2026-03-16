with open(r"C:\Users\rphil\nextplaystars-landing\index.html", "r", encoding="utf-8") as f:
    html = f.read()

changes = []

# ─────────────────────────────────────────────────────────────────────────────
# FIX 1 — Replace hero CSS
# ─────────────────────────────────────────────────────────────────────────────

OLD_HERO_CSS = """.hero { min-height: 100vh; display: flex; align-items: center; padding: 120px 24px 80px; position: relative; overflow: hidden; }
    .hero-bg { position: absolute; inset: 0; background: radial-gradient(ellipse 55% 65% at 72% 50%, rgba(0,174,239,0.08) 0%, transparent 65%), radial-gradient(ellipse 35% 40% at 15% 85%, rgba(0,174,239,0.04) 0%, transparent 60%); pointer-events: none; }
    .hero-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 64px; align-items: center; max-width: 1140px; margin: 0 auto; position: relative; z-index: 1; width: 100%; }
    .hero-badge { display: inline-flex; align-items: center; gap: 8px; padding: 7px 16px; border-radius: 100px; border: 1px solid rgba(0,174,239,0.3); background: rgba(0,174,239,0.06); font-size: 11px; font-weight: 700; letter-spacing: 1.5px; color: var(--cyan); text-transform: uppercase; margin-bottom: 22px; animation: badge-float 3s ease-in-out infinite; }
    .hero-badge-dot { width: 6px; height: 6px; border-radius: 50%; background: var(--cyan); display: inline-block; }
    .hero h1 { font-size: clamp(34px, 4.5vw, 56px); font-weight: 800; line-height: 1.1; margin-bottom: 20px; letter-spacing: -1.5px; }
    .hero h1 em { font-style: normal; background: linear-gradient(135deg, #00AEEF 0%, #a78bfa 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
    .hero-sub { font-size: 17px; color: var(--muted); line-height: 1.7; margin-bottom: 36px; max-width: 460px; }
    .hero-btns { display: flex; gap: 14px; flex-wrap: wrap; }
    .hero-photo { border-radius: 24px; overflow: hidden; border: 1px solid rgba(0,174,239,0.15); box-shadow: 0 32px 80px rgba(0,0,0,0.5), 0 0 60px rgba(0,174,239,0.07); }
    .hero-photo img { width: 100%; height: 520px; object-fit: cover; object-position: center top; display: block; }"""

NEW_HERO_CSS = """.hero { min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 120px 24px 80px; position: relative; overflow: hidden; }
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

assert OLD_HERO_CSS in html, "hero CSS not found"
html = html.replace(OLD_HERO_CSS, NEW_HERO_CSS, 1)
changes.append("Hero CSS replaced: centered layout, orb glow, nikki title styles")

# ─────────────────────────────────────────────────────────────────────────────
# FIX 2 — Replace hero HTML (remove photo, add centered orb + content)
# ─────────────────────────────────────────────────────────────────────────────

OLD_HERO_OPEN = """<section class="hero" id="hero">
  <div class="hero-bg"></div>
  <div class="hero-grid">
    <div class="hero-content fade-up">
      <div class="hero-badge"><span class="hero-badge-dot"></span> AI-Powered &nbsp;&middot;&nbsp; Athlete-Driven</div>
      <h1>Your Athlete&#8217;s Recruiting Assistant <em>is Ready.</em></h1>
      <p class="hero-sub">Meet N.I.K.K.I. &#8212; the AI voice assistant that handles your entire recruiting journey so you can focus on the game.</p>
      <div class="hero-btns">
        <a href="#nikki" class="btn btn-primary">Meet Nikki &#8594;</a>
        <a href="#how" class="btn btn-outline">See How It Works</a>
      </div>
    </div>
    <div class="hero-photo fade-up" style="animation-delay:0.15s">"""

assert OLD_HERO_OPEN in html, "hero open HTML not found"

# Find where the hero photo div ends (closes) — find </div> after hero-photo
photo_div_start = html.index(OLD_HERO_OPEN) + len(OLD_HERO_OPEN)

# We need to find the base64 img inside hero-photo and skip the whole photo div
# The photo div is: <img ... /> then </div> (close hero-photo) then </div> (close hero-grid) then </section>
# Let's find the </section> that closes the hero
hero_section_close = html.index('</section>', photo_div_start)
hero_section_close += len('</section>')

# Extract full hero HTML to replace
OLD_HERO_FULL_START = html.index('<!-- HERO -->')
OLD_HERO_FULL_END = hero_section_close  # up to and including </section>

NEW_HERO_HTML = """<!-- HERO -->
<section class="hero" id="hero">
  <div class="hero-bg"></div>
  <div class="hero-center fade-up">
    <div class="hero-badge"><span class="hero-badge-dot"></span> AI-Powered &nbsp;&middot;&nbsp; Athlete-Driven</div>

    <!-- Orb -->
    <div class="hero-orb-wrap">
      <div class="hero-orb-glow"></div>
      <div class="orb-wrap" style="width:200px;height:200px;">
        <div class="orb-core"><div style="position:absolute;top:18%;left:20%;width:25%;height:18%;background:radial-gradient(ellipse,rgba(255,255,255,0.5),transparent);border-radius:50%;pointer-events:none;"></div></div>
        <div class="orb-ring r1"><div class="orb-ring-inner" style="width:130px;height:130px;"></div></div>
        <div class="orb-ring r2"><div class="orb-ring-inner" style="width:162px;height:162px;"></div></div>
        <div class="orb-ring r3"><div class="orb-ring-inner" style="width:195px;height:195px;"></div></div>
        <div class="orb-ring r4"><div class="orb-ring-inner" style="width:240px;height:240px;"></div></div>
      </div>
    </div>

    <!-- Nikki title -->
    <p class="hero-nikki-title">Meet your AI recruiting assistant</p>
    <h2 class="hero-nikki-name">N.I.K.K.I.</h2>
    <p class="hero-nikki-full">Neurally Integrated Knowledge &amp; Kinetics Intelligence</p>

    <!-- Main headline -->
    <h1>Your Athlete&#8217;s Recruiting Assistant <em>is Ready.</em></h1>
    <p class="hero-sub">The AI voice assistant that handles your entire recruiting journey so you can focus on the game.</p>

    <div class="hero-btns">
      <a href="https://www.nextplayrecruiting.app/signup" class="btn btn-primary">Get Started Free &#8594;</a>
      <a href="#how" class="btn btn-outline">See How It Works</a>
    </div>
  </div>
</section>
"""

html = html[:OLD_HERO_FULL_START] + NEW_HERO_HTML + html[OLD_HERO_FULL_END:]
changes.append("Hero HTML: removed photo, centered layout with orb + Nikki title + CTA")

# ─────────────────────────────────────────────────────────────────────────────
# FIX 3 — Simplify the Meet Nikki section: keep it, remove the orb, make it
#          a clean text-only features section
# ─────────────────────────────────────────────────────────────────────────────

# Re-read the file since we replaced hero HTML (offsets changed)
with open(r"C:\Users\rphil\nextplaystars-landing\index.html", "w", encoding="utf-8") as f:
    f.write(html)

# Reload and now fix the nikki section
with open(r"C:\Users\rphil\nextplaystars-landing\index.html", "r", encoding="utf-8") as f:
    html = f.read()

nikki_start = html.index('<!-- MEET N.I.K.K.I. -->')
nikki_end   = html.index('<!-- HOW IT WORKS -->')

old_nikki_section = html[nikki_start:nikki_end]

NEW_NIKKI_SECTION = """<!-- MEET N.I.K.K.I. -->
<section class="nikki-section" id="nikki" style="padding:100px 24px;">
  <div class="container" style="max-width:860px;margin:0 auto;text-align:center;">
    <p class="section-label">Your AI Recruiting Partner</p>
    <h2 style="font-size:clamp(28px,3.8vw,44px);font-weight:800;letter-spacing:-1px;margin-bottom:16px;">Everything Nikki Does for You</h2>
    <p style="font-size:17px;color:var(--muted);line-height:1.75;max-width:600px;margin:0 auto 56px;">Nikki knows your athlete&#8217;s full profile, works 24/7, and handles every part of the recruiting process &#8212; so your family can focus on the game.</p>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:24px;text-align:left;">
      <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(0,174,239,0.15);border-radius:16px;padding:28px 24px;">
        <div style="width:40px;height:40px;border-radius:10px;background:rgba(0,174,239,0.12);display:flex;align-items:center;justify-content:center;margin-bottom:16px;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#00AEEF" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 12 19.79 19.79 0 0 1 1.61 3.37 2 2 0 0 1 3.61 1.2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L7.91 8.91a16 16 0 0 0 6 6z"/></svg>
        </div>
        <h3 style="font-size:16px;font-weight:700;margin-bottom:8px;">Call or Text Anytime</h3>
        <p style="font-size:14px;color:var(--muted);line-height:1.6;">Reach Nikki 24/7 by phone or text for recruiting questions, email drafts, or calendar updates.</p>
      </div>
      <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(0,174,239,0.15);border-radius:16px;padding:28px 24px;">
        <div style="width:40px;height:40px;border-radius:10px;background:rgba(0,174,239,0.12);display:flex;align-items:center;justify-content:center;margin-bottom:16px;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#00AEEF" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><polyline points="22,4 12,13 2,4"/></svg>
        </div>
        <h3 style="font-size:16px;font-weight:700;margin-bottom:8px;">Automated Coach Emails</h3>
        <p style="font-size:14px;color:var(--muted);line-height:1.6;">Personalized outreach emails and multi-step follow-up sequences sent to coaches on your timeline.</p>
      </div>
      <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(0,174,239,0.15);border-radius:16px;padding:28px 24px;">
        <div style="width:40px;height:40px;border-radius:10px;background:rgba(0,174,239,0.12);display:flex;align-items:center;justify-content:center;margin-bottom:16px;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#00AEEF" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
        </div>
        <h3 style="font-size:16px;font-weight:700;margin-bottom:8px;">Calendar Management</h3>
        <p style="font-size:14px;color:var(--muted);line-height:1.6;">Campus visits, official visits, and recruiting events organized automatically on your calendar.</p>
      </div>
      <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(0,174,239,0.15);border-radius:16px;padding:28px 24px;">
        <div style="width:40px;height:40px;border-radius:10px;background:rgba(0,174,239,0.12);display:flex;align-items:center;justify-content:center;margin-bottom:16px;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#00AEEF" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>
        </div>
        <h3 style="font-size:16px;font-weight:700;margin-bottom:8px;">Target Schools Pipeline</h3>
        <p style="font-size:14px;color:var(--muted);line-height:1.6;">Track every school, coach response, and next step in one organized recruiting CRM.</p>
      </div>
      <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(0,174,239,0.15);border-radius:16px;padding:28px 24px;">
        <div style="width:40px;height:40px;border-radius:10px;background:rgba(0,174,239,0.12);display:flex;align-items:center;justify-content:center;margin-bottom:16px;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#00AEEF" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
        </div>
        <h3 style="font-size:16px;font-weight:700;margin-bottom:8px;">AI Recruiting Report</h3>
        <p style="font-size:14px;color:var(--muted);line-height:1.6;">Personalized intelligence report analyzing your athlete&#8217;s fit, reach schools, and recruiting strategy.</p>
      </div>
      <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(0,174,239,0.15);border-radius:16px;padding:28px 24px;">
        <div style="width:40px;height:40px;border-radius:10px;background:rgba(0,174,239,0.12);display:flex;align-items:center;justify-content:center;margin-bottom:16px;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#00AEEF" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>
        </div>
        <h3 style="font-size:16px;font-weight:700;margin-bottom:8px;">Social Media Posts</h3>
        <p style="font-size:14px;color:var(--muted);line-height:1.6;">Nikki creates highlight social posts to increase your athlete&#8217;s visibility with college coaches.</p>
      </div>
    </div>

    <!-- Voice demo + CTA -->
    <div style="margin-top:56px;">
"""

# Find the voice demo part in the old nikki section (<!-- Nikki Voice Demo --> ... <!-- End Nikki Voice Demo -->)
# and the nikki-btns part
voice_demo_start_marker = "      <!-- Nikki Voice Demo -->"
voice_demo_end_marker   = "      <!-- End Nikki Voice Demo -->\n"
nikki_btns_marker       = '      <div class="nikki-btns">'
nikki_btns_end_marker   = "      </div>\n    </div>\n  </div>\n</section>\n"

if voice_demo_start_marker in old_nikki_section:
    vd_start = old_nikki_section.index(voice_demo_start_marker)
    vd_end   = old_nikki_section.index(voice_demo_end_marker) + len(voice_demo_end_marker)
    voice_demo_html = old_nikki_section[vd_start:vd_end].strip()
    # Strip the 6-space indent, re-indent for new context
    voice_demo_html_clean = '\n'.join(
        '      ' + line.lstrip() if line.strip() else ''
        for line in voice_demo_html.split('\n')
    )
else:
    voice_demo_html_clean = ""

# Find nikki-btns
if nikki_btns_marker in old_nikki_section:
    nb_start = old_nikki_section.index(nikki_btns_marker)
    # Find the closing </div> of nikki-btns
    nb_end   = old_nikki_section.index('</div>', nb_start) + len('</div>')
    nikki_btns_html = old_nikki_section[nb_start:nb_end]
    # Re-style to centered
    nikki_btns_new = nikki_btns_html.replace(
        'class="nikki-btns"',
        'style="display:flex;flex-direction:column;align-items:center;gap:12px;"'
    )
else:
    nikki_btns_new = '<div style="display:flex;flex-direction:column;align-items:center;gap:12px;"><a href="https://www.nextplayrecruiting.app/signup" class="btn btn-primary">Get Access to Nikki &#8594;</a><p style="margin:0;font-size:13px;color:rgba(255,255,255,0.45);">Exclusively for NextPlay members</p></div>'

CLOSE_SECTION = """    </div>
  </div>
</section>
"""

NEW_NIKKI_SECTION = (
    NEW_NIKKI_SECTION
    + "      " + (voice_demo_html_clean if voice_demo_html_clean else "") + "\n"
    + "      " + nikki_btns_new + "\n"
    + CLOSE_SECTION
)

html = html[:nikki_start] + NEW_NIKKI_SECTION + html[nikki_end:]
changes.append("Nikki section: removed orb, converted to text feature cards + voice demo + CTA")

with open(r"C:\Users\rphil\nextplaystars-landing\index.html", "w", encoding="utf-8") as f:
    f.write(html)

import os
for c in changes:
    print("  OK:", c)
print(f"\nDone — {os.path.getsize(r'C:\Users\rphil\nextplaystars-landing\index.html') // 1024} KB")
