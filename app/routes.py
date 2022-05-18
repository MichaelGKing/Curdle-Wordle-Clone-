
import os, csv
from app import app, db, models
from app.forms import AdminLoginForm, PuzzleUploadForm
from flask import render_template, flash, redirect, request
from wtforms import ValidationError
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from app.models import Cheese, Type, Country, Animal, Continent, Admin

authorised = False
# Routes are written as shown below
# The decorators at the beginning (starting with @app) define what URL's the code below them is run on
# The view function contains this code

# Required cheese attributes
types = ("fresh","soft","semi-hard","hard","blue","processed")
animals = ("cow","sheep","goat","moose")
continents = ("Africa","Asia","Europe","Middle East","North and Central America","Oceania","South America")
countries = [
    ["Benin" , 1],
	["Ethiopia",  1],
	["Mauritania", 1],
    ["Armenia", 2],
    ["Azerbaijan", 2],
    ["Bangladesh", 2],
    ["China", 2],
    ["Cyprus", 2],
    ["Georgia", 2],
    ["India", 2],
    ["Indonesia", 2],
    ["Japan", 2],
    ["Korea", 2],
    ["Malaysia", 2],
    ["Mongolia", 2],
    ["Nepal", 2],
    ["Philippines", 2],
    ["Albania", 3],
    ["Austria", 3],
    ["Belgium", 3],
    ["Bosnia and Herzegovina", 3],
    ["Bulgaria", 3],
    ["Croatia", 3],
    ["Czech Republic", 3],
    ["Denmark", 3],
    ["Estonia", 3],
    ["Finland", 3],
    ["France", 3],
    ["Germany", 3],
    ["Greece", 3],
    ["Hungary", 3],
    ["Iceland", 3],
    ["Ireland", 3],
    ["Italy", 3],
    ["Kosovo", 3],
    ["Latvia", 3],
    ["Lithuania", 3],
    ["Malta", 3],
    ["Moldova", 3],
    ["Montenegro", 3],
    ["Netherlands", 3],
    ["North Macedonia", 3],
    ["Norway", 3],
    ["Poland", 3],
    ["Portugal", 3],
    ["Romania", 3],
    ["Russia", 3],
    ["Serbia", 3],
    ["Slovakia", 3],
    ["Slovenia", 3],
    ["Spain", 3],
    ["Sweden", 3],
    ["Switzerland", 3],
    ["Ukraine", 3],
    ["United Kingdom", 3],
    ["Egypt", 4],
    ["Iran", 4],
    ["Israel", 4],
    ["Levant", 4],
    ["Turkey", 4],
    ["Canada", 5],
    ["Costa Rica", 5],
    ["El Salvador", 5],
    ["Honduras", 5],
    ["Mexico", 5],
    ["Nicaragua", 5],
    ["United States", 5],
    ["Australia", 6],
    ["Argentina", 7],
    ["Bolivia", 7],
    ["Brazil", 7],
    ["Chile", 7],
    ["Colombia", 7],
    ["Venezuela", 7]
]

# The current functionality reads puzzle list from a .csv file. 
# This file is used to store initial puzzle list and any puzzles added using the administrators Puzzle Upload form.
# If the server requires restarting and/or the database is lost or overwritten, puzzles will be reloaded from the last write to the csv
# Puzzles must be set in following format to be loaded into the database:
# 
# eg. ['Cheddar', 'hard', 'cow', 'United Kingdom', False, 'cheese1.jpg']
#
# This formatting will be controlled by the puzzle upload form inputs only allowing valid submissions

# Open saved puzzles csv file, and add each line as a array within the cheeses array
file = open('saved_puzzles.csv')
csvreader = csv.reader(file)
cheeses = []
for row in csvreader:
    cheeses.append(row)
print(cheeses)

# Add required cheese attributes to the database

# Deletes any existing values in the database for type
models.Type.query.delete()
# Iterates through the list of types defined above and adds them to the database
for value in types:
    t = Type(type=value)
    db.session.add(t)
    db.session.commit()

# Deletes any existing values in the database for animal
models.Animal.query.delete()
# Iterates through the list of animals defined above and adds them to the database
for value in animals:
    a = Animal(animal_name=value)
    db.session.add(a)
    db.session.commit()

# Deletes any existing values in the database for continent
models.Continent.query.delete()
# Iterates through the list of continents defined above and adds them to the database
for value in continents:
    c = Continent(continent_name=value)
    db.session.add(c)
    db.session.commit()

# Deletes any existing values in the database for country
models.Country.query.delete()
# Iterates through the array of countries defined above and adds them to the database
for value in countries:
    c = Country(country_name=value[0], continent_id=value[1])
    db.session.add(c)
    db.session.commit()

# Deletes any existing values in the database for country
models.Cheese.query.delete()
# Iterates through the array of countries defined above and adds them to the database
for value in cheeses:

    # The csv reader returns all values as strings
    # This checks the mouldy attribute to see if it is true or false and assigns the correct boolean value to a new variable
    if value[4] == 'True' or value[4] == '1':
        is_mouldy = True
    else:
        is_mouldy = False

    c = Cheese(
        cheese_name=value[0], 
        type_id = db.session.query(Type.id).filter(Type.type == value[1]).scalar(), 
        animal_id = db.session.query(Animal.id).filter(Animal.animal_name == value[2]).scalar(), 
        country_id = db.session.query(Country.id).filter(Country.country_name == value[3]).scalar(), 
        mouldy=is_mouldy, 
        image_filename=value[5]
        )
    db.session.add(c)
    db.session.commit()

todays_cheese = 1

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
# A view function for the homepage
def index():
    # Placeholder puzzle - a class will be made for this that will pull a random daily cheese from the database
    cheeses = ["Cheddar", "Camembert", "Parmesan", "Red Leicester", "Blue Cheese", "A NEW CHEESE"]
    image = 'cheese1.jpg'

    # Render a html template in the browser
    # The page renderer also passes the puzzle object through to the front end?
    return render_template('index.html', cheeses=cheeses, image=image)

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
    
@app.route('/check-guess', methods=['GET', 'POST'])
def get_guess():
    
    # Get cheese name from client side
    if request.method == "POST":

        guess = request.get_json()
        print(guess)

    # Get list of cheese attributes from the database for the cheese

    # Check the guess against the correct cheese

    # Produce list of boolean values relatining to attribute matches 

    # Return string in json format to the client side

        return {'message': "Hello Client!"}





