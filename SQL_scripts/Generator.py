import re
import random

accounts = [
    ("Ebony Rush", "Camilla Lawson", "2023-04-19", "est.arcu.ac@yahoo.org", "2023-02-13"),
    ("Leslie Rivas", "Risa House", "2022-06-07", "dolor@yahoo.ca", "2021-08-18"),
    ("Jonas Henry", "Lev Holloway", "2022-07-26", "primis.in@hotmail.org", "2022-09-14"),
    ("Gretchen Rivera", "Samantha Turner", "2021-11-27", "suspendisse@hotmail.ca", "2022-04-27"),
    ("Raymond Sampson", "Mollie Douglas", "2021-12-07", "aliquet.sem@aol.edu", "2021-11-16"),
    ("Griffith Bowen", "Marshall Boyer", "2021-10-31", "orci@outlook.edu", "2022-01-09"),
    ("Donna Wood", "Jakeem Stein", "2022-06-12", "eget.nisi@aol.net", "2021-09-04"),
    ("Gretchen Coleman", "Libby Byrd", "2021-10-28", "fermentum.convallis@outlook.net", "2022-03-02"),
    ("Caryn Burns", "Nadine Harris", "2022-05-05", "quisque.nonummy@aol.com", "2022-01-28"),
    ("Avye Suarez", "Eagan Pearson", "2022-10-29", "in.ornare.sagittis@yahoo.edu", "2021-08-19"),
    ("Chaim Miles", "Gail Hull", "2022-06-01", "nulla.semper@icloud.net", "2022-04-23"),
    ("Phoebe Fry", "Kennan Burke", "2022-06-19", "nullam.ut.nisi@hotmail.couk", "2021-07-06"),
    ("Pandora Castaneda", "Maris Joyce", "2021-12-15", "pharetra.nibh.aliquam@icloud.couk", "2021-09-11"),
    ("Halla Madden", "Preston Reeves", "2022-09-23", "convallis.convallis@outlook.edu", "2021-11-30"),
    ("Eve Barrett", "Kelly Osborne", "2022-02-11", "mollis.integer.tincidunt@hotmail.ca", "2022-09-18"),
    ("Rogan Fitzgerald", "Signe Roberts", "2021-08-06", "ridiculus.mus.donec@icloud.org", "2021-11-02"),
    ("Amanda Miles", "Karina Koch", "2023-05-17", "justo.praesent@outlook.edu", "2021-11-26"),
    ("Lucius Vaughn", "Mariam Bowman", "2022-07-19", "et.rutrum@google.couk", "2022-04-21"),
    ("Jasmine Boyd", "Tad Bradley", "2022-11-22", "mi@outlook.couk", "2022-10-19"),
    ("Kerry Hayden", "Roanna Curry", "2021-06-21", "ullamcorper@hotmail.couk", "2023-04-10"),
    ("Donovan Mccray", "Chanda Cummings", "2022-10-05", "arcu.vestibulum@protonmail.org", "2021-09-17"),
    ("Melvin Chaney", "Anjolie Hendrix", "2022-04-03", "auctor.quis.tristique@outlook.com", "2022-09-15"),
    ("Dean Mccall", "Nichole Oneal", "2022-11-16", "sed@hotmail.net", "2022-01-19"),
    ("Kimberly Gentry", "Ezra Holmes", "2022-04-29", "sit.amet@yahoo.org", "2021-09-25"),
    ("Paloma Mendez", "Elizabeth Avila", "2023-05-12", "est.mauris@hotmail.edu", "2021-10-20"),
    ("Chaim Solis", "Plato Rhodes", "2023-01-08", "ac@yahoo.edu", "2022-09-26"),
    ("Amir Bonner", "Jeanette Marquez", "2023-05-14", "nisi.nibh.lacinia@yahoo.com", "2022-05-24"),
    ("Alan Brewer", "Serina Colon", "2022-01-05", "feugiat.tellus.lorem@hotmail.org", "2022-04-19"),
    ("Vance Whitley", "Murphy Bonner", "2021-06-30", "praesent.eu@protonmail.couk", "2023-01-01"),
    ("Orlando Pena", "Iola Gibbs", "2022-05-31", "ac.urna.ut@google.couk", "2023-01-26"),
    ("Drake Wall", "Ima Pennington", "2021-10-20", "aliquam.adipiscing@yahoo.org", "2022-10-31"),
    ("Lamar Waller", "Halla Sweet", "2022-08-06", "fringilla.euismod.enim@icloud.org", "2022-02-26"),
    ("Whoopi Vargas", "Burke Tran", "2022-02-07", "a@protonmail.com", "2022-07-28"),
    ("Sebastian Pickett", "Sade Acevedo", "2021-06-03", "cras.lorem@yahoo.com", "2022-05-17"),
    ("Bradley Mcdonald", "Jorden Hooper", "2023-01-26", "tellus.suspendisse@outlook.net", "2021-08-07"),
    ("Lionel Valencia", "Rebecca Garza", "2022-06-27", "phasellus.in@google.edu", "2021-12-23"),
    ("Nathaniel Jensen", "Mechelle Petty", "2022-02-21", "tempus@protonmail.ca", "2022-04-16"),
    ("Brendan Turner", "Willa Martin", "2023-02-02", "dolor.sit@yahoo.couk", "2021-06-09"),
    ("Lee Price", "Lucius Cross", "2023-05-28", "lorem.donec.elementum@protonmail.couk", "2022-01-18"),
    ("Lillith Long", "Wyatt Briggs", "2023-02-05", "tristique@outlook.org", "2023-01-30"),
    ("Gisela Griffith", "Alden Merrill", "2021-08-22", "ipsum.suspendisse.non@icloud.net", "2022-06-22"),
    ("Tanya Lara", "Sasha Sutton", "2021-09-05", "at@outlook.edu", "2022-04-11"),
    ("Elijah Long", "Ishmael Edwards", "2023-02-03", "vestibulum.mauris@google.couk", "2022-03-17"),
    ("Judith Melendez", "Abra Hayes", "2021-12-03", "aliquam.auctor.velit@yahoo.ca", "2022-07-21"),
    ("Anne Aguirre", "Gabriel Fuentes", "2022-04-17", "purus.ac@protonmail.couk", "2021-10-19"),
    ("Magee Martinez", "Quynn Stevens", "2022-08-11", "et.commodo@hotmail.ca", "2022-02-22"),
    ("Jemima Dudley", "Jack Gutierrez", "2021-11-25", "ullamcorper.magna@icloud.ca", "2021-07-30"),
    ("Mohammad Franklin", "Gareth Whitaker", "2022-01-17", "dapibus.id.blandit@google.couk", "2021-08-26"),
    ("Willa Rich", "Tanisha Ortiz", "2021-09-12", "odio.aliquam@google.couk", "2021-09-13"),
    ("Whilemina Atkinson", "Marah Parker", "2022-05-27", "vel.venenatis@aol.org", "2021-06-02"),
    ("Alea Mclaughlin", "Judah Graves", "2021-12-10", "duis.gravida@google.net", "2023-04-13"),
    ("Callie Irwin", "Dolan Oneil", "2022-03-01", "est.vitae.sodales@outlook.net", "2022-03-24"),
    ("Leslie Kirk", "Rhonda Wiggins", "2022-03-29", "tellus@hotmail.org", "2022-08-31"),
    ("Ulric Middleton", "Latifah Trujillo", "2021-12-09", "posuere.at@yahoo.net", "2023-05-13"),
    ("Melyssa Mcfadden", "Gareth Kelly", "2023-05-16", "id.sapien.cras@aol.ca", "2023-03-26"),
    ("Alvin Justice", "Piper Lambert", "2023-02-07", "magna.suspendisse.tristique@hotmail.couk", "2022-07-10"),
    ("Violet Duffy", "Sade Mcfadden", "2023-04-11", "et.lacinia@google.org", "2022-09-10"),
    ("Angela Petty", "Shad Olson", "2022-08-24", "in.mi.pede@icloud.couk", "2022-10-22"),
    ("Dacey Gross", "Amity Stein", "2021-09-17", "est.vitae.sodales@hotmail.ca", "2021-10-14"),
    ("Emily Logan", "Drake Kirk", "2023-02-02", "arcu.vivamus.sit@outlook.com", "2023-01-01"),
    ("Inez Hodge", "Chaney William", "2021-07-01", "lobortis.quam.a@yahoo.com", "2022-05-27"),
    ("Stuart Nixon", "Ima Porter", "2022-06-29", "rutrum.magna@aol.edu", "2023-04-01"),
    ("Ezekiel Coffey", "Velma Woodward", "2022-07-03", "magnis@hotmail.ca", "2021-11-28"),
    ("Bert Small", "Karina Kent", "2021-10-07", "donec.non@icloud.couk", "2023-05-21"),
    ("Brenda Hinton", "Ahmed Bass", "2022-01-18", "sed@icloud.com", "2022-01-02"),
    ("Jaquelyn Mcleod", "Bert Bender", "2021-07-20", "auctor.odio@hotmail.com", "2023-04-27"),
    ("Judah Marshall", "Dale Pollard", "2022-02-04", "egestas@google.edu", "2022-05-06"),
    ("Xantha Snow", "Caleb Henson", "2022-01-26", "in.consequat@outlook.couk", "2022-02-13"),
    ("Hanae Burnett", "Aidan Lindsey", "2022-06-22", "cum.sociis.natoque@protonmail.com", "2023-04-12"),
    ("Ayanna Massey", "Mason Richard", "2022-01-12", "mollis.vitae@google.com", "2022-03-26"),
    ("Kimberly Bernard", "Sharon Jarvis", "2022-09-18", "et.netus.et@outlook.edu", "2021-11-10"),
    ("Emily Hensley", "Courtney Howard", "2021-11-05", "nunc@outlook.org", "2021-09-27"),
    ("Whitney Hoffman", "Jessica Mclaughlin", "2021-07-22", "lobortis.quis@yahoo.net", "2023-03-09"),
    ("Vincent Arnold", "Barbara Alexander", "2023-03-30", "rutrum.fusce@icloud.net", "2021-12-30"),
    ("Aurelia Tanner", "Thane Parsons", "2023-05-09", "enim.suspendisse.aliquet@yahoo.ca", "2022-12-08"),
    ("Shoshana Pena", "Walker Fleming", "2021-12-24", "purus.sapien.gravida@hotmail.edu", "2022-03-27"),
    ("Aretha Noel", "Sean Goodwin", "2023-03-13", "ac.feugiat@hotmail.net", "2022-02-16"),
    ("Teegan Hubbard", "Athena King", "2022-12-07", "et.rutrum@icloud.net", "2021-06-16"),
    ("Caryn Manning", "Kadeem Warren", "2021-12-12", "urna.convallis.erat@yahoo.com", "2021-11-11"),
    ("Jack Hoffman", "Hiroko Barlow", "2022-03-18", "id.ante@icloud.net", "2021-06-19"),
    ("Martena Ruiz", "Shelley Levine", "2022-02-08", "sed@outlook.org", "2021-09-23"),
    ("Naomi Mullen", "Garrett Key", "2021-11-24", "amet.consectetuer@protonmail.edu", "2023-06-01"),
    ("Kadeem Craft", "Isaac Wynn", "2022-07-12", "aliquam@outlook.couk", "2022-03-19"),
    ("Montana Navarro", "Nigel Kent", "2022-01-25", "torquent@hotmail.org", "2023-01-12"),
    ("Ahmed Kline", "Carl Wynn", "2023-05-25", "adipiscing.ligula.aenean@yahoo.edu", "2023-04-16"),
    ("Brittany Boyd", "Iona Leblanc", "2022-05-08", "bibendum.ullamcorper.duis@google.net", "2021-06-14"),
    ("Paula Middleton", "Imani Powell", "2022-04-16", "nam.interdum@hotmail.couk", "2022-02-10"),
    ("Kylynn Morin", "Megan Mcintyre", "2022-12-24", "non@protonmail.net", "2022-09-05"),
    ("Ivan Bell", "Samantha Keith", "2022-11-03", "et.libero@google.ca", "2022-12-15"),
    ("Brian Smith", "Bruce Wong", "2022-10-02", "nisl.nulla.eu@aol.ca", "2022-02-05"),
    ("Ingrid Black", "Patricia Mercer", "2022-09-24", "et.rutrum.eu@icloud.net", "2021-11-05"),
    ("Lewis English", "Todd Hull", "2022-08-20", "ornare.elit.elit@yahoo.couk", "2022-03-08"),
    ("Thane Vargas", "Maite Sloan", "2022-04-11", "sed.sem@outlook.ca", "2021-06-09"),
    ("Jarrod Ramirez", "Elvis Goodman", "2022-09-20", "risus@icloud.edu", "2021-08-09"),
    ("Linus Ayala", "Len Dickson", "2023-05-15", "ligula.elit@aol.couk", "2021-09-04"),
    ("Darrel Nicholson", "Willa Ayala", "2022-07-31", "magna.sed@hotmail.couk", "2022-07-16"),
    ("Adrian Bell", "Aquila Griffin", "2022-05-31", "montes@icloud.ca", "2022-09-06"),
    ("Jemima Castillo", "Ezekiel Witt", "2022-12-11", "dignissim.lacus.aliquam@outlook.org", "2022-05-16"),
    ("Anjolie Avila", "Rachel Holmes", "2023-01-23", "nec.cursus.a@google.edu", "2021-12-02"),
    ("Shannon Davidson", "Whilemina Keith", "2021-08-19", "ut@hotmail.com", "2021-07-29"),
    ("Halla Quinn", "Summer Jacobs", "2023-04-09", "etiam.bibendum@outlook.edu", "2021-09-06"),
    ("Emmanuel Hines", "Shad Farmer", "2022-07-30", "cursus@icloud.couk", "2021-06-25"),
    ("Ishmael Ratliff", "Kalia Branch", "2023-01-05", "sapien.imperdiet.ornare@aol.org", "2021-08-29"),
    ("Ria Brock", "Burton Mooney", "2022-05-12", "sapien@icloud.org", "2022-11-20"),
    ("Diana Singleton", "Dahlia Kennedy", "2021-11-18", "eros.nam@protonmail.ca", "2022-11-02"),
    ("John Kaufman", "Palmer Casey", "2022-02-09", "vestibulum.mauris@aol.com", "2021-12-02"),
    ("Vance Freeman", "Patrick Hutchinson", "2021-06-12", "erat.nonummy@outlook.edu", "2021-06-18"),
    ("Diana Irwin", "Adrienne Rush", "2022-10-01", "aliquam.iaculis@yahoo.org", "2022-08-19"),
    ("Hakeem Mays", "Allen Gilliam", "2022-06-11", "fermentum@icloud.com", "2023-03-02"),
    ("Otto Gross", "Aphrodite Pitts", "2022-08-29", "nulla.eu@hotmail.org", "2021-09-24"),
    ("Naomi Barnes", "Gloria Ball", "2021-12-31", "magna.sed@outlook.couk", "2022-03-22"),
    ("Abdul Graves", "Jarrod Bell", "2021-10-09", "sem.ut.cursus@google.org", "2021-08-31"),
    ("Kerry Logan", "Jasper Mercer", "2022-01-15", "dictum.proin@outlook.ca", "2021-07-27"),
    ("Lana Dillon", "Jescie Simon", "2023-01-24", "auctor@icloud.couk", "2022-05-20"),
    ("Brenda Burks", "Neil Kent", "2022-09-07", "vel@yahoo.net", "2022-03-25"),
    ("Alana Lott", "Shana Johnson", "2022-05-05", "purus@hotmail.net", "2022-07-30"),
    ("Isadora Watson", "Sebastian Sandoval", "2022-06-26", "enim@protonmail.org", "2023-03-23"),
    ("Cara Walls", "Hadassah Cameron", "2021-08-20", "mi.fringilla.mi@protonmail.net", "2022-11-05"),
    ("Kalia Turner", "Omar Fisher", "2021-12-27", "enim.mauris@aol.com", "2021-10-27"),
    ("Ross Richard", "Cole Frank", "2022-02-21", "eu@yahoo.com", "2021-06-06"),
    ("Ulysses Vega", "Yuri Shannon", "2022-08-27", "donec.porttitor.tellus@icloud.couk", "2021-06-30"),
    ("Dacey Rutledge", "Rinah Wiggins", "2023-02-25", "fermentum.metus@outlook.couk", "2021-07-19"),
    ("Hadassah Crosby", "Samuel Dennis", "2021-06-23", "nulla.tempor.augue@google.edu", "2021-10-26"),
    ("Oleg Rivera", "Fallon Smith", "2022-05-13", "non.luctus.sit@protonmail.net", "2022-10-03"),
    ("Reece Compton", "Aspen Bullock", "2023-04-12", "ultricies.dignissim.lacus@aol.org", "2022-05-26"),
    ("Leandra Griffin", "Morgan Mcfarland", "2023-01-09", "at.libero@protonmail.couk", "2022-08-08"),
    ("Riley Craig", "Eagan Nelson", "2021-08-03", "dolor.sit@protonmail.net", "2022-01-05"),
    ("September Schroeder", "Lyle Heath", "2022-06-12", "diam@hotmail.couk", "2022-01-28"),
    ("Kibo Beard", "Thaddeus Shelton", "2023-04-05", "porttitor.tellus.non@protonmail.com", "2023-01-30"),
    ("Virginia Rosario", "Faith Morin", "2023-03-25", "ut@hotmail.edu", "2023-02-07"),
    ("Walker Price", "Aileen Morales", "2023-02-04", "scelerisque@yahoo.couk", "2022-07-20"),
    ("Logan Espinoza", "Charles Daniel", "2021-07-19", "at.risus@protonmail.net", "2021-11-04"),
    ("Isadora Mcneil", "Omar Strong", "2023-03-19", "donec@protonmail.org", "2021-08-23"),
    ("McKenzie Horne", "Michelle Carney", "2023-04-09", "ultrices.mauris@yahoo.org", "2022-07-25"),
    ("Tucker Watts", "Maris Oneil", "2022-12-20", "duis.a.mi@icloud.edu", "2022-11-21"),
    ("Nolan Hooper", "Erich Sweet", "2022-10-16", "egestas.blandit@outlook.org", "2021-06-19"),
    ("Tatiana Brooks", "Prescott Albert", "2022-01-03", "sodales.purus.in@outlook.com", "2021-06-21"),
    ("Savannah Rogers", "Whitney Webster", "2022-01-02", "euismod@outlook.com", "2022-12-23"),
    ("Rhoda Baldwin", "Travis Poole", "2022-03-16", "et@outlook.ca", "2023-02-21"),
    ("Mallory Good", "Chiquita Howell", "2022-02-15", "laoreet.lectus.quis@hotmail.net", "2021-08-08"),
    ("Ralph Lott", "Plato Briggs", "2021-10-05", "egestas.rhoncus@outlook.edu", "2022-11-10"),
    ("Vincent Ortega", "Galena Daugherty", "2022-06-18", "magna.phasellus@icloud.ca", "2023-04-29"),
    ("Arsenio Hunt", "Jonah Horton", "2023-04-14", "aenean@protonmail.org", "2022-01-20"),
    ("Karen Bonner", "Allistair Fletcher", "2021-12-23", "augue.ut@protonmail.net", "2021-11-04"),
    ("Natalie Stout", "Galena Osborne", "2023-01-30", "sit.amet@aol.couk", "2021-07-25"),
    ("Yetta Kaufman", "Samson Sharpe", "2021-09-02", "nulla.eu@outlook.org", "2021-12-04"),
    ("Rebecca Hickman", "Malachi Pace", "2022-12-25", "vel.convallis@icloud.net", "2023-04-15"),
    ("Kasper Durham", "Ashton Hurley", "2021-12-28", "in.at.pede@outlook.net", "2021-12-07"),
    ("Cameran Edwards", "Cara Mcdaniel", "2021-06-28", "amet.lorem@protonmail.couk", "2022-09-10"),
    ("Denton Barnett", "Allistair Foster", "2023-02-22", "eu.tellus@google.ca", "2021-08-23"),
    ("Xanthus Neal", "Sage Emerson", "2021-06-17", "proin.velit@aol.couk", "2022-10-22"),
    ("Kennan Wright", "Azalia Mclean", "2022-08-29", "enim.condimentum.eget@yahoo.ca", "2023-05-06"),
    ("Nash Delacruz", "Nehru Bond", "2023-05-18", "nec.ante@outlook.ca", "2022-09-14"),
    ("Georgia Franklin", "Jaquelyn Malone", "2022-01-09", "turpis.aliquam.adipiscing@protonmail.ca", "2022-06-11"),
    ("Christopher Mccarthy", "Gil Cannon", "2021-08-18", "dictum.eu@icloud.edu", "2023-05-16"),
    ("Ezekiel Taylor", "Madaline Sykes", "2022-06-08", "nunc.id@protonmail.couk", "2021-12-02"),
    ("Amber Lyons", "Lewis Garrett", "2022-03-12", "egestas.aliquam.nec@google.ca", "2021-07-10"),
    ("Stuart Clements", "Inga Miles", "2022-11-28", "venenatis.vel@icloud.edu", "2022-07-29"),
    ("Alea Santiago", "Cora Day", "2021-06-29", "erat.volutpat@protonmail.org", "2022-06-25"),
    ("Yen Gill", "Kelsey Gaines", "2022-12-04", "integer@aol.edu", "2022-06-03"),
    ("Aquila Santana", "Colt Kirkland", "2021-12-04", "turpis.in@google.com", "2023-04-15"),
    ("September Ramirez", "Jade Keller", "2023-03-15", "sem@protonmail.ca", "2022-06-15"),
    ("Amena Sweeney", "Emmanuel Pace", "2021-10-26", "interdum.feugiat.sed@outlook.net", "2022-09-15"),
    ("Mason Maddox", "Karly Walter", "2021-11-13", "rutrum.justo@yahoo.com", "2023-04-28"),
    ("Patricia Vargas", "Catherine Maxwell", "2022-01-17", "pede.sagittis@google.org", "2022-04-18"),
    ("Cecilia Houston", "May George", "2023-01-08", "semper.nam@icloud.ca", "2023-01-26"),
    ("Ian Short", "Carla Goodwin", "2022-01-16", "et@google.couk", "2021-06-05"),
    ("Elliott Tate", "Christopher Snider", "2021-11-24", "ullamcorper@hotmail.net", "2021-07-02"),
    ("Karleigh Burnett", "Madeson Hull", "2021-11-21", "lorem.fringilla.ornare@outlook.com", "2021-11-29"),
    ("Drake Santiago", "Idola Mcintyre", "2023-03-12", "massa@icloud.couk", "2021-08-09"),
    ("Kadeem Suarez", "Shad Henderson", "2023-04-13", "ac.turpis@protonmail.couk", "2022-04-20"),
    ("Thane Marsh", "Scott Cummings", "2021-07-14", "velit.pellentesque.ultricies@protonmail.org", "2023-03-11"),
    ("Ashton Hickman", "Jana Hebert", "2022-03-12", "quis.lectus@hotmail.ca", "2021-09-27"),
    ("Randall Underwood", "Chastity Wilcox", "2021-10-25", "aliquet.sem@outlook.com", "2022-09-28"),
    ("Ryder Adkins", "Alec Frederick", "2021-06-11", "eu@aol.couk", "2022-10-03"),
    ("Glenna Colon", "Oliver Padilla", "2021-11-09", "eleifend.nec.malesuada@icloud.ca", "2022-09-05"),
    ("Sophia Gentry", "Ralph Nieves", "2022-11-22", "nunc.mauris.morbi@aol.net", "2023-02-05"),
    ("Jonah Castaneda", "Maia Abbott", "2022-11-03", "urna@outlook.edu", "2022-12-20"),
    ("Neve Munoz", "Rafael Galloway", "2023-01-26", "justo.proin@hotmail.org", "2022-03-16"),
    ("Melinda Stafford", "Theodore Parker", "2022-05-04", "vehicula.risus.nulla@hotmail.ca", "2021-12-05"),
    ("Prescott Schmidt", "Maxwell Andrews", "2022-05-30", "egestas.rhoncus.proin@protonmail.couk", "2022-08-08"),
    ("Diana Morse", "Ashely West", "2022-06-07", "malesuada.fringilla.est@aol.couk", "2021-11-03"),
    ("Piper Small", "Ray Graves", "2021-08-14", "tempus.mauris.erat@protonmail.org", "2022-07-12"),
    ("Philip Jacobs", "Acton Griffith", "2022-12-08", "leo.elementum.sem@yahoo.ca", "2023-04-19"),
    ("Risa Delacruz", "Britanni Thompson", "2022-04-27", "suspendisse.eleifend@icloud.ca", "2022-11-19"),
    ("Ferris Bates", "Ray Alexander", "2021-09-29", "iaculis.nec@hotmail.ca", "2021-12-10"),
    ("Keith Gentry", "Kai Mcclain", "2022-07-05", "vitae.dolor@hotmail.net", "2022-06-04"),
    ("Jeremy Reid", "Perry Gilliam", "2021-09-21", "metus.vivamus@icloud.org", "2021-06-22"),
    ("Donovan Burt", "Addison Ashley", "2022-10-22", "ac.fermentum.vel@protonmail.couk", "2021-10-15"),
    ("Yuli Richmond", "Phelan Wilkerson", "2023-01-24", "vulputate.eu@yahoo.net", "2022-08-12"),
    ("Jermaine Evans", "Vanna Meadows", "2022-08-01", "nisi@hotmail.ca", "2022-12-03"),
    ("Quemby Hendrix", "Brandon Cannon", "2022-10-26", "vulputate.velit@google.com", "2021-09-21"),
    ("Kyla Gillespie", "Tad Hodges", "2022-11-20", "aliquam.ultrices.iaculis@google.couk", "2022-01-15"),
    ("Cooper Tillman", "Hadassah Morse", "2021-10-04", "consequat.nec.mollis@protonmail.net", "2023-05-07"),
    ("Iola Nolan", "Nerea Medina", "2022-02-07", "morbi.neque@yahoo.edu", "2022-07-05"),
    ("Emi Marshall", "Tobias Miles", "2022-12-08", "odio@icloud.ca", "2021-11-07"),
    ("Drake Alford", "Wang Gould", "2022-10-13", "nulla.ante@aol.ca", "2022-02-21"),
    ("Jermaine Gamble", "Vivian Preston", "2023-05-22", "est.vitae.sodales@hotmail.org", "2021-11-02"),
    ("Sonya Watson", "Doris Ramsey", "2021-08-23", "duis.at@icloud.org", "2023-01-27"),
    ("Hedwig Stephens", "Raphael Sanford", "2022-03-13", "sapien.nunc.pulvinar@yahoo.couk", "2022-04-26")]

new = []
n = 1
for client in accounts:
    id = n
    name, surname = client[1].split(' ')
    birth_year, birth_m, birth_d = client[2].split('-')
    birth_year = random.randint(1984, 2000)
    birth_date = f'{birth_year}-{birth_m}-{birth_d}'
    email = client[3]
    effentive_to = client[4]
    result = f"('{id}','{name}','{surname}', STR_TO_DATE('{birth_date}', '%Y-%m-%d'), '{email}', STR_TO_DATE('{effentive_to}', '%Y-%m-%d')),"
    new.append(result)
    n += 1
#for i in new:
#    print(i)

cards = []
card_holder = []

i = 1
while i < 100:
    n = random.randint(1,200)
    if n not in card_holder:
        i += 1
        line = f"('{random.randint(1111, 9999)}{random.randint(1111, 9999)}{random.randint(1111, 9999)}{random.randint(1111, 9999)}',{random.randint(1,200)}, STR_TO_DATE('{random.randint(2018, 2021)}-{random.randint(1, 12)}-{random.randint(1, 28)}', '%Y-%m-%d'), STR_TO_DATE('{random.randint(2022, 2024)}-{random.randint(2, 12)}-{random.randint(1, 28)}', '%Y-%m-%d')),"
        print(line)
        cards.append(line)



"""

def create_mail(name,surname,birthdate):
    birthdate = birthdate.split('.')
    return f'{name}.{surname}{(int(birthdate[0])*random.randint(1,9)*random.randint(1,9))//random.randint(1,100)}{int(birthdate[1])*random.randint(1,9)}'

def create_password():
    length = random.randint(10, 20)
    varchar = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_!@#$%^&*()_!@#$%^&*()_!@#$%^&*()_!@#$%^&*()')
    flag = 'False'
    while flag != "True":
        password = ''.join([random.choice(varchar) for _ in range(length)])
        if re.findall(r'[A-Za-z0-9@#$%^&+=]', password):
            flag = 'True'
    return password
"""