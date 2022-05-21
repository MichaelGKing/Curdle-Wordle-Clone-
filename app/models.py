import csv
from app import db, app
from werkzeug.security import generate_password_hash

class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(64), unique=True, index=True, nullable=False)
    cheeses = db.relationship('Cheese', backref='type', lazy='dynamic')

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal_name = db.Column(db.String(64), unique=True, index=True, nullable=False)
    cheeses = db.relationship('Cheese', backref='animal', lazy='dynamic')

class Continent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    continent_name = db.Column(db.String(64), index=True, nullable=False)
    countries = db.relationship('Country', backref='continent', lazy='dynamic')

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(64), index=True, nullable=False)
    continent_id = db.Column(db.String(64), db.ForeignKey('continent.id'))
    cheeses = db.relationship('Cheese', backref='country', lazy='dynamic')

    def __repr__(self):
        return '<Country {}>'.format(self.country_name)

class Cheese(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cheese_name = db.Column(db.String(64), unique=True, index=True, nullable=False)
    type_id = db.Column(db.String(64), db.ForeignKey('type.id'), nullable=False)
    animal_id = db.Column(db.String(64), db.ForeignKey('animal.id'), nullable=False)
    country_id = db.Column(db.String(64), db.ForeignKey('country.id'), nullable=False)
    mouldy = db.Column(db.Boolean)
    image_filename = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return '<Cheese: {}>'.format(self.cheese_name)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

class PuzzleHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_puzzle_id = db.Column(db.Integer, nullable=False)
    server_puzzle_id = db.Column(db.Integer, nullable=False)

# Define a function to add a puzzle to the database
# Used in routes for puzzle upload, and in dbinit to 
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

# Set account admin password from environment varible if exists, fallback to config varible
User.query.delete()
admin = User(username="curdleadmin", password_hash=generate_password_hash(app.config['ADMIN_PASSWORD']))
db.session.add(admin)
db.session.commit()

# Set puzzle attibutes

# Set cheese types
types = ("fresh","soft","semi-hard","hard","blue","processed")
Type.query.delete()
for value in types:
    t = Type(type=value)
    db.session.add(t)
    db.session.commit()

# Set animals of origin
animals = ("cow","sheep","goat","moose")
Animal.query.delete()
for value in animals:
    a = Animal(animal_name=value)
    db.session.add(a)
    db.session.commit()

# Set continents
continents = ("Africa","Asia","Europe","Middle East","North and Central America","Oceania","South America")
Continent.query.delete()
for value in continents:
    c = Continent(continent_name=value)
    db.session.add(c)
    db.session.commit()

# Set countries - Not all countries on planet listed, only those with recognisable cheeses lmao
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
Country.query.delete()
for value in countries:
    c = Country(country_name=value[0], continent_id=value[1])
    db.session.add(c)
    db.session.commit()

# Set puzzles
def import_puzzles():
    Cheese.query.delete()

    # Open saved puzzles csv file, and add each line as a array within the cheeses array
    file = open('puzzles.csv')
    csvreader = csv.reader(file)
    cheeses = []
    for row in csvreader:
        cheeses.append(row)

    for puzzle in cheeses:
        add_puzzle(puzzle)