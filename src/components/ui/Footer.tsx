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

const SOCIAL_LINKS = [
  {
    label: "X (Twitter)",
    href: "https://x.com/NextPlayStars",
    icon: (
      <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" aria-hidden>
        <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.744l7.737-8.835L1.254 2.25H8.08l4.253 5.622 5.91-5.622Zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
      </svg>
    ),
  },
  {
    label: "Instagram",
    href: "https://www.instagram.com/nextplaystars/",
    icon: (
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round" aria-hidden>
        <rect x="2" y="2" width="20" height="20" rx="5" ry="5"/>
        <circle cx="12" cy="12" r="4"/>
        <circle cx="17.5" cy="6.5" r="0.8" fill="currentColor" stroke="none"/>
      </svg>
    ),
  },
  {
    label: "TikTok",
    href: "https://www.tiktok.com/@nextplaystars",
    icon: (
      <svg width="14" height="15" viewBox="0 0 24 24" fill="currentColor" aria-hidden>
        <path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-2.88 2.5 2.89 2.89 0 0 1-2.89-2.89 2.89 2.89 0 0 1 2.89-2.89c.28 0 .54.04.79.1V9.01a6.33 6.33 0 0 0-.79-.05 6.34 6.34 0 0 0-6.34 6.34 6.34 6.34 0 0 0 6.34 6.34 6.34 6.34 0 0 0 6.33-6.34V8.69a8.18 8.18 0 0 0 4.78 1.52V6.75a4.85 4.85 0 0 1-1.01-.06z"/>
      </svg>
    ),
  },
];

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

          {/* Follow */}
          <div>
            <p
              className="font-body text-white/25 mb-5"
              style={{ fontSize: "11px", letterSpacing: "0.12em", textTransform: "uppercase", fontWeight: 600 }}
            >
              Follow
            </p>
            <ul className="space-y-3">
              {SOCIAL_LINKS.map(({ label, href, icon }) => (
                <li key={label}>
                  <a
                    href={href}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center gap-2 font-body text-white/55 hover:text-white transition-colors duration-150"
                    style={{ fontSize: "14px" }}
                    aria-label={`NextPlay on ${label}`}
                  >
                    {icon}
                    {label}
                  </a>
                </li>
              ))}
            </ul>
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
