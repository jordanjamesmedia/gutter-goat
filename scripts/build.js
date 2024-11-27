const fs = require('fs');
const path = require('path');

// Create dist directory
if (!fs.existsSync('dist')) {
    fs.mkdirSync('dist');
}

// Copy static files
fs.copyFileSync('index.html', 'dist/index.html');
fs.copyFileSync('styles.css', 'dist/styles.css');

// Copy images directory
if (!fs.existsSync('dist/images')) {
    fs.mkdirSync('dist/images');
}
fs.readdirSync('images').forEach(file => {
    fs.copyFileSync(`images/${file}`, `dist/images/${file}`);
});

// Run location generator
require('./generate-locations.js'); 