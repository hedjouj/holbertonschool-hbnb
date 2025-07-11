DROP TABLE IF EXISTS place_amenity;
DROP TABLE IF EXISTS review;
DROP TABLE IF EXISTS place;
DROP TABLE IF EXISTS amenity;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id VARCHAR(36) PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    password VARCHAR(128) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE amenity (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE place (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    price FLOAT NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    owner_id VARCHAR(36) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (owner_id) REFERENCES users(id)
);

CREATE TABLE review (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text VARCHAR(255) NOT NULL,
    rating INTEGER NOT NULL,
    user_id VARCHAR(36) NOT NULL,
    place_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (place_id) REFERENCES place(id)
);

CREATE TABLE place_amenity (
    place_id INTEGER NOT NULL,
    amenity_id INTEGER NOT NULL,
    PRIMARY KEY (place_id, amenity_id),
    FOREIGN KEY (place_id) REFERENCES place(id),
    FOREIGN KEY (amenity_id) REFERENCES amenity(id)
);

INSERT INTO users (id, first_name, last_name, email, password, is_admin)
VALUES ('11111111-1111-1111-1111-111111111111', 'Admin', 'User', 'admin@hbnb.com', 'hashed_password_here', TRUE);

INSERT INTO amenity (name) VALUES ('WiFi');
INSERT INTO amenity (name) VALUES ('Pool');
INSERT INTO amenity (name) VALUES ('Parking');
INSERT INTO amenity (name) VALUES ('Air Conditioning');

INSERT INTO place (title, description, price, latitude, longitude, owner_id)
VALUES ('Cozy Apartment', 'A nice place to stay', 120.0, 48.85, 2.35, '11111111-1111-1111-1111-111111111111');

INSERT INTO review (text, rating, user_id, place_id)
VALUES ('Great place!', 5, '11111111-1111-1111-1111-111111111111', 1);

INSERT INTO place_amenity (place_id, amenity_id) VALUES (1, 1);
INSERT INTO place_amenity (place_id, amenity_id) VALUES (1, 2);

