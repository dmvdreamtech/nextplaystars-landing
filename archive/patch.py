import base64, re

# --- 1. Encode NextPlay logo ---
with open(r"C:\Users\rphil\nextplay\public\images\nextplay-logo.png", "rb") as f:
    logo_b64 = base64.b64encode(f.read()).decode("ascii")

logo_img = (
    f'<img src="data:image/png;base64,{logo_b64}" '
    f'width="160" height="37" alt="NextPlay" style="display:block;object-fit:contain;" />'
)

with open(r"C:\Users\rphil\nextplaystars-landing\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# --- Fix 1: Navbar logo (nav-logo anchor text) ---
html = html.replace(
    '<a href="https://www.nextplayrecruiting.app" class="nav-logo">&#10022; NextPlay</a>',
    f'<a href="https://www.nextplayrecruiting.app" class="nav-logo" style="line-height:0;">{logo_img}</a>'
)

# Remove text-based nav-logo CSS so it doesn't add stray styles
html = html.replace(
    ".nav-logo { font-size: 22px; font-weight: 800; color: var(--cyan); text-decoration: none; letter-spacing: -0.5px; }",
    ".nav-logo { text-decoration: none; display: inline-flex; align-items: center; }"
)

# --- Fix 1b: Footer logo (span) ---
html = html.replace(
    '<span class="footer-logo">&#10022; NextPlay</span>',
    f'<a href="https://www.nextplayrecruiting.app" style="line-height:0;opacity:0.8;">{logo_img}</a>'
)
# Shrink footer logo size via inline override
html = html.replace(
    f'style="line-height:0;opacity:0.8;">{logo_img}',
    f'style="line-height:0;opacity:0.8;"><img src="data:image/png;base64,{logo_b64}" width="120" height="28" alt="NextPlay" style="display:block;object-fit:contain;" />'
)

# --- Fix 2: Feature emoji divs — add filter to make them white ---
# Add style to every <div class="feature-emoji"> element
html = html.replace(
    '<div class="feature-emoji">',
    '<div class="feature-emoji" style="filter:grayscale(1) brightness(10);">'
)

# --- Fix 3: Orb rings — replace negative-margin centering with transform: translate(-50%,-50%) ---
# Current: .r1 { width: 190px; height: 190px; margin: -95px 0 0 -95px; }
# New:     .r1 { width: 190px; height: 190px; transform: translate(-50%, -50%); }
ring_fixes = [
    (".r1 { width: 190px; height: 190px; margin: -95px 0 0 -95px; }",
     ".r1 { width: 190px; height: 190px; transform: translate(-50%, -50%); }"),
    (".r2 { width: 245px; height: 245px; margin: -122.5px 0 0 -122.5px; }",
     ".r2 { width: 245px; height: 245px; transform: translate(-50%, -50%); }"),
    (".r3 { width: 295px; height: 295px; margin: -147.5px 0 0 -147.5px; }",
     ".r3 { width: 295px; height: 295px; transform: translate(-50%, -50%); }"),
    (".r4 { width: 340px; height: 340px; margin: -170px 0 0 -170px; }",
     ".r4 { width: 340px; height: 340px; transform: translate(-50%, -50%); }"),
]
for old, new in ring_fixes:
    if old in html:
        html = html.replace(old, new)
        print(f"  Patched: {old[:50]}")
    else:
        print(f"  NOT FOUND: {old[:50]}")

# Also ensure orb-wrap is centered with margin: 0 auto
html = html.replace(
    ".orb-wrap { position: relative; width: 340px; height: 340px; }",
    ".orb-wrap { position: relative; width: 340px; height: 340px; margin: 0 auto; }"
)

# --- Write output ---
with open(r"C:\Users\rphil\nextplaystars-landing\index.html", "w", encoding="utf-8") as f:
    f.write(html)

import os
size_kb = os.path.getsize(r"C:\Users\rphil\nextplaystars-landing\index.html") // 1024
print(f"\nDone — {size_kb} KB written")
print("Logo embedded:", "nav-logo" in html and "data:image/png" in html)
print("Emoji filter applied:", 'filter:grayscale(1) brightness(10)' in html)
print("Orb translate(-50%,-50%):", "translate(-50%, -50%)" in html)
