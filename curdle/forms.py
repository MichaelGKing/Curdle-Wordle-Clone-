from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField, ValidationError, BooleanField
from wtforms.validators import DataRequired
from curdle import app

# The game does not require users to login to save/track their play statistics.
# Regardless, there is a need for a login form for the administration interface
# The administraion interface is used to upload new puzzles to the database

# The AdminLoginForm class inherits all functions from the FlaskForm imported from the WTForms package
# This includes validators for inputs, so validation can be done server side

# This is a custom validator created following the WTForms official documentation
# It returns an error if the password in entered incorrectly
def validate_successful_auth(form, password):
    if (password.data != app.config['SECRET_KEY']):
        raise ValidationError('The password you entered in incorrect')

class AdminLoginForm(FlaskForm):
    
    password = PasswordField('Password', validators=[DataRequired(), validate_successful_auth])

    submit = SubmitField('Sign In')

    
class PuzzleUploadForm(FlaskForm):

    name = StringField('Cheese Name', validators=[DataRequired()])
    type = SelectField('Cheese Type', choices=['Soft', 'Hard', 'Brined', 'Processed', 'Fresh/Whey', 'Stretched Curd', 'Washed-rind', 'Blue'], validators=[DataRequired()])
    country = SelectField('Country of Origin', choices=['England', 'USA', 'France', 'Switzerland'], validators=[DataRequired()])
    animal = SelectField('Animal of Origin', choices=['Cow', 'Sheep', 'Goat', 'Moose'], validators=[DataRequired()])
    mould = BooleanField('Is mouldy?')
 
    submit = SubmitField('Upload Puzzle to Curdle Database')



