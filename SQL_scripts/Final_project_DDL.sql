DROP DATABASE IF EXISTS online_cinema;
CREATE DATABASE online_cinema;
USE online_cinema;

CREATE TABLE `films` (
    `id` INT NOT NULL,
    `film_name` varchar(255) NOT NULL,
    `release_date` DATE(255) NOT NULL,
    `avr_grade` FLOAT NOT NULL,
    `description` TEXT NOT NULL,
    `duration` TIME NOT NULL,
    `film_age_rating` INT NOT NULL,
    `link` varchar(255) NOT NULL,
    `main_director` INT NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE `actors` (
    `id` SERIAL NOT NULL PRIMARY KEY,
    `name` varchar(255) NOT NULL,
    `birth_date` DATE NOT NULL
    --`films` DATE NOT NULL,
);

CREATE TABLE `actors_in_films` (
    `film_id` INT NOT NULL,
    `actor_id` INT NOT NULL
);

ALTER TABLE `actors_in_films` ADD CONSTRAINT `actors_in_films_fk0`
            FOREIGN KEY (`film_id`) REFERENCES `Films`(`id`)
            ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE `actors_in_films` ADD CONSTRAINT `actors_in_films_fk1`
            FOREIGN KEY (`actor_id`) REFERENCES `actors`(`id`)
            ON UPDATE CASCADE ON DELETE CASCADE;

CREATE TABLE `directors` (
    `id` INT NOT NULL,
    `name` varchar(255) NOT NULL,
    `birth_date` DATE NOT NULL,
    PRIMARY KEY (`id`)
);

ALTER TABLE `Films` ADD CONSTRAINT `Films_fk0`
            FOREIGN KEY (`main_director`) REFERENCES `directors`(`id`)
            ON UPDATE CASCADE ON DELETE CASCADE;

CREATE TABLE `genres` (
    `id` INT NOT NULL,
    `name` varchar(70) NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE `films_genres` (
    `film_id` INT NOT NULL,
    `genre_id` INT(100) NOT NULL
);

ALTER TABLE `films_genres` ADD CONSTRAINT `films_genres_fk0`
        FOREIGN KEY (`film_id`) REFERENCES `Films`(`id`)
        ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE `films_genres` ADD CONSTRAINT `films_genres_fk1`
        FOREIGN KEY (`genre_id`) REFERENCES `genres`(`id`)
        ON UPDATE CASCADE ON DELETE CASCADE;

CREATE TABLE `subscription` (
    `id` INT NOT NULL,
    `description` TEXT NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE `films_id_subscription` (
    `subscription_id` INT NOT NULL,
    `film_id` INT NOT NULL
);

ALTER TABLE `films_id_subscription` ADD CONSTRAINT `films_id_subscription_fk0`
            FOREIGN KEY (`subscription_id`) REFERENCES `subscription`(`id`)
            ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE `films_id_subscription` ADD CONSTRAINT `films_id_subscription_fk1`
            FOREIGN KEY (`film_id`) REFERENCES `Films`(`id`)
            ON UPDATE CASCADE ON DELETE CASCADE;


CREATE TABLE `client` (
    `id` INT NOT NULL,
    `name` varchar(50) NOT NULL,
    `surname` varchar(50) NOT NULL,
    `patronymic` varchar(50) NOT NULL,
    `birthdate` DATE NOT NULL,
    `subscription_id` INT NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE `card` (
    `number` INT NOT NULL,
    `client_id` INT NOT NULL,
    `effective_to` DATE NOT NULL,
    PRIMARY KEY (`number`)
);

ALTER TABLE `client` ADD CONSTRAINT `client_fk0`
            FOREIGN KEY (`subscription`) REFERENCES `subscription`(`id`)
            ON UPDATE CASCADE ON DELETE CASCADE;
ALTER TABLE `card` ADD CONSTRAINT `card_fk0`
            FOREIGN KEY (`owner`) REFERENCES `client`(`id`)
            ON UPDATE CASCADE ON DELETE CASCADE;