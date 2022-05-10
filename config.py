# Instead of setting configuration variables within the application it's self, this file is used instead

import os

class Config(object):

    # Flask and some of it's extensions need a secret key set to use as a cryptographic key
    # For example WTForms uses this to protect web forms
    # It is preffered that a secret key has been set in the environment, but if not, use the one hardcoded into this file
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'password'

    # Configuration items can be accessed with a dictionary syntax from app.config
    # ie. app.config['SECRET_KEY']

    ADMIN_PASSWORD = 'password'