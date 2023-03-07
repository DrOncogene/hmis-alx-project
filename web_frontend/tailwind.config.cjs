/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors: {
        "pri": "#886C63",
        "lightPri": "#ddd2d0",
        "sec": "#F7C815",
        "lightSec": "rgba(247, 200, 21, 0.5)"
      },
      gridTemplateColumns: {
        "default": "1fr 2fr"
      },
      backgroundImage: {
        'homeBg': "url('/src/lib/assets/health-software.jpg')",
        'hmis': "url('/src/lib/assets/hmis-logo.jpg')"
      },
      boxShadow: {
        'side-menu': '-5px 5px 15px 5px #555 inset'
      }
    },
  },
  plugins: [],
}
