<!-- This document needs to be formatted using Markdown as stated in the last slide
	 of the Agile Development lecture slides. -->

Curdle - A daily cheese identification puzzle
=============================================

Curdle is an image identification game that presents players with an image of a unidentified type of cheese and asks them to guess the type of cheese. Players recieve a new image to attempt to identify daily and have a fixed number of attempts available. After each guess players are provided a series of clues confirming characteristics that link their incorrect guess to the solution.

Curdle is a full-stack web application built using Flask, AJAX, and jQuery. The game was created by the authors as for the Web Project assignment while taking CITS3403 in semester one 2022 at The University of Western Australia.

Table of Contents
-----------------

Design and Development
----------------------

How to Install and Run Curdle (from local host)
-----------------------------------------------

### How to set up required environment (In bash terminal)

1. Ensure that python3 and pip are both installed and set up on your host machine

2. After cloning the repositor to your host machine, in a new bash terminal session, navigate to the repository root folder

3. Create new virtual python environment within the current directory and activate the environment

   ```% python3 -m venv ./venv```

   ```% source venv/bin/activate```

   You can exit the virtual environment at any time with the following command:

   ```% deactivate```

4. Install Flask to new virtual environment

   ```(venv) % pip install Flask```

5. Install all required python packages 

   ```% pip install -r requirements.txt```

6. Create a file named '.flaskenv' and add any required tenvironment variables. 
   To tell Flask which file needs to be run to start the application. This is necessary, and having it set in a .flaskenv file avoids the need to set it manually for every new session:

   ```FLASK_APP=setup.py```

   To run Flask in development mode. This enables some debugging tools and automatically reloads browser when changes are made to code
   
   (Do not set this variable for production environments)

   FLASK_ENV=development

### How to Start the Flask Application

How to Play
-----------

How to Add New Puzzles to the Game
----------------------------------

Credits
-------

References
-------------------

