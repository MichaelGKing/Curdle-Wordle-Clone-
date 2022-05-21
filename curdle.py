
from app import app, db
from app.models import Cheese, Type, Country, Animal, Continent, User

# The shell context processor allows any of the classes represented in the return statement to be used in the Flask shell environment
# This can be accessed by Flask Shell
# Very usefull for testing things in the shell while developing an app
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Cheese': Cheese, 'Type': Type, "Country": Country, "Animal": Animal, "Continent": Continent, "User": User}