
import os, csv, json
from app import app, db, models
from app.forms import AdminLoginForm, PuzzleUploadForm
from flask import jsonify, render_template, flash, redirect, request
from wtforms import ValidationError
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from app.models import Cheese, Type, Country, Animal, Continent, Admin

# Used to index a puzzle for the day, should increment by +1 every day
cheese_id_counter = 2
# Somehow increment this every day - APScheduler can help?

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

# The current functionality is to read aqeqwer puzzle list from a .csv file. 
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

# Define a function to add a puzzle to the database, will be used in one of the view functions below
def add_puzzle(puzzle):

    if puzzle[4] == 'True' or puzzle[4] == '1':
        is_mouldy = True
    else:
        is_mouldy = False

    c = Cheese(
        cheese_name=puzzle[0], 
        type_id = db.session.query(Type.id).filter(Type.type == puzzle[1]).scalar(), 
        animal_id = db.session.query(Animal.id).filter(Animal.animal_name == puzzle[2]).scalar(), 
        country_id = db.session.query(Country.id).filter(Country.country_name == puzzle[3]).scalar(), 
        mouldy=is_mouldy, 
        image_filename=puzzle[5]
        )

    db.session.add(c)
    db.session.commit()

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

# Set the admin password from environment variable

# Get admin password from environment variable, if doesnt exist, fallback on hardcoded value from config.py
p = app.config['ADMIN_PASSWORD']
hash = generate_password_hash(p)

models.Admin.query.delete()
p = Admin(password_hash=hash)
db.session.add(p)
db.session.commit()

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
# A view function for the homepage
def index():
    # get cheese puzzle by ID
    # This could be randomised?

    global cheese_id_counter

    image = db.session.query(Cheese.image_filename).filter(Cheese.id == cheese_id_counter).scalar()
    # If the database query fails because the id does not exist it should return none...
    if image == None:
        # If this is the case, reset the cheese id counter to 1, starting the puzzles from the beginning again
        cheese_id_counter = 1
        image = db.session.query(Cheese.image_filename).filter(Cheese.id == cheese_id_counter).scalar()

    # Get list of cheeses from the database to be used in the game's guess selector field
    # SQLAlchemy returns this as a list of KeyedTuples for some reason, even though there is only one value stored..
    result = db.session.query(Cheese.cheese_name).all()
    
    # Iterate through results and add all cheese name values to a list
    cheeses = []
    for row in result:
        cheeses.append(row[0])

    # Render the game html template in the browser
    # Image filename and sorted list of cheeses are passed to the template renderer
    return render_template('index.html', cheeses=sorted(cheeses), image=image)

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
        if check_password_hash(hash, password):
            flash('Administration Portal Authentication Successful')
            return redirect('/puzzle-uploader')
        else:   
            raise ValidationError('The password you entered in incorrect')

    # Else, browser stays at /authorise view
    return render_template('auth.html', form=form)
    

@app.route('/puzzle-uploader', methods=['GET', 'POST']) 
def puzzle_uploader():
    
    #global authorised

    # Create new instance of PuzzleUploadForm()
    form = PuzzleUploadForm()

    # Retreive lists of cheese attributes from the database

    form.type.choices = db.session.query(Type.id, Type.type).all()
    form.animal.choices = db.session.query(Animal.id, Animal.animal_name).all() 
    form.country.choices = db.session.query(Animal.id, Country.country_name).all() 

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
    
    return render_template('puzzle-uploader.html', form=form)
    
@app.route('/check-guess', methods=['GET', 'POST'])
def get_guess():
    
    # Get cheese name from client side
    if request.method == "POST":

        cheese_name = request.get_json() # This returns a single entry dict containing the cheese name

        answer = Cheese.query.filter_by(id=cheese_id_counter).first()

        guess = Cheese.query.filter_by(cheese_name=cheese_name['cheese_name']).first() #cheese_name

        results = {'name': True, 'country': True, 'mould': True, 'animal': True, 'type': True, 'continent': True}

        # If the answer and guess share the same ID, the game is won (id is unique in the database)
        if (answer.id == guess.id) and (answer.cheese_name != guess.cheese_name):
                
                return results

        if (answer.country_id != guess.country_id):
            results["country"] = False

        if (answer.mouldy != guess.mouldy):
            results["mould"] = False

        if (answer.animal_id != guess.animal_id):
            results["name"] = False

        if (answer.type_id != guess.type_id):
            results["type"] = False


        guess_country = Country.query.filter_by(id=guess.country_id).first()

        answer_country = Country.query.filter_by(id=answer.country_id).first()

        if (answer_country.continent_id != guess_country.continent_id):
            results["continent"] = False
        
        return results






