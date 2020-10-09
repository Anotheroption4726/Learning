USE base_services;

#DROP TABLE IF EXISTS services;

CREATE TABLE services (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    user_id INT (10) UNSIGNED NOT NULL,
    service VARCHAR(80) NOT NULL,
    description TEXT NOT NULL,
    address VARCHAR(80) NOT NULL,
    zip_code VARCHAR(5) NOT NULL,
    city VARCHAR(30) NOT NULL,
    country VARCHAR(10) NOT NULL,
    service_date_hour DATETIME NOT NULL,
    additional_information TEXT,
    PRIMARY KEY (id)
)

ENGINE = INNODB;




ALTER TABLE services
ADD INDEX index_service_zip_date (service, zip_code, service_date_hour);



INSERT INTO services (user_id,service,description,address,zip_code,city,country,service_date_hour,additional_information)
VALUES
(1, "coach à domicile", "cours sportif à domicile ouvert à tous", "4 rue Moinot", "78150", "Triel sur Seine" , "France", "2018-12-05 18:30:00", "N'hésitez pas à me contacter pour plus d'information"),
(2, "cours de cuisine", "cours de cuisine italienne à domicile", "7 rue Paul Doumer", "78150", "Triel sur Seine", "France", "2018-12-20 19:00:00", "Contactez moi avant de vous incrire pour décider de la recette"),
(3, "cours de mixologie", "cours de création de cocktail dans mon bar", "32 quai Auguste Roy", "78510", "Triel sur Seine", "France", "2019-01-03 20:00:00", NULL),
(4, "bricolage", "Je propose divers travaux de bricolage, peinture, plomberie etc...", "3 impasse Gustave Eiffel", "78260", "Achères", "France", "2019-01-02 15:30:00", "Je me déplace dans toutes les villes limitrophes"),
(5, "couture", "Réalisation d'ourlet, reprisage, retouche", "5 place Georges Brassens", "78260", "Achères", "France", "2018-12-15 13:00:00", "Disponible que les week ends"),
(6, "Aide comptable", "Ancien comptable à la retraite je peux vous aider pour vos déclarations d'impots", "5 rue Trousseline", "78150", "Triel sur Seine", "France", "2019-04-10 10:00:00", "Actuellement à la retraire je suis disponible en semaine de 9h à 18h"),
(7, "Covoiturage", "Je propose des covoiturages entre la Normandie et les Yvelines", "4 rue de l'Hautil", "78150", "Triel sur Seine", "France", "2019-02-13 19:00:00", "Je pars le vendredi soir à 19h de Yvelines, avec un départ prévu le dimanche à 15h de Normandie"), 

(9,"pose d'autoradio", "Propose pose d'autoradio sur tout type de véhicule dans les hauts de seine, appareil non fourni","12 rue de la sablière","92600","Asnières-sur-Seine", "France","2018-12-15 19:00:00","horaires flexibles"),
(10, "cour de danse", "Propose cour de salsa pour débutant et intermédiaire","33 rue de la paix","75002","Paris","France","2019-01-20 15:00:00","tout âge accepté"),
(11,"cour de peinture", "Bonjour, je suis disponible pour vous initier à la peinture à l'huile à mon domicile, matériel non fourni","48 rue Gustave Eiffel","92110","Clichy","France","2018-11-12 17:00:00"," Je peux me déplace dans un rayon de 45mn en transport "),
(12, "cour de patisserie", "Bonjour, je vous propose de vous apprendre l'art des entremets , je me déplace avec mon propre matériel ","45 rue de la rocade","92200", "Neuilly-sur-Seine","France","2018-12-05 11:00:00", " contact uniquement par téléphone"),
(13, "dog sitter", "Vous ne pouvez pas partir en vacances car personne ne peut garder votre animal de compagnie ? Pas de panique, je suis disponible","83 rue caumartin", "75008","Paris","France","2019-02-07 10:00:00", "Je ne fais pas dans les animaux exotiques"),
(14, "couture" , "Bonjour , je peux vous apprendre le tricot et la couture ou bien pour les plus flemmards, vous tricoter moi même une magnifique écharpe","57 rue de lourmel", "78000","Versailles","France","2018-12-18 09:00:00", " Profitez des fêtes pour offrir un cadeau unique à vos proches"),
(15, "bricolage", "Propose diverses services de petit bricolage en tout genre , montage de meuble, changement d'ampoule, réparation de cloture ....etc","2 rue de la tranquilité", "94100","Saint-Maur","France","2019-01-16 15:00:00", "disponible le week end"),

(17, "déménagement avec camion", "Je déménage avec un camion.", "99 boulevard de la Liberation", "95290", "L'Isle-Adam", "France", "2018-12-17 18:00:00", "ceci est une information"),
(18, "installation de luminaires", "J'installe des lumières. C'est chez moi par contre.", "22 rue Descartes", "75011", "Paris", "France", "2019-02-04 07:30:00", "ceci est une autre information"),
(19, "montage de meuble", "Monter des meubles c'est ma passion. Mais que les meubles de couleur bleue.", "96 rue Léon Dierx", "91160", "Longjumeau", "France", "2019-01-20 13:00:00", NULL),
(20, "aide au déménagement", "J'aide au déménagement, mais faut bien payer. En paquet de chips si possible.", "5 rue de Geneve", "95220", "Herblay-sur-Seine", "France", "2019-05-01 08:15:00", NULL),
(21, "ménage", "T'as vraiment cru que j'allais nettoyer tes chiottes?", "6 rue Nationale", "75005", "Paris", "France", "2019-03-24 11:30:00", "c'est mort je vais rien faire"),
(22, "peinture d'intérieur", "Je repeins des intérieurs, mais des extérieurs aussi.", "4 avenue de Bouvines", "93270", "Le Kremlin-Bicêtre", "France", "2019-01-01 20:00:00", NULL),
(23, "montage de meuble", "Eh oui, un autre passionné de montage de meubles. Rouges cette fois-ci", "1 rue Michel Ange", "94270", "Antony", "France", "2019-01-12 10:30:00", "j'aime aussi le jaune");







INSERT INTO services (user_id,service,description,address,zip_code,city,country,service_date_hour,additional_information)
VALUES
(25, "bricolage", "besoin de gros biscotos hoho haha", "7 avenue de la porte de Champerret", "75017", "Paris" , "France", "2018-12-15 19:30:00", "Je ramène les bierres");




SELECT service_date_hour, service, zip_code, city, country, user_id
FROM services
WHERE user_id != 5
AND service_date_hour > '2018-12-05'
ORDER BY service_date_hour DESC, city ASC;


SELECT service_id, user_id, registration_date
FROM service_utilisateur
WHERE user_id != 5
ORDER BY registration_date DESC;



#Story 10

SELECT S.service_date_hour, S.service, S.zip_code, S.city, S.country
FROM services AS S
WHERE S.user_id != 5 AND service_date_hour > '2018-12-05'
AND 5 NOT IN 
    (
        SELECT SU.user_id FROM service_utilisateur AS SU WHERE SU.service_id = S.id
    )
ORDER BY S.service_date_hour DESC, S.city ASC;



#Story 11

SELECT S.service, S.description, U1.pseudo, U1.mobile_numb, U2.pseudo
FROM services AS S
INNER JOIN users AS U1
ON S.user_id = U1.id
LEFT JOIN service_utilisateur AS SU
ON S.id = SU.service_id
LEFT JOIN users AS U2
ON SU.user_id = U2.id
WHERE S.id = 3;



#Story 12

ALTER TABLE services
ADD FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE;



DELETE FROM services
WHERE id = 13;


