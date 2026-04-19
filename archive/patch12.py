with open(r"C:\Users\rphil\nextplaystars-landing\index.html", "r", encoding="utf-8") as f:
    html = f.read()

changes = []

# 1 — hero-right: add flex-direction:column so orb + buttons stack vertically
old = ".hero-right { display: flex; align-items: center; justify-content: center; position: relative; }"
new = ".hero-right { display: flex; flex-direction: column; align-items: center; justify-content: center; position: relative; }"
assert old in html, "hero-right CSS not found"
html = html.replace(old, new, 1)
changes.append("hero-right: flex-direction column")

# 2 — hero-orb-glow: stronger rgba(0,174,239,0.15)
old = ".hero-orb-glow { position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%); width: 500px; height: 500px; border-radius: 50%; background: radial-gradient(ellipse, rgba(0,174,239,0.13) 0%, transparent 68%); pointer-events: none; }"
new = ".hero-orb-glow { position: absolute; top: 0; left: 50%; transform: translateX(-50%); width: 520px; height: 520px; border-radius: 50%; background: radial-gradient(ellipse, rgba(0,174,239,0.15) 0%, transparent 68%); pointer-events: none; z-index: 0; }"
assert old in html, "hero-orb-glow CSS not found"
html = html.replace(old, new, 1)
changes.append("hero-orb-glow: rgba(0,174,239,0.15), positioned relative to orb")

# 3 — orb-wrap: 380px -> 420px
old = ".orb-wrap { position: relative; width: 380px; height: 380px; margin: 0 auto; perspective: 800px; transform-style: preserve-3d; overflow: visible; }"
new = ".orb-wrap { position: relative; width: 420px; height: 420px; margin: 0 auto; perspective: 800px; transform-style: preserve-3d; overflow: visible; z-index: 1; }"
assert old in html, "orb-wrap CSS not found"
html = html.replace(old, new, 1)
changes.append("orb-wrap: 380 -> 420px")

# 4 — orb-core: 140px -> 160px
old_core_start = ".orb-core { position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%); width: 140px; height: 140px;"
new_core_start = ".orb-core { position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%); width: 160px; height: 160px;"
assert old_core_start in html, "orb-core size not found"
html = html.replace(old_core_start, new_core_start, 1)
changes.append("orb-core: 140 -> 160px")

# 5 — hero-orb-btns: reduce margin-top since glow is now behind orb not absolute-center
old = ".hero-orb-btns { display: flex; flex-direction: column; align-items: center; gap: 12px; margin-top: 36px; position: relative; z-index: 10; }"
new = ".hero-orb-btns { display: flex; flex-direction: column; align-items: center; gap: 12px; margin-top: 32px; position: relative; z-index: 10; }"
assert old in html, "hero-orb-btns CSS not found"
html = html.replace(old, new, 1)
changes.append("hero-orb-btns: z-index confirmed above glow")

# 6 — Also update r4 ring size to match new 420px wrap (it was sized for 380px)
# r4 currently: width: 380px; height: 380px — bump to 420px
old_r4 = ".r4 { transform: rotateX(60deg) rotateY(120deg); }"
# r4 inner width
old_r4_inner_start = ".r4 .orb-ring-inner { width: 380px; height: 380px;"
new_r4_inner_start = ".r4 .orb-ring-inner { width: 420px; height: 420px;"
if old_r4_inner_start in html:
    html = html.replace(old_r4_inner_start, new_r4_inner_start, 1)
    changes.append("r4 ring-inner: 380 -> 420px")
else:
    changes.append("r4 ring-inner: already updated or not found, skipped")

# 7 — Mobile: update orb-wrap mobile override to match new 420px base
# Currently: .orb-wrap { width: 280px; height: 280px; }
# Keep mobile at 300px (scaled proportionally)
old_mob_orb = ".orb-wrap { width: 280px; height: 280px; }"
new_mob_orb = ".orb-wrap { width: 300px; height: 300px; }"
if old_mob_orb in html:
    html = html.replace(old_mob_orb, new_mob_orb, 1)
    changes.append("mobile orb-wrap: 280 -> 300px")

with open(r"C:\Users\rphil\nextplaystars-landing\index.html", "w", encoding="utf-8") as f:
    f.write(html)

import os
for c in changes:
    print("  OK:", c)
print(f"\nDone — {os.path.getsize(r'C:\Users\rphil\nextplaystars-landing\index.html') // 1024} KB")
