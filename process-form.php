<?php
header('Content-Type: application/json');

// Replace with your email
$to_email = 'your@email.com';

$name = $_POST['name'] ?? '';
$email = $_POST['email'] ?? '';
$phone = $_POST['phone'] ?? '';
$message = $_POST['message'] ?? '';

$subject = "New Contact Form Submission from Gutter Goat";
$email_content = "Name: $name\n";
$email_content .= "Email: $email\n";
$email_content .= "Phone: $phone\n\n";
$email_content .= "Message:\n$message";

$headers = "From: $email";

if(mail($to_email, $subject, $email_content, $headers)) {
    echo json_encode(['success' => true]);
} else {
    echo json_encode(['success' => false]);
} 