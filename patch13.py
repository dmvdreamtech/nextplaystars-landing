with open(r"C:\Users\rphil\nextplaystars-landing\index.html", "r", encoding="utf-8") as f:
    html = f.read()

changes = []

# 1 — orb-wrap: overflow visible -> hidden (clips rings to 420px box)
old = ".orb-wrap { position: relative; width: 420px; height: 420px; margin: 0 auto; perspective: 800px; transform-style: preserve-3d; overflow: visible; z-index: 1; }"
new = ".orb-wrap { position: relative; width: 420px; height: 420px; margin: 0 auto; perspective: 800px; transform-style: preserve-3d; overflow: hidden; z-index: 1; }"
assert old in html, "orb-wrap CSS not found"
html = html.replace(old, new, 1)
changes.append("orb-wrap: overflow visible -> hidden")

# 2 — hero-right: add overflow:hidden to prevent ring bleed into other sections
old = ".hero-right { display: flex; flex-direction: column; align-items: center; justify-content: center; position: relative; }"
new = ".hero-right { display: flex; flex-direction: column; align-items: center; justify-content: center; position: relative; overflow: hidden; }"
assert old in html, "hero-right CSS not found"
html = html.replace(old, new, 1)
changes.append("hero-right: overflow hidden")

# 3 — hero-orb-btns: margin-top 32px -> 24px (keep reasonable spacing, already 32)
#     User wants 24px breathing room — update margin-top
old = ".hero-orb-btns { display: flex; flex-direction: column; align-items: center; gap: 12px; margin-top: 32px; position: relative; z-index: 10; }"
new = ".hero-orb-btns { display: flex; flex-direction: column; align-items: center; gap: 12px; margin-top: 24px; position: relative; z-index: 10; }"
assert old in html, "hero-orb-btns CSS not found"
html = html.replace(old, new, 1)
changes.append("hero-orb-btns: margin-top 32 -> 24px explicit breathing room")

with open(r"C:\Users\rphil\nextplaystars-landing\index.html", "w", encoding="utf-8") as f:
    f.write(html)

import os
for c in changes:
    print("  OK:", c)
print(f"\nDone — {os.path.getsize(r'C:\Users\rphil\nextplaystars-landing\index.html') // 1024} KB")
