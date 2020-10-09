<?php

  //require include page 33 du powerpoint
  session_start();

  if(isset($_SESSION['username']))
  {
    echo "Bonjour " . $_SESSION['username'];
  }
  else {
    header('location:index.php');
  }

?>

<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>

    <?php

      if (isset($_POST['logout']))
      {
        unset($_SESSION);
        session_destroy();
        header('location:index.php');
      }

    ?>

    <p>
      <form action="" method="post">

    		  <input type="submit" name="logout" value="Log Out"/>

  	   </form>
    </p>

  </body>
</html>
