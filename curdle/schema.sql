DROP TABLE IF EXISTS cheese;
DROP TABLE IF EXISTS type;
DROP TABLE IF EXISTS animal;
DROP TABLE IF EXISTS country;
DROP TABLE IF EXISTS continent;

CREATE TABLE cheese (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cheese_name TEXT UNIQUE NOT NULL,
    type_id INTEGER NOT NULL,
    animal_id INTEGER NOT NULL,
    country_id INTEGER NOT NULL,
    mouldy INTEGER NOT NULL,
    image_file_name TEXT NOT NULL
    FOREIGN KEY (type_id)
        REFERENCES type (type_id)
    FOREIGN KEY (animal_id)
        REFERENCES animal (animal_id)
    FOREIGN KEY (country_id)
        REFERENCES country (id)
);

CREATE TABLE type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT UNIQUE NOT NULL
);

CREATE TABLE animal (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    animal_name TEXT UNIQUE NOT NULL
);

CREATE TABLE country (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_name TEXT UNIQUE NOT NULL,
    continent_id INTEGER NOT NULL
    FOREIGN KEY (continent_id)
        REFERENCES continent (id)
);

CREATE TABLE continent (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    continent_name TEXT UNIQUE NOT NULL
);
