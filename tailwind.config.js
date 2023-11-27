/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./**/*.html', './**/*.js'],
  theme: {
    extend: {
      width: {
        'calc': 'calc(100% - 2rem)',
      }
    },
    spacing: {
      '1': '8px',
      '2': '12px',
      // ...
      'some_key': {
        '1': '24px',
        '1.5': '36px', // make sure this is set
        // ...
      },
    },
    extend: {},
  },
  plugins: [],
}

