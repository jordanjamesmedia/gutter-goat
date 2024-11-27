const fs = require('fs');
const path = require('path');

console.log('Starting build process...');

// First, create dist directory
if (!fs.existsSync('dist')) {
    fs.mkdirSync('dist');
}

// Copy entire images directory
console.log('Copying images directory...');
if (fs.existsSync('images')) {
    // Create images directory in dist if it doesn't exist
    if (!fs.existsSync('dist/images')) {
        fs.mkdirSync('dist/images');
    }
    
    // Copy each image
    const images = fs.readdirSync('images');
    images.forEach(file => {
        const sourcePath = path.join('images', file);
        const destPath = path.join('dist/images', file);
        fs.copyFileSync(sourcePath, destPath);
        console.log(`Copied: ${file}`);
    });
} else {
    console.error('Images directory not found!');
    process.exit(1);
}

// Copy other files
const filesToCopy = ['index.html', 'styles.css', 'process-form.php'];
filesToCopy.forEach(file => {
    if (fs.existsSync(file)) {
        fs.copyFileSync(file, path.join('dist', file));
        console.log(`Copied: ${file}`);
    }
});

console.log('Build completed!'); 