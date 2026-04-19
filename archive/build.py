import base64, os

photos = {
    "BATTER":  r"C:\Users\rphil\Downloads\DMV Dream 16u Elite 10_26_25___JAM0407.jpg",
    "EMMA":    r"C:\Users\rphil\Downloads\Emma.jpg",
    "JAM0103": r"C:\Users\rphil\Downloads\DMV Dream 16u Elite 10_26_25___JAM0103.jpg",
}

b64 = {}
for key, path in photos.items():
    with open(path, "rb") as f:
        b64[key] = base64.b64encode(f.read()).decode("ascii")

html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>NextPlay – AI Recruiting Assistant for Athletes</title>
  <meta name="description" content="Meet N.I.K.K.I., the AI voice assistant handling your entire college recruiting journey. Call or text anytime." />
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    :root {
      --navy: #0a1628; --navy2: #0f1e36; --navy3: #132240;
      --cyan: #00AEEF; --white: #ffffff;
      --muted: rgba(255,255,255,0.5); --border: rgba(255,255,255,0.07);
    }
    html { scroll-behavior: smooth; }
    body { background: var(--navy); color: var(--white); font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif; line-height: 1.6; overflow-x: hidden; }
    ::-webkit-scrollbar { width: 6px; } ::-webkit-scrollbar-track { background: var(--navy); } ::-webkit-scrollbar-thumb { background: var(--cyan); border-radius: 3px; }
    .container { max-width: 1140px; margin: 0 auto; padding: 0 24px; }
    .btn { display: inline-flex; align-items: center; gap: 8px; padding: 13px 28px; border-radius: 12px; font-weight: 600; font-size: 15px; cursor: pointer; border: none; text-decoration: none; transition: transform 0.15s, box-shadow 0.15s; }
    .btn:hover { transform: translateY(-2px); }
    .btn-primary { background: var(--cyan); color: #fff; box-shadow: 0 0 24px rgba(0,174,239,0.35); }
    .btn-primary:hover { box-shadow: 0 0 44px rgba(0,174,239,0.6); }
    .btn-outline { background: transparent; color: var(--cyan); border: 1.5px solid rgba(0,174,239,0.4); }
    .btn-outline:hover { border-color: var(--cyan); background: rgba(0,174,239,0.06); }

    /* Animations */
    @keyframes orb-pulse { 0%,100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(0,174,239,0.4), 0 0 60px rgba(0,174,239,0.3); } 50% { transform: scale(1.07); box-shadow: 0 0 0 28px rgba(0,174,239,0), 0 0 120px rgba(0,174,239,0.55); } }
    @keyframes ring-spin { to { transform: rotate(360deg); } }
    @keyframes ring-spin-rev { to { transform: rotate(-360deg); } }
    @keyframes fade-up { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }
    @keyframes glow-pulse { 0%,100% { text-shadow: 0 0 20px rgba(0,174,239,0.5); } 50% { text-shadow: 0 0 44px rgba(0,174,239,1), 0 0 90px rgba(0,174,239,0.35); } }
    @keyframes badge-float { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-5px); } }
    .fade-up { opacity: 0; }
    .fade-up.visible { animation: fade-up 0.65s ease forwards; }

    /* NAV */
    nav { position: fixed; top: 0; left: 0; right: 0; z-index: 100; background: rgba(10,22,40,0.88); backdrop-filter: blur(18px); -webkit-backdrop-filter: blur(18px); border-bottom: 1px solid var(--border); }
    .nav-inner { display: flex; align-items: center; justify-content: space-between; padding: 16px 28px; max-width: 1140px; margin: 0 auto; }
    .nav-logo { font-size: 22px; font-weight: 800; color: var(--cyan); text-decoration: none; letter-spacing: -0.5px; }
    .nav-links { display: flex; align-items: center; gap: 12px; }
    .nav-links .sign-in { color: rgba(255,255,255,0.7); text-decoration: none; font-size: 14px; font-weight: 500; padding: 8px 16px; border-radius: 8px; transition: color 0.15s; }
    .nav-links .sign-in:hover { color: #fff; }
    .nav-links .get-started { background: var(--cyan); color: #fff; text-decoration: none; font-size: 14px; font-weight: 600; padding: 9px 20px; border-radius: 10px; box-shadow: 0 0 20px rgba(0,174,239,0.3); transition: transform 0.15s, box-shadow 0.15s; }
    .nav-links .get-started:hover { transform: translateY(-1px); box-shadow: 0 0 32px rgba(0,174,239,0.55); }
    .hamburger { display: none; flex-direction: column; gap: 5px; cursor: pointer; padding: 4px; background: none; border: none; }
    .hamburger span { display: block; width: 24px; height: 2px; background: #fff; border-radius: 2px; transition: 0.2s; }
    .mobile-menu { display: none; flex-direction: column; gap: 10px; padding: 16px 28px 20px; border-top: 1px solid var(--border); background: rgba(10,22,40,0.98); }
    .mobile-menu a { color: var(--white); text-decoration: none; font-size: 16px; font-weight: 500; padding: 8px 0; }
    .mobile-menu .get-started { background: var(--cyan); text-align: center; padding: 12px 20px; border-radius: 10px; margin-top: 4px; }
    .mobile-menu.open { display: flex; }

    /* HERO */
    .hero { min-height: 100vh; display: flex; align-items: center; padding: 120px 24px 80px; position: relative; overflow: hidden; }
    .hero-bg { position: absolute; inset: 0; background: radial-gradient(ellipse 55% 65% at 72% 50%, rgba(0,174,239,0.08) 0%, transparent 65%), radial-gradient(ellipse 35% 40% at 15% 85%, rgba(0,174,239,0.04) 0%, transparent 60%); pointer-events: none; }
    .hero-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 64px; align-items: center; max-width: 1140px; margin: 0 auto; position: relative; z-index: 1; width: 100%; }
    .hero-badge { display: inline-flex; align-items: center; gap: 8px; padding: 7px 16px; border-radius: 100px; border: 1px solid rgba(0,174,239,0.3); background: rgba(0,174,239,0.06); font-size: 11px; font-weight: 700; letter-spacing: 1.5px; color: var(--cyan); text-transform: uppercase; margin-bottom: 22px; animation: badge-float 3s ease-in-out infinite; }
    .hero-badge-dot { width: 6px; height: 6px; border-radius: 50%; background: var(--cyan); display: inline-block; }
    .hero h1 { font-size: clamp(34px, 4.5vw, 56px); font-weight: 800; line-height: 1.1; margin-bottom: 20px; letter-spacing: -1.5px; }
    .hero h1 em { font-style: normal; background: linear-gradient(135deg, #00AEEF 0%, #a78bfa 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
    .hero-sub { font-size: 17px; color: var(--muted); line-height: 1.7; margin-bottom: 36px; max-width: 460px; }
    .hero-btns { display: flex; gap: 14px; flex-wrap: wrap; }
    .hero-photo { border-radius: 24px; overflow: hidden; border: 1px solid rgba(0,174,239,0.15); box-shadow: 0 32px 80px rgba(0,0,0,0.5), 0 0 60px rgba(0,174,239,0.07); }
    .hero-photo img { width: 100%; height: 520px; object-fit: cover; object-position: center top; display: block; }

    /* WHAT */
    .what-section { padding: 100px 24px; background: linear-gradient(180deg, var(--navy) 0%, var(--navy2) 100%); }
    .what-card { max-width: 840px; margin: 0 auto; text-align: center; }
    .section-label { font-size: 11px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: var(--cyan); margin-bottom: 14px; }
    .what-card h2 { font-size: clamp(26px, 3.8vw, 42px); font-weight: 800; letter-spacing: -1px; line-height: 1.15; margin-bottom: 20px; }
    .what-card p { font-size: 17px; color: var(--muted); line-height: 1.75; margin-bottom: 48px; }
    .stat-row { display: flex; border: 1px solid var(--border); border-radius: 16px; overflow: hidden; background: var(--navy3); }
    .stat-item { flex: 1; padding: 28px 20px; text-align: center; border-right: 1px solid var(--border); }
    .stat-item:last-child { border-right: none; }
    .stat-num { font-size: 32px; font-weight: 800; color: var(--cyan); letter-spacing: -1px; display: block; margin-bottom: 4px; }
    .stat-label { font-size: 13px; color: var(--muted); font-weight: 500; }

    /* NIKKI */
    .nikki-section { padding: 100px 24px; background: var(--navy2); position: relative; overflow: hidden; }
    .nikki-section::before { content: ''; position: absolute; inset: 0; background: radial-gradient(ellipse 50% 60% at 25% 50%, rgba(0,174,239,0.05) 0%, transparent 60%); pointer-events: none; }
    .nikki-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: center; max-width: 1140px; margin: 0 auto; position: relative; z-index: 1; }
    .orb-container { display: flex; align-items: center; justify-content: center; min-height: 420px; }
    .orb-wrap { position: relative; width: 340px; height: 340px; }
    .orb-core { position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%); width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle at 38% 33%, rgba(0,215,255,0.95), rgba(0,174,239,0.6)); box-shadow: 0 0 60px rgba(0,174,239,0.7), 0 0 120px rgba(0,174,239,0.25); animation: orb-pulse 3s ease-in-out infinite; z-index: 5; }
    .orb-ring { position: absolute; top: 50%; left: 50%; border-radius: 50%; }
    .orb-ring-inner { border-radius: 50%; border-style: solid; border-color: transparent; position: relative; }
    .orb-ring-inner::before { content: ''; position: absolute; width: 8px; height: 8px; background: var(--cyan); border-radius: 50%; box-shadow: 0 0 10px var(--cyan), 0 0 22px rgba(0,174,239,0.7); top: -4px; left: 50%; transform: translateX(-50%); }
    .r1 { width: 190px; height: 190px; margin: -95px 0 0 -95px; }
    .r1 .orb-ring-inner { width: 190px; height: 190px; border-width: 1.5px; border-color: rgba(0,174,239,0.65); filter: drop-shadow(0 0 4px rgba(0,174,239,0.7)); animation: ring-spin 8s linear infinite; }
    .r2 { width: 245px; height: 245px; margin: -122.5px 0 0 -122.5px; }
    .r2 .orb-ring-inner { width: 245px; height: 245px; border-width: 1.5px; border-color: rgba(0,174,239,0.45); filter: drop-shadow(0 0 3px rgba(0,174,239,0.5)); animation: ring-spin-rev 12s linear infinite; }
    .r3 { width: 295px; height: 295px; margin: -147.5px 0 0 -147.5px; }
    .r3 .orb-ring-inner { width: 295px; height: 295px; border-width: 1.5px; border-color: rgba(0,174,239,0.3); filter: drop-shadow(0 0 3px rgba(0,174,239,0.35)); animation: ring-spin 18s linear infinite; }
    .r4 { width: 340px; height: 340px; margin: -170px 0 0 -170px; }
    .r4 .orb-ring-inner { width: 340px; height: 340px; border-width: 1px; border-color: rgba(0,174,239,0.18); filter: drop-shadow(0 0 2px rgba(0,174,239,0.2)); animation: ring-spin-rev 26s linear infinite; }
    .nikki-content h2 { font-size: clamp(52px, 7vw, 76px); font-weight: 900; letter-spacing: -2px; color: var(--cyan); margin-bottom: 6px; animation: glow-pulse 3s ease-in-out infinite; }
    .nikki-full { font-size: 13px; font-weight: 600; letter-spacing: 0.5px; color: rgba(0,174,239,0.6); margin-bottom: 24px; line-height: 1.5; }
    .nikki-content > p { font-size: 17px; color: var(--muted); line-height: 1.75; margin-bottom: 32px; }
    .nikki-btns { display: flex; gap: 14px; flex-wrap: wrap; }

    /* HOW */
    .how-section { padding: 100px 24px; background: var(--navy); }
    .how-section h2 { font-size: clamp(26px, 3.8vw, 42px); font-weight: 800; letter-spacing: -1px; text-align: center; margin-bottom: 56px; }
    .steps-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; max-width: 960px; margin: 0 auto; }
    .step-card { background: var(--navy2); border: 1px solid var(--border); border-radius: 20px; padding: 36px 28px; transition: border-color 0.2s, transform 0.2s; }
    .step-card:hover { border-color: rgba(0,174,239,0.3); transform: translateY(-4px); }
    .step-num { font-size: 48px; font-weight: 900; color: rgba(0,174,239,0.14); line-height: 1; margin-bottom: 14px; letter-spacing: -2px; }
    .step-icon { font-size: 28px; margin-bottom: 12px; }
    .step-card h3 { font-size: 18px; font-weight: 700; margin-bottom: 10px; }
    .step-card p { font-size: 14px; color: var(--muted); line-height: 1.65; }

    /* FEATURES */
    .features-section { padding: 100px 24px; background: var(--navy2); }
    .features-section h2 { font-size: clamp(26px, 3.8vw, 42px); font-weight: 800; letter-spacing: -1px; text-align: center; margin-bottom: 52px; }
    .features-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; max-width: 1000px; margin: 0 auto; }
    .feature-card { background: var(--navy3); border: 1px solid var(--border); border-radius: 18px; padding: 28px 24px; transition: border-color 0.2s, transform 0.2s, box-shadow 0.2s; }
    .feature-card:hover { border-color: rgba(0,174,239,0.28); transform: translateY(-3px); box-shadow: 0 14px 36px rgba(0,0,0,0.3); }
    .feature-emoji { font-size: 28px; margin-bottom: 12px; }
    .feature-card h3 { font-size: 16px; font-weight: 700; line-height: 1.3; }

    /* PHOTOS */
    .photos-section { padding: 80px 24px; background: var(--navy); }
    .photos-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; max-width: 1100px; margin: 0 auto 24px; }
    .photo-frame { border-radius: 18px; overflow: hidden; border: 1px solid rgba(0,174,239,0.1); box-shadow: 0 16px 48px rgba(0,0,0,0.4); transition: transform 0.25s, box-shadow 0.25s; height: 320px; }
    .photo-frame:hover { transform: translateY(-5px); box-shadow: 0 28px 70px rgba(0,0,0,0.55), 0 0 36px rgba(0,174,239,0.07); }
    .photo-frame img { width: 100%; height: 100%; object-fit: cover; object-position: center top; display: block; }
    .photos-caption { text-align: center; color: var(--muted); font-size: 14px; }
    .photos-caption strong { color: rgba(255,255,255,0.75); }

    /* PRICING */
    .pricing-section { padding: 100px 24px; background: var(--navy2); }
    .pricing-section h2 { font-size: clamp(26px, 3.8vw, 42px); font-weight: 800; letter-spacing: -1px; text-align: center; margin-bottom: 8px; }
    .pricing-sub { text-align: center; color: var(--muted); font-size: 15px; margin-bottom: 16px; }
    .pricing-dmv { text-align: center; margin-bottom: 44px; }
    .pricing-dmv span { display: inline-block; background: rgba(0,174,239,0.08); border: 1px solid rgba(0,174,239,0.25); color: var(--cyan); font-size: 13px; font-weight: 600; padding: 8px 20px; border-radius: 100px; }
    .pricing-cards { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; max-width: 840px; margin: 0 auto 40px; }
    .pricing-card { background: var(--navy3); border: 1px solid var(--border); border-radius: 20px; padding: 32px 24px; text-align: center; transition: border-color 0.2s, transform 0.2s; position: relative; }
    .pricing-card.popular { border-color: rgba(0,174,239,0.35); background: linear-gradient(135deg, rgba(0,174,239,0.07) 0%, transparent 100%); box-shadow: 0 0 40px rgba(0,174,239,0.08); }
    .pricing-card:hover { transform: translateY(-3px); }
    .popular-badge { position: absolute; top: -13px; left: 50%; transform: translateX(-50%); background: var(--cyan); color: #fff; font-size: 11px; font-weight: 700; letter-spacing: 1px; padding: 4px 14px; border-radius: 100px; white-space: nowrap; }
    .plan-name { font-size: 12px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: var(--muted); margin-bottom: 12px; }
    .plan-price { font-size: 40px; font-weight: 800; letter-spacing: -2px; }
    .plan-price span { font-size: 15px; font-weight: 400; color: var(--muted); }
    .pricing-trial { text-align: center; color: var(--muted); font-size: 13px; margin-bottom: 36px; }
    .pricing-cta { text-align: center; }

    /* FOOTER CTA */
    .footer-cta { padding: 84px 24px; background: linear-gradient(135deg, #0090c8 0%, #00AEEF 45%, #007fb5 100%); text-align: center; position: relative; overflow: hidden; }
    .footer-cta::before { content: ''; position: absolute; inset: 0; opacity: 0.5; background-image: radial-gradient(circle, rgba(255,255,255,0.06) 1px, transparent 1px); background-size: 28px 28px; pointer-events: none; }
    .footer-cta h2 { font-size: clamp(26px, 4.5vw, 48px); font-weight: 800; letter-spacing: -1px; color: #fff; margin-bottom: 12px; position: relative; }
    .footer-cta p { font-size: 17px; color: rgba(255,255,255,0.82); margin-bottom: 32px; position: relative; }
    .btn-cta-white { background: #fff; color: #007fb5; font-size: 16px; font-weight: 700; padding: 16px 36px; border-radius: 14px; box-shadow: 0 8px 32px rgba(0,0,0,0.2); display: inline-flex; align-items: center; gap: 8px; text-decoration: none; transition: transform 0.15s, box-shadow 0.15s; position: relative; }
    .btn-cta-white:hover { transform: translateY(-2px); box-shadow: 0 14px 44px rgba(0,0,0,0.28); }

    /* FOOTER */
    footer { padding: 36px 24px; background: #060e1c; border-top: 1px solid var(--border); }
    .footer-inner { max-width: 1140px; margin: 0 auto; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 16px; }
    .footer-logo { font-size: 18px; font-weight: 800; color: var(--cyan); }
    .footer-copy { font-size: 13px; color: rgba(255,255,255,0.28); }
    .footer-links { display: flex; gap: 20px; }
    .footer-links a { font-size: 13px; color: rgba(255,255,255,0.38); text-decoration: none; transition: color 0.15s; }
    .footer-links a:hover { color: var(--cyan); }

    /* RESPONSIVE */
    @media (max-width: 768px) {
      .nav-links { display: none; } .hamburger { display: flex; }
      .hero { padding: 96px 20px 60px; }
      .hero-grid { grid-template-columns: 1fr; gap: 36px; }
      .hero-photo { order: -1; } .hero-photo img { height: 280px; }
      .hero-btns { justify-content: center; }
      .hero-content { text-align: center; } .hero-badge { margin: 0 auto 20px; } .hero-sub { margin: 0 auto 28px; }
      .stat-row { flex-direction: column; border: none; gap: 8px; }
      .stat-item { border-right: none !important; border: 1px solid var(--border); border-radius: 12px; }
      .nikki-grid { grid-template-columns: 1fr; gap: 48px; }
      .orb-container { min-height: 260px; } .orb-wrap { width: 240px; height: 240px; } .orb-core { width: 80px; height: 80px; }
      .r1 { width: 130px; height: 130px; margin: -65px 0 0 -65px; } .r1 .orb-ring-inner { width: 130px; height: 130px; }
      .r2 { width: 168px; height: 168px; margin: -84px 0 0 -84px; } .r2 .orb-ring-inner { width: 168px; height: 168px; }
      .r3 { width: 205px; height: 205px; margin: -102.5px 0 0 -102.5px; } .r3 .orb-ring-inner { width: 205px; height: 205px; }
      .r4 { width: 240px; height: 240px; margin: -120px 0 0 -120px; } .r4 .orb-ring-inner { width: 240px; height: 240px; }
      .nikki-content { text-align: center; } .nikki-btns { justify-content: center; }
      .steps-grid { grid-template-columns: 1fr; gap: 16px; }
      .features-grid { grid-template-columns: repeat(2, 1fr); }
      .photos-grid { grid-template-columns: 1fr; } .photo-frame { height: 250px; }
      .pricing-cards { grid-template-columns: 1fr; max-width: 380px; margin: 0 auto 40px; }
      .footer-inner { flex-direction: column; text-align: center; align-items: center; }
    }
    @media (max-width: 480px) { .features-grid { grid-template-columns: 1fr; } }
  </style>
</head>
<body>

<!-- NAV -->
<nav>
  <div class="nav-inner">
    <a href="https://www.nextplayrecruiting.app" class="nav-logo">&#10022; NextPlay</a>
    <div class="nav-links">
      <a href="https://www.nextplayrecruiting.app" class="sign-in">Sign In</a>
      <a href="https://www.nextplayrecruiting.app" class="get-started">Get Started</a>
    </div>
    <button class="hamburger" id="hamburger" aria-label="Toggle menu">
      <span></span><span></span><span></span>
    </button>
  </div>
  <div class="mobile-menu" id="mobileMenu">
    <a href="#about">About</a>
    <a href="#nikki">Meet Nikki</a>
    <a href="#how">How It Works</a>
    <a href="#pricing">Pricing</a>
    <a href="https://www.nextplayrecruiting.app" style="color:rgba(255,255,255,0.6);">Sign In</a>
    <a href="https://www.nextplayrecruiting.app" class="get-started">Get Started &#8594;</a>
  </div>
</nav>

<!-- HERO -->
<section class="hero" id="hero">
  <div class="hero-bg"></div>
  <div class="hero-grid">
    <div class="hero-content fade-up">
      <div class="hero-badge"><span class="hero-badge-dot"></span> AI-Powered &nbsp;&middot;&nbsp; Athlete-Driven</div>
      <h1>Your Athlete&#8217;s Recruiting Assistant <em>is Ready.</em></h1>
      <p class="hero-sub">Meet N.I.K.K.I. &#8212; the AI voice assistant that handles your entire recruiting journey so you can focus on the game.</p>
      <div class="hero-btns">
        <a href="#nikki" class="btn btn-primary">Meet Nikki &#8594;</a>
        <a href="#how" class="btn btn-outline">See How It Works</a>
      </div>
    </div>
    <div class="hero-photo fade-up" style="animation-delay:0.15s">
      <img src="data:image/jpeg;base64,BATTER_PLACEHOLDER" alt="DMV Dream athlete at the plate" loading="eager" />
    </div>
  </div>
</section>

<!-- WHAT IS NEXTPLAY -->
<section class="what-section" id="about">
  <div class="what-card fade-up">
    <p class="section-label">What is NextPlay</p>
    <h2>Recruiting used to take a village.<br>Now it just takes one call.</h2>
    <p>NextPlay is an AI-powered recruiting platform built specifically for student-athletes and their families. We combine intelligent outreach, calendar management, and real-time coaching insights into one seamless experience &#8212; with N.I.K.K.I. as your always-on recruiting assistant available by phone, text, or app. Whether you&#8217;re targeting D1, D2, or D3 programs, NextPlay puts a full recruiting operation in your pocket.</p>
    <div class="stat-row">
      <div class="stat-item"><span class="stat-num">50+</span><span class="stat-label">Families</span></div>
      <div class="stat-item"><span class="stat-num">3</span><span class="stat-label">Division Levels</span></div>
      <div class="stat-item"><span class="stat-num">1</span><span class="stat-label">AI Assistant</span></div>
    </div>
  </div>
</section>

<!-- MEET N.I.K.K.I. -->
<section class="nikki-section" id="nikki">
  <div class="nikki-grid">
    <div class="orb-container fade-up">
      <div class="orb-wrap">
        <div class="orb-core"></div>
        <div class="orb-ring r1"><div class="orb-ring-inner"></div></div>
        <div class="orb-ring r2"><div class="orb-ring-inner"></div></div>
        <div class="orb-ring r3"><div class="orb-ring-inner"></div></div>
        <div class="orb-ring r4"><div class="orb-ring-inner"></div></div>
      </div>
    </div>
    <div class="nikki-content fade-up" style="animation-delay:0.12s">
      <h2>N.I.K.K.I.</h2>
      <p class="nikki-full">Neurally Integrated Knowledge &amp; Kinetics Intelligence</p>
      <p>Call or text Nikki at any time. She knows your athlete&#8217;s full profile, manages your calendar, sends coach emails, and guides your family through every step of the recruiting process &#8212; 24/7, from anywhere.</p>
      <div class="nikki-btns">
        <a href="tel:2409138592" class="btn btn-primary">&#128222; Call Nikki</a>
        <a href="sms:2409138592" class="btn btn-outline">&#128172; Text Nikki</a>
      </div>
    </div>
  </div>
</section>

<!-- HOW IT WORKS -->
<section class="how-section" id="how">
  <div class="container">
    <p class="section-label" style="text-align:center">How It Works</p>
    <h2>Three steps to get recruited.</h2>
    <div class="steps-grid">
      <div class="step-card fade-up">
        <div class="step-num">01</div>
        <div class="step-icon">&#127942;</div>
        <h3>Build Your Profile</h3>
        <p>Set up your athlete&#8217;s stats, GPA, target schools, and graduation year. Nikki learns everything about your recruiting goals in minutes.</p>
      </div>
      <div class="step-card fade-up" style="animation-delay:0.1s">
        <div class="step-num">02</div>
        <div class="step-icon">&#9889;</div>
        <h3>Nikki Goes to Work</h3>
        <p>She sends personalized coach emails, manages your calendar, tracks responses automatically, and follows up at exactly the right time.</p>
      </div>
      <div class="step-card fade-up" style="animation-delay:0.2s">
        <div class="step-num">03</div>
        <div class="step-icon">&#127919;</div>
        <h3>Get Recruited</h3>
        <p>Follow your pipeline, approve emails before they send, and let Nikki handle the rest. You play &#8212; she recruits.</p>
      </div>
    </div>
  </div>
</section>

<!-- FEATURES -->
<section class="features-section" id="features">
  <div class="container">
    <p class="section-label" style="text-align:center">Everything You Need</p>
    <h2>Built for the whole journey.</h2>
    <div class="features-grid">
      <div class="feature-card fade-up"><div class="feature-emoji">&#128222;</div><h3>Call or Text Nikki Anytime</h3></div>
      <div class="feature-card fade-up" style="animation-delay:0.05s"><div class="feature-emoji">&#128231;</div><h3>Automated Coach Email Sequences</h3></div>
      <div class="feature-card fade-up" style="animation-delay:0.1s"><div class="feature-emoji">&#128197;</div><h3>Calendar &amp; Campus Visit Management</h3></div>
      <div class="feature-card fade-up" style="animation-delay:0.15s"><div class="feature-emoji">&#127919;</div><h3>AI Recruiting Intelligence Report</h3></div>
      <div class="feature-card fade-up" style="animation-delay:0.2s"><div class="feature-emoji">&#128241;</div><h3>Social Media Highlight Posts</h3></div>
      <div class="feature-card fade-up" style="animation-delay:0.25s"><div class="feature-emoji">&#128202;</div><h3>Target Schools Pipeline CRM</h3></div>
    </div>
  </div>
</section>

<!-- PHOTOS -->
<section class="photos-section">
  <div class="container">
    <div class="photos-grid">
      <div class="photo-frame fade-up">
        <img src="data:image/jpeg;base64,BATTER_PLACEHOLDER" alt="DMV Dream athlete at bat" loading="lazy" />
      </div>
      <div class="photo-frame fade-up" style="animation-delay:0.12s">
        <img src="data:image/jpeg;base64,EMMA_PLACEHOLDER" alt="Emma at a college campus visit" loading="lazy" />
      </div>
      <div class="photo-frame fade-up" style="animation-delay:0.24s">
        <img src="data:image/jpeg;base64,JAM0103_PLACEHOLDER" alt="DMV Dream athlete fielding" loading="lazy" />
      </div>
    </div>
    <p class="photos-caption">Built for athletes like these. <strong>DMV Dream Athletics</strong> &#8212; NextPlay&#8217;s founding families.</p>
  </div>
</section>

<!-- PRICING -->
<section class="pricing-section" id="pricing">
  <div class="container">
    <p class="section-label" style="text-align:center">Pricing</p>
    <h2>Simple pricing. No surprises.</h2>
    <p class="pricing-sub">2-day free trial &#183; No credit card required</p>
    <div class="pricing-dmv">
      <span>&#127881; DMV Dream families get 30 days free with code <strong>DMVDREAM</strong></span>
    </div>
    <div class="pricing-cards">
      <div class="pricing-card fade-up">
        <div class="plan-name">Starter</div>
        <div class="plan-price">$39<span>/mo</span></div>
      </div>
      <div class="pricing-card popular fade-up" style="animation-delay:0.1s">
        <div class="popular-badge">MOST POPULAR</div>
        <div class="plan-name">Pro</div>
        <div class="plan-price">$59<span>/mo</span></div>
      </div>
      <div class="pricing-card fade-up" style="animation-delay:0.2s">
        <div class="plan-name">Elite</div>
        <div class="plan-price">$75<span>/mo</span></div>
      </div>
    </div>
    <p class="pricing-trial">All plans include a free trial. Cancel anytime from your billing page.</p>
    <div class="pricing-cta">
      <a href="https://www.nextplayrecruiting.app/pricing" class="btn btn-primary" style="font-size:16px;padding:15px 36px;">Start Free Trial &#8594;</a>
    </div>
  </div>
</section>

<!-- FOOTER CTA -->
<section class="footer-cta">
  <h2>Your athlete&#8217;s journey starts now.</h2>
  <p>Join families across the DMV who are recruiting smarter with NextPlay.</p>
  <a href="https://www.nextplayrecruiting.app/signup" class="btn-cta-white">Get Started Free &#8594;</a>
</section>

<!-- FOOTER -->
<footer>
  <div class="footer-inner">
    <span class="footer-logo">&#10022; NextPlay</span>
    <span class="footer-copy">&copy; 2025 NextPlay Recruiting. All rights reserved.</span>
    <div class="footer-links">
      <a href="https://www.nextplayrecruiting.app/privacy">Privacy Policy</a>
      <a href="https://www.nextplayrecruiting.app/terms">Terms</a>
    </div>
  </div>
</footer>

<script>
  const hamburger = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobileMenu');
  hamburger.addEventListener('click', () => mobileMenu.classList.toggle('open'));
  mobileMenu.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', () => mobileMenu.classList.remove('open'));
  });
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('visible'); observer.unobserve(e.target); }
    });
  }, { threshold: 0.1 });
  document.querySelectorAll('.fade-up').forEach(el => observer.observe(el));
</script>
</body>
</html>"""

# Inject base64 images
html = html.replace("BATTER_PLACEHOLDER", b64["BATTER"])
html = html.replace("EMMA_PLACEHOLDER", b64["EMMA"])
html = html.replace("JAM0103_PLACEHOLDER", b64["JAM0103"])

out_path = r"C:\Users\rphil\nextplaystars-landing\index.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)

size_kb = os.path.getsize(out_path) // 1024
print(f"Written: {out_path}")
print(f"Size: {size_kb} KB ({os.path.getsize(out_path):,} bytes)")
