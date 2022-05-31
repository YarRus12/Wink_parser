USE online_cinema;

INSERT INTO `directors` (`name`, `birth_date`)
VALUES
  ('Брайан Де Пальма>', STR_TO_DATE('1940-09-11', '%Y-%m-%d')),
  ('Фрэнсис Форд Коппола', STR_TO_DATE('1937-04-7', '%Y-%m-%d')),
  ('Андрей Тарковский', STR_TO_DATE('1932-04-4', '%Y-%m-%d')),
  ('Стэнли Кубрик', STR_TO_DATE('1928-07-26', '%Y-%m-%d')),
  ('Мартин Скорсезе', STR_TO_DATE('1942-11-17', '%Y-%m-%d')),
  ('Квентин Тарантино', STR_TO_DATE('1963-03-27', '%Y-%m-%d')),
  ('Гай Ричи', STR_TO_DATE('1968-09-10', '%Y-%m-%d')),
  ('Ридли Скотт', STR_TO_DATE('1937-11-30', '%Y-%m-%d'));

INSERT INTO `films` (`film_name`,`release_date`,`avr_grade`, `description`,
           `duration`, `film_age_rating`, `link`, `main_director_id`)
VALUES
('Миссия невыполнима', STR_TO_DATE('1996-05-21', '%Y-%m-%d'),'8.1', 
'Обвиненный в предательстве агент ЦРУ разоблачает заговор.',
'110', '12', 'https://www.kinopoisk.ru/film/3961', '1'),
('Лицо со шрамом', STR_TO_DATE('1983-12-09', '%Y-%m-%d'),'8.3',
'Кубинский иммигрант становится главой наркомафии в Майами 1980-х. Жесткая драма с выдающейся ролью Аль Пачино',
'170', '18', 'https://www.kinopoisk.ru/film/4695', '1'),
('Кэрри', STR_TO_DATE('1976-11-03', '%Y-%m-%d'),'7.2',
'Робкую и доверчивую Кэрри третируют и обижают в школе и дома. От природы добрая девушка становится замкнутой и мрачной. В то же время она открывает в себе странные и страшные силы. А сверстники готовят очередную изощренную шутку над Кэрри, даже не подозревая, чем это для них закончится.',
'98', '16', 'https://www.kinopoisk.ru/film/7459', '1'),
('Неприкасаемые', STR_TO_DATE('1987-06-02', '%Y-%m-%d'),'7.8',
'Спецагенты противостоят подпольной империи Аль Капоне. Роберт Де Ниро в драме об Америке времен сухого закона.',
'110', '16', 'https://www.kinopoisk.ru/film/533', '1'),
('Путь Карлито', STR_TO_DATE('1993-11-07', '%Y-%m-%d'),'8.0',
'Крупный наркоделец Карлито Бриганте вышел из тюрьмы, где отбыл пять лет. Теперь, возвращаясь в испанский квартал Нью-Йорка к любимой женщине, он хочет все бросить и начать честную жизнь. ',
'144', '16', 'https://www.kinopoisk.ru/film/4275', '1'),
('Роковая женщина', STR_TO_DATE('2002-05=8-2=01', '%Y-%m-%d'),'6.7',
'Лора Эш, участвуя в похищении драгоценностей, обманывает сообщников и бежит в Париж. Там она сталкивается с похожей на неё девушкой, которая совершает самоубийство. Лора решает воспользоваться ситуацией и выдать погибшую за себя, а себя — за неё.',
'114', '16', 'https://www.kinopoisk.ru/film/667', '1'),
('Воскрешение Каина', STR_TO_DATE('1992-08-07', '%Y-%m-%d'),'6.1',
'Дженни Никс, жена выдающегося детского психолога Картера Никса, обеспокоена навязчивой одержимостью мужа воспитанием их дочери.',
'110', '16', 'https://www.kinopoisk.ru/film/15535', '1'),
('Миссия на Марс', STR_TO_DATE('2000-03-06', '%Y-%m-%d'),'6.7',
'Когда первая пилотируемая экспедиция на Марс терпит загадочную катастрофу, спасательная экспедиция отправляется на расследование трагедии и спасение оставшихся в живых.',
'114', '12', 'https://www.kinopoisk.ru/film/7353', '1'),
('Крестный отец', STR_TO_DATE('1972-03-14', '%Y-%m-%d'),'8.7',
'Криминальная сага, повествующая о нью-йоркской сицилийской мафиозной семье Корлеоне. Фильм охватывает период 1945-1955 годов.',
'175', '16', 'https://www.kinopoisk.ru/film/325', '2'),
('Апокалипсис сегодня', STR_TO_DATE('1979-05-19', '%Y-%m-%d'),'8.1',
'Во время Вьетнамской войны капитан Уиллард отправляется вверх по реке в Камбоджу со спецзаданием: найти и убить сумасшедшего полковника Курца, создавшего в отдалённом районе нечто вроде собственного культа.',
'194', '18', 'https://www.kinopoisk.ru/film/354', '2'),
('Сонная Лощина', STR_TO_DATE('1999-11-17', '%Y-%m-%d'),'7.9',
'Нью-Йорк, 1799 год. Икабода Крэйна, молодого констебля, отправляют в местечко Сонная лощина для расследования загадочных убийств. Все жертвы, как сообщает местное население, погибают от меча всадника без головы.',
'105', '16', 'https://www.kinopoisk.ru/film/5622', '2'),
('Солярис', STR_TO_DATE('1972-02-05', '%Y-%m-%d'),'8.0',
'На космической станции Крис встречает призрак умершей жены. Шедевр Тарковского об искушении и о сути любви.',
'169', '12', 'https://www.kinopoisk.ru/film/43911', '3'),
('Андрей Рублев', STR_TO_DATE('1966-12-16', '%Y-%m-%d'),'8.0',
'Русь начала XV века. Страну раздирают княжеские междоусобицы. Набеги татар, голод и мор преследуют народ... В эту трагическую эпоху появляется на Руси великий живописец, жизни и творчеству которого посвящен фильм.',
'175', '12', 'https://www.kinopoisk.ru/film/8385', '3'),
('Сталкер', STR_TO_DATE('1979-01-01', '%Y-%m-%d'),'8.1',
'Мистическое путешествие через Зону к комнате, где исполняются желания. Философский шедевр Андрея Тарковского.',
'163', '12', 'https://www.kinopoisk.ru/film/43970', '3'),
('Сияние', STR_TO_DATE('1980-05-23', '%Y-%m-%d'),'7.8',
'Джек Торренс с женой и сыном приезжает в элегантный отдалённый отель, чтобы работать смотрителем во время мертвого сезона.',
'144', '18', 'https://www.kinopoisk.ru/film/409', '4'),
('Цельнометаллическая оболочка', STR_TO_DATE('1987-06-17', '%Y-%m-%d'),'8.0',
'Американская база подготовки новобранцев корпуса морской пехоты. Жесточайшая, бесчеловечная система призвана превратить домашних мальчишек в натренированных хладнокровных убийц.',
'116', '16', 'https://www.kinopoisk.ru/film/418', '4'),
('2001 год: Космическая одиссея', STR_TO_DATE('1968-04-02', '%Y-%m-%d'),'7.9',
'Экипаж космического корабля «Дискавери» — капитаны Дэйв Боумэн, Фрэнк Пул и их бортовой компьютер HAL 9000 — должны исследовать район галактики и понять, почему инопланетяне следят за Землей.',
'149', '12', 'https://www.kinopoisk.ru/film/380', '4'),
('С широко закрытыми глазами', STR_TO_DATE('1999-07-13', '%Y-%m-%d'),'7.5',
'Билл и Элис Харфорд — супружеская пара, производящая впечатление счастливых людей, живущих размеренной жизнью в полном достатке. Но за фасадом идеальных отношений скрываются потоки ревности, неудовлетворенности, тайных желаний и жажды чего-то запредельного.',
'159', '16', 'https://www.kinopoisk.ru/film/3608', '4'),
('Волк с Уолл-стрит', STR_TO_DATE('2013-12-09', '%Y-%m-%d'),'7.9',
'1987 год. Джордан Белфорт становится брокером в успешном инвестиционном банке. Вскоре банк закрывается после внезапного обвала индекса Доу-Джонса.',
'180', '18', 'https://www.kinopoisk.ru/film/462682', '5'),
('Остров проклятых', STR_TO_DATE('2010-02-10', '%Y-%m-%d'),'7.9',
'Два американских судебных пристава отправляются на один из островов в штате Массачусетс, чтобы расследовать исчезновение пациентки клиники для умалишенных преступников.',
'138', '18', 'https://www.kinopoisk.ru/film/397667', '5'),
('Отступники', STR_TO_DATE('2006-09-26', '%Y-%m-%d'),'8.5',
'Два лучших выпускника полицейской академии оказались по разные стороны баррикады: один из них – агент мафии в рядах правоохранительных органов, другой – «крот», внедрённый в мафию.',
'151', '16', 'https://www.kinopoisk.ru/film/81314', '5'),
('Славные парни', STR_TO_DATE('1990-09-09', '%Y-%m-%d'),'8.1',
'История о Генри Хилле — начинающем гангстере, занимающемся грабежами вместе с подельниками Джими Конвеем и Томми Де Вито, которые с легкостью убивают любого, кто встаёт у них на пути.',
'140', '18', 'https://www.kinopoisk.ru/film/350', '5'),
('Криминальное чтиво', STR_TO_DATE('1994-05-21', '%Y-%m-%d'),'8.6',
'Двое бандитов Винсент Вега и Джулс Винфилд ведут философские беседы в перерывах между разборками и решением проблем с должниками криминального босса Марселласа Уоллеса.',
'154', '18', 'https://www.kinopoisk.ru/film/342', '6'),
('Однажды в… Голливуде', STR_TO_DATE('2019-05-19', '%Y-%m-%d'),'7.6',
'Можно ли переписать историю? Самый ностальгический фильм Тарантино — с Шэрон Тейт, Брюсом Ли и Чарли Мэнсоном.',
'161', '18', 'https://www.kinopoisk.ru/film/1047883', '6'),
('Джанго освобожденный', STR_TO_DATE('2012-12-11', '%Y-%m-%d'),'8.2',
'Метко шутя и стреляя, охотники за головами уничтожают негодяев. Квентин Тарантино пробует силы в вестерне.',
'165', '18', 'https://www.kinopoisk.ru/film/586397', '6'),
('Омерзительная восьмерка', STR_TO_DATE('2015-12-07', '%Y-%m-%d'),'7.9',
'США после Гражданской войны. Легендарный охотник за головами Джон Рут по кличке Вешатель конвоирует заключенную.',
'187', '18', 'https://www.kinopoisk.ru/film/819101', '6'),
('Джентльмены', STR_TO_DATE('2019-12-03', '%Y-%m-%d'),'8.5',
'Один ушлый американец ещё со студенческих лет приторговывал наркотиками, а теперь придумал схему нелегального обогащения с использованием поместий обедневшей английской аристократии и очень неплохо на этом разбогател.',
'113', '18', 'https://www.kinopoisk.ru/film/1143242', '7'),
('Гнев человеческий', STR_TO_DATE('2021-04-22', '%Y-%m-%d'),'7.6',
'Грузовики лос-анджелесской инкассаторской компании Fortico Security часто подвергаются нападениям, и во время очередного ограбления погибают оба охранника.',
'119', '18', 'https://www.kinopoisk.ru/film/1318972', '7'),
('Карты, деньги, два ствола', STR_TO_DATE('1998-08-23', '%Y-%m-%d'),'8.6',
'Четверо молодых парней накопили каждый по 25 тысяч фунтов, чтобы один из них мог сыграть в карты с опытным шулером и матерым преступником, известным по кличке Гарри-Топор.',
'107', '18', 'https://www.kinopoisk.ru/film/522', '7'),
('Большой куш', STR_TO_DATE('2000-08-23', '%Y-%m-%d'),'8.5',
'Фрэнки Четыре Пальца должен был переправить краденый алмаз из Англии в США своему боссу Эви, но, сделав ставку на подпольный боксерский поединок, он попал в круговорот весьма нежелательных событий.',
'104', '18', 'https://www.kinopoisk.ru/film/526', '7'),
('Последняя дуэль', STR_TO_DATE('2021-09-10', '%Y-%m-%d'),'7.4',
'Франция, конец XIV века. Отношения между рыцарем Жаном де Карружем и его соратником и соседом Жаком Ле Гри постепенно портятся, и дело доходит до неразрешимого конфликта.',
'152', '18', 'https://www.kinopoisk.ru/film/1289738', '8'),
('Гладиатор', STR_TO_DATE('2000-05-01', '%Y-%m-%d'),'8.6',
'Отважный генерал, ставший рабом, мстит империи. Культовая историческая драма Ридли Скотта с пятью «Оскарами»',
'155', '16', 'https://www.kinopoisk.ru/film/474', '8'),
('Чужой', STR_TO_DATE('1979-05-25', '%Y-%m-%d'),'8.1',
'Группа космонавтов высаживается на неизвестной планете и знакомится с ксеноморфом.',
'116', '16', 'https://www.kinopoisk.ru/film/386', '8'),
('Прометей', STR_TO_DATE('2012-04-11', '%Y-%m-%d'),'7.0',
'Ученые ищут колыбель человечества, а находят древнее зло. Возвращение Ридли Скотта во франшизу о Чужих.',
'124', '16', 'https://www.kinopoisk.ru/film/467099', '8'),



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
