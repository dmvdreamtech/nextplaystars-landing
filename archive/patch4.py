with open(r"C:\Users\rphil\nextplaystars-landing\index.html", "r", encoding="utf-8") as f:
    html = f.read()

changes = []

# ─────────────────────────────────────────────────────────────────────────────
# FIX 1 — NAVBAR: taller padding + larger logo
# ─────────────────────────────────────────────────────────────────────────────

# More padding in nav-inner
old = ".nav-inner { display: flex; align-items: center; justify-content: space-between; padding: 16px 28px; max-width: 1140px; margin: 0 auto; }"
new = ".nav-inner { display: flex; align-items: center; justify-content: space-between; padding: 20px 28px; max-width: 1140px; margin: 0 auto; }"
assert old in html, "nav-inner padding not found"
html = html.replace(old, new)
changes.append("nav-inner padding: 16px → 20px")

# Logo img: width 160→240, height 37→56  (there are 2 occurrences: navbar + footer)
# Navbar logo
old_logo = 'width="160" height="37" alt="NextPlay" style="display:block;object-fit:contain;"'
new_logo = 'width="240" height="56" alt="NextPlay" style="display:block;object-fit:contain;"'
count = html.count(old_logo)
assert count >= 1, f"logo img attr not found (found {count})"
# Only replace the first occurrence (navbar); footer uses width 120
html = html.replace(old_logo, new_logo, 1)
changes.append(f"navbar logo: 160×37 → 240×56 ({count} instance(s) found, replaced 1)")

# ─────────────────────────────────────────────────────────────────────────────
# FIX 2 — ORB: bigger core, 3D gradient, highlight, stronger rings, larger wrap
# ─────────────────────────────────────────────────────────────────────────────

# orb-wrap: 340px → 380px (desktop)
old = ".orb-wrap { position: relative; width: 340px; height: 340px; margin: 0 auto; perspective: 600px; transform-style: preserve-3d; }"
new = ".orb-wrap { position: relative; width: 380px; height: 380px; margin: 0 auto; perspective: 600px; transform-style: preserve-3d; }"
assert old in html, "orb-wrap CSS not found"
html = html.replace(old, new)
changes.append("orb-wrap: 340 → 380px")

# orb-core: 120px → 140px, new 3D gradient + shadow
old = ".orb-core { position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%); width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle at 38% 33%, rgba(0,215,255,0.95), rgba(0,174,239,0.6)); box-shadow: 0 0 60px rgba(0,174,239,0.7), 0 0 120px rgba(0,174,239,0.25); animation: orb-pulse 3s ease-in-out infinite; z-index: 5; }"
new = ".orb-core { position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%); width: 140px; height: 140px; border-radius: 50%; background: radial-gradient(circle at 30% 30%, #7ee8fa, #00AEEF 30%, #1a6fb8 60%, #0a1628 85%); box-shadow: 0 0 60px rgba(0,174,239,0.5), 0 0 120px rgba(0,174,239,0.2), inset 0 0 40px rgba(0,0,0,0.4); animation: orb-pulse 3s ease-in-out infinite; z-index: 5; }"
assert old in html, "orb-core CSS not found"
html = html.replace(old, new)
changes.append("orb-core: 120 → 140px + 3D gradient + richer shadow")

# Ring r1: boost opacity
old = ".r1 .orb-ring-inner { width: 190px; height: 190px; border-width: 1.5px; border-color: rgba(0,174,239,0.65); filter: drop-shadow(0 0 4px rgba(0,174,239,0.7)); animation: ring-spin 8s linear infinite; }"
new = ".r1 .orb-ring-inner { width: 190px; height: 190px; border-width: 1.5px; border-color: rgba(0,174,239,0.75); filter: drop-shadow(0 0 5px rgba(0,174,239,0.7)); animation: ring-spin 8s linear infinite; }"
assert old in html, "r1 inner not found"
html = html.replace(old, new)
changes.append("r1 ring opacity boosted")

old = ".r2 .orb-ring-inner { width: 245px; height: 245px; border-width: 1.5px; border-color: rgba(0,174,239,0.45); filter: drop-shadow(0 0 3px rgba(0,174,239,0.5)); animation: ring-spin-rev 12s linear infinite; }"
new = ".r2 .orb-ring-inner { width: 245px; height: 245px; border-width: 1.5px; border-color: rgba(0,174,239,0.65); filter: drop-shadow(0 0 5px rgba(0,174,239,0.6)); animation: ring-spin-rev 12s linear infinite; }"
assert old in html, "r2 inner not found"
html = html.replace(old, new)
changes.append("r2 ring opacity boosted")

old = ".r3 .orb-ring-inner { width: 295px; height: 295px; border-width: 1.5px; border-color: rgba(0,174,239,0.3); filter: drop-shadow(0 0 3px rgba(0,174,239,0.35)); animation: ring-spin 18s linear infinite; }"
new = ".r3 .orb-ring-inner { width: 295px; height: 295px; border-width: 1.5px; border-color: rgba(0,174,239,0.55); filter: drop-shadow(0 0 4px rgba(0,174,239,0.55)); animation: ring-spin 18s linear infinite; }"
assert old in html, "r3 inner not found"
html = html.replace(old, new)
changes.append("r3 ring opacity boosted")

old = ".r4 { width: 340px; height: 340px; transform: translate(-50%, -50%) rotateX(60deg) rotateY(120deg); }"
new = ".r4 { width: 380px; height: 380px; transform: translate(-50%, -50%) rotateX(60deg) rotateY(120deg); }"
assert old in html, "r4 CSS not found"
html = html.replace(old, new)

old = ".r4 .orb-ring-inner { width: 340px; height: 340px; border-width: 1px; border-color: rgba(0,174,239,0.18); filter: drop-shadow(0 0 2px rgba(0,174,239,0.2)); animation: ring-spin-rev 26s linear infinite; }"
new = ".r4 .orb-ring-inner { width: 380px; height: 380px; border-width: 1.5px; border-color: rgba(0,174,239,0.45); filter: drop-shadow(0 0 4px rgba(0,174,239,0.45)); animation: ring-spin-rev 26s linear infinite; }"
assert old in html, "r4 inner not found"
html = html.replace(old, new)
changes.append("r4: 340 → 380px + ring opacity boosted")

# Add highlight div + orb-core as sibling inside .orb-wrap HTML
old = '        <div class="orb-core"></div>'
new = ('        <div class="orb-core">'
       '<div style="position:absolute;top:18%;left:20%;width:25%;height:18%;'
       'background:radial-gradient(ellipse,rgba(255,255,255,0.5),transparent);'
       'border-radius:50%;pointer-events:none;"></div>'
       '</div>')
assert old in html, "orb-core HTML not found"
html = html.replace(old, new)
changes.append("highlight spot added inside orb-core")

# Mobile override: bump orb-wrap to 280px, core stays 80px
old = ".orb-container { min-height: 260px; } .orb-wrap { width: 240px; height: 240px; } .orb-core { width: 80px; height: 80px; }"
new = ".orb-container { min-height: 300px; } .orb-wrap { width: 280px; height: 280px; } .orb-core { width: 90px; height: 90px; }"
assert old in html, "mobile orb overrides not found"
html = html.replace(old, new)
changes.append("mobile orb-wrap: 240 → 280px")

with open(r"C:\Users\rphil\nextplaystars-landing\index.html", "w", encoding="utf-8") as f:
    f.write(html)

import os
print("\n".join(f"  ✓ {c}" for c in changes))
print(f"\nDone — {os.path.getsize(r'C:\Users\rphil\nextplaystars-landing\index.html') // 1024} KB")
