from datetime import datetime
from app import app

# The date the application is 'launched' is set in the configuration variables
# ie. launch_time = [2022, 5, 21, 0, 0] where [year, month, day, minute, seconds]

def get_daily_puzzle_id():
    
    ld = app.config['LAUNCH_DATE']

    launch_date = datetime(ld[0], ld[1], ld[2], ld[3], ld[4])

    todays_date = datetime.now()

    return (todays_date - launch_date).days

def get_daily_puzzle_info():
    
    ld = app.config['LAUNCH_DATE']

    launch_date = datetime(ld[0], ld[1], ld[2], ld[3], ld[4])

    todays_date = datetime.now()

    puzzle_info = {'puzzle-id': (todays_date - launch_date).days, 'puzzle-date': todays_date}

    return puzzle_info