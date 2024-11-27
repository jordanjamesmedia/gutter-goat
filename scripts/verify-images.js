const fs = require('fs');
const path = require('path');
const https = require('https');

// List of required images
const requiredImages = [
    'gutter-flowers.jpg',
    'gutter-goat-logo.png',
    'gutter-leaves.jpg',
    'gutter-tree.png',
    'service-areas-map.png'
];

// Image paths in use
const imagePaths = {
    logo: 'https://guttergoat.com.au/images/gutter-goat-logo.png',
    tree: 'https://guttergoat.com.au/images/gutter-tree.png',
    flowers: 'https://guttergoat.com.au/images/gutter-flowers.jpg',
    leaves: 'https://guttergoat.com.au/images/gutter-leaves.jpg',
    map: 'https://guttergoat.com.au/images/service-areas-map.png'
};

console.log('Starting comprehensive image verification...');

// 1. Check local files
console.log('\nChecking local files:');
const imagesDir = path.join(__dirname, '..', 'images');
if (!fs.existsSync(imagesDir)) {
    console.error('❌ Images directory not found!');
} else {
    requiredImages.forEach(image => {
        const imagePath = path.join(imagesDir, image);
        if (fs.existsSync(imagePath)) {
            const stats = fs.statSync(imagePath);
            console.log(`✅ Found: ${image} (${(stats.size / 1024).toFixed(2)} KB)`);
        } else {
            console.error(`❌ Missing: ${image}`);
        }
    });
}

// 2. Check live URLs
console.log('\nChecking live URLs:');
Object.entries(imagePaths).forEach(([key, url]) => {
    const request = https.get(url, (res) => {
        console.log(`✅ ${key}: ${res.statusCode} ${res.statusMessage}`);
    }).on('error', (err) => {
        console.error(`❌ ${key}: Error accessing URL - ${err.message}`);
    });
});

// Export image paths
module.exports = imagePaths; 