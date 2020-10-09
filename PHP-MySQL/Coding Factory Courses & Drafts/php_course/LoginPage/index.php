<?php

  session_start();

  function db_connect()
  {
    try
    {
      $host     = "localhost";
      $dbname   = "cours_bdd";
      $username = "root";
      $password = "";

      $db = new PDO("mysql:host=$host;dbname=$dbname",
                    $username,
                    $password);

      return $db;

    }
    catch (Exception $e)
    {
      echo $e->getMessage();
    }
  }

  $db = db_connect();

  if(isset($_SESSION['username']))
  {
    header('location:acceuil.php');
  }

?>

<!DOCTYPE html>
<html lang="fr" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>index.php</title>
  </head>
  <body>

    <form action="" method="post">
  		<label for="inputUsername">Username</label>
  		<input type="text" name="inputUsername" />
      <br>

      <label for="inputPassword">Password</label>
  		<input type="password" name="inputPassword" />
      <br>

  		<input type="submit" name="submitLogin" value="Login"/>

	   </form>

     <p>

       <?php
         //echo htmlspecialchars(" test");

         if (isset($_POST['submitLogin']))
         {
           if($_POST['inputUsername'] != null && $_POST['inputPassword'] != null)
           {
             //$req = $db->prepare("SELECT username, mdp FROM utilisateurs WHERE username = :inputUsername AND mdp = :inputPassword");
             $req = $db->prepare("SELECT * FROM utilisateurs WHERE username = :inputUsername AND mdp = :inputPassword");
             $req ->execute(array("inputUsername" => $_POST['inputUsername'],
                                  "inputPassword" => $_POST['inputPassword']));

             $data = $req->fetch();

             //var_dump($data['username']);

             if ($data != null)
             {
               //echo "Bonjour ";
               //echo $_POST['inputUsername']."!";

              $_SESSION['username'] = $_POST['inputUsername'];

              header('location:acceuil.php');
             }
             else
             {
               echo "Erreur: Utilisateur ou mot de passe introuvable.";
             }
           }
           else
           {
             echo "Erreur: Veuillez entrer un nom d'utilisateur ou un mot de passe.";
           }
         }
         else
         {
           echo "Bienvenue!";
         }

       ?>

     </p>

  </body>
</html>
