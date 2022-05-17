import os
from curdle import app
from curdle.forms import AdminLoginForm, PuzzleUploadForm
from flask import render_template, flash, redirect, request
from wtforms import ValidationError
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename

authorised = False

# Routes are written as shown below
# The decorators at the beginning (starting with @app) define what URL's the code below them is run on
# The view function contains this code

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
# A view function for the homepage
def index():
    # Placeholder puzzle - a class will be made for this that will pull a random daily cheese from the database
    puzzle = {
        'name': 'Cheddar', 
        'type': 'Hard', 
        'country': 'England', 
        'mould': False,
        'animal': 'Cow',
        'img_path': '/images/cheese1.jpg'
        }

    # Render a html template in the browser
    # The page renderer also passes the puzzle object through to the front end?
    return render_template('index.html', puzzle=puzzle)

# This route below can receive GET and POST requests, required for receiving form data - Default without this set is just to receive GET requests
@app.route('/auth', methods=['GET', 'POST'])
def auth():

    # initialize new object of AdminLoginForm() class
    form = AdminLoginForm()

    # Use WTForms' FlaskForms functions to validate user input
    # The validations set in admin_login.py are checked, and if data is valid, browser is redirected to /index
    if form.validate_on_submit():

        password = request.form['password']
        # Need to start a session for user login - old method did not work
        if check_password_hash(db.get_hashed_password(), password):
            global authorised 
            authorised = True
            flash('Administration Portal Authentication Successful')
            return redirect('/puzzle-uploader')
        else:   
            raise ValidationError('The password you entered in incorrect')

    # Else, browser stays at /authorise view
    return render_template('auth.html', form=form)
    

@app.route('/puzzle-uploader', methods=['GET', 'POST']) 
def puzzle_uploader():
    
    global authorised

    # create new instance of PuzzleUploadForm()
    form = PuzzleUploadForm()
    # retreive lists of cheese attributes from the database and use them to set the choices for the form's SelectFields
    form.set_types(db.get_attribute_list('cheese_type', 'cheese_type'))
    form.set_countries(db.get_attribute_list('animal_name', 'animal'))
    form.set_animals(db.get_attribute_list('country_name', 'country'))

    if form.validate_on_submit():

        # Here goes the code that recieves the data and handles adding it to the database
        if request.method == "POST":

            req = request.form

            f = form.image.data
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.instance_path, 'images', filename))
            
            print(req)

            flash('Puzzle Upload Successful')

            # return redirect(request.url)
    
    if authorised:
        return render_template('puzzle-uploader.html', form=form)
    
    flash('You have not been authorised to view this page, please enter the admin password below to continue.')
    return redirect('/auth')

@app.route('/get-todays-puzzle', methods=['GET', 'POST'])
def get_todays_puzzle():
    return
