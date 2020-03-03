from flask import render_template, url_for
from application import app

bookData = []

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home', books=bookData)

@app.route('/register')
def register():
    return render_template('register.html', title='Register')

@app.route('/login')
def login():
    return render_template('login.html', title='Login')

@app.route('/myaccount')
def myaccount():
    return render_template('myaccount.html', title='My Account')

@app.route('/logout')
def logout():
    return render_template('logout.html', title='Logout')
