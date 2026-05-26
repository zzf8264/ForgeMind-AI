import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./app/**/*.{js,ts,jsx,tsx,mdx}", "./components/**/*.{js,ts,jsx,tsx,mdx}"],
  theme: {
    extend: {
      colors: {
        ink: "#101828",
        line: "#d9e2ec",
        brand: "#1d4ed8",
        mint: "#0f766e",
        amber: "#b45309"
      },
      boxShadow: {
        panel: "0 18px 45px rgba(16, 24, 40, 0.08)"
      }
    }
  },
  plugins: []
};

export default config;
