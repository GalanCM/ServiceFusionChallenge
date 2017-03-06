module.exports = {
  entry: './components/main.js',
  output: {
    path: "./static/",
    publicPath: "./build/",
    filename: 'bundle.js'
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader?-attrs',
        options: {
          postcss: [require('autoprefixer')()]
        }
      },
      {
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: /node_modules/,
        query: {
          presets: ['es2015'],
          plugins: ['transform-runtime']
        }
      },
      {
        test: /\.(png|jpg|gif)$/,
        loader: 'url-loader',
        query: {
          limit: 10000,
          name: './images/[name].[ext]?[hash]'
        }
      }
    ]
  }
};
