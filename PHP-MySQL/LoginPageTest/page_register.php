<?php

  //  __Connection à la base de données__
  include('db_connect.php');

  //  Inclusion du formulaire
  include('section_register.php');


  if(isset($_POST['register_username']) && isset($_POST['register_password']) && $_POST['register_username'] != null && $_POST['register_password'] != null)
  {
    //  Requête vérifiant si le nom d'utilisateur éxiste déjà dans la base de données
    $req = $bdd->prepare('SELECT username FROM login_test WHERE username = :input_username');
    $req->execute(array('input_username' => $_POST['register_username']));
    $data = $req->fetch();
    $req->closeCursor();

    if ($data == null)
    {
      //  Utilisateur n'éxiste pas
      $req = $bdd->prepare('INSERT INTO login_test(username, password) VALUES(:input_username, :input_password)');
      $req->execute(array(
      	'input_username' => htmlspecialchars($_POST['register_username']),
      	'input_password' => htmlspecialchars($_POST['register_password'])
    	));

      echo '<p>Nouvel utilisateur inscrit avec succès</p>';
    }
    else
    {
      //  Utilisateur éxiste déjà
      echo '<p>Utilisateur déjà inscrit</p>';
    }
    $req->closeCursor();
  }

?>

<!DOCTYPE html>
<html>
    <head>
          <meta charset="utf-8" />
          <title>Register</title>
          <body>

            <p>Veuillez entrer un nouveau nom d'utilisateur et un nouveau mot de passe</p>
            <p><a href="page_login.php">Login</a></p>

          </body>
    </head>
</html>
