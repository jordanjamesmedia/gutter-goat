const fs = require('fs');
const path = require('path');

// Read template
const template = fs.readFileSync('scripts/template.html', 'utf8');

// Create locations directory
if (!fs.existsSync('locations')) {
    fs.mkdirSync('locations');
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
    
    fs.writeFileSync(`locations/${slug}.html`, content);
    console.log(`Created: ${slug}.html`);
});

console.log('Generation complete!'); 