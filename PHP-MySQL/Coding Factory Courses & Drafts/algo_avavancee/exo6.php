<?php

function generertableau (int $taille)
{
  $tableau = array ();

  for ($i = 0; $i < $taille; $i ++)
  {
    //$nombre = random_int (0 , getrandmax());
    $nombre = random_int (0 , 100);

    if (!in_array($nombre, $tableau))
    {
      array_push($tableau, $nombre);
    }
    else
    {
      $i--;
    }
  }
  echo implode(', ', $tableau) . PHP_EOL;
  return $tableau;
}




function pickcinq (array $tableau)
{
  //count($tableau)
  $resultats = array ();
  $compteur = 0;

  while ($compteur < 5)
  {
    $randindice = random_int (0 , count($tableau) - 1);
    $nombre = $tableau[$randindice];

    if(!in_array($nombre, $resultats))
    {
      //$resultats[] = $tableau[array_rand($tableau)];
      $resultats[] = $nombre;

      $compteur ++;
    }
  }

  echo implode(', ', $resultats) . /*"<br>"*/ PHP_EOL;
  return $resultats;
}

function sequenciel (array $tableau, int $choix)
{
  
}

//generertableau(20);
//pickcinq (generertableau(20));
sequenciel(pickcinq(generertableau(20)), 67);
?>
