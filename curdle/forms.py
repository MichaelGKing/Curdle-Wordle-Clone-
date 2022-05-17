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
    
    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Sign In')

    
class PuzzleUploadForm(FlaskForm):

    # initialises an object of this class, takes variables for holding lists of cheese attributes
    def __init__(self, type_list, country_list, animal_list):
        self.type_list = type_list
        self.country_list = country_list
        self.animal_list = animal_list

    def self(self):
        print(self.value)

    name = StringField('Cheese Name', validators=[DataRequired()])
    type = SelectField('Cheese Type', choices=self.type_list, validators=[DataRequired()])
    country = SelectField('Country of Origin', choices=self.country_list, validators=[DataRequired()])
    animal = SelectField('Animal of Origin', choices=self.animal_list, validators=[DataRequired()])
    mould = BooleanField('Is mouldy?')
    image = FileField(validators=[FileRequired(), FileAllowed(['png', 'jpg', 'jpeg', 'gif'], 'Only images of .png, .jpg, .jpeg or .gif allowed.')])
 
    submit = SubmitField('Upload Puzzle to Curdle Database')



