<?php
session_start();

@include 'connection.php';

// Calculate the total based on the cart items
if (isset($_POST['checkout_btn'])) {
    $username = $_POST['fullname']; // Get the full name from the form
    $email = $_POST['email']; // Get the email from the form
    $phone = $_POST['phone']; // Get the phone number from the form

    $total = 0; // Initialize the total variable
    $cartItems = $_SESSION['cart']; // Get the cart items from the session

    foreach ($cartItems as $item) {
        $productId = $item['product_id']; // Get the product ID from the cart item
        $quantity = $item['quantity']; // Get the quantity from the cart item

        $query = "SELECT price FROM products WHERE id = $productId"; // Query to get the price of the product
        $result = mysqli_query($conn, $query); // Execute the query
        $product = mysqli_fetch_assoc($result); // Fetch the result as an associative array

        $itemTotal = $product['price'] * $quantity; // Calculate the total for the cart item
        $total += $itemTotal; // Add the item total to the overall total
    }

    $_SESSION['grand_total'] = $total; // Store the grand total in the session
}

// Clear the cart if the clear_cart parameter is present in the URL
if (isset($_GET['clear_cart']) && $_GET['clear_cart'] === 'true') {
    mysqli_query($conn, 'DELETE FROM `cart`'); // Delete all items from the cart table
}
?>


<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">

   <link rel="stylesheet" href="checkout_page_styles.css">
   <link rel="stylesheet" href="header_styles.css">
</head>
<body>

<?php include 'header.php'; ?> <!-- Including the 'header.php' file -->

<form action="checkout.php" method="post">
    <div class="container checkout-container">
        <h1>Order Confirmation</h1>

        <label for="fullname"><b>Full Name</b></label>
        <input type="text" name="fullname" placeholder="Enter First and Last Name" required>

        <label for="email"><b>Email</b></label>
        <input type="text" placeholder="Enter Email" name="email" required>

        <label for="phone"><b>Phone Number</b></label>
        <input type="tel" placeholder="876-000-0000" name="phone" required>

        <p>Your total is $<?php echo number_format($_SESSION['grand_total'], 2); ?></p> <!-- Displaying the total using PHP -->

        <p>By selecting the checkout button below, your invoice will be generated, and subsequently sent to the email provided.</p>

        <div class="clearfix">
            <button type="button" name="checkout_btn" class="btn" onclick="displayModal()">Checkout</button> <!-- Triggering the 'displayModal' function on button click -->
        </div>
    </div>
</form>

<div id="confirmationModal" class="modal">
  <div class="modal-content">
    <p>Are you sure you want to proceed with the checkout?</p>
    <div class="modal-buttons">
      <button id="confirmBtn">Confirm</button>
      <button id="cancelBtn">Cancel</button>
    </div>
  </div>
</div>


<script>
  // Function to display the confirmation modal
  function displayModal() {
    var modal = document.getElementById('confirmationModal');
    modal.style.display = 'block';

    var confirmBtn = document.getElementById('confirmBtn');
    var cancelBtn = document.getElementById('cancelBtn');

    confirmBtn.onclick = function() {
      // Clear the cart using AJAX
      var xhr = new XMLHttpRequest();
      xhr.open('GET', 'checkout.php?clear_cart=true', true);
      xhr.send();

      // Redirect the user to the products page
      window.location.href = 'products.php';
    };

    cancelBtn.onclick = function() {
      // Redirect the user back to the cart page
      window.location.href = 'cart.php';
    };
  }
  
  // Hide the modal on page load
  window.addEventListener('load', function() {
    var modal = document.getElementById('confirmationModal');
    modal.style.display = 'none';
  });
</script>

</body>
</html>
