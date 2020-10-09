USE base_services;

#DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    email VARCHAR(40) UNIQUE NOT NULL,
    password VARCHAR(300) NOT NULL,
    pseudo VARCHAR(25) UNIQUE NOT NULL,
    address VARCHAR(80),
    zip_code VARCHAR(5),
    city VARCHAR(30),
    country VARCHAR(10),
    mobile_numb VARCHAR(20),
    home_numb VARCHAR(20),
    registration_date DATE,
    PRIMARY KEY (id)
)

ENGINE = INNODB




INSERT INTO users (email, password, pseudo, address, zip_code, city, country, mobile_numb, home_numb, registration_date)
VALUES  ("bogossdu78@yahoo.fr", "titato", "BGdu78", "4 rue Moinot", "78150", "Triel sur Seine" , "France", "0645236578", "0139706396", "2017-06-25"),
        ("marcorosso@gmail.com", "abcdefg", "marcoco", "7 rue Paul Doumer", "78150", "Triel sur Seine", "France", "0687345643", "01397634587", "2016-05-31"),
        ("aperolover@hotmail.com", "apero","loveapero", "32 quai Auguste Roy", "78510", "Triel sur Seine", "France", "0621345467", "0139708765", "2018-08-03"),
        ("thierry.poupon@edu.itescia.fr", "vivelarmee", "Thierrylemeilleur", "3 impasse Gustave Eiffel", "78260", "Achères", "France", "0634768723", NULL, "2017-01-13"),
        ("romain.romieu@gmail.com", "dresscode", "romain", "5 place Georges Brassens", "78260", "Achères", "France", "0798456723", "0109452376", "2018-04-23"),
        ("jean.rene@yahoo.fr", "jean78", "Jeanrene", "5 rue Trousseline", "78150", "Triel sur Seine", "France", "0626739854", "0139745678", "2017-03-28"),
        ("michel.chevalier@orange.fr", "hautemarne", "Michel78", "4 rue de l'Hautil", "78150", "Triel sur Seine", "France", "0678542356", "0134897654", "2016-12-13"),
        ("sophie.leroy@gmail.com", "alleluia", "Soso", "13 rue des Feuches", "78570", "Chanteloup les Vignes", "France", "0676876567", "0139749865", "2017-05-22"),
        
        ("jean.jacques45@gmail.com","roudoudou12","daron_du_92","12 rue de la sablière","92600","Asnières-sur-Seine","France","0645249856","0145789058","2016-06-01"),
        ("macumba12@hotmail.com","17aout1983","macumba","33 rue de la paix","75002","Paris","France","0654981176","0145824122","2018-05-12"),
        ("chihiro55@yahoo.fr","Bibiphoque","josette53","48 rue Gustave Eiffel","92110","Clichy","France","0712846057","0189326049","2017-02-15"),
        ("amandine.dupuis@gmail.com","Rorosino!","mandinette","45 rue de la rocade","92200","Neuilly-sur-Seine","France","0616340695","0190382754","2016-01-13"),
        ("bidule_machin@gmail.com","123soleil","ChatPotté","83 rue caumartin","75008","Paris","France","0735274869","0136787433","2018-09-27"),
        ("marie.paul@hotmail.com","MonChat27","paulette46","57 rue de lourmel","78000","Versailles","France","0747329568", NULL,"2016-07-12"),
        ("rimou.gloup@gmail.com","Babinno!","rimouDuGenou","2 rue de la tranquilité","94100","Saint-Maur","France","0619370625","0145382794","2016-03-29"),
        ("paulette.martin@gmail.com","PauletteMartin3","paulette","62 rue de la verdure","75017","Paris","France","0627349692","0400384154","2018-10-05"),
        
        ("AlitaLessard@teleworm.fr", "ma8AhxuoShai", "Sandy76", "99 boulevard de la Liberation", "95290", "L'Isle-Adam", "France", "0648401393", "0159323611", "2014-12-08"),
        ("DaisiTardif@teleworm.fr", "Chat1ohng", "Againe1967", "22 rue Descartes", "75011", "Paris", "France", "0708182002", "0130214376", "2016-02-15"),
        ("DMoniqueVilleneuve@dayrep.com", "EigohGh1i", "Feamend", "96 rue Léon Dierx", "91160", "Longjumeau", "France", "0763877724", "0128458810", "2011-08-02"),
        ("OliverLajeunesse@armyspy.com", "Pheer9sh", "Taging", "5 rue de Geneve", "95220", "Herblay-sur-Seine", "France", "0639603099", "0145325500", "2013-03-10"),
        ("GillesArcouet@teleworm.us", "Kon5Vushoht", "Spreduche1952", "6 rue Nationale", "75005", "Paris", "France", "0722580782", "0182060886", "2015-11-11"),
        ("EglantineCinqMars@dayrep.com", "PeeCei2Ei", "Ansould", "4 avenue de Bouvines", "93270", "Sevran", "France", "0612986665", "0153278569", "2014-10-28"),
        ("IvenTherriault@armyspy.com", "iecoZuChi1oh", "Aunte1996", "1 rue Michel Ange", "94270", "Le Kremlin-Bicêtre", "France", "0733652344", "0161877008", "2014-10-28"),
        ("DeniseCliche@jourrapide.com", "aeghao1Oo", "Hatherst1I0", "92 Avenue De Marlioz", "92160", "Antony", "France", "0733652344", "0102388688", "2012-07-20");



INSERT INTO users (email, password, pseudo, address, zip_code, city, country, mobile_numb, home_numb, registration_date)
VALUES  ("PierrePaulJacques@gmail.com","123456","Popol",NULL,NULL,NULL,NULL,NULL,NULL,"2018-12-04");


UPDATE users
SET address = "7 avenue de la porte de Champerret", zip_code = "75017", city = "Paris", country = "France", mobile_numb = "0634652334", home_numb = "0139756789"
WHERE id = 25;



#Story 14

DELETE FROM users
WHERE id = 20;
