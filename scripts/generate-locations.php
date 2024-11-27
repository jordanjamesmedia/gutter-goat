<?php

// Enable error reporting
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Set absolute paths
$root_dir = dirname(__DIR__);
$template_path = __DIR__ . '/template.html';
$locations_dir = $root_dir . '/locations';

// Verify directories exist
if (!file_exists($locations_dir)) {
    mkdir($locations_dir, 0755, true);
    echo "Created locations directory at: $locations_dir\n";
}

// Verify template exists
if (!file_exists($template_path)) {
    die("Template file not found at: $template_path\n");
}

// Read template file
$template = file_get_contents($template_path);
if ($template === false) {
    die("Failed to read template file\n");
}

// Your locations array remains the same
$locations = [
    'helensburgh' => ['name' => 'Helensburgh', 'postcode' => '2508'],
    'stanwell-park' => ['name' => 'Stanwell Park', 'postcode' => '2508'],
    'coalcliff' => ['name' => 'Coalcliff', 'postcode' => '2508'],
    'scarborough' => ['name' => 'Scarborough', 'postcode' => '2515'],
    'wombarra' => ['name' => 'Wombarra', 'postcode' => '2515'],
    'coledale' => ['name' => 'Coledale', 'postcode' => '2515'],
    'austinmer' => ['name' => 'Austinmer', 'postcode' => '2515'],
    'thirroul' => ['name' => 'Thirroul', 'postcode' => '2515'],
    'bulli' => ['name' => 'Bulli', 'postcode' => '2516'],
    'woonona' => ['name' => 'Woonona', 'postcode' => '2517'],
    'corrimal' => ['name' => 'Corrimal', 'postcode' => '2518'],
    'towradgi' => ['name' => 'Towradgi', 'postcode' => '2518'],
    'fairy-meadow' => ['name' => 'Fairy Meadow', 'postcode' => '2519'],
    'mount-ousley' => ['name' => 'Mount Ousley', 'postcode' => '2519'],
    'north-wollongong' => ['name' => 'North Wollongong', 'postcode' => '2500'],
    'wollongong' => ['name' => 'Wollongong', 'postcode' => '2500'],
    'mangerton' => ['name' => 'Mangerton', 'postcode' => '2500'],
    'mount-keira' => ['name' => 'Mount Keira', 'postcode' => '2500'],
    'coniston' => ['name' => 'Coniston', 'postcode' => '2500'],
    'port-kembla' => ['name' => 'Port Kembla', 'postcode' => '2505'],
    'warrawong' => ['name' => 'Warrawong', 'postcode' => '2502'],
    'lake-heights' => ['name' => 'Lake Heights', 'postcode' => '2502'],
    'berkeley' => ['name' => 'Berkeley', 'postcode' => '2506'],
    'unanderra' => ['name' => 'Unanderra', 'postcode' => '2526'],
    'kembla-grange' => ['name' => 'Kembla Grange', 'postcode' => '2526'],
    'dapto' => ['name' => 'Dapto', 'postcode' => '2530'],
    'horsley' => ['name' => 'Horsley', 'postcode' => '2530'],
    'albion-park' => ['name' => 'Albion Park', 'postcode' => '2527'],
    'shellharbour' => ['name' => 'Shellharbour', 'postcode' => '2529'],
    'shell-cove' => ['name' => 'Shell Cove', 'postcode' => '2529'],
    'jamberoo' => ['name' => 'Jamberoo', 'postcode' => '2533'],
    'kiama' => ['name' => 'Kiama', 'postcode' => '2533'],
    'gerringong' => ['name' => 'Gerringong', 'postcode' => '2534'],
    'berry' => ['name' => 'Berry', 'postcode' => '2535'],
    'shoalhaven-heads' => ['name' => 'Shoalhaven Heads', 'postcode' => '2535']
];

// Generate pages
foreach ($locations as $slug => $location) {
    $output_file = $locations_dir . '/' . $slug . '.html';
    
    // Replace placeholders
    $content = str_replace(
        ['[LOCATION]', '[POSTCODE]'],
        [$location['name'], $location['postcode']],
        $template
    );
    
    // Add location-specific content
    $localContent = getLocationSpecificContent($location['name']);
    $content = str_replace('[LOCAL_CONTENT]', $localContent, $content);
    
    // Save file
    if (file_put_contents($output_file, $content) === false) {
        echo "ERROR: Failed to create $output_file\n";
    } else {
        echo "Created: $output_file\n";
        
        // Verify file exists and is readable
        if (file_exists($output_file) && is_readable($output_file)) {
            echo "Verified: $output_file is accessible\n";
        } else {
            echo "WARNING: $output_file may not be accessible\n";
        }
    }
}

// Verify final structure
echo "\nFinal Directory Structure:\n";
$files = glob($locations_dir . '/*.html');
foreach ($files as $file) {
    echo basename($file) . "\n";
}

echo "\nScript completed.\n";
echo "Root directory: $root_dir\n";
echo "Template path: $template_path\n";
echo "Locations directory: $locations_dir\n"; 