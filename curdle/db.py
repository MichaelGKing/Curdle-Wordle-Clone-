import sqlite3

import click

# current_app points to the Flask application handling a request
from flask import current_app, g
from flask.cli import with_appcontext

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
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # sqlite3.Row returns rows as dicts which can be accessed by column name
        g.db.row_factory = sqlite3.Row

    return g.db

# A function to close the database connection
# The connection to the db should be closed before responding to a request

def close_db(e=None):
    # set current connection to a new local variable
    db = g.pop('db, None')
    # if there is a current database connection, close it
    if db is not None:
        db.close()
 