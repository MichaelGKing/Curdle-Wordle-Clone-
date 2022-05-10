
from curdle import app
from flask import render_template

# routes or views are written as shown below
# the decorators at the beginning (starting with @app) define what URL's the code below them is run on

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')