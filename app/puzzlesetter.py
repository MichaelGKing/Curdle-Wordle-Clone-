import random
from datetime import datetime
from app import app, db
from app.models import Cheese, PuzzleHistory

# The date the application is 'launched' is set in the configuration variables
# ie. launch_time = [2022, 5, 21, 0, 0] where [year, month, day, minute, seconds]

# Returns a dictionary containing the todays client puzzle id
def get_puzzle_id_for_client():
    
    ld = app.config['LAUNCH_DATE']

    launch_date = datetime(ld[0], ld[1], ld[2], ld[3], ld[4])

    todays_date = datetime.now()

    return (todays_date - launch_date).days

# Returns a dictionary containing the todays client puzzle id and server date
def get_daily_puzzle_info():
    
    ld = app.config['LAUNCH_DATE']

    launch_date = datetime(ld[0], ld[1], ld[2], ld[3], ld[4])

    todays_date = datetime.now()

    puzzle_info = {'puzzle-id': (todays_date - launch_date).days, 'puzzle-date': todays_date}

    return puzzle_info

# Returns a random puzzle ID from the list of puzzles in the database
def set_puzzle_id_for_server():
        
    result = db.session.query(Cheese.id).all()

    id_range = len(result) + 1

    random_id = random.randrange(1, id_range, 1)

    return random_id

def get_puzzle_id_for_server():

    result = db.session.query(PuzzleHistory.server_puzzle_id).filter(PuzzleHistory.client_puzzle_id == get_puzzle_id_for_client()).scalar()

    return result