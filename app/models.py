from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(64), unique=True, index=True, nullable=False)

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal_name = db.Column(db.String(64), unique=True, index=True, nullable=False)


class Continent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    continent_name = db.Column(db.String(64), index=True, nullable=False)

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(64), index=True, nullable=False)
    continent_id = db.Column(db.String(64), db.ForeignKey('continent.id'))

    country_continent = db.relationship("Continent", foreign_keys=[continent_id])

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
    image_attribution = db.Column(db.String(256))
    info_link = db.Column(db.String(256))

    cheese_type = db.relationship("Type", foreign_keys=[type_id])
    cheese_animal = db.relationship("Animal", foreign_keys=[animal_id])
    cheese_country = db.relationship("Country", foreign_keys=[country_id])

    def __repr__(self):
        return '<Cheese: {}>'.format(self.cheese_name)   

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class PuzzleHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_puzzle_id = db.Column(db.Integer, nullable=False)
    server_puzzle_id = db.Column(db.Integer, nullable=False)
    puzzle_date = db.Column(db.String(64), nullable=False)

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
    db.session.commit
    
# Configure a user loader function - Loads a user, given an ID, from the database, and registers it with Flask-Login
@login.user_loader
def load_user(id):
    return User.query.get(int(id))