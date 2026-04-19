const items = [
  {
    num: "01",
    heading: "Coaches aren\u2019t looking for your athlete.",
    body: "A D1 coach manages hundreds of recruits. Your athlete isn\u2019t in their database. Families who get recruited are the ones who put themselves in front of the right coaches \u2014 persistently, professionally, and over years. Waiting for an invitation is a strategy that doesn\u2019t work.",
    photo: "/photos/pallotti-game.jpg",
    photoAlt: "Athlete competing in a high school game",
    photoPosition: "center center",
  },
  {
    num: "02",
    heading: "It\u2019s not one email. It\u2019s hundreds.",
    body: "A serious recruiting effort means personalized outreach to 50\u2013100 coaches, multiple follow-ups, video updates, profile maintenance, phone calls, social posts, and campus visits. Most families underestimate the work by an order of magnitude.",
    photo: "/photos/parent-phone.jpg",
    photoAlt: "Parent working through recruiting outreach on their phone",
    photoPosition: "20% center",
  },
  {
    num: "03",
    heading: "The window closes before most families realize it\u2019s open.",
    body: "Division I programs fill verbal commitments years before signing day. The athletes who get those offers started early \u2014 sophomore year, sometimes earlier. If you\u2019re waiting until junior year to think seriously about recruiting, you are already behind.",
    photo: "/photos/hero-softball-pitcher.jpg",
    photoAlt: "Softball pitcher mid-throw during a high school game",
    photoPosition: "center 20%",
  },
];

const photoFilter = "sepia(0.12) contrast(1.04) brightness(0.87)";

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

        {/* Editorial blocks — photo left, number + text right */}
        <div>
          {items.map(({ num, heading, body, photo, photoAlt, photoPosition }) => (
            <div
              key={num}
              style={{
                paddingTop: "44px",
                paddingBottom: "44px",
                borderTop: "1px solid rgba(15,27,46,0.12)",
              }}
            >
              <div className="grid grid-cols-1 lg:grid-cols-[5fr_7fr] gap-10 lg:gap-16 items-start">

                {/* Photo — left column */}
                <div style={{ overflow: "hidden", borderRadius: "3px" }}>
                  <img
                    src={photo}
                    alt={photoAlt}
                    style={{
                      width: "100%",
                      aspectRatio: "4/3",
                      objectFit: "cover",
                      objectPosition: photoPosition,
                      display: "block",
                      filter: photoFilter,
                    }}
                  />
                </div>

                {/* Number + text — right column */}
                <div>
                  <span
                    className="font-display"
                    style={{
                      fontSize: "clamp(56px, 6vw, 88px)",
                      fontWeight: 300,
                      color: "rgba(15,27,46,0.12)",
                      lineHeight: 1,
                      letterSpacing: "-0.02em",
                      display: "block",
                      marginBottom: "16px",
                      userSelect: "none",
                    }}
                    aria-hidden
                  >
                    {num}
                  </span>
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
                      maxWidth: "520px",
                    }}
                  >
                    {body}
                  </p>
                </div>

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
