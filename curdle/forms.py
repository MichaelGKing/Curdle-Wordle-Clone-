from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField, BooleanField
from wtforms.validators import DataRequired
from curdle import db
from werkzeug.security import check_password_hash

# The game does not require users to login to save/track their play statistics.
# Regardless, there is a need for a login form for the administration interface
# The administraion interface is used to upload new puzzles to the database

# The AdminLoginForm class inherits all functions from the FlaskForm imported from the WTForms package
# This includes validators for inputs, so validation can be done server side   

class AdminLoginForm(FlaskForm):
    
    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Sign In')

    
class PuzzleUploadForm(FlaskForm):

    type_list = ['Soft', 'Hard', 'Brined', 'Processed', 'Fresh/Whey', 'Stretched Curd', 'Washed-rind', 'Blue']
    country_list = ['England', 'USA', 'France', 'Switzerland']
    animal_list = ['Cow', 'Sheep', 'Goat', 'Moose']

    name = StringField('Cheese Name', validators=[DataRequired()])
    type = SelectField('Cheese Type', choices=type_list, validators=[DataRequired()])
    country = SelectField('Country of Origin', choices=country_list, validators=[DataRequired()])
    animal = SelectField('Animal of Origin', choices=animal_list, validators=[DataRequired()])
    mould = BooleanField('Is mouldy?')
 
    submit = SubmitField('Upload Puzzle to Curdle Database')



