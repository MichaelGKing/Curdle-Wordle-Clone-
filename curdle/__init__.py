# The __init__ file tells Flask that a folder should be treated as a package
# 

# When the curdle package is imported by 'setup.py' this file is run automatically because of its file name

# From the python package flask, import the class Flask

from flask import Flask

from config import Config

app = Flask(__name__)

app.config.from_object(Config)

from . import db

db.init_app(app)

# Import our python module 'routes' which contains instructions what to render on what URL for the web site/application
# The name of the folder this file is in is 'curdle' 
# This means curdle is a python package, and we can import individual modules from it as needed
from curdle import routes   


