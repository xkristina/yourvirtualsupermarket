<?php

@include 'connection.php'; // Including the 'connection.php' file to establish a database connection.

if(isset($_POST['update_btn'])){ // Checking if the 'update_btn' form field is set and submitted.
  $update_value = $_POST['update_quantity']; // Storing the updated quantity value from the form.
  $update_id = $_POST['update_quantity_id']; // Storing the cart ID for the item to be updated.
  $update_quantity_query = mysqli_query($conn, "UPDATE `cart` SET quantity = '$update_value' WHERE cartID = '$update_id'"); // Updating the quantity of the item in the cart table.
  if($update_quantity_query){
     header('location:cart.php'); // Redirecting to the 'cart.php' page after successfully updating the quantity.
  }
}

if(isset($_POST['remove_btn'])){ // Checking if the 'remove_btn' form field is set and submitted.
   $remove_id = $_POST['remove_id']; // Storing the cart ID for the item to be removed.
   mysqli_query($conn, "DELETE FROM `cart` WHERE cartID = '$remove_id'"); // Deleting the item from the cart table.
   header('location:cart.php'); // Redirecting to the 'cart.php' page after successfully removing the item.
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>shopping cart</title>
   <link rel="stylesheet" href="styles.css"> <!-- Including an external CSS file. -->
</head>
<body class="cart-body">

<?php include 'header.php'; ?> <!-- Including the 'header.php' file. -->

<div class="container">

<section class="shopping-cart">

   <h1 class="heading">Your Virtual Supermarket | shopping cart</h1>

   <?php 
   session_start(); // Starting a session.

   $select_cart = mysqli_query($conn, "SELECT * FROM cart"); // Querying the cart table to select all items.
   $grand_total = 0; // Initializing the grand total variable.

   if(mysqli_num_rows($select_cart) > 0){ // Checking if there are items in the cart.
      ?>
      <div class="basket">
         <div class="basket-module">
            <label for="promo-code">Enter a promotional code</label>
            <input id="promo-code" type="text" name="promo-code" maxlength="50" class="promo-code-field">
            <button class="promo-code-btn">Apply</button>
         </div>
         <div class="basket-labels">
            <ul>
               <li class="item item-heading">Item</li>
               <li class="price">Price</li>
               <li class="quantity">Quantity</li>
               <li class="subtotal">Subtotal</li>
            </ul>
         </div>
         <?php
         while($fetch_cart = mysqli_fetch_assoc($select_cart)){ // Looping through each item in the cart.
            $subtotal = $fetch_cart['price'] * $fetch_cart['quantity']; // Calculating the subtotal for each item.
            $grand_total += $subtotal; // Adding the subtotal to the grand total.
            ?>
            <div class="basket-product">
               <div class="item">
                  <div class="product-image">
                     <img src="images/<?php echo $fetch_cart['image']; ?>" height="100" alt=""> <!-- Displaying the product image.-->

                  </div>
                  <div class="product-details">
                     <h1><span class="item-quantity"><?php echo $fetch_cart['quantity']; ?></span>x <?php echo $fetch_cart['name']; ?></h1> <!-- Displaying the quantity and name of the product.-->
                  </div>
               </div>
               <div class="price">$<?php echo number_format($fetch_cart['price'], 2); ?></div> <!-- Displaying the price of the product. -->
               <div class="quantity">
               <form action="" method="post"> <!-- Form for updating the quantity of the item. -->
                  <input type="hidden" name="update_quantity_id" value="<?php echo $fetch_cart['cartID']; ?>"> <!-- Hidden field to store the cart ID of the item. -->
                  <input type="number" name="update_quantity" min="1" value="<?php echo $fetch_cart['quantity']; ?>"> <!-- Input field to enter the updated quantity. -->
                  <input type="submit" value="update" name="update_btn"> <!-- Submit button to update the quantity. -->
               </form>

               </div>
               <div class="subtotal">$<?php echo number_format($subtotal, 2); ?></div> <!-- Displaying the subtotal for the item. -->

               <div class="remove">
                  <form action="" method="post" onsubmit="return confirm('Are you sure you want to remove this item from your cart?');"> <!-- Form for removing the item from the cart. -->
                     <input type="hidden" name="remove_id" value="<?php echo $fetch_cart['cartID']; ?>"> <!-- Hidden field to store the cart ID of the item.-->
                     <button type="submit" name="remove_btn">Remove</button> <!-- Submit button to remove the item. -->
                  </form>
               </div>
            </div>
            <?php
         }
         ?>
      
         <!-- space holder -->
         <div class="basket-total">
            <h3></h3>
         </div>
      </div>
      <?php
   }
   ?>



   <aside>
      <div class="summary">
         <div class="summary-total-items"><span class="total-items"><?php echo mysqli_num_rows($select_cart); ?></span> Items in your Bag</div> <!-- Displaying the total number of items in the cart. -->
         <div class="summary-subtotal">
            <div class="subtotal-title">Subtotal</div>
            <div class="subtotal-value final-value" id="basket-subtotal">$<?php echo number_format($grand_total, 2); ?></div> <!-- Displaying the subtotal of the cart. -->
            <div class="summary-promo hide">
               <div class="promo-title">Promotion</div>
               <div class="promo-value final-value" id="basket-promo"></div>
            </div>
         </div>
         <div class="summary-delivery">
            <select name="delivery-collection" class="summary-delivery-selection">
               <option value="0" selected="selected">Select Collection or Delivery</option>
               <option value="collection">Pick up at store</option>
               <option value="second-class">Home Delivery</option>
            </select>
         </div>
         <div class="summary-total">
            <div class="total-title">Total</div>
            <div class="total-value final-value" id="basket-total">$<?php echo number_format($grand_total, 2); ?></div> <!-- Displaying the total amount of the cart. -->
         </div>
         <div class="continue-shopping">
            <!-- products.php represents the shopping page, so the user would be redirected there -->
            <a href="products.php" class="option-btn" style="margin-top: 0;">Continue Shopping</a>
         </div>
         <div class="summary-checkout">

            <a href="checkout.php" class="option-btn" id="checkout-btn" style="margin-top: 0;">Proceed to Checkout</a>

            <?php
            if(isset($_POST['checkout_btn'])) {
               $order_total = $grand_total; // Assigning the total amount of the cart to the variable $order_total.

               $stmt = mysqli_prepare($conn, "INSERT INTO `order` (order_total) VALUES (?)"); // Preparing an SQL statement to insert the order total into the database.
               mysqli_stmt_bind_param($stmt, "s", $order_total); // Binding the order total to the prepared statement.

               if(mysqli_stmt_execute($stmt)) { // Executing the prepared statement.
                  $_SESSION['total'] = $grand_total; // Storing the total amount in a session variable.
                  header('Location: checkout.php'); // Redirecting the user to the checkout page.
                  exit();
               } else {
                  echo "Error: " . mysqli_error($conn); // Displaying an error message if the SQL statement execution fails.
               }

               mysqli_stmt_close($stmt); // Closing the prepared statement.
            }
            ?>
         </div>
      </div>
   </aside>

</section>
</div>
</body>
</html>

                 




            