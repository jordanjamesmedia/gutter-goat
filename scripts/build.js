const fs = require('fs');
const path = require('path');

console.log('Starting build process...');

// Required images list
const requiredImages = [
    'gutter-goat-logo.png',
    'gutter-tree.png',
    'gutter-flowers.jpg',
    'gutter-leaves.jpg',
    'service-areas-map.png'
];

// Create dist directory
if (!fs.existsSync('dist')) {
    fs.mkdirSync('dist');
    console.log('Created dist directory');
}

// Handle images
console.log('\nHandling images...');
let imageErrors = [];
let missingImages = [];

// Create images directory in dist
if (!fs.existsSync('dist/images')) {
    fs.mkdirSync('dist/images', { recursive: true });
    console.log('Created dist/images directory');
}

// Check and copy images
if (fs.existsSync('images')) {
    const images = fs.readdirSync('images');
    
    // Check for required images
    requiredImages.forEach(requiredImage => {
        if (!images.includes(requiredImage)) {
            missingImages.push(requiredImage);
        }
    });

    // Copy available images
    images.forEach(file => {
        try {
            const sourcePath = path.join('images', file);
            const destPath = path.join('dist/images', file);
            fs.copyFileSync(sourcePath, destPath);
            console.log(`✅ Copied: ${file}`);
        } catch (error) {
            imageErrors.push({ file, error: error.message });
            console.error(`❌ Error copying ${file}: ${error.message}`);
        }
    });
} else {
    console.error('❌ Images directory not found!');
    console.log('Creating images directory...');
    fs.mkdirSync('images', { recursive: true });
    missingImages = [...requiredImages];
}

// Copy other files
console.log('\nCopying other files...');
const filesToCopy = ['index.html', 'styles.css', 'process-form.php'];
filesToCopy.forEach(file => {
    try {
        if (fs.existsSync(file)) {
            fs.copyFileSync(file, path.join('dist', file));
            console.log(`✅ Copied: ${file}`);
        } else {
            console.error(`❌ Missing file: ${file}`);
        }
    } catch (error) {
        console.error(`❌ Error copying ${file}: ${error.message}`);
    }
});

// Add Cloudflare specific files
const cloudflareFiles = [
    '_redirects',
    '_headers',
    '.cloudflare/config.json'
];

cloudflareFiles.forEach(file => {
    if (fs.existsSync(file)) {
        const destPath = path.join('dist', file);
        const destDir = path.dirname(destPath);
        
        if (!fs.existsSync(destDir)) {
            fs.mkdirSync(destDir, { recursive: true });
        }
        
        fs.copyFileSync(file, destPath);
        console.log(`✅ Copied Cloudflare config: ${file}`);
    }
});

// Build summary
console.log('\nBuild Summary:');
if (missingImages.length > 0) {
    console.error('❌ Missing required images:');
    missingImages.forEach(img => console.error(`   - ${img}`));
}
if (imageErrors.length > 0) {
    console.error('❌ Image copy errors:');
    imageErrors.forEach(err => console.error(`   - ${err.file}: ${err.error}`));
}

// Exit with error if missing required images
if (missingImages.length > 0) {
    console.error('\n❌ Build failed: Missing required images');
    process.exit(1);
} else {
    console.log('\n✅ Build completed successfully!');
}

// Add directory listing at the end of the build
console.log('\nFinal directory structure:');
function listDir(dir, level = 0) {
    const files = fs.readdirSync(dir);
    files.forEach(file => {
        const filePath = path.join(dir, file);
        console.log('  '.repeat(level) + '├── ' + file);
        if (fs.statSync(filePath).isDirectory()) {
            listDir(filePath, level + 1);
        }
    });
}
listDir('dist'); 