<?php
// Script to add Google Analytics to all HTML files
$analytics_code = '
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-16797354549"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag("js", new Date());
  gtag("config", "AW-16797354549");
</script>
';

function addAnalyticsToFile($file) {
    $content = file_get_contents($file);
    if (strpos($content, 'AW-16797354549') === false) {
        $content = str_replace('</head>', $analytics_code . '</head>', $content);
        file_put_contents($file, $content);
    }
}

// Process all HTML files
$files = glob('../**/*.html');
foreach($files as $file) {
    addAnalyticsToFile($file);
} 