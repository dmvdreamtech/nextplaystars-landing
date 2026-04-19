const APP_URL = "https://www.nextplayrecruiting.app";

const tiers = [
  {
    name: "Starter",
    price: "$39",
    athletes: "1 athlete",
    description:
      "Full recruiting platform, N.I.K.K.I. access, recruiting plan, coach outreach, and X post automation.",
    popular: false,
  },
  {
    name: "Pro",
    price: "$59",
    athletes: "Up to 2 athletes",
    description:
      "Same full platform for families with multiple kids in the pipeline.",
    popular: true,
  },
  {
    name: "Elite",
    price: "$75",
    athletes: "Up to 3 athletes",
    description:
      "Everything in Pro, for families managing three active recruiting efforts.",
    popular: false,
  },
  {
    name: "Family",
    price: "$99",
    athletes: "Up to 5 athletes",
    description:
      "For large families, travel organization director households, and multi-sport families managing a full roster of recruiting athletes.",
    popular: false,
  },
];

export default function Pricing() {
  return (
    <section
      id="pricing"
      style={{
        background: "#0F1B2E",
        padding: "96px 0",
        borderTop: "1px solid rgba(255,255,255,0.06)",
      }}
    >
      <div className="max-w-content mx-auto px-6">

        {/* Header */}
        <div style={{ textAlign: "center", marginBottom: "56px" }}>
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
            Pricing
          </p>
          <h2
            className="font-display text-white"
            style={{
              fontSize: "clamp(32px, 3.5vw, 44px)",
              fontWeight: 700,
              lineHeight: 1.1,
              letterSpacing: "-0.02em",
              marginBottom: "16px",
            }}
          >
            Simple pricing. One athlete or up to five.
          </h2>
          <p
            className="font-body"
            style={{
              fontSize: "15px",
              color: "rgba(255,255,255,0.45)",
              lineHeight: 1.6,
            }}
          >
            All plans include a free trial. Cancel anytime from your billing page.
          </p>
        </div>

        {/* Cards */}
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fit, minmax(240px, 1fr))",
            gap: "20px",
            alignItems: "stretch",
          }}
        >
          {tiers.map(({ name, price, athletes, description, popular }) => (
            <div
              key={name}
              style={{
                position: "relative",
                background: popular
                  ? "rgba(0,172,240,0.07)"
                  : "rgba(255,255,255,0.03)",
                border: popular
                  ? "1.5px solid rgba(0,172,240,0.55)"
                  : "1px solid rgba(255,255,255,0.08)",
                borderRadius: "16px",
                padding: "32px 28px",
                display: "flex",
                flexDirection: "column",
              }}
            >
              {/* Most Popular badge */}
              {popular && (
                <div
                  className="font-body"
                  style={{
                    position: "absolute",
                    top: "-13px",
                    left: "50%",
                    transform: "translateX(-50%)",
                    background: "#00ACF0",
                    color: "#0F1B2E",
                    fontSize: "11px",
                    fontWeight: 700,
                    letterSpacing: "0.1em",
                    textTransform: "uppercase",
                    padding: "4px 14px",
                    borderRadius: "20px",
                    whiteSpace: "nowrap",
                  }}
                >
                  Most Popular
                </div>
              )}

              {/* Tier name */}
              <p
                className="font-body"
                style={{
                  fontSize: "13px",
                  fontWeight: 600,
                  letterSpacing: "0.08em",
                  textTransform: "uppercase",
                  color: popular ? "#00ACF0" : "rgba(255,255,255,0.45)",
                  marginBottom: "12px",
                }}
              >
                {name}
              </p>

              {/* Price */}
              <div style={{ marginBottom: "6px" }}>
                <span
                  className="font-display text-white"
                  style={{ fontSize: "42px", fontWeight: 700, lineHeight: 1 }}
                >
                  {price}
                </span>
                <span
                  className="font-body"
                  style={{ fontSize: "14px", color: "rgba(255,255,255,0.38)", marginLeft: "6px" }}
                >
                  /month
                </span>
              </div>

              {/* Athletes */}
              <p
                className="font-body"
                style={{
                  fontSize: "13px",
                  fontWeight: 600,
                  color: "rgba(255,255,255,0.55)",
                  marginBottom: "20px",
                  paddingBottom: "20px",
                  borderBottom: "1px solid rgba(255,255,255,0.07)",
                }}
              >
                {athletes}
              </p>

              {/* Description */}
              <p
                className="font-body"
                style={{
                  fontSize: "14px",
                  lineHeight: 1.65,
                  color: "rgba(255,255,255,0.52)",
                  flexGrow: 1,
                  marginBottom: "28px",
                }}
              >
                {description}
              </p>

              {/* CTA */}
              <a
                href={`${APP_URL}/signup`}
                className={`font-body ${popular ? "pricing-cta-solid" : "pricing-cta-outline"}`}
                style={{
                  display: "block",
                  textAlign: "center",
                  fontSize: "15px",
                  fontWeight: 600,
                  padding: "13px 20px",
                  borderRadius: "10px",
                  textDecoration: "none",
                  color: popular ? "#0F1B2E" : "#00ACF0",
                }}
              >
                Start Free Trial
              </a>
            </div>
          ))}
        </div>

      </div>
    </section>
  );
}
