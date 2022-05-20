from app import db, app
from werkzeug.security import generate_password_hash
from app.models import Type, Animal, Continent, Country, Cheese, Admin, add_puzzle
import csv

# When imported at the end of the application __init__ file, this module imports set values into the database
# This includes hardcoded values for all cheese attributes and a list of puzzles imported from puzzles.csv
# The default admin password is also set

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


# Add required cheese attributes to the database
def import_types():
    # Deletes any existing values in the database for type
    Type.query.delete()
    # Iterates through the list of types defined above and adds them to the database
    for value in types:
        t = Type(type=value)
        db.session.add(t)
        db.session.commit()

def import_animals():
    # Deletes any existing values in the database for animal
    Animal.query.delete()
    # Iterates through the list of animals defined above and adds them to the database
    for value in animals:
        a = Animal(animal_name=value)
        db.session.add(a)
        db.session.commit()

def import_continents():
    # Deletes any existing values in the database for continent
    Continent.query.delete()
    # Iterates through the list of continents defined above and adds them to the database
    for value in continents:
        c = Continent(continent_name=value)
        db.session.add(c)
        db.session.commit()

def import_countries():
    # Deletes any existing values in the database for country
    Country.query.delete()
    # Iterates through the array of countries defined above and adds them to the database
    for value in countries:
        c = Country(country_name=value[0], continent_id=value[1])
        db.session.add(c)
        db.session.commit()

def import_puzzles():
    # Deletes any existing values in the database for cheese
    Cheese.query.delete()

    # Open saved puzzles csv file, and add each line as a array within the cheeses array
    file = open('puzzles.csv')
    csvreader = csv.reader(file)
    cheeses = []
    for row in csvreader:
        cheeses.append(row)

    for puzzle in cheeses:
        add_puzzle(puzzle)

def set_admin_password():
    # Set the admin password from environment variable

    # Get admin password from environment variable, if doesnt exist, fallback on hardcoded value from config.py
    p = app.config['ADMIN_PASSWORD']
    hash = generate_password_hash(p)

    Admin.query.delete()
    p = Admin(password_hash=hash)
    db.session.add(p)
    db.session.commit()