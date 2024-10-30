module.exports = {
    devServer: {
        proxy: {
            '/api': {
                target: 'http://backend:8000', // Target your API container
                changeOrigin: true, // Optional: Change the origin of the request
                pathRewrite: {
                    '^/api': '' // Remove the "/api" prefix from the request path
                }
            }

        }
    }
}