import os
import re

# List of locations with their postcodes
locations = {
    'helensburgh': {'name': 'Helensburgh', 'postcode': '2508'},
    'stanwell-park': {'name': 'Stanwell Park', 'postcode': '2508'},
    'coalcliff': {'name': 'Coalcliff', 'postcode': '2508'},
    'scarborough': {'name': 'Scarborough', 'postcode': '2515'},
    'wombarra': {'name': 'Wombarra', 'postcode': '2515'},
    'coledale': {'name': 'Coledale', 'postcode': '2515'},
    'austinmer': {'name': 'Austinmer', 'postcode': '2515'},
    'thirroul': {'name': 'Thirroul', 'postcode': '2515'},
    'bulli': {'name': 'Bulli', 'postcode': '2516'},
    'woonona': {'name': 'Woonona', 'postcode': '2517'},
    'corrimal': {'name': 'Corrimal', 'postcode': '2518'},
    'towradgi': {'name': 'Towradgi', 'postcode': '2518'},
    'fairy-meadow': {'name': 'Fairy Meadow', 'postcode': '2519'},
    'mount-ousley': {'name': 'Mount Ousley', 'postcode': '2519'},
    'north-wollongong': {'name': 'North Wollongong', 'postcode': '2500'},
    'wollongong': {'name': 'Wollongong', 'postcode': '2500'},
    'mangerton': {'name': 'Mangerton', 'postcode': '2500'},
    'mount-keira': {'name': 'Mount Keira', 'postcode': '2500'},
    'coniston': {'name': 'Coniston', 'postcode': '2500'},
    'port-kembla': {'name': 'Port Kembla', 'postcode': '2505'},
    'warrawong': {'name': 'Warrawong', 'postcode': '2502'},
    'lake-heights': {'name': 'Lake Heights', 'postcode': '2502'},
    'berkeley': {'name': 'Berkeley', 'postcode': '2506'},
    'unanderra': {'name': 'Unanderra', 'postcode': '2526'},
    'kembla-grange': {'name': 'Kembla Grange', 'postcode': '2526'},
    'dapto': {'name': 'Dapto', 'postcode': '2530'},
    'horsley': {'name': 'Horsley', 'postcode': '2530'},
    'albion-park': {'name': 'Albion Park', 'postcode': '2527'},
    'shellharbour': {'name': 'Shellharbour', 'postcode': '2529'},
    'shell-cove': {'name': 'Shell Cove', 'postcode': '2529'},
    'dunmore': {'name': 'Dunmore', 'postcode': '2529'},
    'jamberoo': {'name': 'Jamberoo', 'postcode': '2533'},
    'kiama': {'name': 'Kiama', 'postcode': '2533'},
    'gerringong': {'name': 'Gerringong', 'postcode': '2534'},
    'berry': {'name': 'Berry', 'postcode': '2535'},
    'shoalhaven-heads': {'name': 'Shoalhaven Heads', 'postcode': '2535'}
}

# Generate location links HTML
location_links = ''
for slug, data in sorted(locations.items(), key=lambda x: x[1]['name']):
    location_links += f'<li><a href="../locations/{slug}.html">{data["name"]} ({data["postcode"]})</a></li>\n'

# CSS styles for the dropdown
dropdown_styles = '''
<style>
.locations-dropdown {
    position: relative;
    display: inline-block;
}

.locations-content {
    display: none;
    position: absolute;
    background: #1a1a1a;
    min-width: 300px;
    box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    padding: 1rem;
    z-index: 1000;
    border-radius: 8px;
    right: 0;
}

.locations-dropdown:hover .locations-content {
    display: block;
}

#locationSearch {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
    border: none;
    border-radius: 4px;
    background: #333;
    color: white;
}

.location-list {
    max-height: 300px;
    overflow-y: auto;
    margin: 0;
    padding: 0;
    list-style: none;
}

.location-list li {
    padding: 8px;
    border-radius: 4px;
}

.location-list li:hover {
    background: #333;
}

.location-list a {
    color: white;
    text-decoration: none;
    display: block;
}
</style>
'''

# JavaScript for search functionality
search_script = '''
<script>
document.getElementById('locationSearch').addEventListener('input', function() {
    var searchTerm = this.value.toLowerCase();
    var locations = document.querySelectorAll('.location-list li');
    
    locations.forEach(function(location) {
        var text = location.textContent.toLowerCase();
        if (text.includes(searchTerm)) {
            location.style.display = '';
        } else {
            location.style.display = 'none';
        }
    });
});
</script>
'''

# HTML for the locations dropdown
locations_dropdown = f'''
<li class="locations-dropdown">
    <a href="#" class="locations-link">Locations</a>
    <div class="locations-content">
        <input type="text" id="locationSearch" placeholder="Search locations...">
        <ul class="location-list">
            {location_links}
        </ul>
    </div>
</li>
'''

# Process each file in the locations directory
for filename in os.listdir('locations'):
    if filename.endswith('.html'):
        filepath = os.path.join('locations', filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Add styles to head
        content = content.replace('</head>', f'{dropdown_styles}</head>')

        # Add locations dropdown to navigation
        content = content.replace('<li><a href="../index.html#about">About</a></li>',
                                f'<li><a href="../index.html#about">About</a></li>\n                {locations_dropdown}')

        # Add search script before closing body tag
        content = content.replace('</body>', f'{search_script}</body>')

        # Write the modified content back to the file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated: {filepath}') 