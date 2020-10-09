http://www.wampserver.com/
https://www.mamp.info/en/
https://www.apachefriends.org/fr/index.html




https://openclassrooms.com/fr/courses/918836-concevez-votre-site-web-avec-php-et-mysql



_INTRODUCTION________________________________________________________


<?php /* Balises d'ouverture et de fermeture du code php */ ?>

<?php include("menus.php"); /* Inclusion de portion de page */ ?>
<?php include("includes/menus.php"); ?>


<!DOCTYPE html>
<html>
    <head>
        <title></title>
        <meta charset="utf-8" />
    </head>
    <body>
      <?php /* Insérer du code PHP ici */ ?>
    </body>
</html>


<?php echo "Bonjour!";    // Affichage de Texte ?>
<?php echo "Cette ligne a été écrite \"uniquement\" en PHP."; // Affichage de guillemets" ?>
<?php echo date('d/m/Y h:i:s'); // Affichage de la date et de l'heure ?>


<?php phpinfo(); // Affichage de toutes les informations concernant le serveur, les pages en php, etc... ?>

//  Configurer php.ini:
https://openclassrooms.com/fr/courses/918836-concevez-votre-site-web-avec-php-et-mysql/4238821-configurez-php-pour-visualiser-les-erreurs

//  Erreurs:
https://openclassrooms.com/fr/courses/918836-concevez-votre-site-web-avec-php-et-mysql/4240011-au-secours-mon-script-plante




_VARIABLES___________________________________________________________

<?php
$age_du_visiteur = 17; // La variable est créée et vaut 17
$age_du_visiteur = 23; // La variable est modifiée et vaut 23
$age_du_visiteur = 55; // La variable est modifiée et vaut 55
?>


<?php
$nom_du_visiteur = "Mateo21";
$nom_du_visiteur = 'Mateo21';
?>


<?php
$variable = "Mon \"nom\" est Mateo21";
$variable = 'Je m\'appelle Mateo21';
?>


<?php
$variable = 'Mon "nom" est Mateo21';
$variable = "Je m'appelle Mateo21";
?>


<?php
$je_suis_un_zero = true;
$je_suis_bon_en_php = false;
?>


<?php
$pas_de_valeur = NULL;
?>


<?php
$age_du_visiteur = 17;
echo $age_du_visiteur;
?>


<?php
$age_du_visiteur = 17;
echo "Le visiteur a $age_du_visiteur ans";
?>


<?php
$age_du_visiteur = 17;
echo 'Le visiteur a ' . $age_du_visiteur . ' ans';
?>




_CONDITIONS__________________________________________________________

//  Les deux exemples suivants affichent éxactement la même chose:

<?php
$variable = 23;
if ($variable == 23)
{
    echo '<strong>Bravo !</strong> Vous avez trouvé le nombre mystère !';
}
?>


<?php
$variable = 23;
if ($variable == 23)
{
?>

<strong>Bravo !</strong> Vous avez trouvé le nombre mystère !

<?php
}
?>




//  Les deux exemples suivants font éxactement la même chose:

<?php
$age = 24;
if ($age >= 18)
{
	$majeur = true;
}
else
{
	$majeur = false;
}
?>


<?php
$age = 24;
$majeur = ($age >= 18) ? true : false;
?>




//  Les deux exemples suivants affichent éxactement la même chose:


<?php
$nombre_de_lignes = 1;
while ($nombre_de_lignes <= 100)
{
    echo 'Ceci est la ligne n°' . $nombre_de_lignes . '<br />';
    $nombre_de_lignes++;
}
?>


<?php
	$nombre_de_lignes = 1;
	while ($nombre_de_lignes <= 100)
	{
?>
	Ceci est la ligne n°

<?php echo $nombre_de_lignes; ?>

        <br />

<?php $nombre_de_lignes++;
	}
?>




_TABLEAUX____________________________________________________________

<?php
// La fonction array permet de créer un array
$prenoms = array ('François', 'Michel', 'Nicole', 'Véronique', 'Benoît');
?>

<?php
$prenoms[0] = 'François';
$prenoms[1] = 'Michel';
$prenoms[2] = 'Nicole';
?>

<?php
$prenoms[] = 'François'; // Créera $prenoms[0]
$prenoms[] = 'Michel'; // Créera $prenoms[1]
$prenoms[] = 'Nicole'; // Créera $prenoms[2]
?>

<?php
echo $prenoms[0];
echo $prenoms[1];
echo $prenoms[2];
?>


<?php
// On crée notre array $prenoms
$prenoms = array ('François', 'Michel', 'Nicole', 'Véronique', 'Benoît');
// Puis on fait une boucle pour tout afficher :
for ($numero = 0; $numero < 5; $numero++)
{
    echo $prenoms[$numero] . '<br />'; // affichera $prenoms[0], $prenoms[1] etc.
}
?>


<?php
$prenoms = array ('François', 'Michel', 'Nicole', 'Véronique', 'Benoît');
foreach($prenoms as $element)
{
    echo $element . '<br />'; // affichera $prenoms[0], $prenoms[1] etc.
}
?>





<?php
// On crée notre array $coordonnees
$coordonnees = array (
    'prenom' => 'François',
    'nom' => 'Dupont',
    'adresse' => '3 Rue du Paradis',
    'ville' => 'Marseille');
?>

<?php
$coordonnees['prenom'] = 'François';
$coordonnees['nom'] = 'Dupont';
$coordonnees['adresse'] = '3 Rue du Paradis';
$coordonnees['ville'] = 'Marseille';
?>

<?php
echo $coordonnees['prenom'];
echo $coordonnees['nom'];
echo $coordonnees['adresse'];
echo $coordonnees['ville'];
?>


<?php
$coordonnees = array (
    'prenom' => 'François',
    'nom' => 'Dupont',
    'adresse' => '3 Rue du Paradis',
    'ville' => 'Marseille');
foreach($coordonnees as $element)
{
    echo $element . '<br />';
}
?>


<?php
$coordonnees = array (
    'prenom' => 'François',
    'nom' => 'Dupont',
    'adresse' => '3 Rue du Paradis',
    'ville' => 'Marseille');
echo '<pre>';
print_r($coordonnees);
echo '</pre>';
?>




_RECHERCHER DANS UN TABLEAU__________________________________________

<?php array_key_exists('cle', $array); ?>
<?php in_array('valeur', $array); ?>
<?php array_search('valeur', $array); ?>


<?php
$coordonnees = array (
    'prenom' => 'François',
    'nom' => 'Dupont',
    'adresse' => '3 Rue du Paradis',
    'ville' => 'Marseille');
if (array_key_exists('nom', $coordonnees))
{
    echo 'La clé "nom" se trouve dans les coordonnées !';
}
if (array_key_exists('pays', $coordonnees))
{
    echo 'La clé "pays" se trouve dans les coordonnées !';
}
?>


<?php
$fruits = array ('Banane', 'Pomme', 'Poire', 'Cerise', 'Fraise', 'Framboise');
$position = array_search('Fraise', $fruits);
echo '"Fraise" se trouve en position ' . $position . '<br />';
$position = array_search('Banane', $fruits);
echo '"Banane" se trouve en position ' . $position;
?>




_FONCTIONS___________________________________________________________

<?php
calculCube();
?>

<?php
$volume = calculCube(4);
?>


<?php
$phrase = 'Bonjour tout le monde ! Je suis une phrase !';
$longueur = strlen($phrase);
echo 'La phrase ci-dessous comporte ' . $longueur . ' caractères :<br />' . $phrase;
?>


<?php
$ma_variable = str_replace('b', 'p', 'bim bam boum');
echo $ma_variable;
?>


<?php
$chaine = 'Cette chaîne va être mélangée !';
$chaine = str_shuffle($chaine);
echo $chaine;
?>


<?php
$chaine = 'COMMENT CA JE CRIE TROP FORT ???';
$chaine = strtolower($chaine);
echo $chaine;
?>


<?php
// Enregistrons les informations de date dans des variables
$jour = date('d');
$mois = date('m');
$annee = date('Y');
$heure = date('H');
$minute = date('i');
// Maintenant on peut afficher ce qu'on a recueilli
echo 'Bonjour ! Nous sommes le ' . $jour . '/' . $mois . '/' . $annee . 'et il est ' . $heure. ' h ' . $minute;
?>


<?php
function DireBonjour($nom)
{
    echo 'Bonjour ' . $nom . ' !<br />';
}
DireBonjour('Marie');
DireBonjour('Patrice');
DireBonjour('Edouard');
DireBonjour('Pascale');
DireBonjour('François');
DireBonjour('Benoît');
DireBonjour('Père Noël');
?>


<?php
// Ci-dessous, la fonction qui calcule le volume du cône
function VolumeCone($rayon, $hauteur)
{
   $volume = $rayon * $rayon * 3.14 * $hauteur * (1/3); // calcul du volume
   return $volume; // indique la valeur à renvoyer, ici le volume
}
$volume = VolumeCone(3, 1);
echo 'Le volume d\'un cône de rayon 3 et de hauteur 1 est de ' . $volume;
?>




_TRANSMISSION DE DONNEES_____________________________________________

-Page 1: index.php
<a href="bonjour.php?nom=Dupont&amp;prenom=Jean">Dis-moi bonjour !</a>

-Page 2: bonjour.php
<p>Bonjour <?php echo $_GET['prenom'] . ' ' . $_GET['nom']; ?> !</p>

//	Le lien de la Page 1 affiche un lien qui envoie des données à la Page 2
//	La Page 2 les récupère pour les afficher avec l'Array $_GET['']




<?php
if (isset($_GET['prenom']) && isset($_GET['nom'])) // On a le nom et le prénom
{
	echo 'Bonjour ' . $_GET['prenom'] . ' ' . $_GET['nom'] . ' !';
}
else // Il manque des paramètres, on avertit le visiteur
{
	echo 'Il faut renseigner un nom et un prénom !';
}
?>

//	Même chose qu'au dessus mais cette fois-ci on regarde s'il y a bien des paramêtres qui ont été passés dans l'url






-Page 1: index.php
<a href="bonjour.php?nom=Dupont&prenom=Jean&repeter=8">Dis-moi bonjour !</a>

-Page 2: bonjour.php

<?php
if (isset($_GET['prenom']) AND isset($_GET['nom']) AND isset($_GET['repeter']))
{
	for ($i = 0 ; $i < $_GET['repeter'] ; $i++)
	{
		echo 'Bonjour ' . $_GET['prenom'] . ' ' . $_GET['nom'] . ' !<br />';
	}
}
else
{
   echo 'Il faut renseigner un nom, un prénom et un nombre de répétitions !';
}
?>

//	Cette fois le message d'acceuil "Bonjour Jean Dupont!" est répété 8 fois




<?php
if (isset($_GET['prenom']) AND isset($_GET['nom']) AND isset($_GET['repeter']))
{
	// 1 : On force la conversion en nombre entier
	$_GET['repeter'] = (int) $_GET['repeter'];
	// 2 : Le nombre doit être compris entre 1 et 100
	if ($_GET['repeter'] >= 1 AND $_GET['repeter'] <= 100)
	{
		for ($i = 0 ; $i < $_GET['repeter'] ; $i++)
		{
			echo 'Bonjour ' . $_GET['prenom'] . ' ' . $_GET['nom'] . ' !<br />';
		}
	}
}
else
{
   echo 'Il faut renseigner un nom, un prénom et un nombre de répétitions !';
}
?>

//	Même chose qu'au dessus sauf que cette fois on fait du transtypage sur le paramêtre 'repeter' pour le transformer en entier
//	On vérifie ensuite que le nombre obtenu est bien un nombre positif non nul inférieur à 100




_FORMULAIRES_________________________________________________________

<form method="post" action="cible.php">

	<p>
	    <input type="text" name="prenom" />
	    <input type="submit" value="Valider" />
	</p>

</form>

//	méthode get : les données transitent par l'URL et sont récupérables grâce à l'array $_GET
//	méthode post : les données ne transitent pas par l'URL. Mais elles ne sont pas plus sécurisées qu'avec la méthode get
//	type: possibilité d'utiliser le type="password", type="checkbox", etc...
//	name(obligatoire) : nom de la zone de texte qui va produire une variable
//	value(facultatif) : c'est ce que contient la zone de texte au départ. Par défaut, la zone de texte est vide
//	id: permettent de lier les inputs à leurs labels


<?php echo $_POST['prenom']; ?>
//	récupère le 'prenom' de l'input de la page précédente

<?php echo htmlspecialchars($_POST['prenom']); ?>
//	empêche l'injection de code html


//	Textarea
<textarea name="message" rows="8" cols="45">
	Votre message ici.
</textarea>


//	Liste déroulante
<select name="choix">
    <option value="choix1">Choix 1</option>
    <option value="choix2">Choix 2</option>
    <option value="choix3">Choix 3</option>
    <option value="choix4">Choix 4</option>
</select>

<option value="choix3" selected="selected">Choix 3</option>
//	Optionel mais permet de rendre le choix3 selectionné par défaut


//	Checkbox
<input type="checkbox" name="case" id="case" />
<label for="case">Ma case à cocher</label>

<input type="checkbox" name="case" checked="checked" />


//	Les boutons d'option
Aimez-vous les frites ?
<input type="radio" name="frites" value="oui" id="oui" checked="checked" /> <label for="oui">Oui</label>
<input type="radio" name="frites" value="non" id="non" /> <label for="non">Non</label>


//	Les champs cachés
<input type="hidden" name="pseudo" value="Mateo21" />




_VARIABLES SUPERGLOBALES_____________________________________________

$_SERVER
//	Valeurs renvoyées par le serveur

$_SERVER['REMOTE_ADDR']
//	Donne l'adresse IP du client qui a demandé à voir la page

$_SESSION
//	Variables de session qui restent stockées sur le serveur le temps de la présence d'un visiteur

$_COOKIE
//	Contient les valeurs des cookies enregistrés sur l'ordinateur du visiteur

$_FILES
//	Contient la liste des fichiers qui ont été envoyés via le formulaire précédent




_SESSION & COOKIES___________________________________________________

session_start()
//	démarre le système de sessions. Si le visiteur vient d'arriver sur le site, alors un numéro de session est généré pour lui.
//	Il est necessaire d'appeler cette fonction au tout début de chacune des pages où il y a des variables de session

session_destroy()
//	ferme la session du visiteur. Cette fonction est automatiquement appelée lorsque le visiteur ne charge plus de page du site
//	pendant plusieurs minutes (timeout)


<?php
// On démarre la session AVANT d'écrire du code HTML
session_start();

// On s'amuse à créer quelques variables de session dans $_SESSION
$_SESSION['prenom'] = 'Jean';
$_SESSION['nom'] = 'Dupont';
$_SESSION['age'] = 24;
?>

<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Titre de ma page</title>
    </head>
    <body>
    <p>
        Salut <?php echo $_SESSION['prenom']; ?> !<br />
        Tu es à l'accueil de mon site (index.php). Tu veux aller sur une autre page ?
    </p>
    </body>
</html>
