const path = require("path");
const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  configureWebpack: {
    entry: ["@/app.js", "@css/app.css"],
    output: { chunkFilename: "js/[name].js?id=[chunkhash]" },
    resolve: {
      alias: {
        vue$: "vue/dist/vue.runtime.esm.js",
        "@": path.resolve("src/js"),
        "@css": path.resolve("src/css")
      }
    },
    plugins: [new BundleTracker({ filename: "./webpack-stats.json" })]
  }
};
