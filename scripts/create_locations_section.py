import os

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

# Get unique postcodes for the dropdown
postcodes = sorted(set(data['postcode'] for data in locations.values()))

# Generate postcode options HTML
postcode_options = '\n'.join(f'<option value="{postcode}">{postcode}</option>' for postcode in postcodes)

# Generate locations HTML (sorted alphabetically)
location_items = ''
for slug, data in sorted(locations.items(), key=lambda x: x[1]['name']):
    location_items += f'''
    <div class="location-item" data-postcode="{data['postcode']}">
        <a href="locations/{slug}.html">
            <h3>{data['name']}</h3>
            <p>{data['postcode']}</p>
        </a>
    </div>
'''

# Locations section HTML with fixed CSS syntax
locations_section = '''
<!-- Locations Section -->
<section id="locations" class="locations-section">
    <div class="section-title">
        <h2>Service Locations</h2>
        <p>Find your local gutter cleaning experts</p>
    </div>

    <div class="locations-filter">
        <input type="text" id="locationSearch" placeholder="Search suburbs...">
        <select id="postcodeFilter">
            <option value="">All Postcodes</option>
            {postcode_options}
        </select>
    </div>

    <div class="locations-grid">
        {location_items}
    </div>
</section>

<style>
.locations-section {{
    padding: 5rem 2rem;
    background-color: #f8f9fa;
}}

.locations-filter {{
    max-width: 800px;
    margin: 0 auto 2rem;
    display: flex;
    gap: 1rem;
}}

#locationSearch {{
    flex: 1;
    padding: 0.8rem;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-size: 1rem;
}}

#postcodeFilter {{
    padding: 0.8rem;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-size: 1rem;
    min-width: 150px;
}}

.locations-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 1.5rem;
    max-width: 1200px;
    margin: 0 auto;
}}

.location-item {{
    background: white;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}}

.location-item:hover {{
    transform: translateY(-5px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}}

.location-item a {{
    display: block;
    padding: 1.5rem;
    text-decoration: none;
    color: inherit;
}}

.location-item h3 {{
    margin: 0;
    color: #333;
    font-size: 1.2rem;
}}

.location-item p {{
    margin: 0.5rem 0 0;
    color: #666;
}}

@media (max-width: 768px) {{
    .locations-filter {{
        flex-direction: column;
    }}
}}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const locationSearch = document.getElementById('locationSearch');
    const postcodeFilter = document.getElementById('postcodeFilter');
    const locations = document.querySelectorAll('.location-item');

    function filterLocations() {
        const searchTerm = locationSearch.value.toLowerCase();
        const selectedPostcode = postcodeFilter.value;

        locations.forEach(location => {
            const name = location.querySelector('h3').textContent.toLowerCase();
            const postcode = location.dataset.postcode;
            const matchesSearch = name.includes(searchTerm);
            const matchesPostcode = !selectedPostcode || postcode === selectedPostcode;

            location.style.display = matchesSearch && matchesPostcode ? '' : 'none';
        });
    }

    locationSearch.addEventListener('input', filterLocations);
    postcodeFilter.addEventListener('change', filterLocations);
});
</script>
'''

# Update the script to add phone conversion tracking to the head section
def add_phone_tracking(content):
    # Add phone conversion tracking after the existing Google Analytics code
    analytics_script = '''
    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=AW-16797354549"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'AW-16797354549');
      gtag('config', 'AW-16797354549/pl_SCIq6q-8ZELWUzck-', {
        'phone_conversion_number': '0497 347 752'
      });
      gtag('config', 'AW-16797354549/t24MCMPFpfIZELWUzck-', {
        'phone_conversion_number': '0497 347 752'
      });
    </script>
    '''
    
    # Replace existing analytics code
    if '<!-- Google Analytics -->' in content:
        start = content.find('<!-- Google Analytics -->')
        end = content.find('</script>', start) + 9
        content = content[:start] + analytics_script + content[end:]
    else:
        # If no analytics code exists, add it before </head>
        content = content.replace('</head>', analytics_script + '\n</head>')
    
    return content

# Update phone numbers to be clickable and include tracking
def update_phone_numbers(content):
    # Update phone numbers to be clickable with tracking
    phone_link = '<a href="tel:0497347752" onclick="gtag(\'event\', \'click\', {\'event_category\': \'Phone Call\', \'event_action\': \'Click\', \'event_label\': \'Phone Link\'});">0497 347 752</a>'
    content = content.replace('>0497 347 752<', '>' + phone_link + '<')
    return content

# Read and update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add phone tracking
content = add_phone_tracking(content)

# Update phone numbers
content = update_phone_numbers(content)

# Add locations section (existing code)
if '<!-- Locations Section -->' in content:
    content = content.replace('<!-- Locations Section -->', locations_section)
else:
    content = content.replace('</main>', f'{locations_section}</main>')

# Write the updated content back to index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated index.html with locations section and phone tracking') 