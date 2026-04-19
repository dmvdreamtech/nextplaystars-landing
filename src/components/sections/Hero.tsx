const APP_URL = "https://www.nextplayrecruiting.app";

export default function Hero() {
  return (
    <section
      className="relative min-h-screen flex items-center overflow-hidden"
      style={{ paddingTop: "96px", paddingBottom: "80px" }}
      aria-label="Hero"
    >
      {/* Subtle radial glow */}
      <div
        aria-hidden
        className="absolute inset-0 pointer-events-none"
        style={{
          background:
            "radial-gradient(ellipse 60% 70% at 68% 45%, rgba(0,172,240,0.06) 0%, transparent 65%)",
        }}
      />

      <div className="max-w-content mx-auto px-6 w-full relative z-10">
        <div className="grid grid-cols-1 lg:grid-cols-[1fr_1fr] gap-12 lg:gap-20 items-center">

          {/* LEFT: Text */}
          <div className="flex flex-col items-start">

            <h1
              className="font-display text-white leading-[1.06] tracking-[-0.02em] mb-6 animate-fade-up"
              style={{ fontSize: "clamp(44px, 5.5vw, 68px)", animationDelay: "0ms" }}
            >
              College recruiting isn&apos;t something that happens to your athlete.{" "}
              <span style={{ fontWeight: 900 }}>It&apos;s a job.</span>
              <br />
              <span
                className="font-display text-white/80"
                style={{ fontWeight: 600, fontSize: "clamp(36px, 4.2vw, 54px)" }}
              >
                We make sure it gets done right.
              </span>
            </h1>

            <p
              className="font-body mb-10 max-w-[440px] animate-fade-up"
              style={{
                fontSize: "17px",
                lineHeight: "1.65",
                color: "rgba(255,255,255,0.62)",
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

          {/* RIGHT: Visual panel — intentional editorial block until hero photo is sourced */}
          {/* PHOTO NEEDED (code-only, not visible to visitors):
              /public/photos/hero-parent-field.jpg
              Parent at softball or baseball field, phone in hand.
              Real moment, natural light, photojournalistic, 4:5 crop.
              Uncomment the Image block below when available. */}
          <div
            className="relative w-full order-first lg:order-last animate-fade-up"
            style={{ animationDelay: "80ms" }}
          >
            <div
              className="relative w-full rounded-2xl overflow-hidden"
              style={{ aspectRatio: "4/5", maxHeight: "580px" }}
            >
              {/* Designed panel — reads as intentional, not broken */}
              <div
                className="absolute inset-0"
                style={{
                  background: "linear-gradient(155deg, #132440 0%, #0F1B2E 55%, #0a1422 100%)",
                }}
              />
              {/* Cyan arc — references logo swoosh, editorial scale */}
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
                  stroke="rgba(0,172,240,0.18)"
                  strokeWidth="1.5"
                  fill="none"
                />
                <path
                  d="M-60 520 C100 340, 320 210, 580 60"
                  stroke="rgba(0,172,240,0.10)"
                  strokeWidth="1"
                  fill="none"
                />
                <path
                  d="M-20 560 C140 370, 360 230, 600 90"
                  stroke="rgba(0,172,240,0.06)"
                  strokeWidth="1"
                  fill="none"
                />
                {/* Radial glow at upper right */}
                <ellipse cx="400" cy="120" rx="180" ry="180"
                  fill="url(#hero-glow)" />
                <defs>
                  <radialGradient id="hero-glow" cx="50%" cy="50%" r="50%">
                    <stop offset="0%" stopColor="#00ACF0" stopOpacity="0.08" />
                    <stop offset="100%" stopColor="#00ACF0" stopOpacity="0" />
                  </radialGradient>
                </defs>
              </svg>
              {/* Stat anchors — editorial numbers, feel designed not decorative */}
              <div className="absolute inset-0 flex flex-col justify-end p-10">
                <div
                  className="space-y-6"
                  style={{ borderTop: "1px solid rgba(255,255,255,0.07)", paddingTop: "28px" }}
                >
                  {[
                    { num: "2–3 years", label: "average recruiting timeline" },
                    { num: "50–100", label: "coach contacts per serious effort" },
                    { num: "1", label: "recruiting assistant on the phone" },
                  ].map(({ num, label }) => (
                    <div key={label} className="flex items-baseline gap-4">
                      <span
                        className="font-display text-[#00ACF0] leading-none tabular-nums"
                        style={{ fontSize: "clamp(28px, 3vw, 38px)", fontWeight: 700 }}
                      >
                        {num}
                      </span>
                      <span
                        className="font-body text-white/45"
                        style={{ fontSize: "13px", lineHeight: 1.4 }}
                      >
                        {label}
                      </span>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>
  );
}
