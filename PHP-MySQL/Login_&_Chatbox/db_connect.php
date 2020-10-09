<?php

  //  __Connection à la base de données__
  //  Adresse: localhost
  //  Nom: test
  //  Login: root
  //  Password:
  try
  {
    $bdd = new PDO('mysql: host=localhost; dbname=tech_me_home; charset=utf8', 'root', '', array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION));
  }
  catch (Exception $e)
  {
    die('Erreur : ' . $e->getMessage());
  }

?>
