with open(r"C:\Users\rphil\nextplaystars-landing\index.html", "r", encoding="utf-8") as f:
    html = f.read()

OLD_RIGHT = """    <!-- RIGHT: orb -->
    <div class="hero-right fade-up" style="animation-delay:0.18s">
      <div class="hero-orb-glow"></div>
      <div class="orb-wrap">
        <div class="orb-core"><div style="position:absolute;top:18%;left:20%;width:25%;height:18%;background:radial-gradient(ellipse,rgba(255,255,255,0.5),transparent);border-radius:50%;pointer-events:none;"></div></div>
        <div class="orb-ring r1"><div class="orb-ring-inner"></div></div>
        <div class="orb-ring r2"><div class="orb-ring-inner"></div></div>
        <div class="orb-ring r3"><div class="orb-ring-inner"></div></div>
        <div class="orb-ring r4"><div class="orb-ring-inner"></div></div>
      </div>
    </div>"""

NEW_RIGHT = """    <!-- RIGHT: orb + CTAs -->
    <div class="hero-right fade-up" style="animation-delay:0.18s">
      <div class="hero-orb-glow"></div>
      <div class="orb-wrap">
        <div class="orb-core"><div style="position:absolute;top:18%;left:20%;width:25%;height:18%;background:radial-gradient(ellipse,rgba(255,255,255,0.5),transparent);border-radius:50%;pointer-events:none;"></div></div>
        <div class="orb-ring r1"><div class="orb-ring-inner"></div></div>
        <div class="orb-ring r2"><div class="orb-ring-inner"></div></div>
        <div class="orb-ring r3"><div class="orb-ring-inner"></div></div>
        <div class="orb-ring r4"><div class="orb-ring-inner"></div></div>
      </div>
      <!-- Orb CTAs -->
      <div class="hero-orb-btns">
        <button id="hero-play-btn" onclick="(function(){var a=document.getElementById('nikki-audio');var b=document.getElementById('hero-play-btn');var l=document.getElementById('hero-play-label');if(!a){return;}if(a.paused){a.play();b.classList.add('playing');l.textContent='Playing...';a.onended=function(){b.classList.remove('playing');l.textContent='Hear Nikki\u2019s voice \u2192'};}else{a.pause();a.currentTime=0;b.classList.remove('playing');l.textContent='Hear Nikki\u2019s voice \u2192';}})()" class="btn btn-outline hero-play-btn-style">
          <span style="display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;border-radius:50%;background:rgba(0,174,239,0.15);flex-shrink:0;">
            <svg width="8" height="10" viewBox="0 0 8 10" fill="#00AEEF"><polygon points="0,0 8,5 0,10"/></svg>
          </span>
          <span id="hero-play-label">Hear Nikki&#8217;s voice &#8594;</span>
        </button>
        <a href="https://www.nextplayrecruiting.app/signup" class="btn btn-primary">Get Access to Nikki &#8594;</a>
      </div>
    </div>"""

assert OLD_RIGHT in html, "hero right column not found"
html = html.replace(OLD_RIGHT, NEW_RIGHT, 1)

# Add CSS for hero-orb-btns (insert before the closing </style>)
OLD_STYLE_END = """    .hero-orb-glow { position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%); width: 500px; height: 500px; border-radius: 50%; background: radial-gradient(ellipse, rgba(0,174,239,0.13) 0%, transparent 68%); pointer-events: none; }"""

NEW_STYLE_END = """    .hero-orb-glow { position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%); width: 500px; height: 500px; border-radius: 50%; background: radial-gradient(ellipse, rgba(0,174,239,0.13) 0%, transparent 68%); pointer-events: none; }
    .hero-orb-btns { display: flex; flex-direction: column; align-items: center; gap: 12px; margin-top: 36px; position: relative; z-index: 10; }
    .hero-play-btn-style { display: inline-flex; align-items: center; gap: 10px; }"""

assert OLD_STYLE_END in html, "hero-orb-glow CSS not found"
html = html.replace(OLD_STYLE_END, NEW_STYLE_END, 1)

with open(r"C:\Users\rphil\nextplaystars-landing\index.html", "w", encoding="utf-8") as f:
    f.write(html)

import os
print("  OK: Orb CTAs added to hero right column")
print(f"\nDone — {os.path.getsize(r'C:\Users\rphil\nextplaystars-landing\index.html') // 1024} KB")
