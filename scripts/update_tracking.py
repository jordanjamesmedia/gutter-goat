import os

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
    
    <!-- Event snippet for 0497 347 752 - Mobile conversion page -->
    <script>
    function gtag_report_conversion(url) {
      var callback = function () {
        if (typeof(url) != 'undefined') {
          window.location = url;
        }
      };
      gtag('event', 'conversion', {
          'send_to': 'AW-16797354549/Awk1CMjjlvIZELWUzck-',
          'event_callback': callback
      });
      return false;
    }
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

# Update all location pages
locations_dir = 'locations'
if os.path.exists(locations_dir):
    for filename in os.listdir(locations_dir):
        if filename.endswith('.html'):
            file_path = os.path.join(locations_dir, filename)
            print(f'Updating {file_path}...')
            
            # Read the file
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Add phone tracking
            content = add_phone_tracking(content)
            
            # Write the updated content back
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f'Updated {filename}')

print('Finished updating all location pages with phone tracking') 