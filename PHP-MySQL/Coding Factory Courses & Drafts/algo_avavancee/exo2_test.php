<?php

  function escalier (int $maxnbr, array $tbl)
  {
    $resultat = 0;
    $resultatFinal;
    $winner;
    $goodnbr = array ();

    foreach ($tbl as $nbr)
    {
      if ($maxnbr % $nbr == 0)
      {
        array_push($goodnbr, $nbr);
      }
    }

    foreach ($goodnbr as $nbr)
    {
      $maxtest = $maxnbr;
      while ($maxtest > 0)
      {
        $maxtest -= $nbr;
        $resultat ++;
      }

      if ($resultatFinal == null)
      {
        $resultatFinal = $resultat;
        $resultat = 0;
        $winner = $nbr;
      }
      else if ($resultat < $resultatFinal)
      {
        $resultatFinal = $resultat;
        $resultat = 0;
        $winner = $nbr;
      }
      else
      {
        continue;
      }
    }

    if ($winner == null)
    {
      echo "impossible" . PHP_EOL;
    }
    else
    {
      echo $winner . PHP_EOL;
    }
  }

  /*
  escalier(10, [2]);
  escalier(10, [3]);


  escalier(17, [5]);
  escalier(32, [4, 8, 5]);
  */



  //$index => $nbr

 ?>
