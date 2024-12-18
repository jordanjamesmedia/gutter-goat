<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Set recipient email
    $to = "info@guttergoat.com.au";
    
    // Get form data
    $name = $_POST['name'] ?? 'Not provided';
    $email = $_POST['email'] ?? 'Not provided';
    $phone = $_POST['phone'] ?? 'Not provided';
    $message = $_POST['message'] ?? 'No message';
    
    // Set email subject
    $subject = "New Website Enquiry - Gutter Goat";
    
    // Create email content
    $email_content = "New contact form submission:\n\n";
    $email_content .= "Name: $name\n";
    $email_content .= "Email: $email\n";
    $email_content .= "Phone: $phone\n\n";
    $email_content .= "Message:\n$message\n";
    
    // Email headers
    $headers = "From: $email\r\n";
    $headers .= "Reply-To: $email\r\n";
    $headers .= "X-Mailer: PHP/" . phpversion();
    
    // Send email
    mail($to, $subject, $email_content, $headers);
    
    // Redirect to thank you page
    header('Location: thank-you.html');
    exit;
}
?> 