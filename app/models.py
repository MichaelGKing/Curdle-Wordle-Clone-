from app import db

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

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
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
