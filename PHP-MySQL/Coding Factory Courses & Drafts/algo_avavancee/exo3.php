<?php

function randomtabbubble (int $taille)
{
  $tableau = array ();

  for ($i = 0; $i < $taille; $i ++)
  {
    //$nombre = random_int (0 , getrandmax());
    $nombre = random_int (0 , 10);

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



  $timestart = microtime(true);

  $plusderreur = false;

  $loop = 0;

  do
  {
    $plusderreur = false;

    for($j = 0; $j < count($tableau) - 1 - $loop; $j++)
    {
      if ($tableau[$j] > $tableau[$j + 1])
      {
          $chiffretemp = $tableau[$j];
          $tableau[$j] = $tableau[$j + 1];
          $tableau[$j + 1] = $chiffretemp;
          $plusderreur = true;
      }
    }
    $loop ++;
  }
  while ($plusderreur == true);


  //$triTableau = array_unique ($tableau);
  echo implode(', ', $tableau) . PHP_EOL;
  echo "temps : ".((microtime(true) - $timestart) * 1000) . "ms".PHP_EOL.PHP_EOL;
}





function randomtablechange (int $taille)
{
  $tableau = array ();

  for ($i = 0; $i < $taille; $i ++)
  {
    //$nombre = random_int (0 , getrandmax());
    $nombre = random_int (0 , 10);

    if (!in_array($nombre, $tableau))
    {
      array_push($tableau, $nombre);
    }
    else
    {
      $i--;
    }
  }
  echo implode(', ', $tableau) . "<br>" /*. PHP_EOL*/;

  for ($j = 0; $j < $taille; $j ++)
  {
    for ($k = $j +1; $k < $taille; $k ++)
    {
      if ($tableau[$j] > $tableau[$k])
      {
        $chiffretemp = $tableau[$k];
        $tableau[$k] = $tableau[$j];
        $tableau[$j] = $chiffretemp;
      }
    }
  }

  //$triTableau = array_unique ($tableau);
  echo implode(', ', $tableau) . /*"<br>"*/ PHP_EOL;
}







function randomtabinsert (int $taille)
{
  $tableau = array ();

  for ($i = 0; $i < $taille; $i ++)
  {
    //$nombre = random_int (0 , getrandmax());
    $nombre = random_int (0 , 10);

    if (!in_array($nombre, $tableau))
    {
      array_push($tableau, $nombre);
    }
    else
    {
      $i--;
    }
  }
  echo implode(', ', $tableau) . /*"<br>" .*/ PHP_EOL;



  for ($i = 1; $i < $taille; $i ++)
  {
      //$temp = $tableau[$i];
      for ($j = $i; $j > 0; $j--)
      {
        if ($tableau[$j] < $tableau[$j - 1])
        {
            $temp = $tableau[$j - 1];
            $tableau[$j - 1] = $tableau[$j];
            $tableau[$j] = $temp;
        }
        else
        {
          break;
        }
      }

  }
  echo implode(', ', $tableau) . /*"<br>"*/ PHP_EOL;
}






//randomtabbubble(5);
//randomtablechange(5);
randomtabinsert(5);

?>
