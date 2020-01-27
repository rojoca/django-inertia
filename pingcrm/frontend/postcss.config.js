const purgecss = require("@fullhuman/postcss-purgecss")({
  // Paths to all of the template files in your project
  content: ["./src/**/*.html", "./public/**/*.html", "./src/**/*.vue"],

  // Include any special characters you're using in this regular expression
  defaultExtractor: content => content.match(/[\w-/:]+(?<!:)/g) || []
});

module.exports = {
  plugins: [
    require("postcss-import"),
    require("postcss-nesting"),
    require("tailwindcss"),
    require("autoprefixer"),
    ...(process.env.NODE_ENV === "production" ? [purgecss] : [])
  ]
};
