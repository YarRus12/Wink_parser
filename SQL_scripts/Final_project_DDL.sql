DROP DATABASE IF EXISTS online_cinema;
CREATE DATABASE online_cinema;
USE online_cinema;


DROP TABLE IF EXISTS directors;
CREATE TABLE `directors` (
    `id` BIGINT AUTO_INCREMENT PRIMARY KEY,
    `name` varchar(255) NOT NULL,
    `birth_date` DATE NOT NULL
);

DROP TABLE IF EXISTS films;
CREATE TABLE `films` (
    `id` BIGINT AUTO_INCREMENT PRIMARY KEY,
    `film_name` varchar(255) NOT NULL,
    `release_date` DATE NOT NULL,
    `avr_grade` FLOAT NOT NULL,
    `description` TEXT NOT NULL,
    `duration` VARCHAR(50) NOT NULL,
    `film_age_rating` INT NOT NULL,
    `link` varchar(255) NOT NULL UNIQUE,
    `main_director_id` BIGINT NOT NULL,
    FOREIGN KEY (main_director_id) REFERENCES directors (id) ON UPDATE CASCADE ON DELETE CASCADE);


DROP TABLE IF EXISTS actors;
CREATE TABLE `actors` (
    `id` BIGINT AUTO_INCREMENT PRIMARY KEY,
    `name` varchar(255) NOT NULL,
    `birth_date` DATE NOT NULL
);

DROP TABLE IF EXISTS actors_in_films;
CREATE TABLE `actors_in_films` (
    `film_id` BIGINT   NOT NULL,
    `actor_id` BIGINT  NOT NULL,
    PRIMARY KEY (film_id, actor_id),
    FOREIGN KEY (film_id) REFERENCES films (id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (actor_id) REFERENCES actors (id) ON UPDATE CASCADE ON DELETE CASCADE);


DROP TABLE IF EXISTS genres;  
CREATE TABLE `genres` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` varchar(70) NOT NULL
);

DROP TABLE IF EXISTS films_genres;  
CREATE TABLE `films_genres` (
    `film_id` BIGINT NOT NULL,
    `genre_id` INT NOT NULL,
    PRIMARY KEY (film_id, genre_id),
    FOREIGN KEY (`film_id`) REFERENCES `films`(`id`) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (`genre_id`) REFERENCES `genres`(`id`) ON UPDATE CASCADE ON DELETE CASCADE
);

DROP TABLE IF EXISTS subscription; 
CREATE TABLE `subscription` (
    `id` INT PRIMARY KEY,
    `name` VARCHAR (20),
    `description` TEXT NOT NULL);


DROP TABLE IF EXISTS films_id_subscription;
CREATE TABLE `films_id_subscription` (
    `subscription_id` INT NOT NULL,
    `film_id` BIGINT NOT NULL,
    PRIMARY KEY (subscription_id, film_id),
    FOREIGN KEY (`subscription_id`) REFERENCES `subscription`(`id`) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (`film_id`) REFERENCES `films`(`id`) ON UPDATE CASCADE ON DELETE CASCADE
);


DROP TABLE IF EXISTS clients;
CREATE TABLE `clients` (
    `id` BIGINT AUTO_INCREMENT PRIMARY KEY,
    `name` varchar(50) NOT NULL,
    `surname` varchar(50) NOT NULL,
    `email` varchar(50) NOT NULL,
    `birthdate` DATE NOT NULL,
    `subscription_id` INT NOT NULL DEFAULT '1',
    `subscription_effective_to` DATE NOT NULL,
    FOREIGN KEY (`subscription_id`) REFERENCES `subscription`(`id`) ON UPDATE CASCADE ON DELETE CASCADE);


DROP TABLE IF EXISTS cards;
CREATE TABLE `cards` (
    `number` BIGINT NOT NULL PRIMARY KEY,
    `owner` BIGINT NOT NULL,
    `effective_from` DATE NOT NULL,
    `effective_to` DATE NOT NULL,
    FOREIGN KEY (`owner`) REFERENCES `clients`(`id`) ON UPDATE CASCADE ON DELETE CASCADE
);