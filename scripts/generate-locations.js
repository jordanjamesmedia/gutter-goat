const fs = require('fs');
const path = require('path');

// Read template
const template = fs.readFileSync(path.join(__dirname, 'template.html'), 'utf8');

// Locations data with specific content
const locations = {
    'helensburgh': {
        name: 'Helensburgh',
        postcode: '2508',
        slug: 'helensburgh'
    },
    'stanwell-park': {
        name: 'Stanwell Park',
        postcode: '2508',
        slug: 'stanwell-park'
    },
    'coalcliff': {
        name: 'Coalcliff',
        postcode: '2508',
        slug: 'coalcliff'
    },
    'scarborough': {
        name: 'Scarborough',
        postcode: '2515',
        slug: 'scarborough'
    },
    'wombarra': {
        name: 'Wombarra',
        postcode: '2515',
        slug: 'wombarra'
    },
    'coledale': {
        name: 'Coledale',
        postcode: '2515',
        slug: 'coledale'
    },
    'austinmer': {
        name: 'Austinmer',
        postcode: '2515',
        slug: 'austinmer'
    },
    'thirroul': {
        name: 'Thirroul',
        postcode: '2515',
        slug: 'thirroul'
    },
    'bulli': {
        name: 'Bulli',
        postcode: '2516',
        slug: 'bulli'
    },
    'woonona': {
        name: 'Woonona',
        postcode: '2517',
        slug: 'woonona'
    },
    // Add all other locations...
};

// Hero images to rotate through
const heroImages = [
    'gutter-tree.png',
    'gutter-flowers.jpg',
    'gutter-leaves.jpg'
];

// Create locations directory if it doesn't exist
const locationsDir = path.join(__dirname, '..', 'locations');
if (!fs.existsSync(locationsDir)) {
    fs.mkdirSync(locationsDir, 0755, true);
}

// Generate pages for each location
Object.entries(locations).forEach(([slug, data], index) => {
    // Get hero image for this location
    const heroImage = heroImages[index % heroImages.length];
    
    // Replace all placeholders in template
    let content = template
        .replace(/\[LOCATION\]/g, data.name)
        .replace(/\[POSTCODE\]/g, data.postcode)
        .replace(/\[LOCATION_SLUG\]/g, data.slug)
        .replace(/\[HERO_IMAGE\]/g, heroImage);
    
    // Write the file
    const outputFile = path.join(locationsDir, `${slug}.html`);
    try {
        fs.writeFileSync(outputFile, content);
        console.log(`Created: ${slug}.html`);
        
        // Verify file was created
        if (fs.existsSync(outputFile)) {
            console.log(`Verified: ${slug}.html exists`);
        }
    } catch (error) {
        console.error(`Error creating ${slug}.html:`, error);
    }
});

// Generate sitemap
const generateSitemap = () => {
    const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://guttergoat.com.au/</loc>
        <priority>1.0</priority>
    </url>
    ${Object.entries(locations).map(([slug, data]) => `
    <url>
        <loc>https://guttergoat.com.au/locations/${slug}.html</loc>
        <priority>0.8</priority>
    </url>`).join('\n')}
</urlset>`;

    fs.writeFileSync(path.join(__dirname, '..', 'sitemap.xml'), sitemap);
    console.log('Sitemap generated');
};

// Run the sitemap generation
generateSitemap();

console.log('\nScript completed successfully!');
console.log(`Generated ${Object.keys(locations).length} location pages`); 