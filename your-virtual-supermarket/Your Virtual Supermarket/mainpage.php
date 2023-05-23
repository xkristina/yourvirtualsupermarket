<?php

    $host ="localhost";
	$dbUsername= "root";
	$dbPassword = "";
	$dbname = "virtual_supermarket";

	$conn = new mysqli($host, $dbUsername, $dbPassword, $dbname);
	$result = $conn->query("SELECT booking_id FROM booking");
    
    




    $conn->close();

?>