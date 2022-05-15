import sqlite3

# This is used for hashing the admin password, and potentially image filenames passed to the client side
# Werkzeug is a core dependancy of Flask
from werkzeug.security import generate_password_hash

# Click is a python package for creating CLI interfaces. It is used in this module to create a CLI command for database initialisation
import click

# current_app points to the Flask application handling a request
from flask import g
from flask.cli import with_appcontext
from curdle import app

# The main structure of the below code is taken from the official Flask documentation 
# This explains how to connect to a SQLite database using Flask/Python's native support

# A connection to the database will be created when handling a request
# In the case that the database needs to be accessed more than once during a request, 
# the object 'g' stores the connection for reuse if get_db() is called again

def get_db():
    if 'db' not in g:
        # sqlite3.connect() connects to the file pointed to by the DATABASE config key
        # This key needs to be created after the database is initialised
        g.db = sqlite3.connect(
            app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # sqlite3.Row returns rows as dicts which can be accessed by column name
        g.db.row_factory = sqlite3.Row

    return g.db

# A function to close the database connection
# The connection to the db should be closed after responding to a request
# This needs to be references in the application factory so it gets run after each request
def close_db(e=None):
    # pop() removes an item at the given index from a list and returns the removed example? not sure what the None variable does...
    # This is just how Flask recommend to do it
    db = g.pop('db', None)
    # if there is a current database connection, close it
    if db is not None:
        db.close()
 
 # Initialise the database using the SQL instructions from schema.sql
def init_db():

    # Set current connection to a new local variable - as seen above, get_db() will open a new connection if one not open already
    db = get_db()

    # Open schema.sql, decode it to UTF8 format, and execute the SQL script
    with app.open_resource('schema.sql') as f:
         db.executescript(f.read().decode('utf8'))
    
    # Create hash of the admin password configuration variable
    hash = generate_password_hash(app.config['ADMIN_PASSWORD'])
    # Store hashed password in the database
    db.execute('INSERT INTO admin (password_hash) VALUES(?)', (hash,))
    db.commit()

# The decorators below define a CLI command which will run the function underneath
# The db can be initialised from the CLI using init-db
@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('The database has been initialised.')

# Register above functions with the application instance
def init_app(app):
    # Tell Flask to close the database after returning a response to a request
    app.teardown_appcontext(close_db)
    # Add a new CLI command that can be called with flask command ie. > flask init-db
    app.cli.add_command(init_db_command)

# Take cheese_name from server or client-side source and return dict of values from the cheese table in the database
def get_puzzle(cheese_name):

    # Open new database connection
    db = get_db()

    # Select all values from all columns from cheese table where name equals 'cheese_name'
    # name column in cheese table is unique, so there can only be one row returned - the fetchone() fucntion is called regardless.
    cheese = db.execute(
        'SELECT * FROM cheese where name = ?', (cheese_name,)
    ).fetchone()

    # fetchone() returns None if the query result set is empty 
    if cheese == None:
        print('The result set returned from the query: [ SELECT * FROM cheese where name = cheese_name ] is empty')
    else:
        return cheese

# This is a overly complicated one, due to the decision to normalise the SQLite db...
# 
def set_puzzle(cheese):
    db = get_db()
    db.execute('INSERT INTO cheese (password_hash) VALUES(?)', (hash,))

def set_todays_puzzle():
    return None

# Get hashed admin password from database for authentication
def get_hashed_password():
    db = get_db()
    hash = db.execute(
        'SELECT password_hash FROM admin').fetchone()
        # There should only ever be one admin password, set at DB initialisation
    # Do a check just incase a password is not there..
    if hash == None:
        print('There was no admin password found in the database! Please assign a strong password to ADMIN_PASSWORD in config.py, and reinitialise the database.')
    else:
        return hash['password_hash']


