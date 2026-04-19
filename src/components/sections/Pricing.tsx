const APP_URL = "https://www.nextplayrecruiting.app";

const tiers = [
  {
    name: "Starter",
    price: "$39",
    athletes: "1 athlete",
    features: [
      "Call N.I.K.K.I.: 15 minutes of calls per month",
      "Coach emails: 25/month",
      "Recruiting reports: 1/month",
      "Target schools: up to 5",
      "Calendar management",
      "No social media automation",
    ],
    popular: false,
    travel: false,
    cta: "Start Free Trial",
    href: `${APP_URL}/signup`,
  },
  {
    name: "Pro",
    price: "$59",
    athletes: "Up to 2 athletes",
    features: [
      "Everything in Starter, plus:",
      "Call N.I.K.K.I.: 45 minutes of calls per month",
      "Coach emails: 75/month",
      "Recruiting reports: 1 per week",
      "Target schools: up to 10",
      "Social media automation: 8 X posts per month",
    ],
    popular: true,
    travel: false,
    cta: "Start Free Trial",
    href: `${APP_URL}/signup`,
  },
  {
    name: "Elite",
    price: "$75",
    athletes: "Up to 3 athletes",
    features: [
      "Everything in Pro, plus:",
      "Call N.I.K.K.I.: unlimited calls",
      "Coach emails: unlimited",
      "Recruiting reports: on-demand, unlimited",
      "Target schools: unlimited",
      "Social media automation: unlimited X posts",
      "Priority support",
    ],
    popular: false,
    travel: false,
    cta: "Start Free Trial",
    href: `${APP_URL}/signup`,
  },
  {
    name: "Travel Program",
    price: null,
    athletes: "For travel organizations, clubs & multi-athlete programs (5+ athletes)",
    features: [
      "Custom pricing for organizations managing multiple recruits. Includes director dashboards, bulk family onboarding, and co-branded outreach.",
    ],
    popular: false,
    travel: true,
    cta: "Contact Us",
    href: "mailto:support@nextplaystars.com",
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
            Simple pricing. From one athlete to entire travel programs.
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

        {/* Cards — 4-up on desktop, 1-up on mobile */}
        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-5 items-stretch">
          {tiers.map(({ name, price, athletes, features, popular, travel, cta, href }) => (
            <div
              key={name}
              style={{
                position: "relative",
                background: travel
                  ? "rgba(255,255,255,0.02)"
                  : popular
                  ? "rgba(0,172,240,0.07)"
                  : "rgba(255,255,255,0.03)",
                border: travel
                  ? "1px solid rgba(255,255,255,0.10)"
                  : popular
                  ? "1.5px solid rgba(0,172,240,0.55)"
                  : "1px solid rgba(255,255,255,0.08)",
                borderRadius: "16px",
                padding: "28px 24px",
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
                  color: popular
                    ? "#00ACF0"
                    : travel
                    ? "rgba(255,255,255,0.38)"
                    : "rgba(255,255,255,0.45)",
                  marginBottom: "12px",
                }}
              >
                {name}
              </p>

              {/* Price or contact */}
              {price ? (
                <div style={{ marginBottom: "6px" }}>
                  <span
                    className="font-display text-white"
                    style={{ fontSize: "38px", fontWeight: 700, lineHeight: 1 }}
                  >
                    {price}
                  </span>
                  <span
                    className="font-body"
                    style={{ fontSize: "14px", color: "rgba(255,255,255,0.38)", marginLeft: "5px" }}
                  >
                    /month
                  </span>
                </div>
              ) : (
                <p
                  className="font-body text-white"
                  style={{ fontSize: "17px", fontWeight: 600, marginBottom: "6px" }}
                >
                  Contact for pricing
                </p>
              )}

              {/* Athletes / subhead */}
              <p
                className="font-body"
                style={{
                  fontSize: "12px",
                  fontWeight: travel ? 400 : 600,
                  color: travel ? "rgba(255,255,255,0.40)" : "rgba(255,255,255,0.50)",
                  lineHeight: 1.5,
                  marginBottom: "20px",
                  paddingBottom: "20px",
                  borderBottom: "1px solid rgba(255,255,255,0.07)",
                }}
              >
                {athletes}
              </p>

              {/* Features */}
              <div style={{ flexGrow: 1, marginBottom: "24px" }}>
                {travel ? (
                  <p
                    className="font-body"
                    style={{ fontSize: "13px", lineHeight: 1.7, color: "rgba(255,255,255,0.48)" }}
                  >
                    {features[0]}
                  </p>
                ) : (
                  <ul style={{ display: "flex", flexDirection: "column", gap: "9px", listStyle: "none", padding: 0, margin: 0 }}>
                    {features.map((f) => (
                      <li
                        key={f}
                        className="font-body"
                        style={{
                          fontSize: "13px",
                          lineHeight: 1.5,
                          color: f.startsWith("Everything")
                            ? "rgba(255,255,255,0.35)"
                            : "rgba(255,255,255,0.62)",
                          display: "flex",
                          gap: "8px",
                        }}
                      >
                        {!f.startsWith("Everything") && (
                          <span style={{ color: "#00ACF0", flexShrink: 0, marginTop: "1px" }}>•</span>
                        )}
                        <span>{f}</span>
                      </li>
                    ))}
                  </ul>
                )}
              </div>

              {/* CTA */}
              <a
                href={href}
                className={`font-body ${popular ? "pricing-cta-solid" : travel ? "pricing-cta-outline" : "pricing-cta-outline"}`}
                style={{
                  display: "block",
                  textAlign: "center",
                  fontSize: "14px",
                  fontWeight: 600,
                  padding: "12px 16px",
                  borderRadius: "10px",
                  textDecoration: "none",
                  color: popular ? "#0F1B2E" : "#00ACF0",
                }}
              >
                {cta}
              </a>
            </div>
          ))}
        </div>

      </div>
    </section>
  );
}
