<?php
$fname = $_POST['fname'];
$lname = $_POST['lname'];
$telnum = $_POST['telnum'];
$email = $_POST['email'];
$password = $_POST['password'];


if (!empty($fname) || !empty($lname) || !empty($email) || !empty($telnum) || !empty($password)){
    
    
    $host = "localhost";
    $dbUsername = "root";
    $dbPassword = "";
    $dbname = "virtual_supermarket";
    //create connection
    $conn = new mysqli($host, $dbUsername, $dbPassword, $dbname);
    if (mysqli_connect_error()) {


        die('Connect Error('. mysqli_connect_errno().')'. mysqli_connect_error());
    } else {


        $SELECT = "SELECT email From base Where email = ? Limit 1";
        $INSERT = "INSERT Into customer (id , name, email, phone) values(?, ?, ?, ?)";
        //Prepare statement
        $stmt = $conn->prepare($SELECT);
        $stmt->bind_param("s", $email);
        $stmt->execute();
        $stmt->bind_result($email);
        $stmt->store_result();
        $stmt->store_result();
        $stmt->fetch();
        $rnum = $stmt->num_rows;
        if ($rnum==0) {        
            $stmt->close();
            $stmt = $conn->prepare($INSERT);
            $stmt->bind_param("ssssii", $fname, $lname, $email, $telnum, $password);
            $stmt->execute();
            echo "New record inserted sucessfully";
    
     } else {

        echo "Someone already register using this email";
     }
     $stmt->close();
     $conn->close();
    }
} else {
    echo "All field are required";
    die();
}
?>