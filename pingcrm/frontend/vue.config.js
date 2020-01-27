const path = require("path");
const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  publicPath: "/static/assets",
  outputDir: "dist/assets",
  configureWebpack: {
    entry: "@/main.js",
    output: { chunkFilename: "js/[name].js?id=[chunkhash]" },
    optimization: {
      splitChunks: {
        chunks: "all"
      }
    },
    resolve: {
      alias: {
        vue$: "vue/dist/vue.runtime.esm.js",
        "@": path.resolve("src/js")
      }
    },
    plugins: [new BundleTracker({ filename: "./webpack-stats.json" })]
  }
};
