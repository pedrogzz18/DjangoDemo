const path = require('path');

module.exports = {
    mode: 'development',
    entry: './static/readers/ts/confirm_purchase.ts',
    output: {
        filename: 'confirm_purchase.js',
        path: path.resolve(__dirname, 'static/readers/js'),
    },
    module: {
        rules: [
            {
                test: /\.ts$/,
                use: 'ts-loader',
                exclude: /node_modules/,
            },
        ],
    },
    resolve: {
        extensions: ['.ts', '.tsx', '.js'],
    },
};