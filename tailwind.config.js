module.exports = {
  content: [
    './mi_app/templates/**/*.html',
    './mi_app/templates/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        customBlue: '#1DA1F2',
        customGreen: '#34D399',
      },
      fontSize: {
        'xxs': '0.6rem',
        'xxl': '1.75rem',
      },
      spacing: {
        '72': '18rem',
        '84': '21rem',
        '96': '24rem',
      },
      fontFamily: {
        sans: ['Roboto', 'sans-serif'],
        display: ['Oswald', 'sans-serif'],
        body: ['"Open Sans"', 'sans-serif'],
      },
      borderRadius: {
        'xl': '1rem',
        '2xl': '1.5rem',
      },
      boxShadow: {
        'strong': '0 4px 6px rgba(0, 0, 0, 0.4)',
        'soft': '0 2px 4px rgba(0, 0, 0, 0.1)',
      },
    },
  },
  plugins: [],
}
