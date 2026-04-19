import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./src/**/*.{js,ts,jsx,tsx,mdx}"],
  theme: {
    extend: {
      colors: {
        ink:    "#0F1B2E",
        cyan:   "#00ACF0",
        cream:  "#F5F0E8",
        "cream-2": "#EDE8DF",
      },
      fontFamily: {
        display: ["var(--font-fraunces)", "Georgia", "serif"],
        body:    ["var(--font-manrope)", "system-ui", "sans-serif"],
      },
      maxWidth: {
        content: "1140px",
      },
    },
  },
  plugins: [],
};

export default config;
