
from cProfile import label
from curdle import app
from curdle.admin_login import AdminLoginForm
from flask import render_template, flash, redirect

# Toutes are written as shown below
# The decorators at the beginning (starting with @app) define what URL's the code below them is run on
# The view function contains this code


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
# A view function for the homepage
def index():
    # Placeholder puzzle - a class will be made for this that will pull a random daily cheese from the database
    puzzle = ['Cheddar', 'Hard', 'England', False, 'cheese1.jpg']

    # The page renderer also passes the puzzle object through to the front end?
    return render_template('index.html', puzzle=puzzle)

@app.route('/add-new-puzzle')
def add_new_puzzle():
    return "New puzzle uploading form here"

@app.route('/puzzle-uploader', methods=['GET', 'POST']) 
def puzzle_uploader():
    return 

# This route below can receive GET and POST requests, required for receiving form data - Default without this set is just to receive GET requests
@app.route('/authorize', methods=['GET', 'POST'])
def authorize():

    # initialize new object of AdminLoginForm() class
    form = AdminLoginForm()

    # Use WTForms' FlaskForms functions to validate user input
    # The validations set in admin_login.py are checked, and if data is valid, browser is redirected to /index
    if form.validate_on_submit():
        if (form.password.data == app.config['SECRET_KEY']):
            flash('Administration Portal Authentication Successful')
            return redirect('/add-new-puzzle')

    # Else, browser stays at /authorise view
    return render_template('authorize.html', form=form)
    

