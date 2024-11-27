const fs = require('fs');
const path = require('path');

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

console.log('Starting image verification...');

// Verify images exist
const imagesDir = path.join(__dirname, '..', 'images');
if (!fs.existsSync(imagesDir)) {
    console.error('❌ Images directory not found!');
    process.exit(1);
}

// Check each required image
requiredImages.forEach(image => {
    const imagePath = path.join(imagesDir, image);
    if (fs.existsSync(imagePath)) {
        console.log(`✅ Found: ${image}`);
    } else {
        console.error(`❌ Missing: ${image}`);
    }
});

// Export image paths for use in other scripts
module.exports = imagePaths; 