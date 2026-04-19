const steps = [
  {
    num: "01",
    heading: "Set up your athlete\u2019s profile.",
    body: "Stats, GPA, target schools, positions, graduation year. Takes about an hour, spread over a few sittings if you want. We pull it into a recruiting profile coaches actually read.",
    trust: false,
  },
  {
    num: "02",
    heading: "Get a real recruiting plan.",
    body: "A personalized report showing your athlete\u2019s fit, reach schools, target schools, and likely offers based on her actual numbers and the programs she\u2019s chasing.",
    trust: false,
  },
  {
    num: "03",
    heading: "You approve every coach email before it sends.",
    body: "NextPlay drafts personalized coach emails based on each program\u2019s specific needs and your athlete\u2019s strengths. You read every email. You edit anything that doesn\u2019t sound like you. Nothing goes to a coach until you approve it. Coaches receive personal outreach, not automated blasts.",
    trust: true,
  },
  {
    num: "04",
    heading: "Check in when you want.",
    body: "Open the app on the way to practice or before bed. See what\u2019s happened. See what\u2019s coming up. Approve anything waiting for you. Close it and go.",
    trust: false,
  },
];

export default function HowItWorks() {
  return (
    <section
      id="how"
      style={{ background: "#F5F0E8", padding: "96px 0", borderTop: "1px solid rgba(15,27,46,0.08)" }}
    >
      <div className="max-w-content mx-auto px-6">

        {/* Section header */}
        <div style={{ marginBottom: "72px", maxWidth: "760px" }}>
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
            How NextPlay Works
          </p>
          <h2
            className="font-display"
            style={{
              fontSize: "clamp(32px, 3.5vw, 48px)",
              fontWeight: 700,
              color: "#0F1B2E",
              lineHeight: 1.08,
              letterSpacing: "-0.02em",
              marginBottom: "24px",
            }}
          >
            Set it up once. Check in when it matters. Watch the game.
          </h2>
          <p
            className="font-body"
            style={{
              fontSize: "17px",
              lineHeight: 1.7,
              color: "rgba(15,27,46,0.62)",
              maxWidth: "620px",
            }}
          >
            You give NextPlay the basics. It runs recruiting in the background: coach emails, X posts, schedule updates, follow-ups. You approve everything going out before it sends. You stay in control. Your athlete stays on the field.
          </p>
        </div>

        {/* Steps */}
        <div>
          {steps.map(({ num, heading, body, trust }) => (
            <div
              key={num}
              style={{
                paddingTop: "48px",
                paddingBottom: "48px",
                borderTop: "1px solid rgba(15,27,46,0.12)",
              }}
            >
              <div
                className="flex flex-col sm:grid sm:items-start"
                style={{ gridTemplateColumns: "80px 1fr", gap: "36px" }}
              >
                {/* Ghost number */}
                <span
                  className="font-display"
                  style={{
                    fontSize: "clamp(44px, 5.5vw, 72px)",
                    fontWeight: 300,
                    color: "rgba(15,27,46,0.12)",
                    lineHeight: 1,
                    letterSpacing: "-0.02em",
                    userSelect: "none",
                    paddingTop: "4px",
                  }}
                  aria-hidden
                >
                  {num}
                </span>

                {/* Content */}
                {trust ? (
                  /* Step 03 — trust callout treatment */
                  <div
                    style={{
                      background: "rgba(0,172,240,0.05)",
                      border: "1px solid rgba(0,172,240,0.18)",
                      borderLeftWidth: "3px",
                      borderLeftColor: "#00ACF0",
                      borderRadius: "0 8px 8px 0",
                      padding: "28px 32px",
                    }}
                  >
                    {/* Trust label */}
                    <p
                      className="font-body"
                      style={{
                        fontSize: "10px",
                        letterSpacing: "0.14em",
                        textTransform: "uppercase",
                        color: "#00ACF0",
                        fontWeight: 700,
                        marginBottom: "10px",
                      }}
                    >
                      Your approval. Every time.
                    </p>
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
                        color: "rgba(15,27,46,0.68)",
                        maxWidth: "560px",
                      }}
                    >
                      {body}
                    </p>
                  </div>
                ) : (
                  /* Steps 01, 02, 04 — standard treatment */
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
                        maxWidth: "560px",
                      }}
                    >
                      {body}
                    </p>
                  </div>
                )}
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
