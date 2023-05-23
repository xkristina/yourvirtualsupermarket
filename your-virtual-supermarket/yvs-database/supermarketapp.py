from flask import Flask, request, make_response
import mysql.connector

app = Flask(__name__)

# Define the database connection
cnx = mysql.connector.connect(host='localhost',user='root',password='Student1.',database='virtual_supermarket')
cursor = cnx.cursor()

# Route to add a new account
@app.route('/add_accounts', methods=['POST'])
def add_account():
    try:
        # Get the account data from the request
        id = request.form['id']
        username = request.form['username']
        password = request.form['password']
        account_type = request.form['account_type']
        
        # Insert the new account into the database
        cursor.execute(f"INSERT INTO accounts (id, username, password, account_type) VALUES ('{id}', '{username}', '{password}', '{account_type}')")
        cnx.commit()
        
        return make_response({'message': 'Account added successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to retrieve a specific account
@app.route('/get_accounts/<account_id>', methods=['GET'])
def get_account(account_id):
    try:
        # Query the database for the account with the given ID
        cursor.execute(f"SELECT * FROM accounts WHERE id='{account_id}'")
        row = cursor.fetchone()

        # If the account was found, return it as JSON
        if row is not None:
            account = {'id': row[0], 'username': row[1], 'password': row[2],'account_type': row[3]}
            return make_response(account, 200)
        else:
            return make_response({'error': 'Account not found'}, 404)
    except:
        return make_response({'error': 'An error occurred'}, 500)

# Route to list all accounts
@app.route('/list_accounts', methods=['GET'])
def list_accounts():
    try:
        # Get all accounts from the database
        cursor.execute("SELECT * FROM accounts")
        accounts = []
        for id, username, password, account_type in cursor:
            account = {}
            account['id'] = id
            account['username'] = username
            account['password'] = password
            account['account_type'] = account_type
            accounts.append(account)

        return make_response({'accounts': accounts}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to update an existing account
@app.route('/update_account/<account_id>', methods=['PUT'])
def update_account(account_id):
    try:
        # Get the account data from the request
        username = request.form['username']
        password = request.form['password']
        account_type = request.form['account_type']

        # Update the account in the database
        cursor.execute(f"UPDATE accounts SET username='{username}', password='{password}' account_type='{account_type}' WHERE id='{account_id}'")
        cnx.commit()
        
        return make_response({'message': 'Account updated successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to delete an existing account
@app.route('/delete_accounts/<account_id>', methods=['DELETE'])
def delete_account(account_id):
    try:
        # Delete the account from the database
        cursor.execute(f"DELETE FROM accounts WHERE id='{account_id}'")
        cnx.commit()
        
        return make_response({'message': 'Account deleted successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to add a new employee
@app.route('/add_employees', methods=['POST'])
def add_employee():
    try:
        # Get the employee data from the request
        id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        
        # Insert the new employee into the database
        cursor.execute(f"INSERT INTO employees (id, name, email, phone) VALUES ('{id}', '{name}', '{email}', '{phone}')")
        cnx.commit()
        
        return make_response({'message': 'Employee record added successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

    
# Route to retrieve a specific employee
@app.route('/get_employees/<id>', methods=['GET'])
def get_employee(id):
    try:
        # Get the employee from the database
        cursor.execute(f"SELECT * FROM employees WHERE id='{id}'")
        employee = cursor.fetchone()
        
        # Check if the employee exists
        if employee:
            # Convert the employee data to a dictionary
            employee_data = {'id': employee[0], 'name': employee[1], 'email': employee[2], 'phone': employee[3]}
            
            return make_response({'employee': employee_data}, 200)
        else:
            return make_response({'error': 'Employee not found'}, 404)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to list all employees
@app.route('/list_employees', methods=['GET'])
def list_employees():
    try:
        # Get all employees from the database
        cursor.execute("SELECT * FROM employees")
        employees = []
        for id, name, email, phone in cursor:
            employee = {}
            employee['id'] = id
            employee['name'] = name
            employee['email'] = email
            employee['phone'] = phone
            employees.append(employee)

        return make_response({'employees': employees}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to update an existing employee
@app.route('/update_employees/<employee_id>', methods=['PUT'])
def update_employee(employee_id):
    try:
        # Get the employee data from the request
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        
        # Update the employee in the database
        cursor.execute(f"UPDATE employees SET name='{name}', email='{email}', phone='{phone}' WHERE id='{employee_id}'")
        cnx.commit()
    
        return make_response({'message': 'Employee updated successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to delete an existing employee
@app.route('/delete_employee/<employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    try:
        # Delete the employee from the database
        cursor.execute(f"DELETE FROM employees WHERE id='{employee_id}'")
        cnx.commit()

        return make_response({'message': 'Employee deleted successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to add a new employee role
@app.route('/add_employee_role', methods=['POST'])
def add_employee_role():
    try:
        # Get the employee role data from the request
        id = request.form['id']
        role_name = request.form['role_name']
        
        # Insert the employee role into the database
        cursor.execute(f"INSERT INTO roles (id, role_name) VALUES ('{id}', '{role_name}')")
        cnx.commit()
        
        return make_response({'message': 'Employee role added successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to get all employee roles
@app.route('/get_employee_roles', methods=['GET'])
def get_employee_roles():
    try:
        # Get all employee roles from the database
        cursor.execute("SELECT * FROM roles")
        roles = []
        for id, role_name in cursor:
            role = {}
            role['id'] = id
            role['role_name'] = role_name
            roles.append(role)

        return make_response({'employee_roles': roles}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to list all employee roles
@app.route('/list_employee_roles', methods=['GET'])
def list_employee_roles():
    try:
        # Get all employee roles from the database
        cursor.execute("SELECT * FROM roles")
        roles = []
        for id, role_name in cursor:
            employee_role = {}
            employee_role['id'] = id
            employee_role['role_name'] = role_name
            roles.append(employee_role)

        return make_response({'employee_roles': roles}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to update an existing employee role
@app.route('/update_employee_role/<id>', methods=['PUT'])
def update_employee_role(id):
    try:
        # Get the employee role data from the request
        role_name = request.form['role_name']
        
        # Update the employee role in the database
        cursor.execute(f"UPDATE roles SET role_name='{role_name}' WHERE id='{id}'")
        cnx.commit()
        
        return make_response({'message': 'Employee role updated successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to delete an existing employee role
@app.route('/delete_employee_role/<id>', methods=['DELETE'])
def delete_employee_role(id):
    try:
        # Delete the employee role from the database
        cursor.execute(f"DELETE FROM roles WHERE id='{id}'")
        cnx.commit()
        
        return make_response({'message': 'Employee role deleted successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

 #Route to add a new customer
@app.route('/add_customer', methods=['POST'])
def add_customer():
    try:
        # Get the customer data from the request
        id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        
        # Insert the new customer into the database
        cursor.execute(f"INSERT INTO customers (id, name, email, phone) VALUES ('{id}', '{name}', '{email}', '{phone}')")
        cnx.commit()
        
        return make_response({'message': 'Customer added successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to retrieve a specific customer
@app.route('/get_customer/<id>', methods=['GET'])
def get_customer(id):
    try:
        # Retrieve the customer from the database
        cursor.execute(f"SELECT * FROM customers WHERE id='{id}'")
        customer = cursor.fetchone()
        
        # Check if the customer exists
        if customer is not None:
            # Return the customer data
            return make_response({'customer': {'id': customer[0], 'name': customer[1], 'email': customer[2], 'phone': customer[3]}}, 200)
        else:
            # Return an error if the customer does not exist
            return make_response({'error': 'Customer not found'}, 404)
    except:
        return make_response({'error': 'An error occurred'}, 400)
    
# Route to list all customers
@app.route('/list_customers', methods=['GET'])
def list_customers():
    try:
        # Get all customers from the database
        cursor.execute("SELECT * FROM customers")
        customers = []
        for id, name, email, phone in cursor:
            customer = {}
            customer['id'] = id
            customer['name'] = name
            customer['email'] = email
            customer['phone'] = phone
            customers.append(customer)

        return make_response({'customers': customers}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to update an existing customer
@app.route('/update_customer/<id>', methods=['PUT'])
def update_customer(id):
    try:
        # Get the customer data from the request
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        
        # Update the customer in the database
        cursor.execute(f"UPDATE customers SET name='{name}', email='{email}', phone='{phone}' WHERE id='{id}'")
        cnx.commit()
        
        return make_response({'message': 'Customer updated successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to delete an existing customer
@app.route('/delete_customer/<customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    try:
        # Delete the employee from the database
        cursor.execute(f"DELETE FROM customers WHERE id='{customer_id}'")
        cnx.commit()

        return make_response({'message': 'Customer deleted successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to add a new supermarket
@app.route('/add_supermarket', methods=['POST'])
def add_supermarket():
    try:
        # Get the supplier data from the request
        id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        
        # Insert the new supplier into the database
        cursor.execute(f"INSERT INTO supermarkets (id, name, email, phone) VALUES ('{id}', '{name}', '{email}', '{phone}')")
        cnx.commit()
        
        return make_response({'message': 'Supermarket added successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)
    
# Route to retrieve a specific supplier
@app.route('/get_supermarket/<id>', methods=['GET'])
def get_supermarket(id):
    try:
        # Retrieve the supplier from the database
        cursor.execute(f"SELECT * FROM supermarkets WHERE id='{id}'")
        supermarket = cursor.fetchone()

        # Check if the supermarket exists
        if supermarket is not None:
            # Return the supermarket data
            return make_response({'supermarket': {'id': supermarket[0], 'name': supermarket[1], 'email': supermarket[2], 'phone': supermarket[3]}}, 200)
        else:
            # Return an error if the supermarket does not exist
            return make_response({'error': 'Supermarket not found'}, 404)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to list all supermarkets
@app.route('/list_supermarkets', methods=['GET'])
def list_supermarkets():
    try:
        # Get all supermarkets from the database
        cursor.execute("SELECT * FROM supermarkets")
        supermarkets = []
        for id, name, email, phone in cursor:
            supermarket = {}
            supermarket['id'] = id
            supermarket['name'] = name
            supermarket['email'] = email
            supermarket['phone'] = phone
            supermarkets.append(supermarket)

        return make_response({'supermarkets': supermarkets}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)
    
# Route to update an existing supermakert
@app.route('/update_supermarket/<supermarket_id>', methods=['PUT'])
def update_supermarket(supermarket_id):
    try:
        # Get the supermarket data from the request
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        
        # Update the supermarket in the database
        cursor.execute(f"UPDATE supermarkets SET name='{name}', email='{email}', phone='{phone}' WHERE id='{supermarket_id}'")
        cnx.commit()
        
        return make_response({'message': 'Supermrket updated successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to delete an existing supermarket
@app.route('/delete_supermarket/<supermarket_id>', methods=['DELETE'])
def delete_supermarket(supermarket_id):
    try:
        # Delete the supermarket from the database
        cursor.execute(f"DELETE FROM supermarkets WHERE id='{supermarket_id}'")
        cnx.commit()
        
        return make_response({'message': 'Supermarket deleted successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to add a new address
@app.route('/add_address', methods=['POST'])
def add_address():
    try:
        # Get the address data from the request
        id = request.form['id']
        street_address = request.form['street_address']
        city = request.form['city']
        parish = request.form['parish']
        
        # Insert the new address into the database
        cursor.execute(f"INSERT INTO addresses (id, street_address, city, parish) VALUES ('{id}', '{street_address}', '{city}', '{parish}')")
        cnx.commit()
        
        return make_response({'message': 'Address added successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)
    
# Route to retrieve a specific address
@app.route('/get_address/<id>', methods=['GET'])
def get_address(id):
    try:
        # Retrieve the address from the database
        cursor.execute(f"SELECT * FROM addresses WHERE id='{id}'")
        address = cursor.fetchone()

        # Check if the address exists
        if address is not None:
            # Return the address data
            return make_response({'address': {'id': address[0], 'street_address': address[1], 'city': address[2], 'parish': address[3]}}, 200)
        else:
            # Return an error if the address does not exist
            return make_response({'error': 'Address not found'}, 404)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to list all addresses
@app.route('/list_addresses', methods=['GET'])
def list_addresses():
    try:
        # Get all addresses from the database
        cursor.execute("SELECT * FROM addresses")
        addresses = []
        for id, street_address, city, parish in cursor:
            address = {}
            address['id'] = id
            address['street_address'] = street_address
            address['city'] = city
            address['parish'] = parish
            addresses.append(address)

        return make_response({'addresses': addresses}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to update an existing address
@app.route('/update_address/<address_id>', methods=['PUT'])
def update_address(address_id):
    try:
        # Get the address data from the request
        street_address = request.form['street_address']
        city = request.form['city']
        parish = request.form['parish']
        
        # Update the address in the database
        cursor.execute(f"UPDATE addresses SET street_address='{street_address}', city='{city}', parish='{parish}' WHERE id='{address_id}'")
        cnx.commit()
        
        return make_response({'message': 'Address updated successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)
    
# Route to delete an existing address
@app.route('/delete_address/<address_id>', methods=['DELETE'])
def delete_address(address_id):
    try:
        # Delete the address from the database
        cursor.execute(f"DELETE FROM addresses WHERE id='{address_id}'")
        cnx.commit()
        
        return make_response({'message': 'Address deleted successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

@app.route('/add_product', methods=['POST']) 
def add_product(): 
    try: 
        # Get the product data from the request
        name = request.form['name'] 
        category = request.form['category'] 
        price = request.form['price'] 
        stock = request.form['stock']

        # Insert the new product into the database
        cursor.execute(f"INSERT INTO products (name, category, price, stock) VALUES ('{name}', '{category}', '{price}', '{stock}')")
        cnx.commit()
    
        return make_response({'message': 'Product added successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

@app.route('/get_product/<id>', methods=['GET']) 
def get_product(id): 
    try: 
        # Retrieve the product from the database 
        cursor.execute(f"SELECT * FROM products WHERE id='{id}'") 
        product = cursor.fetchone()

        # Check if the product exists
        if product is not None:
            # Return the product data
            return make_response({'product': {'id': product[0], 'name': product[1], 'category': product[2], 'price': product[3], 'stock': product[4]}}, 200)
        else:
            # Return an error if the product does not exist
            return make_response({'error': 'Product not found'}, 404)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to list all products
@app.route('/list_products', methods=['GET'])
def list_products():
    try:
        # Get all products from the database
        cursor.execute("SELECT * FROM products")
        products = []
        for id, name, category, price, stock in cursor:
            product = {}
            product['id'] = id
            product['name'] = name
            product['category'] = category
            product['price'] = price
            product['stock'] = stock
            products.append(product)

        return make_response({'products': products}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)
    
# Route to update an existing product
@app.route('/update_product/<product_id>', methods=['PUT']) 
def update_product(product_id): 
    try: 
        # Get the product data from the request 
        name = request.form['name'] 
        description = request.form['description'] 
        price = request.form['price']

        # Update the product in the database
        cursor.execute(f"UPDATE products SET name='{name}', description='{description}', price='{price}' WHERE id='{product_id}'")
        cnx.commit()
    
        return make_response({'message': 'Product updated successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to delete an existing product
@app.route('/delete_product/<product_id>', methods=['DELETE']) 
def delete_product(product_id): 
    try: 
        # Delete the product from the database 
        cursor.execute(f"DELETE FROM products WHERE id='{product_id}'") 
        cnx.commit()

        return make_response({'message': 'Product deleted successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to place an order
@app.route('/place_order', methods=['POST']) 
def place_order(): 
    try: 
        # Get the order data from the request 
        customer_id = request.form['customer_id'] 
        product_id = request.form['product_id'] 
        quantity = request.form['quantity'] 
        price = request.form['price'] 
        date = request.form['date']

        # Insert the new order into the database
        cursor.execute(f"INSERT INTO orders (customer_id, product_id, quantity, price, date) VALUES ('{customer_id}', '{product_id}', '{quantity}', '{price}', '{date}')")
        cnx.commit()
    
        return make_response({'message': 'Order placed successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to retrieve a specific order
@app.route('/get_order/<id>', methods=['GET']) 
def get_order(id): 
    try: 
        # Retrieve the order from the database 
        cursor.execute(f"SELECT * FROM orders WHERE id='{id}'") 
        order = cursor.fetchone()

        # Check if the order exists
        if order is not None:
            # Return the order data
            return make_response({'order': {'id': order[0], 'customer_id': order[1], 'product_id': order[2], 'quantity': order[3], 'price': order[4], 'date': order[5]}}, 200)
        else:
            # Return an error if the order does not exist
            return make_response({'error': 'Order not found'}, 404)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to list all orders
@app.route('/list_orders', methods=['GET'])
def list_orders():
    try:
        # Get all orders from the database
        cursor.execute("SELECT * FROM orders")
        orders = []
        for id, customer_id, product_id, quantity, price, date in cursor:
            order = {}
            order['id'] = id
            order['customer_id'] = customer_id
            order['product_id'] = product_id
            order['quantity'] = quantity
            order['price'] = price
            order['date'] = date.strftime('%Y-%m-%d')
            orders.append(order)

        return make_response({'orders': orders}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to update an existing order 
@app.route('/update_order/<order_id>', methods=['PUT']) 
def update_order(order_id): 
    try: 
        # Get the order data from the request 
        customer_id = request.form['customer_id'] 
        product_id = request.form['product_id'] 
        quantity = request.form['quantity']
        price = request.form['price']
        date = request.form['date']

        # Update the order in the database
        cursor.execute(f"UPDATE order SET customer_id='{customer_id}', product_id='{product_id}', quantity= '{quantity}', price='{price}, date='{date}' WHERE id='{order_id}'")
        cnx.commit()
    
        return make_response({'message': 'Order updated successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)
    
# Route to delete an existing order
@app.route('/delete_order/<order_id>', methods=['DELETE']) 
def delete_order(order_id): 
    try: 
        # Delete the order from the database 
        cursor.execute(f"DELETE FROM orders WHERE id='{order_id}'") 
        cnx.commit()

        return make_response({'message': 'Order deleted successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)
    
# Route to add a new item to a cart
@app.route('/carts/add_item', methods=['POST'])
def add_item_to_cart():
    try:
        # Get the item data from the request
        product_id = request.form['product_id']
        quantity = request.form['quantity']
        
        # Insert the new item into the cart
        cursor.execute(f"INSERT INTO carts (product_id, quantity) VALUES ('{product_id}', '{quantity}')")
        cnx.commit()
        
        return make_response({'message': 'Item added to cart successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to get a specific item from a cart
@app.route('/carts/get_item/<cart_id>', methods=['GET'])
def get_item_from_cart(cart_id):
    try:
        # Retrieve the item from the cart
        cursor.execute(f"SELECT * FROM carts WHERE id='{cart_id}'")
        item = cursor.fetchone()
        
        # Check if the item exists
        if item is not None:
            # Return the item data
            return make_response({'item': {'id': item[0], 'product_id': item[1], 'quantity': item[2]}}, 200)
        else:
            # Return an error if the item does not exist
            return make_response({'error': 'Item not found in cart'}, 404)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to list all items in a cart
@app.route('/carts/list_items', methods=['GET'])
def list_items_in_cart():
    try:
        # Get all items from the cart
        cursor.execute("SELECT * FROM carts")
        items = []
        for id, product_id, quantity in cursor:
            item = {}
            item['id'] = id
            item['product_id'] = product_id
            item['quantity'] = quantity
            items.append(item)

        return make_response({'items': items}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to update an existing item in a cart
@app.route('/carts/update_item/<cart_id>', methods=['PUT'])
def update_item_in_cart(cart_id):
    try:
        # Get the item data from the request
        product_id = request.form['product_id']
        quantity = request.form['quantity']
        
        # Update the item in the cart
        cursor.execute(f"UPDATE carts SET product_id='{product_id}', quantity='{quantity}' WHERE id='{cart_id}'")
        cnx.commit()
        
        return make_response({'message': 'Item updated in cart successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to delete an existing item from a cart
@app.route('/carts/delete_item/<cart_id>', methods=['DELETE'])
def delete_item_from_cart(cart_id):
    try:
        # Delete the item from the cart
        cursor.execute(f"DELETE FROM carts WHERE id='{cart_id}'")
        cnx.commit()
        
        return make_response({'message': 'Item deleted from cart successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)
    
# Route to add a new sale
@app.route('/add_sale', methods=['POST'])
def add_sale():
    try:
        # Get the sale data from the request
        customer_id = request.form['customer_id']
        product_id = request.form['product_id']
        quantity = request.form['quantity']
        price = request.form['price']
        date = request.form['date']
        
        # Add the sale to the database
        cursor.execute(f"INSERT INTO sales (customer_id, product_id, quantity, price, date) VALUES ('{customer_id}', '{product_id}', '{quantity}', '{price}', '{date}')")
        cnx.commit()
        
        return make_response({'message': 'Sale added successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)


# Route to get a single sale by ID
@app.route('/get_sale/<sale_id>', methods=['GET'])
def get_sale(sale_id):
    try:
        # Get the sale from the database
        cursor.execute(f"SELECT * FROM sales WHERE id='{sale_id}'")
        sale = cursor.fetchone()
        if sale is None:
            return make_response({'error': 'Sale not found'}, 404)
        
        # Create a dictionary of the sale data
        sale_data = {}
        sale_data['id'] = sale[0]
        sale_data['customer_id'] = sale[1]
        sale_data['product_id'] = sale[2]
        sale_data['quantity'] = sale[3]
        sale_data['price'] = sale[4]
        sale_data['date'] = sale[5].strftime('%Y-%m-%d')
        
        return make_response({'sale': sale_data}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)


# Route to list all sales
@app.route('/list_sales', methods=['GET'])
def list_sales():
    try:
        # Get all sales from the database
        cursor.execute("SELECT * FROM sales")
        sales = []
        for id, customer_id, product_id, quantity, price, date in cursor:
            sale = {}
            sale['id'] = id
            sale['customer_id'] = customer_id
            sale['product_id'] = product_id
            sale['quantity'] = quantity
            sale['price'] = price
            sale['date'] = date.strftime('%Y-%m-%d')
            sales.append(sale)

        return make_response({'sales': sales}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)


# Route to update an existing sale
@app.route('/update_sale/<sale_id>', methods=['PUT'])
def update_sale(sale_id):
    try:
        # Get the sale data from the request
        customer_id = request.form['customer_id']
        product_id = request.form['product_id']
        quantity = request.form['quantity']
        price = request.form['price']
        date = request.form['date']
        
        # Update the sale in the database
        cursor.execute(f"UPDATE sales SET customer_id='{customer_id}', product_id='{product_id}', quantity='{quantity}', price='{price}', date='{date}' WHERE id='{sale_id}'")
        cnx.commit()
        
        return make_response({'message': 'Sale updated successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)


# Route to delete an existing sale
@app.route('/delete_sale/<sale_id>', methods=['DELETE'])
def delete_sale(sale_id):
    try:
        # Delete the sale from the database
        cursor.execute(f"DELETE FROM sales WHERE id='{sale_id}'")
        cnx.commit()
        
        return make_response({'message': 'Sale deleted successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to add a payment
@app.route('/add_payment', methods=['POST'])
def add_payment():
    try:
        # Get the payment data from the request
        customer_id = request.form['customer_id']
        amount = request.form['amount']
        date = request.form['date']
        
        # Insert the payment into the database
        cursor.execute(f"INSERT INTO payments (customer_id, amount, date) VALUES ('{customer_id}', {amount}, '{date}')")
        cnx.commit()
        
        return make_response({'message': 'Payment added successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to get a payment by ID
@app.route('/get_payment/<payment_id>', methods=['GET'])
def get_payment(payment_id):
    try:
        # Get the payment from the database
        cursor.execute(f"SELECT * FROM payments WHERE id='{payment_id}'")
        payment = cursor.fetchone()
        if payment:
            # Return the payment
            payment_dict = {}
            payment_dict['id'] = payment[0]
            payment_dict['customer_id'] = payment[1]
            payment_dict['amount'] = float(payment[2])
            payment_dict['date'] = str(payment[3])
            return make_response({'payment': payment_dict}, 200)
        else:
            return make_response({'error': 'Payment not found'}, 404)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to list all payments
@app.route('/list_payments', methods=['GET'])
def list_payments():
    try:
        # Get all payments from the database
        cursor.execute("SELECT * FROM payments")
        payments = []
        for payment in cursor:
            payment_dict = {}
            payment_dict['id'] = payment[0]
            payment_dict['customer_id'] = payment[1]
            payment_dict['amount'] = float(payment[2])
            payment_dict['date'] = str(payment[3])
            payments.append(payment_dict)

        return make_response({'payments': payments}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to update a payment
@app.route('/update_payment/<payment_id>', methods=['PUT'])
def update_payment(payment_id):
    try:
        # Get the payment data from the request
        customer_id = request.form['customer_id']
        amount = request.form['amount']
        date = request.form['date']
        
        # Update the payment in the database
        cursor.execute(f"UPDATE payments SET customer_id='{customer_id}', amount={amount}, date='{date}' WHERE id='{payment_id}'")
        cnx.commit()
        
        return make_response({'message': 'Payment updated successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

# Route to delete an existing payment
@app.route('/delete_payment/<payment_id>', methods=['DELETE'])
def delete_payment(payment_id):
    try:
        # Delete the payment from the database
        cursor.execute(f"DELETE FROM payments WHERE id='{payment_id}'")
        cnx.commit()
        
        return make_response({'message': 'Payment deleted successfully'}, 200)
    except:
        return make_response({'error': 'An error occurred'}, 400)

if __name__ == '__main__':
    app.run(port=5001)
