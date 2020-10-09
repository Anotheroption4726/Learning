framework .NET - MSDN library: https://msdn.microsoft.com/fr-fr/library/
https://docs.microsoft.com/fr-fr/dotnet/api/




_SANS NAMESPACE______________________________________________________

System.Console.WriteLine(System.DateTime.Now);




_AVEC NAMESPACE______________________________________________________

using System;

Console.WriteLine(DateTime.Now);








_COMMENTAIRES________________________________________________________

/* */

//




_REPERTOIRE__________________________________________________________

namespace MaPremiereApplication
{

}




_CLASSE______________________________________________________________

class ProgramName
{
    
}








_DECLARATION DE VARIABLE_____________________________________________

int age;




_INITIALIZATION DE VARIABLE__________________________________________

int age = 30;




_MANIPULATION DE VARIABLE____________________________________________

age = 30;

age++;		//équivaut à age = age + 1
age--;		//équivaut à age = age - 1
age += 10; 	// équivalent à age = age + 10
age -= 10; 	// équivalent à age = age - 10
age /= 2; 	// équivalent à age = age / 2




_VARIABLE GENERALE___________________________________________________

var x = 1;
var y = 2;
var sum = x + y;    //La somme sera considérée comme un integer




_VARIABLE BOOLEAN____________________________________________________

bool estVrai = true;
bool estFaux = false;




_VARIABLE DE CHARACTERE______________________________________________

char lit = 'X';        // Character literal
char hex = '\x0058';   // Hexadecimal
char typ = (char)88;   // Cast from integral type
char uni = '\u0058';   // Unicode

Console.WriteLine(lit); //Affiche X
Console.WriteLine(hex); //Affiche X
Console.WriteLine(typ); //Affiche X
Console.WriteLine(uni); //Affiche X




_VARIABLE CHAINE DE CHARACTERES______________________________________

string prenom = "romain";

string prenom = "romain";
string nom = "brian";
string nomPrenom = nom + " " + prenom;
Console.WriteLine(nomPrenom); // affiche : romain brian

\"			//Guillemet
\n			//Retour à la ligne
\t			//Tabulation
\\			//Affiche \\




_VARIABLES DE NOMBRES ENTIERS________________________________________

byte age;	//Entier de 0 à 255
short age;	//Entier de -32768 à 32767
int age;	//Entier de -2147483648 à 2147483647
long age;	//Entier de -9223372036854775808 à 9223372036854775807




_VARIABLES DE NOMBRES DECIMAUX_______________________________________

float age;	//Nombre simple précision de -3,402823e38 à 3,402823e38
double age;	//Nombre double précision de -1,79769313486232e308 à 1,79769313486232e308
decimal age;	//Nombre décimal de très grande précision

float myFloat = 1f; //Peut aussi s'écrire de cette manière




_CONVERSION/CASTING NUMERIQUES_______________________________________

short s = 200;
int i = s;

int i = 200;
short s = (short)i;

int i = 100000;
short s = i;	//Erreur

int i = 200;
short s = i;	//Erreur

int i = 40000;
short s = (short)i;
Console.WriteLine(s);	//Affiche -25536

int i = 20;
double d = i;

double s = 125.55;
int i = (int)s;	// i vaut 125

double i = 125.55;
int s = i;	//Erreur

string i = "123";
int s = (int)i;	//Erreur








_DECLARATION DE TABLEAU______________________________________________

string[] jours = new string[] {};
string[] jours = new string[7];




_INITIALIZATION DE TABLEAU___________________________________________

string[] jours = new string[] { "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi" };

Console.WriteLine(jours[3]); // affiche Jeudi
Console.WriteLine(jours[0]); // affiche Lundi
Console.WriteLine(jours[10]); // provoque une erreur d'exécution car l'indice n'existe pas




_MANIPULATION DE TABLEAU_____________________________________________

jours = new string[] { "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche" };

jours[0] = "Lundi";
jours[1] = "Mardi";
jours[2] = "Mercredi";
jours[3] = "Jeudi";
jours[4] = "Vendredi";
jours[5] = "Samedi";
jours[6] = "Dimanche";

Console.WriteLine(jours.Length);    //Affiche la taille du tableau




_TABLEAUX MULTIDIMENSIONELS/MATRICES_________________________________

int[,] matrix = new int[2,2];

matrix[0,0] = 1;
matrix[0,1] = 2;
matrix[1,0] = 3;
matrix[1,1] = 4;

int[,] predefinedMatrix = new int[2,2] { { 1, 2 }, { 3, 4 } };




_CREATION DE LISTE___________________________________________________

List<int> chiffres = new List<int>();
List<string> jours = new List<string> { "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche" };




_MANIPULATION DE LISTE_______________________________________________

chiffres.Add(8);			// chiffres contient 8
chiffres.Add(9);			// chiffres contient 8, 9
chiffres.Add(4);			// chiffres contient 8, 9, 4
chiffres.Add(7);            // chiffres contient 8, 9, 4, 7

chiffres.Remove(7);         // chiffres contient 8, 9, 4
chiffres.RemoveAt(1);		// chiffres contient 8, 4

int element = chiffres[0];              // element vaut 8
int element = chiffres.ElementAt(0);    // element vaut 8

int indice = chiffres.IndexOf(4);   // indice vaut 1
int indice = jours.IndexOf("Mercredi"); // indice vaut 2

int taille = liste.Count; //Taille de la Liste


List<int> numbers = new List<int>();
int[] array = new int[] { 1, 2, 3 };
numbers.AddRange(array);
//.AddRange() permet d'insérer/concaténer les éléments d'un tableau ou d'une liste dans une
// autre liste


List<string> food = new List<string>();
food.Add("apple");
food.Add("banana");

List<string> vegetables = new List<string>();
vegetables.Add("tomato");
vegetables.Add("carrot");

food.AddRange(vegetables);
Console.WriteLine(food.Count);




_DICTIONNAIRES_______________________________________________________

Dictionary<string, long> phonebook = new Dictionary<string, long>();
phonebook.Add("Alex", 415434543);
phonebook["Jessica"] = 415984588;

if (phonebook.ContainsKey("Alex") || phonebook.ContainsKey("Jessica"))
{
    Console.WriteLine("Alex's number is " + phonebook["Alex"]);
    Console.WriteLine("Jessica's number is " + phonebook["Jessica"]);
}


phonebook.Remove("Jessica");
Console.WriteLine(phonebook["Jessica"]);    //Erreur




_ENUMERATIONS________________________________________________________

enum Jours
{
    Lundi,
    Mardi,
    Mercredi,
    Jeudi,
    Vendredi,
    Samedi,
    Dimanche
}

//une énumération est un type dont toutes les valeurs définies sont des entiers. La première vaut 0, et chaque valeur suivante prend la valeur précédente augmentée de 1. C'est-à-dire que Lundi vaut 0, Mardi vaut 1, etc


enum Jours
{
    Lundi = 5, // lundi vaut 5
    Mardi, // mardi vaut 6
    Mercredi = 9, // mercredi vaut 9
    Jeudi = 10, // jeudi vaut 10
    Vendredi, // vendredi vaut 11
    Samedi, // samedi vaut 12
    Dimanche = 20 // dimanche vaut 20
}

int valeur = (int)Jours.Lundi; // valeur vaut 5


class Program
{
    enum Jours
    {
        Lundi,
        Mardi,
        Mercredi,
        Jeudi,
        Vendredi,
        Samedi,
        Dimanche
    }

    static void Main(string[] args)
    {
        Jours lundi = Jours.Lundi;
        Console.WriteLine(lundi);
    }
}

//Affiche Lundi


if (jourDeLaSemaine == Jours.Dimanche || jourDeLaSemaine == Jours.Samedi)
{

	Console.WriteLine("Bon week-end");

}








_OPERATEURS DE COMPARAISON___________________________________________

==	//Egalité
!=	//Différence

>	//Supérieur à
<	//Inférieur à

>=	//Supérieur ou égal
<=	//Inférieur ou égal

&&	//ET logique
||	//OU logique

!	//Négation




_INSTRUCTION IF______________________________________________________

if (x > 0){

	Console.WriteLine("x est supèrieur à 0");

}
else if (x < 0){

	Console.WriteLine("x est infèrieur à 0");

}
else {

	Console.WriteLine("x est égal à 0");

}




_INSTRUCTION SWITCH__________________________________________________

string civilite = "M.";

switch (civilite)
{

	case "M." :
		Console.WriteLine("Bonjour monsieur");
	break;

	case "Mme":
		Console.WriteLine("Bonjour madame");
	break;

	default:
    		Console.WriteLine("Error");
    	break;

}


string mois = "Novembre";

switch (mois)
{

	case "Mars":
	case "Avril":
	case "Mai":
		Console.WriteLine("C'est le printemps");
	break;

	case "Juin":
	case "Juillet":
	case "Aout":
		Console.WriteLine("C'est l'été");
	break;

	case "Septembre":
	case "Octobre":
	case "Novembre":
		Console.WriteLine("C'est l'automne");
	break;

	case "Décembre":
	case "Janvier":
	case "Février":
		Console.WriteLine("C'est l'hiver");
	break;

}




_BOUCLE FOR__________________________________________________________

int compteur;

for (compteur = 0; compteur < 50; compteur++)
{
    
}


for (int i = 9; i > 0; i -= 2)
{

}


for (int i = 0; i < 20; i++)
{
	if (i % 2 == 0)
	{
		continue;
	}
	Console.WriteLine(i);
	//Affiche une liste de nombres impairs allant de 1 à 19
}


string[] jours = new string[] { "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche" };

for (int jcount = 0; jcount < jours.Length; jcount++)
{
	Console.WriteLine(jours[jcount]);
	//Affiche une liste comportant tous les jours de la semaine
}


List<string> jours = new List<string> { "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche" };

for (int i = jours.Count - 1; i >= 0; i--)
{
    if (jours[i] == "Mercredi")
        jours.Remove(jours[i]);

	//Parcourir la liste à l'envers: meilleure méthode (pour l'instant) pour supprimer un élément d'une liste
}




_BOUCLE FOREACH______________________________________________________

string[] jours = new string[] { "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche" };

foreach (string jourName in jours)
{
	Console.WriteLine(jourName);
}


bool trouve = false;
foreach (string jourName in jours)
{
    if (jour == "Jeudi")
    {
        trouve = true;
        break;
    }
}


foreach (string jourName in jours)
{
	jourName = "pas de jour !";

    //Erreur de compilation. La boucle foreach est une boucle en lecture seule.
    //Utiliser plutot une boucle for pour modifier/supprimer un élément
}


foreach (string jourName in jours)
{
    if (jourName == "Mercredi")
        jours.Remove(jourName);

    //Là aussi erreur de compilation
}




_BOUCLE WHILE________________________________________________________

int i = 0;

while (i < 50)
{
    Console.WriteLine("Bonjour C#");
    i++;
}


int i = 0;
while (true)
{
	if (i >= 50)
	{
		break;
	}
	Console.WriteLine("Bonjour C#");
	i++;
}


do
{
    Console.WriteLine("Bonjour C#");
    i++;

    //Condition de sortie de boucle est évaluée à la fin de la boucle
    //On passera au moins une fois dans le corps de la boucle
}
while (i < 50);


string[] jours = new string[] { "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche" };
int i = 0;
bool trouve = false;

while (i < jours.Length && !trouve)
{
    string valeur = jours[i];
    if (valeur == "Jeudi")
    {
        trouve = true;
    }
    else
    {
        i++;
    }
}
if (!trouve)
    Console.WriteLine("Valeur non trouvée");
else
    Console.WriteLine("Trouvé à l'indice " + i);








_DECLARATION DE METHODE______________________________________________

Signature de la méthode
{
 
	Bloc de code de la méthode

}


static void AffichageBienvenue ()
{
	
	Console.WriteLine("Bonjour Nicolas");

}


static void DireBonjour (string prenom, int age)
{

	Console.WriteLine("Bonjour " + prenom);
	Console.WriteLine("Vous avez " + age + " ans");

}


static double LongueurHypotenuse (double a, double b)
{
	double sommeDesCarres = a * a + b * b;
	double resultat = Math.Sqrt(sommeDesCarres);
	return resultat;
}


static string Conjugaison(string genre)
{

	if (genre == "homme")
	return "é";

	else
        return "ée";

}


static string Conjugaison(string genre)
{

	if (genre == "homme")
	{
		return "é";
	}
	
	else
	{
        	if (genre == "femme")
		{
			return "ée";
		}
	}
	
	return "";

}




_METHODE MAIN________________________________________________________

static void Main(string[] args)
{


}

static void Main(string[] args)
{

	Console.WriteLine("Le résultat est : " + LongueurHypotenuse(10, 30));

}




_APPEL DE METHODE____________________________________________________

static void AffichageBienvenue();

//une méthode statique ne peut appeler que des méthodes statiques?




_INSTANTIATION DE CLASSE_____________________________________________

class Box
{
    public double l, b, h;

    public double volume()
    {

        return (this.l * this.b * this.h);

    }

}

class Program
{

    static void Main(string[] args)
    {

        Box box1 = new Box();
        box1.l = 45;
        box1.b = 10;
        box1.h = 20;

        Console.WriteLine("Volume of box1 is " + box1.volume());

    }

}




_APPEL METHODE D'AFFICHAGE CONSOLE___________________________________

Console.WriteLine();




_APPEL METHODE DE CALCUL DE RACINE CARREE____________________________

Math.Sqrt();

//prend en paramètre un double et retourne une valeur de type double




_APPEL METHODE DE CALCUL EN PUISSANCE________________________________

Math.Pow(a, 2)	//a au carré
Math.Pow(a, 3)	//a^3




_CLASSEMENT DES ELEMENTS D'UN TABLEAU PAR ORDRE ALPHABETIQUE_________

Array.Sort(tableau);




_AFFICHAGE DE LA DATE COURANTE_______________________________________

using System;

Console.WriteLine(DateTime.Now); // Sinon c'est ' System.Console.WriteLine(System.DateTime.Now);




_CONVERSION/CASTING ENTRE TYPES______________________________________

string chaineAge = "20";
int age = Convert.ToInt32(chaineAge); // age vaut 20

string chaineAge = "20";
int age = int.Parse(chaineAge); // age vaut 20

string chaineAge = "vingt ans";
int age = Convert.ToInt32(chaineAge);	// Erreur


string chaineAge = "ab20cd";
int age;
if (int.TryParse(chaineAge, out age))
{
    Console.WriteLine("La conversion est possible, age vaut " + age);
}
else
{
    Console.WriteLine("Conversion impossible");
}


Convert.ToString()
Convert.ToDecimal()
int.TryParse()
double.TryParse()
...




_SAISIE CLAVIER______________________________________________________

string saisie = Console.ReadLine();

Console.WriteLine("Veuillez saisir une phrase et valider avec la touche \"Entrée\"");
string saisie = Console.ReadLine();
Console.WriteLine("Vous avez saisi : " + saisie);


bool ageIsValid = false;
int age = -1;
while (!ageIsValid)
{
    Console.WriteLine("Veuillez saisir votre age");
    string saisie = Console.ReadLine();
    if (int.TryParse(saisie, out age))
        ageIsValid = true;
    else
    {
        //ageIsValid = false;
        Console.WriteLine("L'age que vous avez saisi est incorrect ...");
    }
}
Console.WriteLine("Votre âge est de : " + age);




_DETECTION CLAVIER___________________________________________________

Console.ReadKey(true);	//Le paramêtre "true" indique que nous ne souhaitions pas que notre saisie apparaisse à l’écran

Console.WriteLine("Veuillez appuyer sur une touche pour démarrer le calcul ...");
Console.ReadKey(true);
int somme = 0;

for (int i = 0; i < 100; i++)
{
    somme += i;
}
Console.WriteLine(somme);


Console.WriteLine("Voulez-vous continuer (O/N) ?");
ConsoleKeyInfo saisie = Console.ReadKey(true);

if (saisie.Key == ConsoleKey.O)
{
    Console.WriteLine("On continue ...");
}
else
{
    Console.WriteLine("On s'arrête ...");
}

//	"ConsoleKeyInfo» est une structure. "Key" est une propriété de la structure. Il s’agit d’une variable évoluée qui
//	permet de contenir plusieurs choses.




_AFFICHAGE DE COULEURS_______________________________________________

Console.ForegroundColor = ConsoleColor.DarkBlue;
Console.BackgroundColor = ConsoleColor.Yellow;
Console.Write("Hello ");
Console.ForegroundColor = ConsoleColor.Yellow;
Console.BackgroundColor = ConsoleColor.Red;
Console.Write("les couleurs");
Console.ForegroundColor = ConsoleColor.Black;
Console.BackgroundColor = ConsoleColor.White;
Console.Write(" dans la console\n");

Console.ResetColor();




_EFFACER L'AFFICHAGE CONSOLE_________________________________________

Console.Clear();


for( int i = 1; i <= 40; i++ )
{
    Console.WriteLine("Ligne numéro " + i);
    if( i % 10 == 0 )
    {
        Console.ReadKey();
        Console.Clear();
    }
}
