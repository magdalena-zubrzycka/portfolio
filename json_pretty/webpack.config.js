const webpack = require('webpack');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const config = {
    entry: {
        bundle: __dirname + '/index.jsx',
    },
    output: {
        path: __dirname + '/dist',
        filename: '[name].js',
    },
    resolve: {
        extensions: ['.js', '.jsx', '.css', '.scss']
    },
    module: {
        rules: [
            {
                test: /\.jsx?/,
                exclude: [/node_modules/, /flow-typed/],
                use: 'babel-loader'
            },
            {
                test: /\.(jpg|png|gif|svg)$/,
                exclude: [/node_modules/, /flow-typed/],
                use: [
                    {
                        loader: 'file-loader',
                        options: {
                            name: '[path][name].[ext]',
                            outputPath: '/client/'}
                    },
                ]
            },
            {
                test: /\.scss$/,
                exclude: [/node_modules/, /flow-typed/],
                use: [
                    MiniCssExtractPlugin.loader,
                    "css-loader?localIdentName=[name]__[local]___[hash:base64:5]",
                    "sass-loader"
                ]
            }
        ]
    },
    plugins: [
        new MiniCssExtractPlugin({
            // Options similar to the same options in webpackOptions.output
            // both options are optional
            filename: "[name].css",
            chunkFilename: "[id].css"
        })
    ],
    watchOptions: {
        ignored: [/node_modules/, /flow-typed/],
        poll: 1000, // Check for changes every second
    }
}

module.exports = config;
