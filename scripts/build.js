const fs = require('fs');
const path = require('path');

console.log('Starting build process...');

// Create dist directory
if (!fs.existsSync('dist')) {
    fs.mkdirSync('dist', { recursive: true });
}

// Create dist/images directory
if (!fs.existsSync('dist/images')) {
    fs.mkdirSync('dist/images', { recursive: true });
}

// Copy images
if (fs.existsSync('images')) {
    const images = fs.readdirSync('images');
    images.forEach(file => {
        fs.copyFileSync(
            path.join('images', file),
            path.join('dist/images', file)
        );
        console.log(`Copied image: ${file}`);
    });
}

// Copy main files
const files = ['index.html', 'styles.css', 'thank-you.html'];
files.forEach(file => {
    if (fs.existsSync(file)) {
        fs.copyFileSync(file, path.join('dist', file));
        console.log(`Copied: ${file}`);
    }
});

console.log('Build completed!'); 