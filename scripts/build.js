const fs = require('fs');
const path = require('path');

console.log('Starting build process...');

// Create dist directory
if (!fs.existsSync('dist')) {
    fs.mkdirSync('dist');
    console.log('Created dist directory');
}

// Copy images directory
if (!fs.existsSync('dist/images')) {
    fs.mkdirSync('dist/images');
}

// Copy all images
const imageFiles = fs.readdirSync('images');
imageFiles.forEach(file => {
    fs.copyFileSync(
        path.join('images', file),
        path.join('dist/images', file)
    );
    console.log(`Copied image: ${file}`);
});

// Copy main files
fs.copyFileSync('index.html', 'dist/index.html');
fs.copyFileSync('styles.css', 'dist/styles.css');

console.log('Build completed!'); 