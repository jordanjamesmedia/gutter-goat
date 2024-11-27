const fs = require('fs');
const path = require('path');

// Read template
const template = fs.readFileSync('scripts/template.html', 'utf8');

// Create locations directory in dist
if (!fs.existsSync('dist/locations')) {
    fs.mkdirSync('dist/locations');
}

// Generate pages
const locations = {
    'helensburgh': { name: 'Helensburgh', postcode: '2508' }
    // ... other locations
};

Object.entries(locations).forEach(([slug, data]) => {
    const content = template
        .replace(/\[LOCATION\]/g, data.name)
        .replace(/\[POSTCODE\]/g, data.postcode);
    
    fs.writeFileSync(`dist/locations/${slug}.html`, content);
    console.log(`Created: ${slug}.html`);
});

console.log('Generation complete!'); 