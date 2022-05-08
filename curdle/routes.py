# From the package curdle (that routes is part of), import app 
# app is the new flask instance created by __init__

from curdle import app

# routes or views are written as shown below
# the decorators at the beginning (starting with @app) define what URL's the code below them is run on

@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World!'