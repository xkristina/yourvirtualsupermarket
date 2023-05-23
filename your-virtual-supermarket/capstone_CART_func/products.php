<?php

@include 'connection.php'; // Including the connection file to establish a database connection

if(isset($_POST['add_to_cart'])){ // Checking if the 'add_to_cart' form has been submitted

   // Retrieving form data
   $product_name = $_POST['product_name'];
   $product_price = $_POST['product_price'];
   $product_image = $_POST['product_image'];
   $product_measurement = $_POST['product_measurement'];
   $product_details = $_POST['product_details'];
   $product_quantity = 1;

   // Checking if the product is already in the cart
   $select_cart = mysqli_query($conn, "SELECT * FROM `cart` WHERE name = '$product_name'");
   
   if(mysqli_num_rows($select_cart) > 0){
      $message[] = 'product already added to cart'; // Adding a message indicating that the product is already in the cart
   }else{
      // Inserting the product into the cart table
      $insert_product = mysqli_query($conn, "INSERT INTO `cart`(name, price, image, quantity) VALUES('$product_name', '$product_price', '$product_image', '$product_quantity')");
      $message[] = 'product added to cart successfully'; // Adding a message indicating that the product has been added to the cart
   }

}

?>

<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>products</title>


   <link rel="stylesheet" href="cart_styles.css">
</head>
<body>
   
<?php include 'header.php'; ?> <!-- Including the header file -->

<div class="container">
<section class="products">

   <h1 class="heading">Products | Frozen Section</h1>
   <div class="box-container">

      <?php
      
        $select_products = mysqli_query($conn, "SELECT * FROM `products`"); // Selecting all products from the products table
        if(mysqli_num_rows($select_products) > 0){
            while($fetch_product = mysqli_fetch_assoc($select_products)){ // Fetching each product as an associative array
        ?>

        <form action="" method="post"> <!-- Form to add the product to the cart -->
            <div class="box">
                <img src="images/<?php echo $fetch_product['image']; ?>" alt=""> <!-- Displaying the product image -->
                <div class="details-container">
                    <h3><?php echo $fetch_product['name']; ?></h3> <!-- Displaying the product name -->
                    <div class="details"><?php echo $fetch_product['details']; ?></div> <!-- Displaying the product details -->
                </div>
                <div class="price-measurement-container">
                    <div class="price">$<?php echo $fetch_product['price']; ?></div> <!-- Displaying the product price -->
                    <div class="measurement"><?php echo $fetch_product['measurement']; ?></div> <!-- Displaying the product measurement -->
                </div>
                <input type="hidden" name="product_name" value="<?php echo $fetch_product['name']; ?>"> <!-- Hidden input field to store the product name -->
                <input type="hidden" name="product_price" value="<?php echo $fetch_product['price']; ?>"> <!-- Hidden input field to store the product price -->
                <input type="hidden" name="product_image" value="<?php echo $fetch_product['image']; ?>"> <!-- Hidden input field to store the product image -->
                <input type="hidden" name="product_measurement" value="<?php echo $fetch_product['measurement']; ?>"> <!-- Hidden input field to store the product measurement -->
                <input type="hidden" name="product_details" value="<?php echo $fetch_product['details']; ?>"> <!-- Hidden input field to store the product details -->
                <input type="submit" class="btn" value="add to cart" name="add_to_cart"> <!-- Button to add the product to the cart -->
            </div>
        </form>

      <?php
         };
      };
      ?>

   </div>
</section>
</div>


</body>
</html>
