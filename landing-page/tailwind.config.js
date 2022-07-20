/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./*.html'],
  theme: {
    extend: {
      colors: {
        pri: "#005B64",
        sec: "#00BBD6",
        darkPri: "#0B2123",
        lightPri: "rgba(0, 91, 100, 0.7)",
        semiPri: "rgba(0, 91, 100, 0.95)",
        veryLightPri: "rgba(0, 91, 100, 0.35)"
      },
      animation: {
        'btn': 'bg 1s ease-in forwards',
      },
      keyframes: {
        bg: {
          '50%': {background: 'rgba(0, 91, 100, 0.5)'},
          '100%': {background: '#005B64'}
        },
      },
      backgroundImage: {
        'logo': "url('../img/hmis-logo.svg')",
        'hero': "url('../img/hero-bg.jpg')",
        'services': "url('../img/services-bg.jpg')",
        'why-us': "url('../img/why-bg.webp')",
      }
    },
  },
  plugins: [],
}
