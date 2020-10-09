CREATE DATABASE base_services CHARACTER SET 'utf8';

USE base_services;


#DROP TABLE IF EXISTS messages;

CREATE TABLE messages (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	expeditor_id INT UNSIGNED NOT NULL,
	recipient_id INT UNSIGNED NOT NULL,
	message_content TEXT NOT NULL,
	message_date DATE NOT NULL,

	PRIMARY KEY (id)

)
ENGINE = INNODB;



INSERT INTO messages (expeditor_id, recipient_id, message_content, message_date)
VALUES	
		(5, 1, "Bonjour je serais interessé par une séance de sport, êtes vous disponible samedi?", "2018-12-04"),
        (13, 2, "Bonsoir, Je suis végétarienne, réalisez vous des recettes sans viande?", "2018-12-03"),
        (24, 3, "Bonjour, Acceptez vous les groupes ? Ce serait pour un enterement de vie de jeune fille! Bonne soirée", "2018-12-02"),
        (4, 5, "Bonjour, J'aimerais vraiment apprendre a cours mais je n'ai jamais essayé, prenez vous les grands débutants? Merci Bonne soirée", "2018-12-04"),
        (7, 10, "Olé, j'adore la danse, quand etes vous disponible au plus tot??", "2018-12-01"),
        (16, 18, "Bonjour, j'adore les luminaires, puis je poser les votres?", "2018-12-02"),
        (6, 19, "Bonjour, je sors de chez Ikea et je croule sous les meubles à monter....SOS", "2018-12-02"),
        (20, 7, "Bonsoir, je suis interessé par un covoiturage vendredi prochain mais je ne serais disponible qu'à partir de 20h est ce bon quand même?", "2018-12-02"),
        (24, 9, "Bonjour, Je souhaiterais changer d'auto radio mais je ne sais pas lequel choisir? Pourriez vous m'aider?", "2018-12-01"),
        (14, 6, "Bonjour, Je viens d'hériter et je suis perdu....Etes vous calé en gestion de patrimoine?D'avance merci", "2018-12-02"),

		(5, 11, "Bonjour, pourriez vous me conseiller du matériel pour débutant afin de pouvoir tester la peinture à l'huile sans me ruiner svp?","2018-11-03"),
		(11,5,"Bonjour, vous pouvez commencer par acheter un petit kit de couleur primaire de qualité étude, ainsi que 2 pinceaux en soie de porc plus un petit bloc de papier à grain très épais. N'hésitez pas à me contacter si besoin.","2018-11-04"),
		(2,11, "Bonjour, accepteriez vous de vous déplacer jusqu'a Triel sur seine car j'ai des enfants en bas age et je ne peux pas me deplacer.","2018-12-02"),
		(11,2,"Bonjour, désolé mais je ne me déplace pas aussi loin. Cordialement.","2018-12-02"),
		(23,13,"Bonjour, combien vendriez vous une écharpe svp ?","2018-12-18"),
		(13,23,"Bonjour, tout dépend de la laine , de la taille désirée. Mais je peux vous donner une fourchette de prix entre 20 et 60 euro.","2018-12-19"),
		(1,17,"Bonjour, quelle est la taille de votre camion svp?","2018-12-05"),
		(15,7, " Bonsoir, pourriez vous rapprocher un peu de Paris avant d'aller en Normandie?","2018-11-01"),
		(3,12,"Bonjour, est ce que je pourrai vous commander un gateau d'anniversaire svp ?","2018-12-01"),
		(23,19,"Vous montez que les meubles bleus?","2018-11-25"),

		(2, 11, "Clique sur mon lien pour apprendre à devenir riche sur internet.", "2018-07-04"),
		(22, 5, "Etonnement subitement boulevards electrique le entrainait infanterie je.", "2018-12-10"),
		(4, 19, "Preferait detourner descendit en la expliquer.", "2018-10-15"),
		(11, 2, "Cool merci beaucoup!", "2018-09-20"),
		(20, 21, "Je entraine tenacite te havresac propager heureuse.", "2018-08-05"),
		(5, 22, "Gens quoi son nez dieu dans fait ifs.", "2018-10-28"),
		(3, 2, "Saules les venait eau car crosse que.", "2018-11-22"),
		(9, 20, "J'aime bien la salsa", "2018-08-17"),
		(21, 15, "Mais pourquoi?", "2018-11-10"),
		(13, 6, "Est-ce que le chien sait parler? Il fait la cuisine?", "2018-09-29");



INSERT INTO messages (expeditor_id, recipient_id, message_content, message_date)
VALUES                
        (10, 25, "J'aime pas la bière mais si t'amène le champagne, jsuis ok :))))", "2018-12-06");



#STORY 8 A REFAIRE!!!!!!!

SELECT message_content, message_date
FROM messages
WHERE recipient_id = 2 OR expeditor_id = 2
ORDER BY message_date DESC;

SELECT message_content, expeditor_id, recipient_id
FROM messages
ORDER BY recipient_id ASC;


#Story 9

SELECT message_content, message_date
FROM messages
WHERE (recipient_id = 2 AND expeditor_id = 11) OR (recipient_id = 11 AND expeditor_id = 2)
ORDER BY message_date DESC;


#Story 12

ALTER TABLE messages
ADD FOREIGN KEY (expeditor_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE,
ADD FOREIGN KEY (recipient_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE;


#Story 15

DELETE FROM messages
WHERE id = 20;
