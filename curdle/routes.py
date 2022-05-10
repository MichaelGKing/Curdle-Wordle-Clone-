
from curdle import app, AdminLoginForm
from flask import render_template, redirect

# Toutes are written as shown below
# The decorators at the beginning (starting with @app) define what URL's the code below them is run on
# The view function contains this code


@app.route('/')
@app.route('/index')
# A view function for the homepage
def index():
    return render_template('index.html')

@app.route('/add-new-puzzle')
def add_new_puzzle():
    return "New puzzle uploading form here"

@app.route('/puzzle-uploader') 
def puzzle_uploader():
    return 

# This route below can recieve GET and POST HTTP methods, required for receiving form data
@app.route('/authorize', methods=['GET', 'POST'])
def authorize():

    # initialize new object of AdminLoginForm() class
    form = AdminLoginForm()

    # Use WTForms' FlaskForms functions to validate user input
    # The validations set in admin_login.py are checked, and if data is valid, browser is redirected to /index
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')

    # Else, browser stays at /authorise view
    return '''
    
    <h1>Sign In</h1>
    <form action="" method="post" novalidate>
        {{ form.hidden_tag() }}
        <p>
            {{ form.password.label }}<br>
            {{ form.password(size=32) }}
        </p>
        <p>{{ form.remember_me() }} {{ form.remember_me.label }}</p>
        <p>{{ form.submit() }}</p>
    </form>
    
    '''
    

