const APP_URL = "https://www.nextplayrecruiting.app";

export default function Hero() {
  return (
    <section
      className="relative min-h-screen flex items-center overflow-hidden"
      style={{ paddingTop: "128px", paddingBottom: "80px" }}
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
        <div className="grid grid-cols-1 lg:grid-cols-[3fr_2fr] gap-12 lg:gap-16 items-center">

          {/* LEFT */}
          <div className="flex flex-col items-start max-w-[640px]">
            <div
              className="inline-flex items-center font-body animate-fade-up"
              style={{
                fontSize: "11px",
                letterSpacing: "0.13em",
                textTransform: "uppercase",
                fontWeight: 600,
                color: "#00ACF0",
                border: "1px solid rgba(0,172,240,0.30)",
                borderRadius: "100px",
                padding: "5px 14px",
                marginBottom: "22px",
                animationDelay: "0ms",
              }}
            >
              For Softball &amp; Baseball Families
            </div>

            <h1
              className="font-display text-white leading-[1.08] tracking-[-0.02em] mb-5 animate-fade-up"
              style={{ fontSize: "clamp(40px, 4.5vw, 56px)", animationDelay: "80ms", fontWeight: 700 }}
            >
              College recruiting isn&apos;t something that happens to your athlete.
              <br />
              <span style={{ color: "#00ACF0" }}>It&apos;s a job.</span>
            </h1>

            <p
              className="font-display text-white/50 mb-6 animate-fade-up"
              style={{ fontSize: "clamp(20px, 2vw, 26px)", fontWeight: 400, lineHeight: 1.35, animationDelay: "160ms" }}
            >
              We make sure it gets done right.
            </p>

            <p
              className="font-body mb-10 animate-fade-up"
              style={{ fontSize: "17px", lineHeight: "1.65", color: "rgba(255,255,255,0.62)", maxWidth: "480px", animationDelay: "240ms" }}
            >
              Most families don&apos;t realize college coaches won&apos;t find their kid
              on their own. Recruiting takes hundreds of emails, dozens of calls,
              a real plan, and follow-through for two to three years. NextPlay
              handles all of it. You set it up, check in when something needs
              you, and watch the game.
            </p>

            <div
              className="flex flex-col sm:flex-row gap-3 w-full sm:w-auto animate-fade-up"
              style={{ animationDelay: "340ms" }}
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

          {/* RIGHT: Sport photo + N.I.K.K.I. chat panel */}
          <div
            className="relative w-full order-first lg:order-last animate-fade-up flex flex-col"
            style={{ animationDelay: "80ms", gap: "20px" }}
          >

            {/* Sport photo */}
            <div style={{
              overflow: "hidden",
              borderRadius: "8px",
              boxShadow: "0 6px 28px rgba(0,0,0,0.28), inset 0 0 50px rgba(0,0,0,0.15)",
            }}>
              <img
                src="/photos/firefly-action.jpg"
                alt="High school softball game in action"
                style={{
                  width: "100%",
                  aspectRatio: "16/9",
                  objectFit: "cover",
                  objectPosition: "center center",
                  display: "block",
                  filter: "sepia(0.12) contrast(1.04) brightness(0.87)",
                }}
              />
            </div>

            {/* N.I.K.K.I. chat panel */}
            <div
              className="relative w-full rounded-2xl overflow-hidden flex flex-col"
              style={{ background: "linear-gradient(155deg, #0d1f38 0%, #0F1B2E 60%, #0a1422 100%)" }}
            >
              {/* Background swoosh */}
              <svg
                aria-hidden
                viewBox="0 0 480 600"
                fill="none"
                className="absolute inset-0 w-full h-full"
                preserveAspectRatio="xMidYMid slice"
              >
                <path d="M-60 480 C80 320, 280 200, 540 80" stroke="rgba(0,172,240,0.12)" strokeWidth="1.5" fill="none" />
                <ellipse cx="420" cy="80" rx="160" ry="160" fill="url(#hero-conv-glow)" />
                <defs>
                  <radialGradient id="hero-conv-glow" cx="50%" cy="50%" r="50%">
                    <stop offset="0%" stopColor="#00ACF0" stopOpacity="0.10" />
                    <stop offset="100%" stopColor="#00ACF0" stopOpacity="0" />
                  </radialGradient>
                </defs>
              </svg>

              {/* Header bar */}
              <div
                className="relative flex items-center gap-3 px-6 py-4 flex-shrink-0"
                style={{ borderBottom: "1px solid rgba(255,255,255,0.07)" }}
              >
                <div
                  style={{
                    width: "36px",
                    height: "36px",
                    borderRadius: "50%",
                    background: "linear-gradient(135deg, #00ACF0 0%, #0077b6 100%)",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                    flexShrink: 0,
                  }}
                >
                  <span className="font-display text-white" style={{ fontSize: "13px", fontWeight: 700 }}>N</span>
                </div>
                <div>
                  <p className="font-body text-white" style={{ fontSize: "14px", fontWeight: 600, lineHeight: 1 }}>N.I.K.K.I.</p>
                  <p className="font-body text-[#00ACF0]" style={{ fontSize: "11px", marginTop: "3px" }}>● Active now</p>
                </div>
                <div className="ml-auto">
                  <p className="font-body text-white/20" style={{ fontSize: "10px", letterSpacing: "0.08em", textTransform: "uppercase" }}>NextPlay</p>
                </div>
              </div>

              {/* Messages */}
              <div className="relative flex flex-col justify-center flex-1 px-6 py-8 gap-4">
                <p
                  className="font-body text-white/20 text-center"
                  style={{ fontSize: "10px", letterSpacing: "0.06em", textTransform: "uppercase", marginBottom: "4px" }}
                >
                  Today · 3:42 PM
                </p>

                {/* Parent bubble */}
                <div className="flex justify-end">
                  <div
                    className="font-body text-white"
                    style={{
                      background: "rgba(0,172,240,0.18)",
                      border: "1px solid rgba(0,172,240,0.25)",
                      borderRadius: "18px 18px 4px 18px",
                      padding: "12px 16px",
                      maxWidth: "80%",
                      fontSize: "15px",
                      lineHeight: 1.45,
                    }}
                  >
                    Peyton just hit a home run at the showcase.
                  </div>
                </div>

                {/* N.I.K.K.I. bubble */}
                <div className="flex items-end gap-2">
                  <div
                    style={{
                      width: "28px",
                      height: "28px",
                      borderRadius: "50%",
                      background: "linear-gradient(135deg, #00ACF0 0%, #0077b6 100%)",
                      display: "flex",
                      alignItems: "center",
                      justifyContent: "center",
                      flexShrink: 0,
                      marginBottom: "2px",
                    }}
                  >
                    <span className="font-display text-white" style={{ fontSize: "10px", fontWeight: 700 }}>N</span>
                  </div>
                  <div>
                    <p className="font-body text-white/30" style={{ fontSize: "11px", marginBottom: "5px" }}>N.I.K.K.I.</p>
                    <div
                      className="font-body text-white/85"
                      style={{
                        background: "rgba(255,255,255,0.06)",
                        border: "1px solid rgba(255,255,255,0.08)",
                        borderRadius: "4px 18px 18px 18px",
                        padding: "12px 16px",
                        fontSize: "15px",
                        lineHeight: 1.5,
                      }}
                    >
                      I&apos;ll draft updates to your target coach list for your approval.{" "}
                      <span style={{ color: "#00ACF0" }}>Calendar updated</span> with her next tournament.
                    </div>
                  </div>
                </div>

                {/* Input bar */}
                <div
                  className="flex items-center gap-3 mt-auto"
                  style={{
                    background: "rgba(255,255,255,0.04)",
                    border: "1px solid rgba(255,255,255,0.08)",
                    borderRadius: "24px",
                    padding: "11px 18px",
                    marginTop: "20px",
                  }}
                >
                  <p className="font-body text-white/20 flex-1" style={{ fontSize: "14px" }}>Message N.I.K.K.I…</p>
                  <div
                    style={{
                      width: "30px",
                      height: "30px",
                      borderRadius: "50%",
                      background: "#00ACF0",
                      display: "flex",
                      alignItems: "center",
                      justifyContent: "center",
                      flexShrink: 0,
                    }}
                  >
                    <svg width="12" height="12" viewBox="0 0 12 12" fill="none" aria-hidden>
                      <path d="M2 6h8M6 2l4 4-4 4" stroke="white" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/>
                    </svg>
                  </div>
                </div>
              </div>
            </div>

          </div>

        </div>
      </div>
    </section>
  );
}
