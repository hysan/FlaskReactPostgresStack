var webpack = require('webpack');
var path = require('path');

module.exports = {
    entry: {
        main: path.resolve(__dirname, 'project/server/static/scripts/jsx', 'main.js'),
        api: path.resolve(__dirname, 'project/server/static/scripts/jsx', 'api.js'),
        react: ['react', 'react-dom']
    },
    output: {
        path: path.resolve(__dirname, 'project/server/static/scripts/js'),
        filename: '[name].js'
    },
    plugins: [
        new webpack.optimize.CommonsChunkPlugin({
            name: 'react',
            minChunks: function (module) {
                // this assumes your vendor imports exist in the node_modules directory
                return module.context && module.context.indexOf('node_modules') !== -1;
            }
        }),
        //CommonChunksPlugin will now extract all the common modules from vendor and main bundles
        new webpack.optimize.CommonsChunkPlugin({
            name: 'manifest' //But since there are no more common modules between them we end up with just the runtime code included in the manifest file
        })
    ],
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /(node_modules)/,
                use: [{
                    loader: 'babel-loader',
                    options: {
                        presets: [['env', { modules: false }], "react"],
                        plugins: [
                            'syntax-dynamic-import',
                            'transform-async-to-generator',
                            'transform-regenerator',
                            'transform-runtime'
                        ]
                    }
                }]
            }
        ]
    }
};