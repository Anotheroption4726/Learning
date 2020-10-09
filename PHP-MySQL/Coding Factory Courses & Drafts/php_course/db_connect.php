<?php

function db_connect(){
  try  {
    $host     = "localhost";
    $dbname   = "cours_bdd";
    $username = "root";
    $password = "";

    $db = new PDO("mysql:host=$host;dbname=$dbname",
                  $username,
                  $password);

    return $db;

  } catch (Exception $e){
    echo $e->getMessage();
  }
}
