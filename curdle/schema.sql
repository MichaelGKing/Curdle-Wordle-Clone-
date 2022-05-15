DROP TABLE IF EXISTS cheese;
DROP TABLE IF EXISTS type;
DROP TABLE IF EXISTS animal;
DROP TABLE IF EXISTS country;
DROP TABLE IF EXISTS continent;

CREATE TABLE cheese (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cheese_name TEXT UNIQUE NOT NULL,
    cheese_type_id INTEGER NOT NULL,
    animal_id INTEGER NOT NULL,
    country_id INTEGER NOT NULL,
    mouldy INTEGER NOT NULL,
    image_file_name TEXT NOT NULL,
    CONSTRAINT fk_cheese_type
        FOREIGN KEY (cheese_type_id)
        REFERENCES cheese_type (cheese_type_id)
    CONSTRAINT fk_animal
        FOREIGN KEY (animal_id)
        REFERENCES animal (animal_id)
    CONSTRAINT fk_country
        FOREIGN KEY (country_id)
        REFERENCES country (country_id)
);

CREATE TABLE cheese_type (
    cheese_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cheese_type TEXT UNIQUE NOT NULL
);

CREATE TABLE animal (
    animal_id INTEGER PRIMARY KEY AUTOINCREMENT,
    animal_name TEXT UNIQUE NOT NULL
);

CREATE TABLE country (
    country_id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_name TEXT UNIQUE NOT NULL,
    continent_id INTEGER NOT NULL,
    CONSTRAINT fk_continent
        FOREIGN KEY (continent_id)
        REFERENCES continent (continent_id)
);

CREATE TABLE continent (
    continent_id INTEGER PRIMARY KEY AUTOINCREMENT,
    continent_name TEXT UNIQUE NOT NULL
);

CREATE TABLE admin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    password_hash  TEXT UNIQUE NOT NULL
);

CREATE VIEW view_cheese
AS 
SELECT
	cheese_name,
	cheese_type.type_name,
	animal.animal_name,
	country.country_name,
	continent.continent_name,
	mouldy
FROM
	cheese
INNER JOIN cheese_type ON cheese_type.type_name = cheese.cheese_type_id
INNER JOIN animal ON animal.animal_name = cheese.animal_id
INNER JOIN country ON country.country_name = cheese.country_id
INNER JOIN continent ON continent.continent_name = country.continent_id;

INSERT INTO cheese_type (cheese_type)
VALUES
	("fresh"),
	("soft"),
	("semi-hard"),
    ("hard"),
    ("blue"),
    ("processed");

INSERT INTO animal (animal_name)
VALUES
	("cow"),
	("sheep"),
	("goat"),
    ("moose");

INSERT INTO continent (continent_name)
VALUES
	("Africa"),
	("Asia"),
	("Europe"),
    ("Middle East"),
    ("North and Central America"),
    ("Oceania"),
    ("South America");

/* 
Insert a list of countries that have known cheeses (list sourced from https://en.wikipedia.org/wiki/List_of_cheeses)
This is not a list of every country, just of countries who may be associated with notable cheese types.
*/
INSERT INTO country (country_name, continent_id)
VALUES
	("Benin", 1),
	("Ethiopia", 1),
	("Mauritania", 1),
    ("Armenia", 2),
    ("Azerbaijan", 2),
    ("Bangladesh", 2),
    ("China", 2),
    ("Cyprus", 2),
    ("Georgia", 2),
    ("India", 2),
    ("Indonesia", 2),
    ("Japan", 2),
    ("Korea", 2),
    ("Malaysia", 2),
    ("Mongolia", 2),
    ("Nepal", 2),
    ("Malaysia", 2),
    ("Philippines", 2),
    ("Albania", 3),
    ("Austria", 3),
    ("Belgium", 3),
    ("Bosnia and Herzegovina", 3),
    ("Bulgaria", 3),
    ("Croatia", 3),
    ("Czech Republic", 3),
    ("Denmark", 3),
    ("Estonia", 3),
    ("Finland", 3),
    ("France", 3),
    ("Germany", 3),
    ("Greece", 3),
    ("Hungary", 3),
    ("Iceland", 3),
    ("Ireland", 3),
    ("Italy", 3),
    ("Kosovo", 3),
    ("Latvia", 3),
    ("Lithuania", 3),
    ("Malta", 3),
    ("Moldova", 3),
    ("Montenegro", 3),
    ("Netherlands", 3),
    ("North Macedonia", 3),
    ("Norway", 3),
    ("Poland", 3),
    ("Portugal", 3),
    ("Romania", 3),
    ("Russia", 3),
    ("Serbia", 3),
    ("Slovakia", 3),
    ("Slovenia", 3),
    ("Spain", 3),
    ("Sweden", 3),
    ("Switzerland", 3),
    ("Ukraine", 3),
    ("United Kingdom", 3),
    ("Egypt", 4),
    ("Iran", 4),
    ("Israel", 4),
    ("Levant", 4),
    ("Turkey", 4),
    ("Canada", 5),
    ("Costa Rica", 5),
    ("El Salvador", 5),
    ("Honduras", 5),
    ("Mexico", 5),
    ("Nicaragua", 5),
    ("United States", 5),
    ("Australia", 6),
    ("Argentina", 7),
    ("Bolivia", 7),
    ("Brazil", 7),
    ("Chile", 7),
    ("Colombia", 7),
    ("Venezuela", 7);



