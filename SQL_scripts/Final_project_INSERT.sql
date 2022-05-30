
USE online_cinema;

INSERT INTO `directors` (`name`, `birth_date`)
VALUES
  ('Brian De Palma', STR_TO_DATE('1940-09-11', '%Y-%m-%d'));


   

INSERT INTO `films` (`film_name`,`release_date`,`avr_grade`, `description`,
           `duration`, `film_age_rating`, `link`, `main_director_id`)
VALUES
('Миссия невыполнима', STR_TO_DATE('1996-05-21', '%Y-%m-%d'),'8.1', 
'Обвиненный в предательстве агент ЦРУ разоблачает заговор.',
'110', '12', 
'https://www.kinopoisk.ru/film/3961',
'1');



INSERT INTO `actors` (`name`,`birth_date`)
VALUES
  ('Tom Cruise', STR_TO_DATE('1962-07-03', '%Y-%m-%d')),
  ('Jon Voight', STR_TO_DATE('1938-12-29', '%Y-%m-%d')),
  ('Emmanuelle Béart', STR_TO_DATE('1963-08-14', '%Y-%m-%d'));



   
INSERT INTO `actors_in_films` (`film_id`,`actor_id`)
VALUES
  ('1', '1'),
  ('1', '2'),
  ('1', '3');




INSERT INTO `genres` (`name`)
VALUES
  ("comedy"),
  ("thriller"),
  ("drama"),
  ("sport"),
  ("documentary"),
  ("militants");


INSERT INTO `films_genres` (`film_id`,`genre_id`)
VALUES
  ('1', '2'),
  ('1', '6');


INSERT INTO `subscription` (`id`, `name`,`description`)
VALUES
('1', 'free', 'Подписка включает фильмы, вышедшие не менее 2 лет назад'),
('2', 'light', 'Подписка включает фильмы, вышедшие не менее чем 6 месяцев назад'),
('3', 'medium', 'Подписка включает фильмы, вышедшие не менее чем 1 месяцев назад'),
('4', 'full', 'Подписка включает все фильмы, в том числе новинки');


INSERT INTO `films_id_subscription` (`subscription_id`, `film_id`)
VALUES
  ('1', '1'),
  ('2', '1'),
  ('3', '1'),
  ('4', '1');


   
INSERT INTO clients (`id`, `name`, `surname`, `birthdate`, `email`, `subscription_id`, `subscription_effective_to`)
VALUES
  ('1', 'Meredith','Parks',STR_TO_DATE('1962-07-03', '%Y-%m-%d'),'parks-meredith8064@google.com',2, STR_TO_DATE('2022-07-03', '%Y-%m-%d')),
  ('2', 'Jolie','Middleton',STR_TO_DATE('1963-06-03', '%Y-%m-%d'),'j_middleton9079@google.com',3, STR_TO_DATE('2023-07-03', '%Y-%m-%d')),
  ('3', 'Ginger','Stout',STR_TO_DATE('1966-07-21', '%Y-%m-%d'),'stout_ginger@google.com',1, STR_TO_DATE('9999-12-31', '%Y-%m-%d')),
  ('4', 'Charles','Roberts',STR_TO_DATE('1993-07-23', '%Y-%m-%d'),'c_roberts1636@google.com',1, STR_TO_DATE('9999-12-31', '%Y-%m-%d')),
  ('5','Pearl','Ramsey',STR_TO_DATE('1982-12-08', '%Y-%m-%d'),'ramseypearl2602@google.com',2, STR_TO_DATE('2022-12-31', '%Y-%m-%d')),
  ('6', 'Lana','Lopez',STR_TO_DATE('1952-11-11', '%Y-%m-%d'),'llopez4080@google.com',1, STR_TO_DATE('9999-12-31', '%Y-%m-%d'));
  



INSERT INTO `cards` (`number`,`owner`, `effective_from`, `effective_to`)
VALUES
  ("5136492986789739",1,STR_TO_DATE('2021-07-03', '%Y-%m-%d'),STR_TO_DATE('2024-07-03', '%Y-%m-%d')),
  ("5152346436523438",2,STR_TO_DATE('2020-07-03', '%Y-%m-%d'),STR_TO_DATE('2023-07-03', '%Y-%m-%d')),
  ("5284257139342458",3,STR_TO_DATE('2019-07-03', '%Y-%m-%d'),STR_TO_DATE('2022-07-03', '%Y-%m-%d')),
  ("5515473242252556",4,STR_TO_DATE('2019-04-03', '%Y-%m-%d'),STR_TO_DATE('2022-04-03', '%Y-%m-%d')),
  ("5373594548722140",5,STR_TO_DATE('2021-08-03', '%Y-%m-%d'),STR_TO_DATE('2022-08-03', '%Y-%m-%d')),
  ("5272344287845575",6,STR_TO_DATE('2021-02-03', '%Y-%m-%d'),STR_TO_DATE('2024-02-03', '%Y-%m-%d'));
