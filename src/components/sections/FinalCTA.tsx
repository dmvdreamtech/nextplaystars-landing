const APP_URL = "https://www.nextplayrecruiting.app";

export default function FinalCTA() {
  return (
    <section
      id="get-started"
      style={{
        background: "#F5F0E8",
        padding: "120px 0 136px",
        borderTop: "1px solid rgba(15,27,46,0.10)",
      }}
    >
      <div className="max-w-content mx-auto px-6">
        <div style={{ maxWidth: "640px", margin: "0 auto", textAlign: "center" }}>

          <h2
            className="font-display"
            style={{
              fontSize: "clamp(28px, 3vw, 40px)",
              fontWeight: 700,
              lineHeight: 1.15,
              letterSpacing: "-0.02em",
              marginBottom: "24px",
              color: "#0F1B2E",
            }}
          >
            Give your athlete the recruiting effort she deserves.
          </h2>

          <p
            className="font-body"
            style={{
              fontSize: "17px",
              lineHeight: 1.7,
              color: "rgba(15,27,46,0.58)",
              marginBottom: "44px",
            }}
          >
            Join softball and baseball families who are finally handling the recruiting part. First month free. Cancel anytime.
          </p>

          <a
            href={`${APP_URL}/signup`}
            className="font-body cta-primary"
            style={{
              display: "inline-block",
              fontSize: "16px",
              fontWeight: 600,
              color: "#0F1B2E",
              padding: "16px 36px",
              borderRadius: "10px",
              textDecoration: "none",
            }}
          >
            Start Your Athlete&apos;s Recruiting Plan
          </a>

        </div>
      </div>
    </section>
  );
}
