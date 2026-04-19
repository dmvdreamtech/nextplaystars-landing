import base64, re

# --- Encode audio ---
with open(r"C:\Users\rphil\nextplaystars-landing\nikki-demo.mp3", "rb") as f:
    audio_b64 = base64.b64encode(f.read()).decode("ascii")

with open(r"C:\Users\rphil\nextplaystars-landing\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# --- Build the audio player HTML ---
# We'll insert it just before the "Get Access to Nikki" button inside the Nikki section.
# The button has distinctive text "Get Access to Nikki"
AUDIO_PLAYER = f"""      <!-- Nikki Voice Demo -->
      <div style="margin:0 0 28px 0;">
        <audio id="nikki-audio" src="data:audio/mpeg;base64,{audio_b64}" preload="auto"></audio>
        <button id="nikki-play-btn" onclick="(function(){{
          var audio=document.getElementById('nikki-audio');
          var btn=document.getElementById('nikki-play-btn');
          var label=document.getElementById('nikki-play-label');
          if(audio.paused){{
            audio.play();
            btn.classList.add('playing');
            label.textContent='Playing...';
            audio.onended=function(){{btn.classList.remove('playing');label.textContent='Hear Nikki\u2019s voice \u2192';}};
          }} else {{
            audio.pause();
            audio.currentTime=0;
            btn.classList.remove('playing');
            label.textContent='Hear Nikki\u2019s voice \u2192';
          }}
        }})()" style="display:inline-flex;align-items:center;gap:12px;background:transparent;border:1.5px solid rgba(0,174,239,0.5);border-radius:50px;padding:12px 24px;cursor:pointer;color:#00AEEF;font-size:15px;font-weight:600;letter-spacing:0.3px;transition:all 0.25s;" onmouseover="this.style.borderColor='rgba(0,174,239,0.9)';this.style.background='rgba(0,174,239,0.08)'" onmouseout="if(!this.classList.contains('playing')){{this.style.borderColor='rgba(0,174,239,0.5)';this.style.background='transparent'}}">
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
"""

# Insert audio player above the nikki-btns div
TARGET = '      <div class="nikki-btns">'
assert TARGET in html, "nikki-btns not found"
html = html.replace(TARGET, AUDIO_PLAYER + TARGET, 1)
print("Inserted audio player above nikki-btns")

with open(r"C:\Users\rphil\nextplaystars-landing\index.html", "w", encoding="utf-8") as f:
    f.write(html)

import os
print(f"\nDone — {os.path.getsize(r'C:\Users\rphil\nextplaystars-landing\index.html') // 1024} KB")
print("Audio embedded:", "nikki-audio" in html)
