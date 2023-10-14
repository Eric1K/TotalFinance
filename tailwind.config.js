/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./pages/*.{html,js}","./node_modules/flowbite/**/*.js"],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('flowbite/plugin')({
      charts: true,
  }),
  ],
}

