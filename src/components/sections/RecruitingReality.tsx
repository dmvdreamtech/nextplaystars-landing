const items = [
  {
    num: "01",
    heading: "Coaches aren't looking for your athlete.",
    body: "A D1 coach manages hundreds of recruits. Your athlete isn't in their database. Families who get recruited are the ones who put themselves in front of the right coaches — persistently, professionally, and over years. Waiting for an invitation is a strategy that doesn't work.",
  },
  {
    num: "02",
    heading: "It's not one email. It's hundreds.",
    body: "A serious recruiting effort means personalized outreach to 50–100 coaches, multiple follow-ups, video updates, profile maintenance, phone calls, social posts, and campus visits. Most families underestimate the work by an order of magnitude.",
  },
  {
    num: "03",
    heading: "The window closes before most families realize it's open.",
    body: "Division I programs fill verbal commitments years before signing day. The athletes who get those offers started early — sophomore year, sometimes earlier. If you're waiting until junior year to think seriously about recruiting, you are already behind.",
  },
];

export default function RecruitingReality() {
  return (
    <section
      id="reality"
      style={{ background: "#F5F0E8", padding: "96px 0" }}
    >
      <div className="max-w-content mx-auto px-6">

        {/* Section header */}
        <div style={{ marginBottom: "64px" }}>
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
            The recruiting reality
          </p>
          <h2
            className="font-display"
            style={{
              fontSize: "clamp(32px, 3.5vw, 44px)",
              fontWeight: 700,
              color: "#0F1B2E",
              lineHeight: 1.1,
              letterSpacing: "-0.02em",
              maxWidth: "520px",
            }}
          >
            What most families find out too late.
          </h2>
        </div>

        {/* Editorial blocks */}
        <div>
          {items.map(({ num, heading, body }, i) => (
            <div
              key={num}
              style={{
                display: "grid",
                gridTemplateColumns: "72px 1fr",
                gap: "40px",
                paddingTop: "44px",
                paddingBottom: "44px",
                borderTop: "1px solid rgba(15,27,46,0.12)",
                alignItems: "start",
              }}
            >
              <span
                className="font-display"
                style={{
                  fontSize: "clamp(52px, 5vw, 72px)",
                  fontWeight: 300,
                  color: "rgba(15,27,46,0.15)",
                  lineHeight: 1,
                  letterSpacing: "-0.02em",
                  userSelect: "none",
                }}
                aria-hidden
              >
                {num}
              </span>
              <div>
                <h3
                  className="font-display"
                  style={{
                    fontSize: "clamp(20px, 2.2vw, 28px)",
                    fontWeight: 700,
                    color: "#0F1B2E",
                    marginBottom: "14px",
                    lineHeight: 1.2,
                    letterSpacing: "-0.01em",
                  }}
                >
                  {heading}
                </h3>
                <p
                  className="font-body"
                  style={{
                    fontSize: "16px",
                    lineHeight: 1.75,
                    color: "rgba(15,27,46,0.62)",
                    maxWidth: "600px",
                  }}
                >
                  {body}
                </p>
              </div>
            </div>
          ))}
          {/* Closing rule */}
          <div style={{ borderTop: "1px solid rgba(15,27,46,0.12)" }} />
        </div>

      </div>
    </section>
  );
}
