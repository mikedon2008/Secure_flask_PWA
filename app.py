from flask import Flask, render_template, request, redirect
import sqlite3
import os

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = os.urandom(24)

# Define the route for the login page
@app.route('/')
def login():
    return render_template("login.html")

# Define the route for login validation
@app.route('/login_validation', methods=['POST'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')

    connection = sqlite3.connect('LoginData.db')
    cursor = connection.cursor()

    user = cursor.execute("SELECT * FROM USERS WHERE email=? AND password=?", (email, password)).fetchall()
    connection.close()

    if len(user) > 0:
        # Redirect to /home with user details as URL parameters
        return redirect(f'/home?fname={user[0][0]}&lname={user[0][1]}&email={user[0][2]}')
    else:
        return redirect('/')

# Define the route for the home page after login
@app.route('/home')
def home():
    fname = request.args.get('fname')
    lname = request.args.get('lname')
    email = request.args.get('email')

    return render_template('home.html', fname=fname, lname=lname, email=email)

# Run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
