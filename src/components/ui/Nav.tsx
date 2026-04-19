"use client";

import { useState, useEffect } from "react";
import Image from "next/image";
import Link from "next/link";

const APP_URL = "https://www.nextplayrecruiting.app";

export default function Nav() {
  const [scrolled, setScrolled] = useState(false);
  const [menuOpen, setMenuOpen] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 12);
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <nav
      className="fixed top-0 left-0 right-0 z-50 transition-all duration-300"
      style={{
        background: scrolled
          ? "rgba(15,27,46,0.92)"
          : "rgba(15,27,46,0.75)",
        backdropFilter: "blur(16px)",
        WebkitBackdropFilter: "blur(16px)",
        borderBottom: scrolled
          ? "1px solid rgba(255,255,255,0.08)"
          : "1px solid transparent",
      }}
    >
      <div className="max-w-content mx-auto px-6 flex items-center justify-between h-16">
        {/* Logo */}
        <Link href="/" aria-label="NextPlay home" className="flex-shrink-0">
          <Image
            src="/logo.png"
            alt="NextPlay"
            width={180}
            height={41}
            priority
            className="h-10 w-auto"
          />
        </Link>

        {/* Desktop links */}
        <div className="hidden md:flex items-center gap-2">
          <a
            href={APP_URL}
            className="text-sm font-medium text-white/70 hover:text-white px-4 py-2 rounded-lg transition-colors duration-150"
          >
            Sign In
          </a>
          <a
            href={`${APP_URL}/signup`}
            className="text-sm font-semibold text-ink bg-[#00ACF0] hover:bg-[#0099D8] px-5 py-2.5 rounded-lg transition-colors duration-150"
          >
            Start Free
          </a>
        </div>

        {/* Hamburger */}
        <button
          className="md:hidden flex flex-col gap-1.5 p-2 cursor-pointer"
          onClick={() => setMenuOpen(!menuOpen)}
          aria-label="Toggle menu"
          aria-expanded={menuOpen}
        >
          <span
            className="block w-6 h-0.5 bg-white rounded transition-transform duration-200"
            style={{ transform: menuOpen ? "rotate(45deg) translate(3px,3px)" : "none" }}
          />
          <span
            className="block w-6 h-0.5 bg-white rounded transition-opacity duration-200"
            style={{ opacity: menuOpen ? 0 : 1 }}
          />
          <span
            className="block w-6 h-0.5 bg-white rounded transition-transform duration-200"
            style={{ transform: menuOpen ? "rotate(-45deg) translate(3px,-3px)" : "none" }}
          />
        </button>
      </div>

      {/* Mobile menu */}
      {menuOpen && (
        <div
          className="md:hidden flex flex-col gap-1 px-6 pb-5 pt-2"
          style={{ borderTop: "1px solid rgba(255,255,255,0.08)", background: "rgba(15,27,46,0.98)" }}
        >
          <a href="#how" onClick={() => setMenuOpen(false)} className="text-white/80 py-2.5 text-base font-medium hover:text-white">How It Works</a>
          <a href="#nikki" onClick={() => setMenuOpen(false)} className="text-white/80 py-2.5 text-base font-medium hover:text-white">Meet N.I.K.K.I.</a>
          <a href="#pricing" onClick={() => setMenuOpen(false)} className="text-white/80 py-2.5 text-base font-medium hover:text-white">Pricing</a>
          <a href={APP_URL} className="text-white/60 py-2.5 text-base font-medium hover:text-white">Sign In</a>
          <a
            href={`${APP_URL}/signup`}
            className="mt-2 text-center text-base font-semibold text-ink bg-[#00ACF0] py-3 rounded-lg"
          >
            Start Free →
          </a>
        </div>
      )}
    </nav>
  );
}
