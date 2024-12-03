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

# Generate location links HTML
location_links = ''
for slug, data in sorted(locations.items(), key=lambda x: x[1]['name']):
    location_links += f'<li><a href="../locations/{slug}.html">{data["name"]} ({data["postcode"]})</a></li>\n'

# Base HTML template for each location
page_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- SEO Meta Tags -->
    <meta name="description" content="Professional gutter cleaning services in {name} ({postcode}). Expert local gutter maintenance, cleaning, and repairs throughout {name} and surrounding areas.">
    <meta name="keywords" content="gutter cleaning {name}, gutter maintenance {name}, {name} gutter services, gutter repairs {postcode}, Gutter Goat {name}">
    <title>Gutter Cleaning {name} ({postcode}) | Professional Service by Gutter Goat</title>
    
    <!-- Open Graph / Social Media -->
    <meta property="og:title" content="Gutter Cleaning {name} | Gutter Goat">
    <meta property="og:description" content="Professional gutter cleaning services in {name}. Local experts, fully insured, satisfaction guaranteed.">
    <meta property="og:image" content="https://guttergoat.com.au/images/gutter-goat-logo.png">
    <meta property="og:url" content="https://guttergoat.com.au/locations/{slug}">
    
    <link rel="canonical" href="https://guttergoat.com.au/locations/{slug}">
    <link rel="stylesheet" href="../styles.css">
    
    <!-- Google Analytics and Phone Conversion Tracking -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=AW-16797354549"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'AW-16797354549');
      gtag('config', 'AW-16797354549/pl_SCIq6q-8ZELWUzck-', {{
        'phone_conversion_number': '0497 347 752'
      }});
    </script>
</head>
<body>
    <header>
        <nav>
            <div class="logo">
                <a href="../index.html">
                    <img src="../images/gutter-goat-logo.png" alt="Gutter Goat Logo">
                    <span class="logo-text">Gutter Goat</span>
                </a>
            </div>
            <ul>
                <li><a href="../index.html#services">Services</a></li>
                <li><a href="../index.html#about">About</a></li>
                <li><a href="../index.html#locations">Locations</a></li>
                <li><a href="../index.html#contact">Contact</a></li>
                <li><a href="tel:0497347752" class="phone-link" onclick="gtag('event', 'click', {{'event_category': 'Phone Call', 'event_action': 'Click', 'event_label': 'Header Phone'}});">0497 347 752</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section class="location-hero" style="background-image: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url('{hero_image}')">
            <div class="location-hero-content">
                <h1>Professional Gutter Cleaning in {name}</h1>
                <p>Expert local service in {name} and surrounding areas</p>
                <div class="hero-cta">
                    <a href="tel:0497347752" class="cta-button" onclick="gtag('event', 'click', {{'event_category': 'Phone Call', 'event_action': 'Click', 'event_label': 'Hero CTA'}});">Call Now</a>
                    <a href="#quote-form" class="cta-button secondary">Get Quote</a>
                </div>
            </div>
        </section>

        <section class="location-services" id="services">
            <div class="section-title">
                <h2>Our Services in {name}</h2>
            </div>
            <div class="service-grid">
                <div class="service-card">
                    <div class="service-card-content">
                        <h3>Gutter Cleaning</h3>
                        <p>Professional gutter cleaning service in {name} to prevent water damage and maintain your home.</p>
                        <ul>
                            <li>Complete debris removal</li>
                            <li>Downpipe checking</li>
                            <li>Gutter flushing</li>
                        </ul>
                    </div>
                </div>
                <div class="service-card">
                    <div class="service-card-content">
                        <h3>Gutter Maintenance</h3>
                        <p>Regular maintenance to keep your gutters in perfect working order.</p>
                        <ul>
                            <li>Rust treatment</li>
                            <li>Minor repairs</li>
                            <li>Preventative care</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <section class="location-benefits">
            <div class="benefits-grid">
                <div class="benefit-card">
                    <div class="benefit-icon">✓</div>
                    <h3>Local Expertise</h3>
                    <p>Specialised knowledge of {name}'s unique challenges</p>
                </div>
                <div class="benefit-card">
                    <div class="benefit-icon">🛡️</div>
                    <h3>Fully Insured</h3>
                    <p>Complete peace of mind with comprehensive coverage</p>
                </div>
                <div class="benefit-card">
                    <div class="benefit-icon">⭐</div>
                    <h3>5-Star Service</h3>
                    <p>Trusted by {name} homeowners</p>
                </div>
            </div>
        </section>

        <section id="quote-form" class="quote-section">
            <div class="quote-container">
                <h2>Get a Free Quote</h2>
                <form action="../thank-you.html" method="POST" class="location-form">
                    <div class="form-row">
                        <input type="text" name="name" placeholder="Name" required>
                        <input type="tel" name="phone" placeholder="Phone" required>
                    </div>
                    <button type="submit" class="cta-button">Request Quote</button>
                </form>
            </div>
        </section>
    </main>

    <footer>
        <div class="footer-content">
            <div class="contact-info">
                <h3>Contact Info</h3>
                <p>Phone: <a href="tel:0497347752" onclick="gtag('event', 'click', {{'event_category': 'Phone Call', 'event_action': 'Click', 'event_label': 'Footer Phone'}});">0497 347 752</a></p>
                <p>Email: <a href="mailto:info@guttergoat.com.au">info@guttergoat.com.au</a></p>
                <p>Servicing {name} {postcode}</p>
            </div>
            <div class="social-links">
                <a href="#">Facebook</a>
                <a href="#">Instagram</a>
            </div>
        </div>
        <div class="copyright">
            <p>&copy; 2024 Gutter Goat. All rights reserved.</p>
        </div>
    </footer>

    <script>
        document.getElementById('locationSearch').addEventListener('input', function() {{
            var searchTerm = this.value.toLowerCase();
            var locations = document.querySelectorAll('.location-list li');
            
            locations.forEach(function(location) {{
                var text = location.textContent.toLowerCase();
                if (text.includes(searchTerm)) {{
                    location.style.display = '';
                }} else {{
                    location.style.display = 'none';
                }}
            }});
        }});
    </script>
</body>
</html>
'''

# Create locations directory if it doesn't exist
if not os.path.exists('locations'):
    os.makedirs('locations')

# Generate pages for each location
for slug, data in locations.items():
    # Get hero image if specified, otherwise use default
    hero_image = data.get('hero_image', '../images/gutter-cleaning.jpg')
    
    # Generate the page content
    page_content = page_template.format(
        name=data['name'],
        postcode=data['postcode'],
        slug=slug,
        location_links=location_links,
        hero_image=hero_image
    )
    
    # Write the file
    file_path = f'locations/{slug}.html'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(page_content)
    print(f'Created: {file_path}') 