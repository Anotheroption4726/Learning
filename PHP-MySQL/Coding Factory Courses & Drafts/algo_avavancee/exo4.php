<?php

function fibonaccirecursif (int $n)
{
  if ($n < 2)
  {
    return $n;
  }
  else
  {
      return fibonaccirecursif($n-1) + fibonaccirecursif($n - 2);
  }
}


//fibonaccirecursif(5);

/*
$i = 0;

while ($i < 50)
{
  echo "f($i)=" . fibonaccirecursif($i)." ; ";
  if ($i % 5 == 0)
  {
    echo PHP_EOL;
  }
  $i++;
}
*/



function fibonacci($n, &$calls)
{
   if(!array_key_exists($n, $calls))
   {
       $calls[$n] = 0;
   }

   $calls[$n]++;

   if($n <= 1)
   {
       $fibo = $n;
   }
   else
   {
       $fibo = fibonacci($n - 1, $calls) + fibonacci($n - 2, $calls);
   }
   return $fibo;
}

$calls = [];
echo fibonacci(35, $calls);
print_r($calls);



?>
