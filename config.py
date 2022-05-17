# Instead of setting configuration variables within the application it's self, this file is used instead

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    # Flask and some of it's extensions need a secret key set to use as a cryptographic key
    # For example WTForms uses this to protect web forms
    # It is preffered that a secret key has been set in the environment, but if not, use the one hardcoded into this file
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'password'

    # Configuration items can be accessed with a dictionary syntax from app.config
    # ie. app.config['SECRET_KEY']

    ADMIN_PASSWORD = 'password'

    # This config variable is used to define where new images should be uploaded from the puzzle upload form

    UPLOAD_FOLDER = '/images'

    # This is used to set allowed cheese image upload file types

    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

    # This one is used to specify the maximum file size in bytes that can be uploaded - 524288 bytes is 512 kilobytes (web friendly)

    MAX_CONTENT_PATH = 524288

    # Tells SQLAlchemy where the database should be found
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
        
    # When true, SQLAlchemy sends a signal to the application everytime a change is about to be made to the database
    SQLALCHEMY_TRACK_MODIFICATIONS = False