with open(r"C:\Users\rphil\nextplaystars-landing\index.html", "r", encoding="utf-8") as f:
    html = f.read()

changes = []

# 1 — Remove overflow:hidden from hero-right (was clipping the orb)
old = ".hero-right { display: flex; flex-direction: column; align-items: center; justify-content: center; position: relative; overflow: hidden; }"
new = ".hero-right { display: flex; flex-direction: column; align-items: center; justify-content: center; position: relative; min-width: 0; padding: 0 20px; }"
assert old in html, "hero-right CSS not found"
html = html.replace(old, new, 1)
changes.append("hero-right: removed overflow:hidden, added min-width:0 and padding")

# 2 — Remove overflow:hidden from orb-wrap (reverts to visible so 3D rings render properly)
old = ".orb-wrap { position: relative; width: 420px; height: 420px; margin: 0 auto; perspective: 800px; transform-style: preserve-3d; overflow: hidden; z-index: 1; }"
new = ".orb-wrap { position: relative; width: 360px; height: 360px; margin: 0 auto; perspective: 800px; transform-style: preserve-3d; overflow: visible; z-index: 1; }"
assert old in html, "orb-wrap CSS not found"
html = html.replace(old, new, 1)
changes.append("orb-wrap: 420->360px, overflow visible restored")

# 3 — Scale orb-core down to match 360px wrap (was 160px for 420px wrap -> ~137px for 360px)
old = ".orb-core { position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%); width: 160px; height: 160px;"
new = ".orb-core { position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%); width: 140px; height: 140px;"
assert old in html, "orb-core size not found"
html = html.replace(old, new, 1)
changes.append("orb-core: 160->140px")

# 4 — Scale r4 ring inner to match new 360px wrap
old = ".r4 .orb-ring-inner { width: 420px; height: 420px;"
new = ".r4 .orb-ring-inner { width: 360px; height: 360px;"
assert old in html, "r4 ring-inner not found"
html = html.replace(old, new, 1)
changes.append("r4 ring-inner: 420->360px")

# 5 — Resize hero-orb-glow to match smaller orb
old = ".hero-orb-glow { position: absolute; top: 0; left: 50%; transform: translateX(-50%); width: 520px; height: 520px; border-radius: 50%; background: radial-gradient(ellipse, rgba(0,174,239,0.15) 0%, transparent 68%); pointer-events: none; z-index: 0; }"
new = ".hero-orb-glow { position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%); width: 480px; height: 480px; border-radius: 50%; background: radial-gradient(ellipse, rgba(0,174,239,0.15) 0%, transparent 68%); pointer-events: none; z-index: 0; }"
assert old in html, "hero-orb-glow CSS not found"
html = html.replace(old, new, 1)
changes.append("hero-orb-glow: 520->480px, centered via translate")

# 6 — Mobile orb-wrap: 300->280px to match smaller desktop size
old = ".orb-wrap { width: 300px; height: 300px; }"
new = ".orb-wrap { width: 280px; height: 280px; }"
if old in html:
    html = html.replace(old, new, 1)
    changes.append("mobile orb-wrap: 300->280px")

with open(r"C:\Users\rphil\nextplaystars-landing\index.html", "w", encoding="utf-8") as f:
    f.write(html)

import os
for c in changes:
    print("  OK:", c)
print(f"\nDone — {os.path.getsize(r'C:\Users\rphil\nextplaystars-landing\index.html') // 1024} KB")
