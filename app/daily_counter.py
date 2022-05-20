import datetime
from app import app

launch_time = app.config['LAUNCH_DATE']
print(launch_time)

start_counter = datetime.datetime()