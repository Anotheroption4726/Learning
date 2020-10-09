#__INTRODUCTION______________________________________________________
#
#
#   - Histoire
"""

        Python est un langage de programmation, dont la première version est sortie en 1991. 
        Créé par Guido van Rossum, il a voyagé du Macintosh de son créateur, qui travaillait 
        à cette époque au Centrum voor Wiskunde en Informatica aux Pays-Bas, jusqu'à se voir 
        associer une organisation à but non lucratif particulièrement dévouée, la Python 
        Software Foundation, créée en 2001. Ce langage a été baptisé ainsi en hommage à la 
        troupe de comiques les « Monty Python ».

"""
#
#
#   - Langage Interprete
"""

        Python est un langage de programmation interprété, c'est-à-dire que les instructions 
        que vous lui envoyez sont « transcrites » en langage machine au fur et à mesure de 
        leur lecture. D'autres langages (comme le C / C++) sont appelés « langages compilés » 
        car, avant de pouvoir les exécuter, un logiciel spécialisé se charge de transformer 
        le code du programme en langage machine. On appelle cette étape la « compilation ». À 
        chaque modification du code, il faut rappeler une étape de compilation.

        Les avantages d'un langage interprété sont la simplicité (on ne passe pas par une 
        étape de compilation avant d'exécuter son programme) et la portabilité (un langage tel 
        que Python est censé fonctionner aussi bien sous Windows que sous Linux ou Mac OS, et 
        on ne devrait avoir à effectuer aucun changement dans le code pour le passer d'un 
        système à l'autre). Cela ne veut pas dire que les langages compilés ne sont pas 
        portables. Mais on doit utiliser des compilateurs différents et, d'un système à 
        l'autre, certaines instructions ne sont pas compatibles, voire se comportent 
        différemment.

        En contrepartie, un langage compilé se révélera bien plus rapide qu'un langage 
        interprété (la traduction à la volée de votre programme ralentit l'exécution), bien 
        que cette différence tende à se faire de moins en moins sentir au fil des 
        améliorations. De plus, il faudra installer Python sur le système d'exploitation que 
        vous utilisez pour que l'ordinateur puisse comprendre votre code.

"""
#
#
#   - Versions
"""

        Lors de la création de la Python Software Foundation, en 2001, et durant les années 
        qui ont suivi, le langage Python est passé par une suite de versions que l'on a 
        englobées dans l'appellation Python 2.x (2.3, 2.5, 2.6…). Depuis le 13 février 2009, 
        la version 3.0.1 est disponible. Cette version casse la compatibilité ascendante qui 
        prévalait lors des dernières versions.

        Quand un langage de programmation est mis à jour, les développeurs se gardent bien de 
        supprimer ou de trop modifier d'anciennes fonctionnalités. L'intérêt est qu'un 
        programme qui fonctionne sous une certaine version marchera toujours avec la nouvelle 
        version en date. Cependant, la Python Software Foundation, observant un bon nombre de 
        fonctionnalités obsolètes a décidé de nettoyer tout le projet. Un programme qui 
        tourne à la perfection sous Python 2.x devra donc être mis à jour un minimum pour 
        fonctionner de nouveau sous Python 3. Certaines des fonctionnalités de Python 3 ne 
        seront pas accessibles (ou n'auront pas le même nom) dans les anciennes versions.

"""
#
#
#
#
#
#
#
#
#__CONSOLE___________________________________________________________
#
#
#   - Installation
"""

        sudo apt update
        sudo apt install python3-minimal

        OR

        sudo add-apt-repository ppa:jonathonf/python-3.8
        sudo apt update
        sudo apt-get install python3.8

"""
#
#
#   - Commandes UNIX
"""

        - python -V :
        Affiche la version de Python installée. Fonctionne aussi avec "python2 -V", "python3 -V" ou encore "python3.8 -V"


        - python :
        Démarre l'interpréteur Python. Fonctionne aussi avec "python2", "python3" ou encore "python3.8"


        - ./nomDuProgramme.py :
        Exécute le programme "nomDuProgramme.py". Ne pas oublier d'attribuer les droits d'éxecution ainsi que les en-têtes "#!/usr/bin/python3.8" et "# -*-coding:Utf-8 -*" au fichier.

"""
#
#
#   - Commandes Python
"""
        - ctrl + D :
        Quitte l'interpréteur Python

        - ctrl + L :
        Nettoie la console (comme "clear" dans UNIX)
"""
#
#
#
#
#
#
#
#
#__VARIABLES_________________________________________________________
#	
#
#	- Mots-clés réservés
"""

and, as, assert, break, class, continue, def, del, elif, else, except,
false,finally, for, from, global, if, import, in, is, lambda, none,
nonlocal, not, or, pass, raise, return, true, try, while, with, yield

"""
#
#
#	- Booleans
#
variableBoolean_1 = True
variableBoolean_2 = False
#
#
#	- Nombres entiers et flottants
#
variableEntier = int()
variableEntier = 1
variableFloat = 1.25
#
#
#	- Chaîne de caractères
#
variableString = str()
variableString_1 = '''Exemple de chaîne'''
variableString_2 = """Exemple de chaîne"""
variableString_3 = 'Exemple de chaîne avec \''
variableString_4 = "Exemple de chaîne avec \""
#
varibaleString_5 = """Exemple de chaîne
					avec tab et saut à la ligne"""
#
#
prenom = "Paul"
nom = "Dupont"
age = 21
#
print("Je m'appelle {0} {1} et j'ai {2} ans.".format(prenom, nom, age))
#	Affiche "Je m'appelle Paul Dupont et j'ai 21 ans."
#
varibaleString_6 = "Je m'appelle {0} {1} et j'ai {2} ans.".format(prenom, nom, age)
#	"varibaleString_6" contient "Je m'appelle Paul Dupont et j'ai 21 ans."
#
#
date = "Dimanche 24 juillet 2011"
heure = "17:00"
#
print("Cela s'est produit le {}, à {}.".format(date, heure))
#	Affiche "Cela s'est produit le Dimanche 24 juillet 2011, à 17:00."
#
#
adresse = "{no_rue}, {nom_rue} {code_postal} {nom_ville} ({pays})".format(no_rue = 5, nom_rue = "rue des Postes", code_postal = 75003, nom_ville = "Paris", pays = "France")
print(adresse)
#	Affiche "5, rue des Postes 75003 Paris (France)"
#
#
prenom = "Paul"
message = "Bonjour"
print(message + " " + prenom)
#	Affiche "Bonjour Paul"
#
#
age = 21
message = "J'ai " + str(age) + " ans."
print(message)
#	Affiche "J'ai 21 ans."
#
#
chaine = "Hello World !"
#
print(chaine[0])
#	Affiche 'H'
#
print(chaine[2])
#	Affiche 'l'
#
print(chaine[-1])
#	Affiche '!'
#
#
chaine = "Salut"
print(len(chaine))
#	Taille de la chaine. Affiche '5'
#
#
presentation = "salut"
#
print(presentation[0:2])
#	Affiche 'sa'
#
print(presentation[2:len(presentation)])
#	Affiche 'lut'
#
print(presentation[:2])
#	Affiche 'sa'
#
print(presentation[2:])
#	Affiche 'lut'
#
#
#
#
#	- Caractères spéciaux
"""

\t                    Tab
\\                    Inserts a back slash
\'                    Inserts a single quote
\"                    Inserts a double quote
\n                    Inserts a ASCII Linefeed (a new line)

"""
#
#
#	- Affectations multiples
#
x = y = 3
#	x est égal à 3
#	y est égal à 3
#
#
#
#
#	- Permutation
#
a = 5
b = 32
a,b = b,a
#	a est maintenant égal à 32
#	b est maintenant égal à 5
#
#
#
#
#	- Instruction sur plusieures lignes
#
variableLigne = 1 + 4 - 3 * 19 + 33 - 45 * 2 + (8 - 3) \
-6 + 23.5
#
#
#
#
#	- Suppression
#
variable = 34
#
del variable
print(variable)
#	NameError: name 'variable' is not defined
#
#
#
#
#
#
#
#
#__LISTES ET TUPLES__________________________________________________
#
#
ma_liste = list()
print(ma_liste)
#	Affiche '[]'
#
ma_liste = []
print(ma_liste)
#	Affiche '[]'
#
ma_liste = [1, 2, 3, 4, 5]
print(ma_liste)
#	Affiche '[1, 2, 3, 4, 5]'
#
ma_liste = [1, 3.5, "une chaine", []]
print(ma_liste)
#	Affiche "[1, 3.5, 'une chaine', []]"
#
ma_liste = [
        [".", ".", ".", ".", "."],
        ["O", "O", "O", "O", "O"],
        [".", ".", ".", ".", "."],
    ]
#
#
liste_des_parametres = [1, 4, 9, 16, 25, 36]
print(*liste_des_parametres)
#   Affiche "1 4 9 16 25 36"
#
#
ma_liste = ['c', 'f', 'm']
#
print(ma_liste[0])
#	Affiche 'c'
#
print(ma_liste[2])
#	Affiche 'm'
#
ma_liste[1] = 'Z'
print(ma_liste)
#	Affiche "['c', 'Z', 'm']"
#
ma_liste = [1, 2, 3]
ma_liste.append(56)
print(ma_liste)
#	Affiche "[1, 2, 3, 56]"
#
#
liste1 = [1, 5.5, 18]
liste2 = liste1.append(-15)
#
print(liste1)
#	Affiche "[1, 5.5, 18, -15]"
#
print(liste2)
#	Affiche 'None'
#	!!! Il faut bien faire la différence entre les méthodes de chaînes, 
#	où l'objet d'origine n'est jamais modifié et qui renvoient un 
#	nouvel objet, et les méthodes de listes, qui ne renvoient rien 
#	mais modifient l'objet d'origine. !!!
#
#
ma_liste = ['a', 'b', 'd', 'e']
ma_liste.insert(2, 'c')
print(ma_liste)
#	Affiche "['a', 'b', 'c', 'd', 'e']"
#
#
liste_origine = [0, 1, 2, 3, 4, 5]
print([nb * nb for nb in liste_origine])
#   Affiche "[0, 1, 4, 9, 16, 25]"
#
liste_origine = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([nb for nb in liste_origine if nb % 2 == 0])
#   Affiche "[2, 4, 6, 8, 10]"
#   Syntaxe: nouvelle_squence = ['manipulationElement' for 'element' in 'ancienne_squence' if 'condition']
#
#
qtt_a_retirer = 7
fruits_stockes = [15, 3, 18, 21]
#
print([nb_fruits - qtt_a_retirer for nb_fruits in fruits_stockes if nb_fruits > qtt_a_retirer])
#   Affiche "[8, 11, 14]"
#
#
#
#
#	- Concaténation
#
ma_liste1 = [3, 4, 5]
ma_liste2 = [8, 9, 10]
#
ma_liste1.extend(ma_liste2)
print(ma_liste1)
#	Affiche "[3, 4, 5, 8, 9, 10]"
#
#
ma_liste1 = [3, 4, 5]
ma_liste2 = [8, 9, 10]
#
print(ma_liste1 + ma_liste2)
#	Affiche "[3, 4, 5, 8, 9, 10]"
#
#
ma_liste1 = [3, 4, 5]
ma_liste2 = [8, 9, 10]
#
ma_liste1 += ma_liste2
print(ma_liste1)
#	Affiche "[3, 4, 5, 8, 9, 10]"
#
#
#
#
#	- Suppression
#
ma_liste = [-5, -2, 1, 4, 7, 10]
#
del ma_liste[0]
print(ma_liste)
#	Affiche "[-2, 1, 4, 7, 10]"
#
del ma_liste[2]
print(ma_liste)
#	Affiche "[-2, 1, 7, 10]"
#
#
ma_liste = [31, 32, 33, 34, 35]
ma_liste.remove(32)
print(ma_liste)
#	Affiche "[31, 33, 34, 35]"
#	!!! La méthode remove ne retire que la première occurrence de la valeur trouvée dans la liste !!!
#
#
#
#
#	- Tuples
#
tuple_vide = ()
tuple_non_vide = (1,)
tuple_non_vide = 1,
tuple_avec_plusieurs_valeurs = (1, 2, 5)
#
varTuple = ("a", "b", "c", "d", "e")
varList = list(varTuple)
print(varList)
#   Affiche "['a', 'b', 'c', 'd', 'e']"
#
#
#
#
#
#
#
#
#__INSTRUCTIONS CONDITIONNELLES______________________________________
#
#
"""
	<	Strictement inférieur à

	>	Strictement supérieur à

	<=	Inférieur ou égal à

	>=	Supérieur ou égal à

	==	Égal à

	!=	Différent de

	is 

	is not
"""
#
#
a = 5
#
if a > 0:
	print("a est supérieur à 0.")

#	Affiche "a est supérieur à 0" !!! Ne pas oublier d'utiliser une tabulation à l'intérieur du bloc et de sauter une ligne pour le fermer !!!
#
#
a = 5
b = 8
#
if a > 0:
    b += 1
    print("a = ",a,"et b = ",b)

#	Affiche "a = 5 et b = 9"
#
#
a = 5
#
if a > 0:
	print("a est supérieur à 0.")
else:
	print("a est inférieur ou égal à 0.")

#	Affiche "a est supérieur à 0."
#
#
a = 5
#
if a > 0:
	print("a est positif.")
elif a < 0:
	print("a est négatif.")
else:
	print("a est nul.")
#
#	Affiche "a est positif."
#
#
a = 5
#
if a >= 2 and a <= 8:
    print("a est dans l'intervalle.")
else:
    print("a n'est pas dans l'intervalle.")

#	Affiche "a est dans l'intervalle."
#
#
a = 5
#
if a < 2 or a > 8:
    print("a n'est pas dans l'intervalle.")
else:
    print("a est dans l'intervalle.")

#	Affiche "a est dans l'intervalle."
#
#
variableBoolean = False
#
if variableBoolean is not True:
	print("variableBoolean est False.")

#	Affiche "variableBoolean est False."
#
#
#
#
#
#
#
#
#__BOUCLES___________________________________________________________
#
#
#	- While
#
i = 0
#
while i < 10:
    print(i)
    i += 1

#
#
while 1: # 1 est toujours vrai -> boucle infinie
    lettre = input("Tapez 'q' pour quitter : ")
    if lettre == "q":
        print("Fin de la boucle")
        break

#
#
i = 1
#
while i < 20: # Tant que i est inférieure à 20
    if i % 3 == 0:
        i += 4 # On ajoute 4 à i
        print("On incrémente i de 4. i est maintenant égale à", i)
        continue # On retourne au while sans exécuter les autres lignes
    print("La variable i =", i)
    i += 1 # Dans le cas classique on ajoute juste 1 à i

#
#
chaine = "Salut"
i = 0
#
while i < len(chaine):
    print(chaine[i])
    i += 1

#	Attention! Il est impossible de changer les lettres de la chaîne en utilisant les indices (TypeError: 'str' object does not support item assignment)
#
#
#
#
#	- For
#
chaine = "Hello World !"
#
for lettre in chaine:
    print(lettre)

#
#
chaine = "Hello World !"
#
for lettre in chaine:
    if lettre in "AEIOUYaeiouy":
        print(lettre)
    else:
        print("*")

#	Affiche les voyelles de la chaine de caractères "chaine"
#
#
#
#
#	- Listes
#
ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
i = 0
#
while i < len(ma_liste):
	print(ma_liste[i])
	i += 1

#
for element in ma_liste:
	print(element)

#
for i, element in enumerate(ma_liste):
	print("À l'indice {} se trouve {}.".format(i, element))

#
#
for element in enumerate(ma_liste):
	print(element)

#	Affiche des tuples qui contiennent deux éléments: d'abord l'indice, puis l'objet se trouvant à cet indice (0, 'a') (1, 'b') ...
#	Les tuples sont des séquences, assez semblables aux listes, sauf qu'on ne peut modifier un tuple après qu'il ait été créé. Cela 
#	signifie qu'on définit le contenu d'un tuple (les objets qu'il doit contenir) lors de sa création, mais qu'on ne peut en ajouter 
#	ou en retirer par la suite.
#
#
#
#
autre_liste = [
				[1, 'a'],
				[4, 'd'],
				[7, 'g'],
				[26, 'z'],
	]
#
for nb, lettre in autre_liste:
	print("La lettre {} est la {}e de l'alphabet.".format(lettre, nb))

#
#
#
#
#
#
#
#
#__FONCTIONS_________________________________________________________
#
#
def table(nb, max):
#
    i = 0
#
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1

#
#
def table(nb, max=10):
#
    i = 0
#
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1

#	Ici, si l'on décide de ne pas préciser le deuxième paramêtre lors de l'appel de la fonction, celui-ci sera égal à 0 par défaut
#
#
#
#
def fonc(a=1, b=2, c=3, d=4, e=5):
    print("a =", a, "b =", b, "c =", c, "d =", d, "e =", e)
#
fonc()
#	Affiche "a = 1 b = 2 c = 3 d = 4 e = 5"
#
fonc(4)
#	Affiche "a = 4 b = 2 c = 3 d = 4 e = 5"
#
fonc(3,5)
#	Affiche "a = 3 b = 5 c = 3 d = 4 e = 5"
#
fonc(b=8, d=5)
#	Affiche "a = 1 b = 8 c = 3 d = 5 e = 5"
#
fonc(b=35, c=48, a=4, e=9)
#	Affiche "a = 4 b = 35 c = 48 d = 4 e = 9"
#
#
#
#
def functionCarre(valeur):
    return valeur * valeur

print(functionCarre(5))
#	Affiche "25"
#
#
#
#
def decomposer(entier, divise_par):
    p_e = entier // divise_par
    rst = entier % divise_par
    return p_e, rst

#	Cette fonction renvoie un tuple
#
partie_entiere, reste = decomposer(20, 3)
#
print(partie_entiere)
#	Affiche '6'
#
print(reste)
#	Affiche '2'
#
#
#
#
#   - Paramêtres multiples
#
def param_multiples(*parametres):
    parametres = list(parametres)
    return parametres

#
print(param_multiples("f", "b", 45))
#   Affiche "['f', 'b', 45]"
#
#
def fonction_inconnue(*parametres):
    print("J'ai reçu : {}.".format(parametres))

#
fonction_inconnue()
#   Affiche "J'ai reçu : ()."
#
fonction_inconnue(33)
#   Affiche "J'ai reçu : (33,)."
#
fonction_inconnue('a', 'e', 'f')
#   Affiche "J'ai reçu : ('a', 'e', 'f')."
#
var = 3.5
fonction_inconnue(var, [4], "...")
#   Affiche "J'ai reçu : (3.5, [4], '...')."
#
#   Le fait de préciser une étoile * devant le nom du paramètre fait 
#   que Python va placer tous les paramètres de la fonction dans un 
#   tuple, que l'on peut ensuite traiter comme on le souhaite.
#
#   Si on définit une liste variable de paramètres, elle doit se trouver 
#   après la liste des paramètres standard. En revanche, si l'on 
#   souhaite avoir des paramètres nommés, il faut les mettre après 
#   cette liste. 
#
#
#
#
#   - Fonction Lambda
#
f = lambda x: x * x
#
print(f(4))
#	Affiche "16"
#
#
#
#
#	- Print
#
print("Hello World !")
#	Affiche "Hello World !"
#
#
a = 3
print(a)
#	Affiche "3"
#
#
from platform import python_version
print("Python " + python_version())
#	Affiche la version courante de Python
#
#
import datetime
print("Current date and time : ")
print(datetime.datetime.now(), "\n")
#	Affiche la date et l'heure courante
#
#
import datetime
now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"), "\n")
#	Affiche la date et l'heure courante (formaté)
#
#
#
#
#	- Types
#
a = 3
print(type(a))
#	Affiche "<class 'int'>"
#
#
print(type(3.4))
#	Affiche "<class 'float'>"
#
#
print(type("string"))
#	Affiche "<class 'str'>"
#
#
#
#
#	- Doctstring
#
def docstringFunction():
    """Voici le docstring de la fonction"""
    print("Hello World !")
 
help(docstringFunction)
#	Affiche "Voici le docstring de la fonction" dans une interface ("q" pour quitter)
#
#
#
#
#	- Str
#
chaine = "CHAINE"
print(chaine.lower())
#
#
chaine = str()
#
while chaine.lower() != "q":
    print("Tapez 'Q' pour quitter...")
    chaine = input()
#
#
minuscules = "une chaine en minuscules"
#
minuscules.upper()									# Mettre en majuscules
minuscules.capitalize()								# La première lettre en majuscule
#
espaces = "   une  chaine avec  des espaces   "
espaces.strip()										# On retire les espaces au début et à la fin de la chaîne
#
titre = "introduction"
titre.upper().center(20)							#'    INTRODUCTION    '
#
#
ma_chaine = "Bonjour à tous"
print(ma_chaine.split(" "))
#   Affiche '['Bonjour', 'à', 'tous']'
#
#
ma_liste = ['Bonjour', 'à', 'tous']
print(" ".join(ma_liste))
#   Affiche 'Bonjour à tous'
#
#
#
#
#
#
#
#
#__MODULES & PACKAGES________________________________________________
#
#
import math
print(math.sqrt(16))
#	Affiche "4.0"
#
#
import math
help(math)
#	Affiche la docstring du module "math" ("Entrée" pour avancer d'une ligne, "Espace" pour avancer d'une page et "q" pour quitter)
#
#
import math as mathematiques
print(mathematiques.sqrt(25))
#	Affiche "5.0"
#
#
from math import sqrt
print(sqrt(16))
#	Affiche "4.0"
#
#
from math import *
print(sqrt(4))
#	Affiche "2.0"
#
#
#
#
if __name__ == "__main__":
    print("Hello World !")

#	La variable "__name__" est une variable qui existe dès le lancement de l'interpréteur. Si elle vaut "__main__", cela veut dire que le 
#	fichier appelé est le fichier exécuté. Autrement dit, si "__name__" vaut "__main__", vous pouvez mettre un code qui sera exécuté si 
#	le fichier est lancé directement comme un exécutable (et non importé dans un autre fichier).
#	=> Voir dossier "OpenClassrooms/exempleModules/"
#
#
#
#
#
#
#
#
#__EXCEPTIONS & ASSERTIONS___________________________________________
#
#
annee = input()
#
try:
    annee = int(annee)
except:
    print("Erreur lors de la conversion de l'année.")
#
#
#
#
try:
    resultat = numerateur / denominateur
except NameError:
    print("La variable numerateur ou denominateur n'a pas été définie.")
except TypeError:
    print("La variable numerateur ou denominateur possède un type incompatible avec la division.")
except ZeroDivisionError:
    print("La variable denominateur est égale à 0.")
#
#
#
#
try:
    # Bloc de test
except type_de_l_exception as exception_retournee:
    print("Voici l'erreur :", exception_retournee)
#
#
#
#
try:
    resultat = numerateur / denominateur
except NameError:
    print("La variable numerateur ou denominateur n'a pas été définie.")
except TypeError:
    print("La variable numerateur ou denominateur possède un type incompatible avec la division.")
except ZeroDivisionError:
    print("La variable denominateur est égale à 0.")
else:
    print("Le résultat obtenu est", resultat)
#
#
#
#
try:
    # Test d'instruction(s)
except type_de_l_exception:
    # Traitement en cas d'erreur
finally:
    # Instruction(s) exécutée(s) qu'il y ait eu des erreurs ou non (même si on met un "return" dans l'une des exceptions)
#
#
#
#
annee = input("Saisissez une année supérieure à 0 :")
#
try:
    annee = int(annee)
    assert annee > 0
except ValueError:
    print("Vous n'avez pas saisi un nombre.")
except AssertionError:
    print("L'année saisie est inférieure ou égale à 0.")
#
#
#
#
annee = input()
#
try:
    annee = int(annee)
    if annee <= 0:
        raise ValueError("l'année saisie est négative ou nulle")
except ValueError:
    print("La valeur saisie est invalide (l'année est peut-être négative).")