<header class="header">

   <div class="flex">

      <a href="#" class="logo">Online Supermarket</a>

      <nav class="navbar">
         <a href="products.php">products</a> <!-- Navigation link to the products page -->
      </nav>

      <?php
      
      $select_rows = mysqli_query($conn, "SELECT * FROM `cart`") or die('query failed'); // Query to select all rows from the 'cart' table
      $row_count = mysqli_num_rows($select_rows); // Counting the number of rows in the cart

      ?>

      <a href="cart.php" class="cart">cart <span><?php echo $row_count; ?></span> </a> <!-- Link to the cart page -->

      <div id="menu-btn" class="fas fa-bars"></div> <!-- Menu button -->

   </div>

</header>
