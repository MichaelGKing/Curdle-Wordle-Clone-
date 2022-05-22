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

2. After cloning the repository to your host machine, in a new bash terminal session, navigate to the repository root folder

3. Create new virtual python environment within the current directory and activate the environment

   ```bash
   % python3 -m venv ./venv
   ```

   ```bash
   % source venv/bin/activate
   ```

   You can exit the virtual environment at any time with the following command:

   ```bash
   % deactivate
   ```

4. Install Flask to new virtual environment

   ```bash
   (venv) % pip install Flask
   ```

5. Install all required python packages 

   ```bash
   (venv) % pip install -r requirements.txt
   ```

6. Create a file named '.flaskenv' and add any required environment variables. 

   REQUIRED:
   
   To tell Flask which file needs to be run to start the application. This is necessary, and having it set in a .flaskenv file avoids the need to set it manually for every new session:

   ```FLASK_APP=curdle```

   To tell Flask-SQLAlchemy and Flask-Migrate how to connect to the database:

   ```DATABASE_URL='sqlite:///app.db'```

   OPTIONAL:

   To run Flask in development mode. This enables some debugging tools and automatically reloads browser when changes are made to code
   
   (Do not set this variable for production environments)

   ```FLASK_ENV=development```

   To allow the Flask application to print debugging messages to console, disable stdout buffering

   ```PYTHONUNBUFFERED='any_non_empty_string'```

7. Build the application database. Return to your terminal within the curdle folder with your virtual env active

   ```bash
   (venv) % flask db upgrade
   ```

8. Load the database with hard-coded cheese attribute data, and any puzzles found in puzzles.csv

   ```bash
   (venv) % flask import_data
   ```

### How to Start the Flask Application

How to Play
-----------
Guess the CURDLE in 6 guesses from the image shown.

Type your guess in the box. Each guess must be a valid cheese, see the dropdown menu.

After you submit your guess, your submission will appear surrounded by a border (green if correct, red if incorrect).

Icons will also appear indicating if your guess shares the same region, country, and animal of oirign with the answer. As well as it's mold content, and type. These attributes are explained below.

Icons will appear red if your guess and the answer do not share the attribute. For example if your guess uses cow products, and the answer uses goat products the icon will appear red.

If you succeed or fail to get the cheese it will be revealed in a black box below your guesses. Click the box for information on the cheese! 😀

How to Add New Puzzles to the Game
----------------------------------

Credits
-------

### 3rd party extentions and libraries
Title-font: https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;800&family=Rubik+Microbe&display=swap
Body-font: https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;800&display=swap
Header-icons: https://ionic.io/ionicons
AJAX: https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js
Attribute-icons: https://fontawesome.com/

To avoid the need for 

References
-------------------

### DBDiagram

The SQLite database for the project was designed using DBDiagram, a relational database diagram tool found at https://dbdiagram.io/

The database diagram can be viewed below:

<iframe width="560" height="315" src='https://dbdiagram.io/embed/627fc6307f945876b61ae11e'> </iframe>

### Flask development references

A large proportion of the basic Flask application set up was designed following the offical documentation found at https://flask.palletsprojects.com/

Miguel Grinberg's The Flask Mega-Tutorial also provided a valuable guide for many aspects of the development process not covered in the official flask docuemtation. Miguel's tutorial can be found here: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

