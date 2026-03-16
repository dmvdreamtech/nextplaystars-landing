import base64

with open(r"C:\Users\rphil\nextplaystars-landing\nikki-demo.mp3", "rb") as f:
    audio_b64 = base64.b64encode(f.read()).decode("ascii")

with open(r"C:\Users\rphil\nextplaystars-landing\index.html", "r", encoding="utf-8") as f:
    html = f.read()

changes = []

# ─────────────────────────────────────────────────────────────────────────────
# FIX 1 — Replace Call/Text Nikki buttons with Get Access signup button
# ─────────────────────────────────────────────────────────────────────────────

old_btns = '''      <div class="nikki-btns">
        <a href="tel:2409138592" class="btn btn-primary">&#128222; Call Nikki</a>
        <a href="sms:2409138592" class="btn btn-outline">&#128172; Text Nikki</a>
      </div>'''

new_btns = '''      <div class="nikki-btns">
        <a href="https://www.nextplayrecruiting.app/signup" class="btn btn-primary">Get Access to Nikki &#8594;</a>
        <p style="margin:10px 0 0 0;font-size:13px;color:rgba(255,255,255,0.45);letter-spacing:0.2px;">Exclusively for NextPlay members</p>
      </div>'''

assert old_btns in html, "nikki-btns not found"
html = html.replace(old_btns, new_btns, 1)
changes.append("Replaced Call/Text Nikki buttons with Get Access signup CTA")

# ─────────────────────────────────────────────────────────────────────────────
# FIX 2 — Replace the existing audio player (if present) with updated one,
#          or insert fresh if not present
# ─────────────────────────────────────────────────────────────────────────────

NEW_PLAYER = f'''      <!-- Nikki Voice Demo -->
      <div style="margin:0 0 28px 0;">
        <audio id="nikki-audio" src="data:audio/mpeg;base64,{audio_b64}" preload="auto"></audio>
        <button id="nikki-play-btn" onclick="(function(){{var a=document.getElementById('nikki-audio');var b=document.getElementById('nikki-play-btn');var l=document.getElementById('nikki-play-label');if(a.paused){{a.play();b.classList.add('playing');l.textContent='Playing...';a.onended=function(){{b.classList.remove('playing');l.textContent='Hear Nikki\u2019s voice \u2192';}}}}else{{a.pause();a.currentTime=0;b.classList.remove('playing');l.textContent='Hear Nikki\u2019s voice \u2192';}}}})()" style="display:inline-flex;align-items:center;gap:12px;background:transparent;border:1.5px solid rgba(0,174,239,0.5);border-radius:50px;padding:12px 24px;cursor:pointer;color:#00AEEF;font-size:15px;font-weight:600;letter-spacing:0.3px;transition:all 0.25s;" onmouseover="this.style.borderColor='rgba(0,174,239,0.9)';this.style.background='rgba(0,174,239,0.08)'" onmouseout="if(!this.classList.contains('playing')){{this.style.borderColor='rgba(0,174,239,0.5)';this.style.background='transparent'}}">
          <span style="position:relative;width:36px;height:36px;flex-shrink:0;">
            <span style="position:absolute;inset:0;border-radius:50%;background:rgba(0,174,239,0.15);animation:orb-pulse 2s ease-in-out infinite;"></span>
            <span style="position:absolute;inset:5px;border-radius:50%;background:#00AEEF;display:flex;align-items:center;justify-content:center;">
              <svg width="12" height="14" viewBox="0 0 12 14" fill="white"><polygon points="0,0 12,7 0,14"/></svg>
            </span>
          </span>
          <span id="nikki-play-label">Hear Nikki&#8217;s voice &#8594;</span>
        </button>
      </div>
      <!-- End Nikki Voice Demo -->
'''

OLD_PLAYER_START = "      <!-- Nikki Voice Demo -->"
OLD_PLAYER_END   = "      <!-- End Nikki Voice Demo -->"

if OLD_PLAYER_START in html and OLD_PLAYER_END in html:
    start_idx = html.index(OLD_PLAYER_START)
    end_idx   = html.index(OLD_PLAYER_END) + len(OLD_PLAYER_END) + 1  # +1 for \n
    html = html[:start_idx] + NEW_PLAYER + html[end_idx:]
    changes.append("Replaced existing audio player with updated audio + new base64")
else:
    # Insert above nikki-btns
    target = '      <div class="nikki-btns">'
    assert target in html, "nikki-btns target not found for insertion"
    html = html.replace(target, NEW_PLAYER + target, 1)
    changes.append("Inserted new audio player above nikki-btns")

with open(r"C:\Users\rphil\nextplaystars-landing\index.html", "w", encoding="utf-8") as f:
    f.write(html)

import os
for c in changes:
    print("  OK:", c)
print(f"\nDone — {os.path.getsize(r'C:\Users\rphil\nextplaystars-landing\index.html') // 1024} KB")
