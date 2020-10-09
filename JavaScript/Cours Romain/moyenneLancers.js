function nbrCoups()
{
  var tableau = [0, 0, 0, 0, 0, 0];
  var remplissage = 0;
  compteur = 0;

  while (remplissage < tableau.length)
  {
    compteur++;
    resultat = Math.floor(6 * Math.random()) + 1;

    for (var i = 0; i < tableau.length; i++)
    {
      if (tableau[i] == resultat)
      {
        break;
      }
      else if (i == remplissage)
      {
        tableau[i] = resultat;
        remplissage++;
        break;
      }
      else
      {
        continue;
      }
    }
  }

  return compteur;
}


function moyenneCoups(nombres)
{
  var tableau2 = [];
  var moyenne = 0;

  for (var j = 0; j < nombres; j++)
  {
    tableau2.push(nbrCoups());
  }

  for (var k = 0; k < tableau2.length; k++)
  {
    moyenne += tableau2[k];
  }

  return moyenne/nombres;
}
console.log(moyenneCoups(10000));
