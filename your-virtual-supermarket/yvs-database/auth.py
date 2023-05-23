from flask import Flask, request, make_response, session, redirect
from werkzeug.security import generate_password_hash, check_password_hash
import os
import mysql.connector


app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a random secret key for session encryption

# Define the database connection
cnx = mysql.connector.connect(host='localhost', user='root', password='Student1.', database='virtual_supermarket')
cursor = cnx.cursor()


# Login route
@app.route('/login', methods=['POST'])
def login():
    try:
        password = request.form['password']

        if password == 'fruit':
            # Authentication successful
            session['user_id'] = 'special_user'
            return make_response({'message': 'Logged in successfully'}, 200)
        else:
            return make_response({'error': 'Invalid credentials'}, 401)
    except Exception as e:
        return make_response({'error': str(e)}, 500)

# Logout route
@app.route('/logout')
def logout():
    # Check if the user is logged in
    if 'user_id' in session:
        # Clear the user's id from the session
        session.pop('user_id', None)
        return make_response({'message': 'Logged out successfully'}, 200)
    else:
        return make_response({'error': 'Unauthorized'}, 401)


if __name__ == '__main__':
    app.run()
