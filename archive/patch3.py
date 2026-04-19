with open(r"C:\Users\rphil\nextplaystars-landing\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# ─────────────────────────────────────────────────────────────────────────────
# FIX 1 — Replace emoji feature-card divs with inline SVG icons
# ─────────────────────────────────────────────────────────────────────────────

SVG_WRAP = '<div class="feature-icon" style="margin-bottom:14px;line-height:0;">'

# Each icon: 32×32, stroke=white, fill=none, stroke-width=1.8
ICONS = {
    # 📞 Phone handset
    "phone": """<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 12 19.79 19.79 0 0 1 1.61 3.37 2 2 0 0 1 3.61 1.2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L7.91 8.91a16 16 0 0 0 6 6l.91-.91a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 21.73 16.92z"/></svg>""",

    # 📧 Envelope
    "envelope": """<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><polyline points="22,4 12,13 2,4"/></svg>""",

    # 📅 Calendar
    "calendar": """<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>""",

    # 🎯 Target / bullseye
    "target": """<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>""",

    # 📱 Mobile phone
    "mobile": """<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>""",

    # 📊 Bar chart
    "barchart": """<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/><line x1="2" y1="20" x2="22" y2="20"/></svg>""",
}

# Map old emoji HTML → new SVG
REPLACEMENTS = [
    (
        '<div class="feature-card fade-up"><div class="feature-emoji" style="filter:grayscale(1) brightness(10);">&#128222;</div><h3>Call or Text Nikki Anytime</h3></div>',
        f'<div class="feature-card fade-up">{SVG_WRAP}{ICONS["phone"]}</div><h3>Call or Text Nikki Anytime</h3></div>'
    ),
    (
        '<div class="feature-card fade-up" style="animation-delay:0.05s"><div class="feature-emoji" style="filter:grayscale(1) brightness(10);">&#128231;</div><h3>Automated Coach Email Sequences</h3></div>',
        f'<div class="feature-card fade-up" style="animation-delay:0.05s">{SVG_WRAP}{ICONS["envelope"]}</div><h3>Automated Coach Email Sequences</h3></div>'
    ),
    (
        '<div class="feature-card fade-up" style="animation-delay:0.1s"><div class="feature-emoji" style="filter:grayscale(1) brightness(10);">&#128197;</div><h3>Calendar &amp; Campus Visit Management</h3></div>',
        f'<div class="feature-card fade-up" style="animation-delay:0.1s">{SVG_WRAP}{ICONS["calendar"]}</div><h3>Calendar &amp; Campus Visit Management</h3></div>'
    ),
    (
        '<div class="feature-card fade-up" style="animation-delay:0.15s"><div class="feature-emoji" style="filter:grayscale(1) brightness(10);">&#127919;</div><h3>AI Recruiting Intelligence Report</h3></div>',
        f'<div class="feature-card fade-up" style="animation-delay:0.15s">{SVG_WRAP}{ICONS["target"]}</div><h3>AI Recruiting Intelligence Report</h3></div>'
    ),
    (
        '<div class="feature-card fade-up" style="animation-delay:0.2s"><div class="feature-emoji" style="filter:grayscale(1) brightness(10);">&#128241;</div><h3>Social Media Highlight Posts</h3></div>',
        f'<div class="feature-card fade-up" style="animation-delay:0.2s">{SVG_WRAP}{ICONS["mobile"]}</div><h3>Social Media Highlight Posts</h3></div>'
    ),
    (
        '<div class="feature-card fade-up" style="animation-delay:0.25s"><div class="feature-emoji" style="filter:grayscale(1) brightness(10);">&#128202;</div><h3>Target Schools Pipeline CRM</h3></div>',
        f'<div class="feature-card fade-up" style="animation-delay:0.25s">{SVG_WRAP}{ICONS["barchart"]}</div><h3>Target Schools Pipeline CRM</h3></div>'
    ),
]

for old, new in REPLACEMENTS:
    if old in html:
        html = html.replace(old, new)
        print(f"  SVG replaced for: {old[70:110].strip()}...")
    else:
        print(f"  NOT FOUND: {old[70:110].strip()}...")

# ─────────────────────────────────────────────────────────────────────────────
# FIX 2 — Orb: add perspective + preserve-3d to wrap; tilt each ring
# ─────────────────────────────────────────────────────────────────────────────

# Update .orb-wrap to add perspective + preserve-3d
html = html.replace(
    ".orb-wrap { position: relative; width: 340px; height: 340px; margin: 0 auto; }",
    ".orb-wrap { position: relative; width: 340px; height: 340px; margin: 0 auto; perspective: 600px; transform-style: preserve-3d; }"
)

# Update each ring to use translate(-50%,-50%) + rotateX/Y tilt
# The spin animation stays on orb-ring-inner; tilt is on .rX
ring_tilt_fixes = [
    (".r1 { width: 190px; height: 190px; transform: translate(-50%, -50%); }",
     ".r1 { width: 190px; height: 190px; transform: translate(-50%, -50%) rotateX(75deg) rotateY(20deg); }"),
    (".r2 { width: 245px; height: 245px; transform: translate(-50%, -50%); }",
     ".r2 { width: 245px; height: 245px; transform: translate(-50%, -50%) rotateX(45deg) rotateY(60deg); }"),
    (".r3 { width: 295px; height: 295px; transform: translate(-50%, -50%); }",
     ".r3 { width: 295px; height: 295px; transform: translate(-50%, -50%) rotateX(15deg) rotateY(45deg); }"),
    (".r4 { width: 340px; height: 340px; transform: translate(-50%, -50%); }",
     ".r4 { width: 340px; height: 340px; transform: translate(-50%, -50%) rotateX(60deg) rotateY(120deg); }"),
]

for old, new in ring_tilt_fixes:
    if old in html:
        html = html.replace(old, new)
        print(f"  Ring tilt applied: {new[5:60]}...")
    else:
        print(f"  NOT FOUND: {old[:60]}")

# Also add preserve-3d to orb-ring itself so tilts render in 3D
html = html.replace(
    ".orb-ring { position: absolute; top: 50%; left: 50%; border-radius: 50%; }",
    ".orb-ring { position: absolute; top: 50%; left: 50%; border-radius: 50%; transform-style: preserve-3d; }"
)

print("\nAll patches done.")

with open(r"C:\Users\rphil\nextplaystars-landing\index.html", "w", encoding="utf-8") as f:
    f.write(html)

import os
print(f"File size: {os.path.getsize(r'C:\Users\rphil\nextplaystars-landing\index.html') // 1024} KB")
