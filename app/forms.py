from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField, SelectField, SubmitField, BooleanField
from wtforms.validators import DataRequired


# The game does not require users to login to save/track their play statistics.
# Regardless, there is a need for a login form for the administration interface
# The administraion interface is used to upload new puzzles to the database

# The AdminLoginForm class inherits all functions from the FlaskForm imported from the WTForms package
# This includes validators for inputs, so validation can be done server side   

class AdminLoginForm(FlaskForm):
    
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

    
class PuzzleUploadForm(FlaskForm):

    name = StringField('Cheese Name', validators=[DataRequired()])
    type = SelectField('Cheese Type', choices=[], validators=[DataRequired()])
    country = SelectField('Country of Origin', choices=[], validators=[DataRequired()])
    animal = SelectField('Animal of Origin', choices=[], validators=[DataRequired()])
    mould = BooleanField('Is mouldy?')
    image = FileField(validators=[FileRequired(), FileAllowed(['png', 'jpg', 'jpeg', 'gif'], 'Only images of .png, .jpg, .jpeg or .gif allowed.')])
    submit = SubmitField('Upload Puzzle to Curdle Database')

    # Setter functions are required so that the type, country and animal form fields can have their options set
    # with data from the corresponding database tables. 
    def set_types(list):
        global type
        type = SelectField('Cheese Type', choices=list, validators=[DataRequired()])

    def set_countries(list):
        global country
        country = SelectField('Country of Origin', choices=list, validators=[DataRequired()])
    
    def set_animals(list):
        global animal
        animal = SelectField('Animal of Origin', choices=list, validators=[DataRequired()])



