CREATE DATABASE base_services CHARACTER SET 'utf8';

USE base_services;



#DROP TABLE IF EXISTS service_utilisateur; #supprime un tableau déjà éxistant

CREATE TABLE service_utilisateur (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	service_id INT UNSIGNED NOT NULL,
	user_id INT UNSIGNED NOT NULL,
	registration_date DATE NOT NULL,

	PRIMARY KEY (id)

)
ENGINE = INNODB;


INSERT INTO service_utilisateur (service_id, user_id, registration_date)
VALUES  (1, 5, "2018-12-05"),
        (2, 13, "2018-12-04"),
        (3, 24, "2018-12-01"),
        (4, 4, "2018-12-03"),

		(10,5,"2018-11-04"),
		(12,12,"2018-10-21"),
		(14,23,"2018-09-28"),

		(9, 20, "2018-11-22"),
		(21, 15, "2018-10-01"),
		(13, 6, "2018-11-24");



INSERT INTO service_utilisateur (service_id, user_id, registration_date)
VALUES  (22, 10, "2018-12-06");



#Story 12

ALTER TABLE service_utilisateur
ADD FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE ON UPDATE CASCADE,
ADD FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE;



#Story 13

DELETE FROM service_utilisateur
WHERE user_id = 5;





#Story 16
