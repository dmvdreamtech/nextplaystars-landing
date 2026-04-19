import Image from "next/image";

const APP_URL = "https://www.nextplayrecruiting.app";

/*
  Two headline treatments are rendered — visible via CSS class toggle.
  Treatment A: "It's a job." in heavier weight (900) — same ink color, pure typographic punch.
  Treatment B: "job" in cyan — color as punctuation.

  To switch between them in the browser, open DevTools and toggle:
    .headline-treatment-a  (default, visible)
    .headline-treatment-b  (hidden, swap display to see)

  Report back which reads stronger in context.
*/

export default function Hero() {
  return (
    <section
      className="relative min-h-screen flex items-center overflow-hidden"
      style={{ paddingTop: "96px", paddingBottom: "80px" }}
      aria-label="Hero"
    >
      {/* Subtle radial glow — ink side only, no tech-gradient feel */}
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

            {/* Headline — Treatment A (default) */}
            <h1
              className="headline-treatment-a font-display text-white leading-[1.06] tracking-[-0.02em] mb-6"
              style={{ fontSize: "clamp(44px, 5.5vw, 68px)" }}
            >
              College recruiting
              {" "}isn&apos;t something
              {" "}that happens to
              {" "}your athlete.{" "}
              <span style={{ fontWeight: 900 }}>It&apos;s a job.</span>
              <br />
              <span
                className="font-display text-white/80"
                style={{ fontWeight: 600, fontSize: "clamp(36px, 4.2vw, 54px)" }}
              >
                We make sure it
                {" "}gets done right.
              </span>
            </h1>

            {/* Headline — Treatment B (hidden — toggle to compare) */}
            <h1
              className="headline-treatment-b font-display text-white leading-[1.06] tracking-[-0.02em] mb-6 hidden"
              style={{ fontSize: "clamp(44px, 5.5vw, 68px)" }}
            >
              College recruiting
              {" "}isn&apos;t something
              {" "}that happens to
              {" "}your athlete.{" "}
              <span style={{ fontWeight: 700 }}>
                It&apos;s a{" "}
                <span style={{ color: "#00ACF0" }}>job.</span>
              </span>
              <br />
              <span
                className="font-display text-white/80"
                style={{ fontWeight: 600, fontSize: "clamp(36px, 4.2vw, 54px)" }}
              >
                We make sure it
                {" "}gets done right.
              </span>
            </h1>

            {/* Subhead */}
            <p
              className="font-body mb-10 max-w-[440px]"
              style={{
                fontSize: "17px",
                lineHeight: "1.65",
                color: "rgba(255,255,255,0.62)",
              }}
            >
              Most families don&apos;t realize college coaches won&apos;t find their kid
              on their own. Recruiting takes hundreds of emails, dozens of calls,
              a real plan, and follow-through for two to three years. NextPlay
              handles all of it. You set it up, check in when something needs
              you, and watch the game.
            </p>

            {/* CTAs */}
            <div className="flex flex-col sm:flex-row gap-3 w-full sm:w-auto">
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

          {/* RIGHT: Photo */}
          <div
            className="relative w-full animate-fade-up order-first lg:order-last"
            style={{ animationDelay: "80ms" }}
          >
            {/* Photo placeholder — replace with real hero photo */}
            {/* PHOTO NEEDED: Parent at softball or baseball field, phone in hand.
                Real moment, natural light, photojournalistic feel.
                Portrait or 4:5 crop. Warm grade, slight vignette. No stock. */}
            <div
              className="relative w-full overflow-hidden rounded-2xl"
              style={{ aspectRatio: "4/5", maxHeight: "580px" }}
            >
              {/* Fallback while photo is sourced */}
              <div
                className="absolute inset-0 flex flex-col items-center justify-center gap-3"
                style={{ background: "rgba(0,172,240,0.04)", border: "1px dashed rgba(0,172,240,0.2)", borderRadius: "16px" }}
              >
                <svg width="40" height="40" viewBox="0 0 40 40" fill="none" aria-hidden>
                  <rect x="4" y="8" width="32" height="26" rx="3" stroke="rgba(0,172,240,0.4)" strokeWidth="1.5"/>
                  <circle cx="20" cy="21" r="7" stroke="rgba(0,172,240,0.4)" strokeWidth="1.5"/>
                  <circle cx="20" cy="21" r="3" fill="rgba(0,172,240,0.25)"/>
                  <path d="M14 8V6a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v2" stroke="rgba(0,172,240,0.4)" strokeWidth="1.5"/>
                </svg>
                <p className="font-body text-center px-8" style={{ fontSize: "13px", color: "rgba(0,172,240,0.5)", lineHeight: 1.5 }}>
                  PHOTO NEEDED<br/>
                  Parent at field · phone in hand<br/>
                  Photojournalistic · warm light
                </p>
              </div>

              {/* Uncomment and replace src when photo is available:
              <Image
                src="/photos/hero-parent-field.jpg"
                alt="Parent checking NextPlay at a softball tournament"
                fill
                className="object-cover object-center"
                priority
                sizes="(max-width: 1024px) 100vw, 50vw"
              />
              <div
                className="absolute inset-0 pointer-events-none"
                style={{ background: "linear-gradient(to bottom, transparent 50%, rgba(15,27,46,0.35) 100%)" }}
              />
              */}
            </div>
          </div>

        </div>
      </div>

      {/* Staggered load animations for left column children */}
      <style>{`
        .hero-left-animate > *:nth-child(1) { animation-delay: 0ms; }
        .hero-left-animate > *:nth-child(2) { animation-delay: 120ms; }
        .hero-left-animate > *:nth-child(3) { animation-delay: 240ms; }
      `}</style>
    </section>
  );
}
