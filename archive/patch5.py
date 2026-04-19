import re

with open(r"C:\Users\rphil\nextplaystars-landing\index.html", "r", encoding="utf-8") as f:
    html = f.read()

changes = []

# ─────────────────────────────────────────────────────────────────────────────
# FIX 1 — Logo: 240x56 -> 280x66, nav padding 20px -> 24px
# ─────────────────────────────────────────────────────────────────────────────

old = 'padding: 20px 28px;'
new = 'padding: 22px 28px;'
assert '.nav-inner' in html and old in html, "nav padding not found"
# Only replace inside the nav-inner rule
idx = html.index('.nav-inner {')
end = html.index('}', idx)
nav_rule = html[idx:end+1]
html = html[:idx] + nav_rule.replace(old, new) + html[end+1:]
changes.append("nav padding 20px -> 22px")

# Logo img dimensions - navbar logo is the first occurrence (240x56)
old_logo_attr = 'width="240" height="56" alt="NextPlay" style="display:block;object-fit:contain;"'
new_logo_attr = 'width="280" height="66" alt="NextPlay" style="display:block;object-fit:contain;"'
assert html.count(old_logo_attr) == 1, f"Expected 1 navbar logo, found {html.count(old_logo_attr)}"
html = html.replace(old_logo_attr, new_logo_attr)
changes.append("navbar logo 240x56 -> 280x66")

# ─────────────────────────────────────────────────────────────────────────────
# FIX 2 — Orb: enforce perfect centering
# ─────────────────────────────────────────────────────────────────────────────

# orb-wrap: confirm 380x380, add overflow:visible so rings don't clip
old = ".orb-wrap { position: relative; width: 380px; height: 380px; margin: 0 auto; perspective: 600px; transform-style: preserve-3d; }"
new = ".orb-wrap { position: relative; width: 380px; height: 380px; margin: 0 auto; perspective: 800px; transform-style: preserve-3d; overflow: visible; }"
assert old in html, "orb-wrap not found"
html = html.replace(old, new)
changes.append("orb-wrap: perspective 600->800, overflow:visible")

# orb-core: ensure exact centering with translate(-50%,-50%), add overflow:hidden for highlight
old = ".orb-core { position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%); width: 140px; height: 140px; border-radius: 50%; background: radial-gradient(circle at 30% 30%, #7ee8fa, #00AEEF 30%, #1a6fb8 60%, #0a1628 85%); box-shadow: 0 0 60px rgba(0,174,239,0.5), 0 0 120px rgba(0,174,239,0.2), inset 0 0 40px rgba(0,0,0,0.4); animation: orb-pulse 3s ease-in-out infinite; z-index: 5; }"
new = ".orb-core { position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%); width: 140px; height: 140px; border-radius: 50%; background: radial-gradient(circle at 30% 30%, #7ee8fa, #00AEEF 30%, #1a6fb8 60%, #0a1628 85%); box-shadow: 0 0 60px rgba(0,174,239,0.5), 0 0 120px rgba(0,174,239,0.2), inset 0 0 40px rgba(0,0,0,0.4); animation: orb-pulse 3s ease-in-out infinite; z-index: 5; overflow: hidden; }"
assert old in html, "orb-core not found"
html = html.replace(old, new)
changes.append("orb-core: overflow:hidden (clips highlight to sphere)")

# orb-ring base: remove top/left from base class - let the .rX classes own it entirely
# Also add width:0;height:0 so the base ring element itself is zero-sized at the center point
old = ".orb-ring { position: absolute; top: 50%; left: 50%; border-radius: 50%; transform-style: preserve-3d; }"
new = ".orb-ring { position: absolute; top: 50%; left: 50%; border-radius: 50%; transform-style: preserve-3d; width: 0; height: 0; }"
assert old in html, "orb-ring base not found"
html = html.replace(old, new)
changes.append("orb-ring base: width:0;height:0 — centering anchored at wrap midpoint")

# orb-ring-inner: make it position:absolute offset from center of the zero-size parent
# Since parent is 0x0 at 50%/50%, inner needs to be centered via its own translate
old = ".orb-ring-inner { border-radius: 50%; border-style: solid; border-color: transparent; position: relative; }"
new = ".orb-ring-inner { border-radius: 50%; border-style: solid; border-color: transparent; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); }"
assert old in html, "orb-ring-inner not found"
html = html.replace(old, new)
changes.append("orb-ring-inner: absolute + translate(-50%,-50%) for perfect centering")

# Remove translate(-50%,-50%) from .rX since zero-size parent + inner centering handles it
# .rX just needs the 3D tilt - the parent ring is at top:50%;left:50% = center of wrap
ring_replacements = [
    (".r1 { width: 190px; height: 190px; transform: translate(-50%, -50%) rotateX(75deg) rotateY(20deg); }",
     ".r1 { transform: rotateX(75deg) rotateY(20deg); }"),
    (".r2 { width: 245px; height: 245px; transform: translate(-50%, -50%) rotateX(45deg) rotateY(60deg); }",
     ".r2 { transform: rotateX(45deg) rotateY(60deg); }"),
    (".r3 { width: 295px; height: 295px; transform: translate(-50%, -50%) rotateX(15deg) rotateY(45deg); }",
     ".r3 { transform: rotateX(15deg) rotateY(45deg); }"),
    (".r4 { width: 380px; height: 380px; transform: translate(-50%, -50%) rotateX(60deg) rotateY(120deg); }",
     ".r4 { transform: rotateX(60deg) rotateY(120deg); }"),
]
for old_r, new_r in ring_replacements:
    assert old_r in html, f"Ring not found: {old_r[:50]}"
    html = html.replace(old_r, new_r)
changes.append("r1-r4: width/height moved to inner; only tilt on outer")

# orb-ring-inner widths stay on the .rX .orb-ring-inner rules — those are already correct
# Verify they're still there
for size in ["190px", "245px", "295px", "380px"]:
    assert f"width: {size}" in html, f"Missing ring inner size {size}"
changes.append("ring inner sizes confirmed present")

# Mobile overrides: simplify (no 3D on mobile)
# Already have: .r1 { width: 130px; height: 130px; transform: translate(-50%, -50%); }
# With new approach, mobile rings also need just the tilt (or none), inner handles centering
old_mob = "      .r1 { width: 130px; height: 130px; transform: translate(-50%, -50%); } .r1 .orb-ring-inner { width: 130px; height: 130px; }"
new_mob = "      .r1 { } .r1 .orb-ring-inner { width: 130px; height: 130px; }"
html = html.replace(old_mob, new_mob) if old_mob in html else html

old_mob = "      .r2 { width: 168px; height: 168px; transform: translate(-50%, -50%); } .r2 .orb-ring-inner { width: 168px; height: 168px; }"
new_mob = "      .r2 { } .r2 .orb-ring-inner { width: 168px; height: 168px; }"
html = html.replace(old_mob, new_mob) if old_mob in html else html

old_mob = "      .r3 { width: 205px; height: 205px; transform: translate(-50%, -50%); } .r3 .orb-ring-inner { width: 205px; height: 205px; }"
new_mob = "      .r3 { } .r3 .orb-ring-inner { width: 205px; height: 205px; }"
html = html.replace(old_mob, new_mob) if old_mob in html else html

old_mob = "      .r4 { width: 240px; height: 240px; transform: translate(-50%, -50%); } .r4 .orb-ring-inner { width: 240px; height: 240px; }"
new_mob = "      .r4 { } .r4 .orb-ring-inner { width: 240px; height: 240px; }"
html = html.replace(old_mob, new_mob) if old_mob in html else html

changes.append("mobile ring overrides simplified")

with open(r"C:\Users\rphil\nextplaystars-landing\index.html", "w", encoding="utf-8") as f:
    f.write(html)

import os
for c in changes:
    print("  OK:", c)
print(f"\nDone — {os.path.getsize(r'C:\Users\rphil\nextplaystars-landing\index.html') // 1024} KB")
