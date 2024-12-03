import os

def update_navigation(content):
    # New navigation HTML
    new_nav = '''    <header>
        <nav>
            <a href="/" class="logo">
                <img src="/images/gutter-goat-logo.png" alt="Gutter Goat Logo">
                <span class="logo-text">Gutter Goat</span>
            </a>
            <ul>
                <li><a href="/services.html">Services</a></li>
                <li><a href="/about.html">About</a></li>
                <li><a href="/locations.html">Locations</a></li>
                <li><a href="/#contact">Contact</a></li>
                <li><a href="tel:0497347752" class="phone-link" onclick="gtag('event', 'click', {'event_category': 'Phone Call', 'event_action': 'Click', 'event_label': 'Header Phone'});">0497 347 752</a></li>
            </ul>
        </nav>
    </header>'''
    
    # Find and replace the header section
    start = content.find('<header')
    end = content.find('</header>') + 9
    if start != -1 and end != -1:
        content = content[:start] + new_nav + content[end:]
    
    return content

# Update all location pages
locations_dir = 'locations'
if os.path.exists(locations_dir):
    for filename in os.listdir(locations_dir):
        if filename.endswith('.html'):
            file_path = os.path.join(locations_dir, filename)
            print(f'Updating navigation in {file_path}...')
            
            # Read the file
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Update navigation
            content = update_navigation(content)
            
            # Write the updated content back
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f'Updated {filename}')

print('Finished updating navigation in all location pages') 