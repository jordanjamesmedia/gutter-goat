const fs = require('fs');
const path = require('path');

console.log('Starting build process...');

// Create dist directory
if (!fs.existsSync('dist')) {
    fs.mkdirSync('dist');
    console.log('Created dist directory');
}

// Create dist/images directory
if (!fs.existsSync('dist/images')) {
    fs.mkdirSync('dist/images', { recursive: true });
    console.log('Created dist/images directory');
}

// Check if images directory exists before trying to copy
if (fs.existsSync('images')) {
    console.log('Found images directory, copying files...');
    const imageFiles = fs.readdirSync('images');
    imageFiles.forEach(file => {
        try {
            fs.copyFileSync(
                path.join('images', file),
                path.join('dist/images', file)
            );
            console.log(`✅ Copied image: ${file}`);
        } catch (error) {
            console.error(`❌ Error copying ${file}:`, error.message);
        }
    });
} else {
    console.warn('⚠️ Warning: images directory not found');
    // Create empty images directory
    fs.mkdirSync('images', { recursive: true });
    console.log('Created empty images directory');
}

// Copy main files with error handling
try {
    fs.copyFileSync('index.html', 'dist/index.html');
    console.log('✅ Copied index.html');
    fs.copyFileSync('styles.css', 'dist/styles.css');
    console.log('✅ Copied styles.css');
} catch (error) {
    console.error('❌ Error copying main files:', error.message);
}

console.log('Build completed!'); 