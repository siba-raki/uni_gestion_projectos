/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors: {
        'custom-blue': '#004c6d',
        'custom-lightblue': '#4c7c9b',
        'custom-skyblue': '#86b0cc',
        'custom-paleblue': '#c1e7ff',
        'custom-bg-color': '#232627',
      },
    }
  },
  plugins: []
};