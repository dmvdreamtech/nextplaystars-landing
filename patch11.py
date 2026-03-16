with open(r"C:\Users\rphil\nextplaystars-landing\index.html", "r", encoding="utf-8") as f:
    html = f.read()

changes = []

# ─────────────────────────────────────────────────────────────────────────────
# FIX 1 — Remove DMV Dream promo line from pricing section
# ─────────────────────────────────────────────────────────────────────────────
old_dmv = """    <div class="pricing-dmv">
      <span>&#127881; DMV Dream families get 30 days free with code <strong>DMVDREAM</strong></span>
    </div>
    """
new_dmv = "    "
assert old_dmv in html, "DMV line not found"
html = html.replace(old_dmv, new_dmv, 1)
changes.append("Removed DMV Dream promo line")

# ─────────────────────────────────────────────────────────────────────────────
# FIX 2 — Replace pricing cards with feature lists
# ─────────────────────────────────────────────────────────────────────────────

def feat(items):
    rows = []
    for item in items:
        rows.append(
            f'        <li style="display:flex;align-items:flex-start;gap:9px;padding:7px 0;border-bottom:1px solid rgba(255,255,255,0.06);">'
            f'<svg style="flex-shrink:0;margin-top:2px" width="14" height="14" viewBox="0 0 14 14" fill="none">'
            f'<circle cx="7" cy="7" r="7" fill="rgba(0,174,239,0.15)"/>'
            f'<polyline points="3.5,7 6,9.5 10.5,4.5" stroke="#00AEEF" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>'
            f'</svg>'
            f'<span style="font-size:14px;color:rgba(255,255,255,0.75);line-height:1.4;">{item}</span>'
            f'</li>'
        )
    return '\n'.join(rows)

STARTER_FEATS = feat([
    "N.I.K.K.I. Voice Calls",
    "10 Target Schools",
    "1 Email Sequence",
    "5 Social Posts/month",
    "Calendar Sync",
    "AI Recruiting Report",
])

PRO_FEATS = feat([
    "Everything in Starter",
    "25 Target Schools",
    "3 Email Sequences",
    "20 Social Posts/month",
    "N.I.K.K.I. SMS",
    "Priority Support",
])

ELITE_FEATS = feat([
    "Everything in Pro",
    "Unlimited Schools",
    "Unlimited Sequences",
    "Unlimited Social Posts",
    "Personal Onboarding Call",
    "SMS + Voice Outreach",
])

FEAT_LIST_STYLE = 'style="list-style:none;margin:0 0 24px;padding:0;text-align:left;"'

OLD_CARDS = """    <div class="pricing-cards">
      <div class="pricing-card fade-up">
        <div class="plan-name">Starter</div>
        <div class="plan-price">$39<span>/mo</span></div>
      </div>
      <div class="pricing-card popular fade-up" style="animation-delay:0.1s">
        <div class="popular-badge">MOST POPULAR</div>
        <div class="plan-name">Pro</div>
        <div class="plan-price">$59<span>/mo</span></div>
      </div>
      <div class="pricing-card fade-up" style="animation-delay:0.2s">
        <div class="plan-name">Elite</div>
        <div class="plan-price">$75<span>/mo</span></div>
      </div>
    </div>"""

NEW_CARDS = f"""    <div class="pricing-cards">
      <div class="pricing-card fade-up">
        <div class="plan-name">Starter</div>
        <div class="plan-price">$39<span>/mo</span></div>
        <ul {FEAT_LIST_STYLE}>
{STARTER_FEATS}
        </ul>
        <a href="https://www.nextplayrecruiting.app/pricing" class="btn btn-outline" style="width:100%;text-align:center;justify-content:center;">Get Started &#8594;</a>
      </div>
      <div class="pricing-card popular fade-up" style="animation-delay:0.1s">
        <div class="popular-badge">MOST POPULAR</div>
        <div class="plan-name">Pro</div>
        <div class="plan-price">$59<span>/mo</span></div>
        <ul {FEAT_LIST_STYLE}>
{PRO_FEATS}
        </ul>
        <a href="https://www.nextplayrecruiting.app/pricing" class="btn btn-primary" style="width:100%;text-align:center;justify-content:center;">Get Started &#8594;</a>
      </div>
      <div class="pricing-card fade-up" style="animation-delay:0.2s">
        <div class="plan-name">Elite</div>
        <div class="plan-price">$75<span>/mo</span></div>
        <ul {FEAT_LIST_STYLE}>
{ELITE_FEATS}
        </ul>
        <a href="https://www.nextplayrecruiting.app/pricing" class="btn btn-outline" style="width:100%;text-align:center;justify-content:center;">Get Started &#8594;</a>
      </div>
    </div>"""

assert OLD_CARDS in html, "pricing cards not found"
html = html.replace(OLD_CARDS, NEW_CARDS, 1)
changes.append("Added feature lists to all 3 pricing cards")

# ─────────────────────────────────────────────────────────────────────────────
# FIX 3 — Footer CTA: dark navy background instead of cyan gradient
# ─────────────────────────────────────────────────────────────────────────────
old_cta_css = """.footer-cta { padding: 84px 24px; background: linear-gradient(135deg, #0090c8 0%, #00AEEF 45%, #007fb5 100%); text-align: center; position: relative; overflow: hidden; }
    .footer-cta::before { content: ''; position: absolute; inset: 0; opacity: 0.5; background-image: radial-gradient(circle, rgba(255,255,255,0.06) 1px, transparent 1px); background-size: 28px 28px; pointer-events: none; }
    .footer-cta h2 { font-size: clamp(26px, 4.5vw, 48px); font-weight: 800; letter-spacing: -1px; color: #fff; margin-bottom: 12px; position: relative; }
    .footer-cta p { font-size: 17px; color: rgba(255,255,255,0.82); margin-bottom: 32px; position: relative; }"""

new_cta_css = """.footer-cta { padding: 84px 24px; background: #0a1628; border-top: 1px solid rgba(0,174,239,0.15); text-align: center; position: relative; overflow: hidden; }
    .footer-cta::before { content: ''; position: absolute; inset: 0; background: radial-gradient(ellipse 70% 60% at 50% 50%, rgba(0,174,239,0.07) 0%, transparent 70%); pointer-events: none; }
    .footer-cta h2 { font-size: clamp(26px, 4.5vw, 48px); font-weight: 800; letter-spacing: -1px; color: #fff; margin-bottom: 12px; position: relative; }
    .footer-cta p { font-size: 17px; color: rgba(255,255,255,0.55); margin-bottom: 32px; position: relative; }"""

assert old_cta_css in html, "footer-cta CSS not found"
html = html.replace(old_cta_css, new_cta_css, 1)
changes.append("Footer CTA: dark navy background with cyan radial glow")

# Also fix the button — was white on cyan, now should be cyan filled on dark
old_btn = '  <a href="https://www.nextplayrecruiting.app/signup" class="btn-cta-white">Get Started Free &#8594;</a>'
new_btn = '  <a href="https://www.nextplayrecruiting.app/signup" class="btn btn-primary" style="font-size:16px;padding:15px 36px;">Get Started Free &#8594;</a>'
assert old_btn in html, "footer CTA button not found"
html = html.replace(old_btn, new_btn, 1)
changes.append("Footer CTA button: switched to btn-primary (cyan) to match dark bg")

with open(r"C:\Users\rphil\nextplaystars-landing\index.html", "w", encoding="utf-8") as f:
    f.write(html)

import os
for c in changes:
    print("  OK:", c)
print(f"\nDone — {os.path.getsize(r'C:\Users\rphil\nextplaystars-landing\index.html') // 1024} KB")
