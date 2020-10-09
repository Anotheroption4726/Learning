function lancerDe(faces)
{
  return Math.floor(faces * Math.random()) + 1;
}


function course()
{
  var tortue = 0;
  //var fin = false;

  while (true)
  {
    resultat = lancerDe(6)

    if (resultat == 6)
    {
      // console.log("Lapin a gagné!");
      //fin = true;
      return "lapin";
    }
    else
    {
      tortue += 1;
    }

    if(tortue == 6)
    {
      // console.log("Tortue a gagné!");
      //fin = true;
      return "tortue";
    }
  }
}



function pourcentageVictoires(nombres)
{
  tableau = [];
  resultat = 0;

  for (var i = 0; i < nombres; i++)
  {
    tableau.push(course());
  }

  for (var j = 0; j < tableau.length; j++)
  {
    if (tableau[j] == "lapin")
    {
      resultat += 1;
    }
  }

  //return resultat;
  return (resultat/nombres)*100;
}


console.log("Le lapin a gagné " + Math.floor(pourcentageVictoires(10000)) + "% des fois.");
