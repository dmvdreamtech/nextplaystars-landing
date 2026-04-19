import type { Metadata } from "next";
import { Fraunces, Manrope } from "next/font/google";
import "./globals.css";

const fraunces = Fraunces({
  subsets: ["latin"],
  variable: "--font-fraunces",
  axes: ["opsz", "SOFT", "WONK"],
  display: "swap",
});

const manrope = Manrope({
  subsets: ["latin"],
  variable: "--font-manrope",
  display: "swap",
});

export const metadata: Metadata = {
  title: "NextPlay — Your Athlete's College Recruiting Assistant",
  description:
    "NextPlay handles the college recruiting work for softball and baseball families. Personalized coach outreach, X posts that get noticed, and an assistant you can call anytime. Set it up once. Check in when it matters.",
  keywords: [
    "softball recruiting",
    "baseball recruiting",
    "college recruiting",
    "athletic recruiting",
    "recruiting assistant",
  ],
  openGraph: {
    title: "NextPlay — Your Athlete's College Recruiting Assistant",
    description:
      "NextPlay handles the college recruiting work for softball and baseball families. Set it up once. Check in when it matters.",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={`${fraunces.variable} ${manrope.variable}`}>
      <body>{children}</body>
    </html>
  );
}
