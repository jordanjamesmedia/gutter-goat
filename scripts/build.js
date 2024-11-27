const fs = require('fs');
const path = require('path');

console.log('Starting full build process...');

// Create all necessary directories
const dirs = ['dist', 'dist/images', 'dist/locations', 'dist/scripts'];
dirs.forEach(dir => {
    if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
        console.log(`Created directory: ${dir}`);
    }
});

// Copy static files
const staticFiles = [
    'index.html',
    'styles.css',
    'thank-you.html',
    'robots.txt',
    '_headers'
];

staticFiles.forEach(file => {
    if (fs.existsSync(file)) {
        fs.copyFileSync(file, `dist/${file}`);
        console.log(`Copied: ${file}`);
    }
});

// Copy images
if (fs.existsSync('images')) {
    const images = fs.readdirSync('images');
    images.forEach(image => {
        fs.copyFileSync(
            path.join('images', image),
            path.join('dist/images', image)
        );
        console.log(`Copied image: ${image}`);
    });
}

// Copy scripts
if (fs.existsSync('scripts')) {
    const scripts = fs.readdirSync('scripts').filter(file => file.endsWith('.js'));
    scripts.forEach(script => {
        fs.copyFileSync(
            path.join('scripts', script),
            path.join('dist/scripts', script)
        );
        console.log(`Copied script: ${script}`);
    });
}

// Generate location pages
console.log('Generating location pages...');
require('./generate-locations.js');

console.log('Build completed successfully!'); 