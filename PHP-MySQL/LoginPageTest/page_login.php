<?php

  //	Démarre le système de sessions. Si le visiteur vient d'arriver sur le site, alors un numéro de session est généré pour lui.
  session_start();


  //  __Connection à la base de données__
  include('db_connect.php');


  if (isset($_POST['login_username']) && isset($_POST['login_password']) && $_POST['login_username'] != null && $_POST['login_password'] != null)
  {
    //  Requète SQL récupérant dans la table l'username et le password envoyé par le formulaire
    $req = $bdd->prepare('SELECT username, password FROM login_test WHERE username = :input_username AND password = :input_password');
    $req->execute(array('input_username' => $_POST['login_username'], 'input_password' => $_POST['login_password']));
    $data = $req->fetch();

    if ($data != null)
    {
      //  Affiche un message de bienvenue ainsi qu'un bouton de logout si les informations sont bonnes
      $_SESSION['session_username'] = $data['username'];

      echo '<p>Bonjour ' . $_SESSION['session_username'] .' !</p>';
      include('section_delete.php');
      include('section_logout.php');
    }
    else
    {
      //  Affiche un message d'erreur si les informations ne sont pas bonnes
      include('section_login.php');
      echo '<p>Nom utilisateur ou mot de passe incorrect</p>';

      //  Affichage du lien vers la page d'inscription
      RegisterLink();
    }

    //  Fermeture du curseur d'analyse des résultats
    $req->closeCursor();
  }
  else
  {
    //  Affiche la page de Login si jamais aucun formulaire n'a été envoyé
    include('section_login.php');

    if (isset($_POST['logout']))
    {
      //  Affiche un message de déconnection si jamais l'utilisateur s'est deconnecté
      echo '<p>Vous êtes déconnecté</p>';

      session_destroy();
    }
    elseif (isset($_POST['delete']))
    {
      //  Requète de suppression d'utilisateur
      $req = $bdd->prepare('DELETE FROM login_test WHERE username = :delete_user');
      $req->execute(array('delete_user' => $_SESSION['session_username']));

      //  Fermeture du curseur d'analyse des résultats
      $req->closeCursor();

      //  Affiche un message de suppression si jamais l'utilisateur a supprimé son compte
      echo '<p>Compte supprimé avec succès</p>';

      session_destroy();
    }

    echo '<p>Veuillez entrer un nom utilisateur et un mot de passe</p>';

    //  Affichage du lien vers la page d'inscription
    RegisterLink();
  }

  //  Lien vers la page d'inscription
  function RegisterLink()
  {
    echo '<p><a href="page_register.php">Register</a></p>';
  }
?>

<!DOCTYPE html>
<html>
    <head>
          <meta charset="utf-8" />
          <title>Login</title>
    </head>
</html>
