# The __init__ file tells Flask that a folder should be treated as a package
# When the app package is imported by 'setup.py' this file is run automatically because of its file name
# From the python package flask, import the class Flask

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import click
from flask.cli import with_appcontext

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

from commands.import_data import import_puzzle_data
@click.command(name='import_data')
@with_appcontext
def import_data():
    import_puzzle_data()

app.cli.add_command(import_data)

from app import models, routes

# Import our python module 'routes' which contains instructions what to render on what URL for the web site/application
# The name of the folder this file is in is 'app'. This means app is a python package, and we can import individual modules from it as needed
# Models is a python module containing object models relating to each table in the SQLite database - required for SQLAlchemy flask extension




