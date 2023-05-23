import mysql.connector

# Connect to the database server
cnx = mysql.connector.connect(host="localhost",user="root",password="Student1.")

# Create a database for the supermarket
cursor = cnx.cursor()
cursor.execute("CREATE DATABASE virtual_supermarket")
cnx.database = "virtual_supermarket"

# Create a table for accounts
cursor.execute('''
    CREATE TABLE accounts(
    id VARCHAR(255) PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    account_type VARCHAR(10) NOT NULL
    )
''')

# Create a table for employees
cursor.execute('''
    CREATE TABLE employees (
        id VARCHAR(255) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        phone VARCHAR(255) NOT NULL

    )
''')

# Create a table for employee roles
cursor.execute('''
    CREATE TABLE roles (
        id VARCHAR(255) NOT NULL,
        role_name VARCHAR(255) NOT NULL,
        FOREIGN KEY (id) REFERENCES employees(id)
    )
''')

# Create a table for customers
cursor.execute('''
    CREATE TABLE customers (
        id VARCHAR(255) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        phone VARCHAR(255) NOT NULL

    )
''')

# Create a table for supermarkets
cursor.execute('''
    CREATE TABLE supermarkets (
        id VARCHAR(255) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        phone VARCHAR(255) NOT NULL
    )
''')


# Create a table for addresses
cursor.execute('''
    CREATE TABLE addresses (
        id VARCHAR(255) NOT NULL,
        street_address VARCHAR(255) NOT NULL,
        city VARCHAR(255) NOT NULL,
        parish VARCHAR(255) NOT NULL
    )
''')

# Create a table for products
cursor.execute('''
    CREATE TABLE products (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        category VARCHAR(255) NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        stock INT NOT NULL
    )
''')

# Create a table for orders
cursor.execute('''
    CREATE TABLE orders (
        id INT AUTO_INCREMENT PRIMARY KEY,
        customer_id VARCHAR(255) NOT NULL,
        product_id INT NOT NULL,
        quantity INT NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        date DATE NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers(id),
        FOREIGN KEY (product_id) REFERENCES products(id)
    )
''')

# Create a table for carts
cursor.execute('''
    CREATE TABLE carts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        customer_id VARCHAR(255) NOT NULL,
        product_id INT NOT NULL,
        quantity INT NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers(id),
        FOREIGN KEY (product_id) REFERENCES products(id)
    )
''')

# Create a table for sales
cursor.execute('''
    CREATE TABLE sales (
        id INT AUTO_INCREMENT PRIMARY KEY,
        customer_id VARCHAR(255) NOT NULL,
        product_id INT NOT NULL,
        quantity INT NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        date DATE NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers(id),
        FOREIGN KEY (product_id) REFERENCES products(id)
    )
''')

# Create a table for payments
cursor.execute('''
    CREATE TABLE payments (
        id INT AUTO_INCREMENT PRIMARY KEY,
        customer_id VARCHAR(255) NOT NULL,
        amount DECIMAL(10, 2) NOT NULL,
        date DATE NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers(id)
    )
''')

# Save the changes and close the connection
cnx.commit()
cnx.close()
