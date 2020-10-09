var resultat = 0;
var tableau = [0, 1];
const nbrValeurs = 50;

for (var i = 2; i < nbrValeurs; i++)
{
  resultat = tableau[i-2] + tableau[i-1];
  tableau.push(resultat);
}

console.log(tableau);
