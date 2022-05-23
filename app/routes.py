import os, csv
from app import app, db
from app.forms import AdminLoginForm, PuzzleUploadForm
from flask import render_template, flash, redirect, request, url_for
from wtforms import ValidationError
from app.models import Cheese, PuzzleHistory, Type, Country, Animal, Continent, User, add_puzzle
from . import puzzlesetter
from datetime import date
from flask_login import current_user, login_user, login_required, logout_user

# Routes are written as shown below
# The decorators at the beginning (starting with @app) define what URL's the code below them is run on
# The view function contains this code

# Set global variables for client and server side puzzle IDs
todays_server_puzzle_id = 0
todays_client_puzzle_id = 0


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
# A view function for the homepage which displays the game
def index():

    global todays_server_puzzle_id
    global todays_client_puzzle_id
    
    # If TESTING set to True, use a static client-side puzzle ID that can be incremented from the admin page
    if app.config['TESTING']:
        todays_client_puzzle_id = 1

    # if TESTING False, use proper game logic and increment the client side id each day, starting at LAUNCH_DATE
    else:
        todays_client_puzzle_id = puzzlesetter.get_puzzle_id_for_client()

    # Check database to see if a puzzle has been generated for today
    result = db.session.query(PuzzleHistory).filter(PuzzleHistory.client_puzzle_id == todays_client_puzzle_id).scalar()

    # If no entry has been stored for todays puzzle, add an entry and set a server side puzzle id
    if result is None:
        todays_server_puzzle_id = puzzlesetter.set_puzzle_id_for_server()
        p = PuzzleHistory(client_puzzle_id=todays_client_puzzle_id, server_puzzle_id=todays_server_puzzle_id, puzzle_date=date.today())
        db.session.add(p)
        db.session.commit()
    # Else, use the value stored in the database
    else:
        todays_server_puzzle_id = db.session.query(PuzzleHistory.server_puzzle_id).filter(PuzzleHistory.client_puzzle_id == todays_client_puzzle_id).scalar()
        print(todays_server_puzzle_id)

    print("Todays client puzzle ID is: " + str(todays_client_puzzle_id))
    print("Todays server puzzle ID is: " + str(todays_server_puzzle_id))

    image = db.session.query(Cheese.image_filename).filter(Cheese.id == todays_server_puzzle_id).scalar()

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
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Check if user authernicated already, if so redirect to the admin page
    if current_user.is_authenticated:
        return redirect(url_for('admin'))
     # Create new form object
    form = AdminLoginForm()

    if form.validate_on_submit():

        # Create user object from results returned by searching username
        user = User.query.filter_by(username=form.username.data).first()
        # If user doesnt exist, flash message to user explaining
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))
        # Create new Flask-Login login session for the user
        login_user(user, remember=form.remember_me.data)
        # Redirect to the admin page
        return redirect(url_for('admin'))

    return render_template('login.html', title='Curdle Administrator Portal', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout: Successful', 'success')
    return redirect('/login')

@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():

    # Create new instance of PuzzleUploadForm()
    form = PuzzleUploadForm()

    # Retreive lists of cheese attributes from the database

    form.type.choices = db.session.query(Type.id, Type.type).all()
    form.animal.choices = db.session.query(Animal.id, Animal.animal_name).all() 
    form.country.choices = db.session.query(Animal.id, Country.country_name).all() 

    if form.validate_on_submit():
        # Here goes the code that recieves the data and handles adding it to the database
        if request.method == "POST":

            # Determine the next puzzle database id number

            # Count existing puzzles in database
            puzzle_count = db.session.query(Cheese).count()
            print(puzzle_count)
            # Add one to count - this will be the new id
            new_puzzle_id = puzzle_count + 1
            print(new_puzzle_id)

            # Assign new cheese name data to local variables for checking formats of data and debugging
            name = form.name.data.capitalize()
            # Check if cheese already in the database, if not None, flash message to user and reload page
            result = db.session.query(Cheese.cheese_name).filter(Cheese.cheese_name == name).first()
            if result != None:
                flash('! Upload failed !', 'error')
                flash('There was already a cheese of that name in the database.', 'error')
                return render_template('admin.html', title="Curdle Administrator Console", form=form)

            # Assing rest of puzzle data to local variables...
            type = eval(form.type.data) # This data is returned in a string, but in tuple format.. eval fixes this.
            animal = eval(form.animal.data) # Unfortunately this now means the client could pass malicious code to the server..
            country = eval(form.country.data) # And it will be run, no questions asked?
            mould = form.mould.data
            image = form.image.data
            attribution = form.attribution.data
            link = form.link.data

            # Generate new generic image file name in format: cheese<id>.<file extension>
            ext_list = list(app.config['ALLOWED_EXTENSIONS'])
            filename = 'cheese'
            for ext in ext_list:
                print(ext)
                print(image.filename.endswith(ext))
                if image.filename.endswith(ext):
                    filename = filename+str(new_puzzle_id)+'.'+ext
                    break
            
            # Set filepath for new image to be uploaded to then save image
            filepath = os.path.join(os.path.dirname(app.instance_path), 'app', 'static', 'images',  filename)
            image.save(filepath)

            # Set a list of puzzle attributes in format that add_puzzle() can understand
            puzzle = [ name, type[1], animal[1], country[1], mould, "/images/"+filename, attribution, link ]
            
            # Write the list to the puzzles.csv file for backup incase the database needs to be rebuilt
            with open('puzzles.csv', 'a', newline='') as f:
                writer_object = csv.writer(f)
                writer_object.writerow(puzzle)
                f.close()

            # Add puzzle to the database
            add_puzzle(puzzle)
            flash('* Puzzle Upload Successful *', 'success')
    
    return render_template('admin.html', title="Curdle Administrator Console", form=form)
    
@app.route('/check-guess', methods=['GET', 'POST'])
def check_guess():
    
    # Get cheese name from client side
    if request.method == "POST":

        cheese_name = request.get_json() # This returns a single entry dict containing the cheese name

        answer = Cheese.query.filter_by(id=puzzlesetter.get_puzzle_id_for_server()).first()

        guess = Cheese.query.filter_by(cheese_name=cheese_name['cheese_name']).first() #cheese_name

        results = {'name': True, 'country': True, 'mould': True, 'animal': True, 'type': True, 'continent': True}

        # If the answer and guess share the same ID, the game is won (id is unique in the database)
        if (answer.id == guess.id) and (answer.cheese_name != guess.cheese_name):
                
                return results
        
        if (answer.cheese_name != guess.cheese_name):
            results['name'] = False

        if (answer.country_id != guess.country_id):
            results["country"] = False

        if (answer.mouldy != guess.mouldy):
            results["mould"] = False

        if (answer.animal_id != guess.animal_id):
            results["animal"] = False

        if (answer.type_id != guess.type_id):
            results["type"] = False

        guess_country = Country.query.filter_by(id=guess.country_id).first()

        answer_country = Country.query.filter_by(id=answer.country_id).first()

        if (answer_country.continent_id != guess_country.continent_id):
            results["continent"] = False

        print(results)
        return results

@app.route('/get-cheeses', methods=['GET', 'POST'])
def get_cheeses():

    if request.method == "POST":
        
        result = db.session.query(Cheese.id, Cheese.cheese_name).all()
    
        # Iterate through results and add all cheese name values to a list
        cheeses = {}
        for row in result:
            cheeses[row[0]] = row[1]
        print(cheeses)
        return cheeses

# Respond to client request todays puzzle id (the client facing one) and the puzzles date
@app.route('/puzzle-id', methods=['GET', 'POST'])
def puzzle_id():

    if request.method == "POST":
        
        puzzle_data = puzzlesetter.get_daily_puzzle_info()

        print(puzzle_data)
        
        return puzzle_data

# Returns the correct answer - used by client to inform 
@app.route('/get-answer', methods=['GET', 'POST'])
def get_answer():

    if request.method == "POST":

        answer = db.session.query(Cheese.cheese_name, Type.type, Animal.animal_name, Country.country_name, Cheese.mouldy, Continent.continent_name, Cheese.image_attribution, Cheese.info_link)\
            .join(Cheese.cheese_type)\
            .join(Cheese.cheese_animal)\
            .join(Cheese.cheese_country)\
            .join(Country.country_continent)\
            .filter(Cheese.id == todays_server_puzzle_id).first()

        json_answer = {
            'name' : answer[0],
            'type' : answer[1],
            'animal' : answer[2],
            'country' : answer[3],
            'mouldy' : answer[4],
            'continent' : answer[5],
            'image_attribution' : answer[6],
            'info_link' : answer[7]
            }
        
        return(json_answer)

# Clear puzzle history table in the database for testing/demonstration
@app.route('/reset-puzzle-history', methods=['GET', 'POST'])
def reset_puzzle_history():

    if request.method == "POST":

        print(request.get_json)

        PuzzleHistory.query.delete()

        flash('* Server puzzle history cleared *', 'success')

        return redirect(url_for('admin'))
        
# Increment the client-side puzzle id counter for testing/demonstration
@app.route('/increment-puzzle-id', methods=['GET', 'POST'])
def increment_puzzle_id():
    
    if request.method == "POST":

        print(request.get_json)
        
        global todays_client_puzzle_id
        todays_client_puzzle_id += 1

        flash('* It is a new day! *', 'success')

        return redirect(url_for('admin'))

