with open(r"C:\Users\rphil\nextplaystars-landing\index.html", "r", encoding="utf-8") as f:
    html = f.read()

mobile_fixes = [
    (".r1 { width: 130px; height: 130px; margin: -65px 0 0 -65px; }",
     ".r1 { width: 130px; height: 130px; transform: translate(-50%, -50%); }"),
    (".r2 { width: 168px; height: 168px; margin: -84px 0 0 -84px; }",
     ".r2 { width: 168px; height: 168px; transform: translate(-50%, -50%); }"),
    (".r3 { width: 205px; height: 205px; margin: -102.5px 0 0 -102.5px; }",
     ".r3 { width: 205px; height: 205px; transform: translate(-50%, -50%); }"),
    (".r4 { width: 240px; height: 240px; margin: -120px 0 0 -120px; }",
     ".r4 { width: 240px; height: 240px; transform: translate(-50%, -50%); }"),
]

for old, new in mobile_fixes:
    html = html.replace(old, new)
    print(f"Patched mobile: {new[:60]}")

with open(r"C:\Users\rphil\nextplaystars-landing\index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Done")
