const fs = require('fs');
const path = require('path');

console.log('Starting build process...');

// Create all required directories
const dirs = [
    'dist',
    'dist/images',
    'dist/locations',
    'dist/scripts'
];

dirs.forEach(dir => {
    if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
        console.log(`Created directory: ${dir}`);
    }
});

// Copy images with verification
const requiredImages = [
    'gutter-goat-logo.png',
    'gutter-tree.png',
    'gutter-flowers.jpg',
    'gutter-leaves.jpg',
    'service-areas-map.png'
];

requiredImages.forEach(image => {
    const sourcePath = path.join('images', image);
    const destPath = path.join('dist/images', image);
    
    if (fs.existsSync(sourcePath)) {
        fs.copyFileSync(sourcePath, destPath);
        console.log(`✅ Copied ${image}`);
    } else {
        console.error(`❌ Missing required image: ${image}`);
    }
});

// Copy main files
const mainFiles = [
    'index.html',
    'styles.css',
    'robots.txt',
    '_headers'
];

mainFiles.forEach(file => {
    if (fs.existsSync(file)) {
        fs.copyFileSync(file, `dist/${file}`);
        console.log(`✅ Copied ${file}`);
    }
});

console.log('Build completed!'); 