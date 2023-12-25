/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./flaskmain/templates/*.{html,js}","./node_modules/flowbite/**/*.js"],
  theme: {
    extend: {
      colors: {
        cblue: "#172554"
      }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('flowbite/plugin')({
      charts: true,
  }),
  ],
}

