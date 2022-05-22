import csv
from app import db, app
from app.models import User, Type, Animal, Continent, Country, Cheese, add_puzzle


# Set account admin password from environment varible if exists, fallback to config varible
def import_admin_user():
    User.query.delete()
    u = User(username='curdleadmin', email="admin@curdle.com")
    u.set_password(app.config['ADMIN_PASSWORD'])
    db.session.add(u)
    db.session.commit()

# Set puzzle attibutes

# Set cheese types
def import_types():
    types = ("blue","soft-ripened","washed-rined","smear-ripened","processed", "hard", "fresh")
    Type.query.delete()
    for value in types:
        t = Type(type=value)
        db.session.add(t)
        db.session.commit()

# Set animals of origin
def import_animals():
    animals = ("cow","sheep","goat","moose")
    Animal.query.delete()
    for value in animals:
        a = Animal(animal_name=value)
        db.session.add(a)
        db.session.commit()

# Set continents
def import_continents():
    continents = ("Africa","Asia","Europe","Middle East","North and Central America","Oceania","South America")
    Continent.query.delete()
    for value in continents:
        c = Continent(continent_name=value)
        db.session.add(c)
        db.session.commit()

# Set countries - Not all countries on planet listed, only those with recognisable cheeses lmao
def import_countries():
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

def import_puzzle_data():
    import_admin_user()
    import_types()
    import_animals()
    import_countries()
    import_continents()
    import_puzzles()
