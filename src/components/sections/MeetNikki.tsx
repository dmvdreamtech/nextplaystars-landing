const chips = [
  { label: "Coach outreach emails", detail: "drafted and sent on your behalf" },
  { label: "X posts and updates", detail: "written and posted on your timeline" },
  { label: "Recruiting questions", detail: "answered 24/7 by phone or text" },
  { label: "Recruiting calendar", detail: "events added automatically" },
];

export default function MeetNikki() {
  return (
    <section
      id="nikki"
      style={{ background: "#0F1B2E", padding: "96px 0", borderTop: "1px solid rgba(255,255,255,0.06)" }}
    >
      <div className="max-w-content mx-auto px-6">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 lg:gap-24 items-center">

          {/* LEFT: Orb — centerpiece */}
          <div className="flex flex-col items-center order-last lg:order-first">

            {/* Orb — 4 rings, full energy */}
            <div
              aria-hidden
              style={{
                position: "relative",
                width: "380px",
                height: "380px",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                perspective: "800px",
              }}
            >
              {/* Ambient glow pool */}
              <div
                style={{
                  position: "absolute",
                  width: "200px",
                  height: "200px",
                  borderRadius: "50%",
                  background: "radial-gradient(circle, rgba(0,172,240,0.28) 0%, transparent 70%)",
                  filter: "blur(24px)",
                }}
              />
              {/* Core */}
              <div
                style={{
                  position: "absolute",
                  width: "88px",
                  height: "88px",
                  borderRadius: "50%",
                  background: "radial-gradient(circle, rgba(255,255,255,0.98) 0%, #00ACF0 36%, rgba(0,172,240,0.14) 66%, transparent 100%)",
                  animation: "orb-pulse 3.5s ease-in-out infinite",
                  zIndex: 2,
                }}
              />
              {/* Ring 1 — innermost */}
              <div
                style={{
                  position: "absolute",
                  width: "188px",
                  height: "188px",
                  borderRadius: "50%",
                  border: "1.5px solid rgba(0,172,240,0.45)",
                  animation: "ring-spin 10s linear infinite",
                  transformStyle: "preserve-3d",
                }}
              />
              {/* Ring 2 */}
              <div
                style={{
                  position: "absolute",
                  width: "256px",
                  height: "256px",
                  borderRadius: "50%",
                  border: "1px solid rgba(0,172,240,0.28)",
                  animation: "ring-spin-rev 16s linear infinite",
                  transformStyle: "preserve-3d",
                }}
              />
              {/* Ring 3 */}
              <div
                style={{
                  position: "absolute",
                  width: "318px",
                  height: "318px",
                  borderRadius: "50%",
                  border: "1px solid rgba(0,172,240,0.16)",
                  animation: "ring-spin 23s linear infinite",
                  transformStyle: "preserve-3d",
                }}
              />
              {/* Ring 4 — outermost */}
              <div
                style={{
                  position: "absolute",
                  width: "372px",
                  height: "372px",
                  borderRadius: "50%",
                  border: "1px solid rgba(0,172,240,0.08)",
                  animation: "ring-spin-rev 32s linear infinite",
                  transformStyle: "preserve-3d",
                }}
              />
            </div>
          </div>

          {/* RIGHT: Content */}
          <div>
            <p
              className="font-body text-[#00ACF0]"
              style={{ fontSize: "11px", letterSpacing: "0.15em", textTransform: "uppercase", fontWeight: 600, marginBottom: "14px" }}
            >
              N.I.K.K.I. by NextPlay
            </p>
            <h2
              className="font-display text-white"
              style={{
                fontSize: "clamp(32px, 3.5vw, 44px)",
                fontWeight: 700,
                lineHeight: 1.1,
                letterSpacing: "-0.02em",
                marginBottom: "20px",
              }}
            >
              Your recruiting assistant.<br />On it before you ask.
            </h2>
            <p
              className="font-body"
              style={{
                fontSize: "17px",
                lineHeight: 1.65,
                color: "rgba(255,255,255,0.58)",
                maxWidth: "440px",
                marginBottom: "40px",
              }}
            >
              Call N.I.K.K.I. anytime. Ask any recruiting question and get real-time advice from a recruiting assistant that knows your athlete, your target schools, and where you are in the process.
            </p>

            {/* Use-case chips — 2-column grid */}
            <div
              style={{
                display: "grid",
                gridTemplateColumns: "repeat(2, 1fr)",
                gap: "12px",
                marginBottom: "36px",
              }}
            >
              {chips.map(({ label, detail }) => (
                <div
                  key={label}
                  style={{
                    background: "rgba(0,172,240,0.06)",
                    border: "1px solid rgba(0,172,240,0.16)",
                    borderRadius: "12px",
                    padding: "18px 20px",
                  }}
                >
                  <p className="font-body text-white" style={{ fontSize: "14px", fontWeight: 600, marginBottom: "5px" }}>
                    {label}
                  </p>
                  <p className="font-body text-white/40" style={{ fontSize: "12px", lineHeight: 1.4 }}>
                    {detail}
                  </p>
                </div>
              ))}
            </div>

            <p
              className="font-body text-white/28"
              style={{
                fontSize: "13px",
                lineHeight: 1.65,
                borderTop: "1px solid rgba(255,255,255,0.06)",
                paddingTop: "20px",
                maxWidth: "400px",
              }}
            >
              N.I.K.K.I. adds events to your recruiting calendar automatically. Call with a question anytime — you&apos;ll get a real response, not a form.
            </p>
          </div>

        </div>
      </div>
    </section>
  );
}
