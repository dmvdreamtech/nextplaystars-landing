const APP_URL = "https://www.nextplayrecruiting.app";

export default function Hero() {
  return (
    <>
      <section
        className="relative min-h-screen flex items-center overflow-hidden"
        style={{ paddingTop: "96px", paddingBottom: "80px" }}
        aria-label="Hero"
      >
        <div
          aria-hidden
          className="absolute inset-0 pointer-events-none"
          style={{
            background:
              "radial-gradient(ellipse 60% 70% at 68% 45%, rgba(0,172,240,0.07) 0%, transparent 65%)",
          }}
        />

        <div className="max-w-content mx-auto px-6 w-full relative z-10">
          {/* 3fr / 2fr split ≈ 60/40 at 1140px content width */}
          <div className="grid grid-cols-1 lg:grid-cols-[3fr_2fr] gap-12 lg:gap-16 items-center">

            {/* LEFT: Text — max-w keeps headline from over-stretching */}
            <div className="flex flex-col items-start max-w-[640px]">

              <h1
                className="font-display text-white leading-[1.08] tracking-[-0.02em] mb-5 animate-fade-up"
                style={{ fontSize: "clamp(40px, 4.5vw, 56px)", animationDelay: "0ms", fontWeight: 700 }}
              >
                College recruiting isn&apos;t something that happens to your athlete.
                <br />
                {/* Option A active in hero — cyan color. See comparison section below for Option B. */}
                <span style={{ color: "#00ACF0" }}>It&apos;s a job.</span>
              </h1>

              {/* Demoted subhead — lighter weight, clearly subordinate */}
              <p
                className="font-display text-white/50 mb-6 animate-fade-up"
                style={{
                  fontSize: "clamp(20px, 2vw, 26px)",
                  fontWeight: 400,
                  lineHeight: 1.35,
                  animationDelay: "60ms",
                }}
              >
                We make sure it gets done right.
              </p>

              <p
                className="font-body mb-10 animate-fade-up"
                style={{
                  fontSize: "17px",
                  lineHeight: "1.65",
                  color: "rgba(255,255,255,0.62)",
                  maxWidth: "480px",
                  animationDelay: "120ms",
                }}
              >
                Most families don&apos;t realize college coaches won&apos;t find their kid
                on their own. Recruiting takes hundreds of emails, dozens of calls,
                a real plan, and follow-through for two to three years. NextPlay
                handles all of it. You set it up, check in when something needs
                you, and watch the game.
              </p>

              <div
                className="flex flex-col sm:flex-row gap-3 w-full sm:w-auto animate-fade-up"
                style={{ animationDelay: "240ms" }}
              >
                <a
                  href={`${APP_URL}/signup`}
                  className="inline-flex items-center justify-center gap-2 font-body font-semibold text-ink bg-[#00ACF0] hover:bg-[#0099D8] active:bg-[#0088C4] transition-colors duration-150 rounded-xl cursor-pointer"
                  style={{ fontSize: "15px", padding: "13px 28px" }}
                >
                  Start Your Athlete&apos;s Recruiting Plan
                  <svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden>
                    <path d="M2 7h10M8 3l4 4-4 4" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round"/>
                  </svg>
                </a>
                <a
                  href="#how"
                  className="inline-flex items-center justify-center font-body font-medium text-white/75 hover:text-white transition-colors duration-150"
                  style={{ fontSize: "15px", padding: "13px 20px" }}
                >
                  See How It Works ↓
                </a>
              </div>
            </div>

            {/* RIGHT: Visual panel */}
            {/* PHOTO NEEDED (code-only, not visible to visitors):
                /public/photos/hero-parent-field.jpg
                Parent at softball or baseball field, phone in hand.
                Real moment, natural light, photojournalistic, 4:5 crop.
                Uncomment next/image block when available. */}
            <div
              className="relative w-full order-first lg:order-last animate-fade-up"
              style={{ animationDelay: "80ms" }}
            >
              <div
                className="relative w-full rounded-2xl overflow-hidden"
                style={{ aspectRatio: "4/5", maxHeight: "560px" }}
              >
                <div
                  className="absolute inset-0"
                  style={{
                    background: "linear-gradient(155deg, #132440 0%, #0F1B2E 55%, #0a1422 100%)",
                  }}
                />

                {/* Swoosh arcs — boosted to 0.40/0.22/0.12, thicker strokes */}
                <svg
                  aria-hidden
                  viewBox="0 0 480 600"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                  className="absolute inset-0 w-full h-full"
                  preserveAspectRatio="xMidYMid slice"
                >
                  <path
                    d="M-60 480 C80 320, 280 200, 540 80"
                    stroke="rgba(0,172,240,0.40)"
                    strokeWidth="2.5"
                    fill="none"
                  />
                  <path
                    d="M-60 520 C100 340, 320 210, 580 60"
                    stroke="rgba(0,172,240,0.22)"
                    strokeWidth="1.5"
                    fill="none"
                  />
                  <path
                    d="M-20 560 C140 370, 360 230, 600 90"
                    stroke="rgba(0,172,240,0.12)"
                    strokeWidth="1"
                    fill="none"
                  />
                  <ellipse cx="400" cy="120" rx="200" ry="200" fill="url(#hero-glow)" />
                  <defs>
                    <radialGradient id="hero-glow" cx="50%" cy="50%" r="50%">
                      <stop offset="0%" stopColor="#00ACF0" stopOpacity="0.14" />
                      <stop offset="100%" stopColor="#00ACF0" stopOpacity="0" />
                    </radialGradient>
                  </defs>
                </svg>

                {/* Stats — vertically centered, stacked hierarchy */}
                <div className="absolute inset-0 flex flex-col justify-center px-10 py-10">
                  <p
                    className="font-body text-[#00ACF0] mb-8"
                    style={{ fontSize: "11px", letterSpacing: "0.15em", textTransform: "uppercase", fontWeight: 600 }}
                  >
                    The recruiting math
                  </p>

                  <div className="space-y-8">
                    {[
                      { num: "2–3 years", label: "average recruiting timeline" },
                      { num: "50–100", label: "coach contacts per serious effort" },
                      { num: "1", label: "recruiting assistant on the phone" },
                    ].map(({ num, label }, i) => (
                      <div key={label}>
                        {i === 0 && (
                          <div
                            style={{
                              width: "40px",
                              height: "2px",
                              background: "#00ACF0",
                              opacity: 0.7,
                              marginBottom: "16px",
                            }}
                          />
                        )}
                        <div className="flex flex-col gap-1.5">
                          <span
                            className="font-display text-[#00ACF0] leading-none tabular-nums"
                            style={{ fontSize: "clamp(30px, 3.2vw, 42px)", fontWeight: 700 }}
                          >
                            {num}
                          </span>
                          <span
                            className="font-body text-white/50"
                            style={{ fontSize: "13px", lineHeight: 1.4 }}
                          >
                            {label}
                          </span>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            </div>

          </div>
        </div>
      </section>

      {/* ── DESIGN REVIEW — remove before launch ── */}
      <section
        style={{
          background: "#07111E",
          borderTop: "1px solid rgba(255,255,255,0.06)",
          padding: "64px 24px",
        }}
        aria-label="Design review — headline options"
      >
        <div className="max-w-content mx-auto">
          <p
            className="font-body text-white/25 mb-10"
            style={{ fontSize: "11px", letterSpacing: "0.15em", textTransform: "uppercase" }}
          >
            Design review — headline options (remove before launch)
          </p>
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">

            <div
              style={{
                padding: "40px",
                background: "#0F1B2E",
                borderRadius: "16px",
                border: "1px solid rgba(255,255,255,0.07)",
              }}
            >
              <p
                className="font-body text-[#00ACF0] mb-6"
                style={{ fontSize: "11px", letterSpacing: "0.12em", textTransform: "uppercase", fontWeight: 600 }}
              >
                Option A — "It&apos;s a job." in cyan
              </p>
              <h2
                className="font-display text-white leading-[1.08] tracking-[-0.02em]"
                style={{ fontSize: "clamp(40px, 4.5vw, 56px)", fontWeight: 700 }}
              >
                College recruiting isn&apos;t something that happens to your athlete.
                <br />
                <span style={{ color: "#00ACF0" }}>It&apos;s a job.</span>
              </h2>
            </div>

            <div
              style={{
                padding: "40px",
                background: "#0F1B2E",
                borderRadius: "16px",
                border: "1px solid rgba(255,255,255,0.07)",
              }}
            >
              <p
                className="font-body text-white/30 mb-6"
                style={{ fontSize: "11px", letterSpacing: "0.12em", textTransform: "uppercase", fontWeight: 600 }}
              >
                Option B — heavier weight (800), white
              </p>
              <h2
                className="font-display text-white leading-[1.08] tracking-[-0.02em]"
                style={{ fontSize: "clamp(40px, 4.5vw, 56px)", fontWeight: 700 }}
              >
                College recruiting isn&apos;t something that happens to your athlete.
                <br />
                <span style={{ fontWeight: 800 }}>It&apos;s a job.</span>
              </h2>
            </div>

          </div>
        </div>
      </section>
    </>
  );
}
