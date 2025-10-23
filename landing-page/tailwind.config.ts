import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        // Surfing Digital Brand Colors
        navy: {
          DEFAULT: '#001639',
          dark: '#001639',
        },
        'navy-light': '#003453',
        teal: {
          DEFAULT: '#00586A',
          dark: '#00586A',
        },
        'teal-light': '#0BB7B7',
        blue: {
          DEFAULT: '#0056A0',
          light: '#009FD5',
        },
        pink: '#ED4A6D',
        purple: '#9D80B9',
        peach: '#FFD08D',
        'light-pink': '#E2AAC4',
      },
      fontFamily: {
        'dm-sans': ['var(--font-dm-sans)', 'sans-serif'],
        'open-sans': ['var(--font-open-sans)', 'sans-serif'],
      },
    },
  },
  plugins: [],
};
export default config;

