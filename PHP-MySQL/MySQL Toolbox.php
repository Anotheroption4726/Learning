_INFORMATIONS________________________________________________________

Champ : permet de définir le nom du champ

Type : le type de données que va stocker le champ (nombre entier, texte, date…)

Taille/Valeurs : indique la taille maximale du champ, utile pour le type VARCHAR

Index : active l'indexation du champ. Le champ sera mieux adapté aux recherches. Le plus souvent, on utilise l'index PRIMARY (clé primaire) sur les champs de type id

AUTO_INCREMENT : permet au champ de s'incrémenter tout seul à chaque nouvelle entrée. Utilisé aussi fréquemment sur les champs de type id.




_TYPES_______________________________________________________________

NUMERIC : nombres. On y trouve des types dédiés aux petits nombres entiers (TINYINT), aux gros nombres entiers (BIGINT), aux nombres décimaux, etc.

DATE and TIME : ce sont les dates et les heures. De nombreux types différents permettent de stocker une date, une heure, ou les deux à la fois

STRING : ce sont les chaînes de caractères. Là encore, il y a des types adaptés à toutes les tailles

SPATIAL : cela concerne les bases de données spatiales, utiles pour ceux qui font de la cartographie

INT : nombre entier

VARCHAR : type adapté aux textes courts, sa seule exigence est qu'il faut obligatoirement indiquer la taille maximale du champ (entre 1 et 255)

TEXT : long texte (on peut y stocker un roman sans problème)

DATE : date (jour, mois, année)




_TEMPS & DATES_______________________________________________________

DATE : stocke une date au format AAAA-MM-JJ (Année-Mois-Jour) ;

TIME : stocke un moment au format HH:MM:SS (Heures:Minutes:Secondes) ;

DATETIME : stocke la combinaison d'une date et d'un moment de la journée au format AAAA-MM-JJ HH:MM:SS. Ce type de champ est donc plus précis ;

TIMESTAMP : stocke le nombre de secondes passées depuis le 1er janvier 1970 à 00 h 00 min 00 s ;

YEAR : stocke une année, soit au format AA, soit au format AAAA.




_CONNECTION__________________________________________________________

<?php
  // Sous WAMP (Windows)
  $bdd = new PDO('mysql:host=localhost;dbname=test;charset=utf8', 'root', '');
  // Sous MAMP (Mac)
  $bdd = new PDO('mysql:host=localhost;dbname=test;charset=utf8', 'root', 'root');
?>

//  le nom d'hôte: localhost
//  la base de données: test
//  le login: root
//  le mot de passe: sous WAMP il n'y a pas de mot de passe par défaut, sous MAMP le mot de passe est "root"


<?php
  try
  {
  	$bdd = new PDO('mysql:host=localhost;dbname=test;charset=utf8', 'root', '');
  }
  catch (Exception $e)
  {
          die('Erreur : ' . $e->getMessage());
  }
?>
//  Tester la présence d'erreurs. Evite que PHP affiche toute la ligne qui pose l'erreur, incluant le mot de passe


<?php
  $bdd = new PDO('mysql:host=localhost;dbname=test;charset=utf8', 'root', '', array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION));
?>
//  Les requêtes SQL qui comportent des erreurs les afficheront avec un message beaucoup plus clair




_REQUÊTES____________________________________________________________

<?php $reponse = $bdd->query('SELECT * FROM nom_de_table'); ?>
//  On demande à effectuer une requête sur la base de données ("Prendre tout ce qu'il y a dans la table nom_de_table"). On
//  récupère ce que la base de données a renvoyé dans un autre objet appelé ici $reponse


<?php $reponse = $bdd->query('SELECT colonne1, colonne2 FROM nom_de_table'); ?>
//  Même chose qu'au dessus sauf que cette fois on prend juste les informations contenues dans colonne1 et colonne2 de nom_de_table


<?php
  $donnees = $reponse->fetch();
  echo $donnees['colonne1'];
?>
//  Affiche l'information de la première ligne de la colonne1


<?php
  while ($donnees = $reponse->fetch())
  {
    echo $donnees['colonne1'].'<br>';
  }
?>
//  Affiche à la suite toutes les informations contenues dans la colonne1


<?php $reponse->closeCursor(); ?>
//  Provoque la « fermeture du curseur d'analyse des résultats ». Cela veut dire qu'on a terminé le travail sur la requête (afin
//  d'éviter d'avoir des problèmes à la requête suivante)




_CRITERES DE SELECTION_______________________________________________

<?php
  $reponse = $bdd->query('SELECT * FROM nom_de_table WHERE colonne2="nom_de_valeur"');
  while ($donnees = $reponse->fetch())
  {
  	echo $donnees['colonne1'].'<br />';
  }
  $reponse->closeCursor();
?>
//  Affiche à la suite toutes les informations contenues dans la colonne1 dont la valeur située à la colonne2 est égale à
//  nom_de_valeur


<?php $reponse = $bdd->query('SELECT * FROM nom_de_table WHERE colonne2="nom_de_valeur" AND colonne3 < 20'); ?>

//  Récupère toutes les informations dont la valeur située à la colonne2 est égale à nom_de_valeur et dont la valeur numérique
//  située à la colonne3 est inférieure à 20


<?php $reponse = $bdd->query('SELECT * FROM nom_de_table ORDER BY colonne3'); ?>
//  Récupère toutes les informations et les ordonne par ordre croissant en se basant sur les valeurs contenues dans la colonne3

<?php $reponse = $bdd->query('SELECT * FROM nom_de_table ORDER BY colonne3 DESC'); ?>
//  Récupère toutes les informations et les ordonne par ordre décroissant en se basant sur les valeurs contenues dans la colonne3


<?php $reponse = $bdd->query('SELECT * FROM nom_de_table LIMIT 0, 20'); ?>
//  Récupère les vingt premières entrées

<?php $reponse = $bdd->query('SELECT * FROM nom_de_table LIMIT 5, 10'); ?>
//  Récupère de la sixième à la quinzième entrée

<?php $reponse = $bdd->query('SELECT * FROM nom_de_table LIMIT 10, 2'); ?>
//  Récupère la onzième et la douzième entrée


<?php
  $reponse = $bdd->query('SELECT colonne1, colonne3 FROM nom_de_table WHERE colonne2="nom_de_valeur" AND colonne3 < 20 ORDER BY colonne3 DESC LIMIT 1, 2');
  while ($donnees = $reponse->fetch())
  {
    echo $donnees['colonne1'].'<br>';
    echo $donnees['colonne3'];
  }
  $reponse->closeCursor();
?>
//  Affiche les informations contenues dans la colonne1 et la colonne3 dont la valeur située à la colonne2 est égale à
//  nom_de_valeur, dont la valeur numérique située à la colonne3 est inférieure à 20 et les ordonne par ordre décroissant en se
//  basant sur les valeurs contenues dans la colonne3
//  Il faut utiliser les mots-clés dans l'ordre : WHERE puis ORDER BY puis LIMIT, sinon MySQL ne comprendra pas la requête




_REQUÊTES PREPAREES__________________________________________________

<?php
  $req = $bdd->prepare('SELECT colonne1 FROM nom_de_table WHERE colonne2 = ?');
  $req->execute(array($_POST['nom_de_valeur']));
?>
//  La requête est exécutée à l'aide du paramètre indiqué sous forme d'array $_POST. Ces paramètres vont remplacer le "?" indiqué
//  dans la colonne2


<?php
  $req = $bdd->prepare('SELECT colonne1 FROM nom_de_table WHERE colonne2 = ? AND colonne3 <= ?');
  $req->execute(array($_GET['nom_de_valeur_1'], $_GET['nom_de_valeur_2']));
?>
//  S'il y a plusieurs marqueurs, il faut indiquer les paramètres dans le bon ordre. Le premier point d'interrogation de la
//  requête est remplacé par le contenu de la variable $_GET['nom_de_valeur_1'], et le second par le contenu de
//  $_GET['nom_de_valeur_2'].


<?php
  $req = $bdd->prepare('SELECT colonne1, colonne2 FROM nom_de_table WHERE colonne2 = :marqueur1 AND colonne3 <= :marqueur2');
  $req->execute(array('marqueur1' => $_POST['nom_de_valeur_1'], 'marqueur2' => $_POST['nom_de_valeur_2']));
?>
//  Les points d'interrogation ont été remplacés par les marqueurs nominatifs :marqueur1 et :marqueur2. Ceux-ci sont ensuite
//  appellés par les variables à l'aide d'un array associatif. Quand il y a beaucoup de paramètres, cela permet parfois d'avoir
//  plus de clarté. De plus, contrairement aux points d'interrogation, il n'est plus necessaire d'envoyer les variables dans le
//  même ordre que la requête




_INSERTION DE DONNEES________________________________________________

<?php
  $req = $bdd->prepare('INSERT INTO nom_de_table(colonne1, colonne2, colonne3) VALUES(:marqueur1, :marqueur2, :marqueur3)');
  $req->execute(array(
  	'marqueur1' => $variable1,
  	'marqueur2' => $variable2,
  	'marqueur3' => $variable3
  	));
?>
//  Insérer des nouvelles données dans une table


<?php
  $req = $bdd->prepare('UPDATE nom_de_table SET colonne2 = :marqueur2, colonne3 = :marqueur3 WHERE colonne1 = :marqueur1');
  $req->execute(array(
  	'marqueur2' => $variable2,
  	'marqueur3' => $variable3,
  	'marqueur1' => $variable1
  	));
?>
//  Mettre à jour/modifier des données déjà présentes dans une table


<?php
  $req = $bdd->prepare('DELETE FROM nom_de_table WHERE colonne1 = :delete_ligne');
  $req->execute(array('delete_ligne' => $_SESSION['variable']));
  $req->closeCursor();
?>
//  Supprimer une ligne dans une table
