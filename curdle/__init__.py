# When the curdle package is imported by 'setup.py' this file is run automatically because of its file name

# From the python package flask, import the class Flask

from flask import Flask

from config import Config

# Create a new instance of the Flask application, called app

app = Flask(__name__)

# Set Flask configuration variables from Config Class variables

app.config.from_object(Config)

# Import our python module 'routes' which contains instructions what to render on what URL for the web site/application
# The name of the folder this file is in is 'curdle' 
# This means curdle is a python package, and we can import individual modules from it as needed

from curdle import routes

