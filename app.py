from flask import Flask, render_template, request, redirect
import sqlite3
import os

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = os.urandom(24)

# Define the route for the home page
@app.route('/')
def login():
    return render_template(login.html)

# Run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)

