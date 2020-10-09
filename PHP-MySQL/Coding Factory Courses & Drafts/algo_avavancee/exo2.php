<?php

  function escalier (int $maxnbr, array $tbl)
  {
    foreach ($tbl as $nbr)
    {
      $resultats = array ();

      for ($i = 0; $i < $maxnbr; $i += $nbr)
      {
        array_push($resultats, $nbr);
      }

      echo implode(', ', $resultats) . PHP_EOL;
    }
  }

  escalier(10, [2]);
  //escalier(10, [3]);

  //escalier(17, [5]);
  //escalier(32, [4, 8, 5]);

?>
