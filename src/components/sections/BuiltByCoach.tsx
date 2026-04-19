export default function BuiltByCoach() {
  return (
    <section
      id="founder"
      style={{ background: "#F5F0E8", padding: "96px 0", borderTop: "1px solid rgba(15,27,46,0.10)" }}
    >
      <div className="max-w-content mx-auto px-6">
        <div style={{ maxWidth: "720px", margin: "0 auto" }}>

          {/* Eyebrow */}
          <p
            className="font-body"
            style={{
              fontSize: "11px",
              letterSpacing: "0.15em",
              textTransform: "uppercase",
              color: "#00ACF0",
              fontWeight: 600,
              marginBottom: "14px",
            }}
          >
            About NextPlay
          </p>

          {/* Heading */}
          <h2
            className="font-display"
            style={{
              fontSize: "clamp(32px, 3.5vw, 44px)",
              fontWeight: 700,
              color: "#0F1B2E",
              lineHeight: 1.1,
              letterSpacing: "-0.02em",
              marginBottom: "32px",
            }}
          >
            Built by a coach, for families like yours.
          </h2>

          {/* Body */}
          <div
            style={{
              borderTop: "1px solid rgba(15,27,46,0.12)",
              paddingTop: "32px",
              display: "flex",
              flexDirection: "column",
              gap: "20px",
            }}
          >
            <p
              className="font-body"
              style={{ fontSize: "17px", lineHeight: 1.75, color: "rgba(15,27,46,0.72)" }}
            >
              NextPlay was built by a head varsity softball coach and the president of DMV Dream Athletics. After years of watching talented athletes get missed because their families didn&apos;t know the recruiting game, he built the platform he wished every family had.
            </p>
            <p
              className="font-body"
              style={{ fontSize: "17px", lineHeight: 1.75, color: "rgba(15,27,46,0.72)" }}
            >
              The founding families of NextPlay are real softball and baseball families recruiting right now, across positions, graduation years, and target divisions. We built this for them first. Now we&apos;re building it for you.
            </p>
          </div>

          {/* CTA */}
          <div style={{ marginTop: "48px", textAlign: "center" }}>
            <a
              href="/about"
              className="font-body inline-flex items-center gap-3 transition-all duration-150"
              style={{
                fontSize: "16px",
                fontWeight: 600,
                color: "#00ACF0",
                border: "1.5px solid rgba(0,172,240,0.45)",
                borderRadius: "10px",
                padding: "14px 32px",
                textDecoration: "none",
              }}
              onMouseEnter={(e) => {
                (e.currentTarget as HTMLElement).style.background = "rgba(0,172,240,0.06)";
                (e.currentTarget as HTMLElement).style.borderColor = "#00ACF0";
              }}
              onMouseLeave={(e) => {
                (e.currentTarget as HTMLElement).style.background = "transparent";
                (e.currentTarget as HTMLElement).style.borderColor = "rgba(0,172,240,0.45)";
              }}
            >
              Meet the coach who built this
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden>
                <path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round"/>
              </svg>
            </a>
          </div>

        </div>
      </div>
    </section>
  );
}
