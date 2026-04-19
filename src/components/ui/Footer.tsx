import Image from "next/image";

const APP_URL = "https://www.nextplayrecruiting.app";

const PRODUCT_LINKS = [
  { label: "The Reality", href: "#reality" },
  { label: "Meet N.I.K.K.I.", href: "#nikki" },
  { label: "How It Works", href: "#how" },
  { label: "About", href: "#founder" },
  { label: "Pricing", href: "#pricing" },
];

const COMPANY_LINKS = [
  { label: "Sign In", href: APP_URL },
  { label: "Start Free", href: `${APP_URL}/signup` },
];

// Update X handle with the real @handle before launch
const X_URL = "https://x.com/nextplayrecruit";

export default function Footer() {
  const year = new Date().getFullYear();

  return (
    <footer
      style={{
        background: "#07111E",
        borderTop: "1px solid rgba(255,255,255,0.06)",
        paddingTop: "64px",
        paddingBottom: "40px",
      }}
    >
      <div className="max-w-content mx-auto px-6">

        {/* Top: logo + columns */}
        <div className="grid grid-cols-1 lg:grid-cols-[2fr_1fr_1fr_1fr] gap-12 mb-16">

          {/* Logo + tagline */}
          <div>
            <Image
              src="/logo.png"
              alt="NextPlay"
              width={160}
              height={37}
              className="h-8 w-auto mb-4"
            />
            <p
              className="font-body text-white/35"
              style={{ fontSize: "14px", lineHeight: 1.6, maxWidth: "260px" }}
            >
              College recruiting handled. Coach outreach, social posts, and a recruiting assistant available anytime.
            </p>
          </div>

          {/* Product */}
          <div>
            <p
              className="font-body text-white/25 mb-5"
              style={{ fontSize: "11px", letterSpacing: "0.12em", textTransform: "uppercase", fontWeight: 600 }}
            >
              Product
            </p>
            <ul className="space-y-3">
              {PRODUCT_LINKS.map(({ label, href }) => (
                <li key={label}>
                  <a
                    href={href}
                    className="font-body text-white/55 hover:text-white transition-colors duration-150"
                    style={{ fontSize: "14px" }}
                  >
                    {label}
                  </a>
                </li>
              ))}
            </ul>
          </div>

          {/* Company */}
          <div>
            <p
              className="font-body text-white/25 mb-5"
              style={{ fontSize: "11px", letterSpacing: "0.12em", textTransform: "uppercase", fontWeight: 600 }}
            >
              Account
            </p>
            <ul className="space-y-3">
              {COMPANY_LINKS.map(({ label, href }) => (
                <li key={label}>
                  <a
                    href={href}
                    className="font-body text-white/55 hover:text-white transition-colors duration-150"
                    style={{ fontSize: "14px" }}
                  >
                    {label}
                  </a>
                </li>
              ))}
            </ul>
          </div>

          {/* Contact */}
          <div>
            <p
              className="font-body text-white/25 mb-5"
              style={{ fontSize: "11px", letterSpacing: "0.12em", textTransform: "uppercase", fontWeight: 600 }}
            >
              Follow
            </p>
            <a
              href={X_URL}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-2 font-body text-white/55 hover:text-white transition-colors duration-150"
              style={{ fontSize: "14px" }}
              aria-label="NextPlay on X (Twitter)"
            >
              {/* X / Twitter wordmark icon */}
              <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" aria-hidden>
                <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.744l7.737-8.835L1.254 2.25H8.08l4.253 5.622 5.91-5.622Zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
              </svg>
              X (Twitter)
            </a>
          </div>

        </div>

        {/* Bottom rule + legal */}
        <div
          className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4"
          style={{ borderTop: "1px solid rgba(255,255,255,0.06)", paddingTop: "28px" }}
        >
          <p
            className="font-body text-white/25"
            style={{ fontSize: "13px" }}
          >
            © {year} NextPlay Recruiting. All rights reserved.
          </p>
          <p
            className="font-body text-white/20"
            style={{ fontSize: "13px", letterSpacing: "0.03em" }}
          >
            Built by coaches, for families.
          </p>
        </div>

      </div>
    </footer>
  );
}
