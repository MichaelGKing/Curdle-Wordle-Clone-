from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import DataRequired

# The game does not require users to login to save/track their play statistics.
# Regardless, there is a need for a login form for the administration interface
# The administraion interface is used to upload new puzzles to the database

# The class below inherits all functions from the FlaskForm imported from the WTForms package
# This includes validators for inputs, so validation can be done server side

class AdminLoginForm(FlaskForm):
    
    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Sign In')

