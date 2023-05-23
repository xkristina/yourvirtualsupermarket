<?php
    $servername = "localhost";
    $username = "admin";
    $password = "password4321";
    $dbname = "capstone_cartfunc";

    // Create database connection
    $conn = mysqli_connect($servername, $username, $password, $dbname);

    // Check connection
    if (!$conn) {
        die("Connection failed: " . mysqli_connect_error());
    }
?>
