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
            {/* Sport tag — signals audience immediately */}
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

          {/* RIGHT: Hero photo */}
          <div
            className="relative w-full order-first lg:order-last animate-fade-up"
            style={{ animationDelay: "80ms" }}
          >
            <div style={{
              position: "relative",
              overflow: "hidden",
              borderRadius: "8px",
              aspectRatio: "4/5",
              background: "#0F1B2E",
              boxShadow: "0 6px 28px rgba(0,0,0,0.28), inset 0 0 60px rgba(0,0,0,0.35)",
            }}>
              <img
                src="/photos/hero-baseball-batter.jpg"
                alt="Baseball batter in action during a high school game"
                style={{
                  width: "100%",
                  height: "100%",
                  objectFit: "contain",
                  display: "block",
                  filter: "sepia(0.35) saturate(0.7) contrast(1.04) brightness(0.65)",
                }}
              />
              {/* Navy tint overlay — pulls photo toward page aesthetic */}
              <div
                aria-hidden
                style={{
                  position: "absolute",
                  inset: 0,
                  background: "rgba(15,27,46,0.15)",
                  pointerEvents: "none",
                }}
              />
            </div>
          </div>

        </div>
      </div>
    </section>
  );
}
