/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './public/**/*.html',
    './src/**/*.{vue,js,ts,jsx,tsx}'
  ],
  theme: {
    extend: {
      colors: {
        'brown1': '#fbe4ca',
        'brown2': '#fbd5bb',
        'brown3': '#c18661',
        'brown4': '#876353',
        'dark1': '#0d0404',
      },
    },
  },
  plugins: [],
}
