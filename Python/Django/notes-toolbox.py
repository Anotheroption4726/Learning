#__INTRODUCTION______________________________________________________
#
#
"""

	- Framework

		Django est un framework web écrit en Python, qui se veut 
		complet tout en facilitant la création d’applications web 
		riches.  Ce n’est pas le seul dans sa catégorie, nous pouvons 
		compter d’autres frameworks Python du même genre comme 
		web2py, TurboGears, Tornado ou encore Flask. Il a cependant 
		le mérite d’être le plus exhaustif, d’automatiser un bon 
		nombre de tâches et de disposer d’une très grande communauté.


	- Histoire

		Django est créé en 2003 dans une agence de presse, Lawrence 
		Journal-World, qui devait développer des sites web complets 
		dans des laps de temps très courts (d’où l’idée du 
		framework). En 2005, cette agence décide de proposer Django 
		au grand public, le jugeant assez mature pour être réutilisé 
		n’importe où. Trois ans plus tard, la fondation Django 
		Software est créée par les fondateurs du framework afin de 
		pouvoir maintenir celui-ci et la communauté très active qui 
		l’entoure. Aujourd’hui, Django est utilisé par des sociétés 
		du monde entier, telles qu’Instagram, Pinterest, et même la 
		NASA.


	- Don't repeat yourself

		Si Django est devenu très populaire, c’est notamment grâce à 
		sa philosophie qui a su séduire de nombreux développeurs et 
		chefs de projets. En effet, le framework prône le principe du 
		« Don't repeat yourself ».

		Django applique sa philosophie de plusieurs manières. Par 
		exemple, l’interaction avec une base de données se fait via 
		un ensemble d’outils spécialisés et très pratiques. Il est 
		donc inutile de perdre son temps à écrire directement des 
		requêtes, car Django le fait automatiquement. De plus, le 
		framework inclut des fonctionnalités diverses comme un espace 
		membres, ou une bibliothèque permettant la traduction de 
		votre application web en plusieurs langues.


	- Documentation

		https://docs.djangoproject.com/en/3.0/


	- Packages

		https://djangopackages.org/


	- Snippets

		https://djangosnippets.org/

"""
#
#
#
#
#
#
#
#
#__ARCHITECTURE______________________________________________________
#
#
#	- MVC
#
#		Le modèle MVC s’agit d’un modèle distinguant plusieurs rôles 
#		précis d’une application, qui doivent être accomplis. Comme 
#		son nom l’indique, l’architecture (ou « patron ») 
#		Modèle-Vue-Contrôleur est composée de trois entités 
#		distinctes, chacune ayant son propre rôle à remplir.
#
#
#	- Modèle
#
#		Le modèle représente une information enregistrée quelque 
#		part, le plus souvent dans une base de données. Il permet 
#		d’accéder à l’information, de la modifier, d’en ajouter une 
#		nouvelle, de la mettre à jour, etc. Il s’agit d’une interface 
#		supplémentaire entre votre code et la base de données.
#
#
#	- Vue
#
#		La vue est, comme son nom l’indique, la visualisation de 
#		l’information. C’est la seule chose que l’utilisateur peut 
#		voir. Non seulement elle sert à présenter une donnée, mais 
#		elle permet aussi de recueillir une éventuelle action de 
#		l’utilisateur (un clic sur un lien, ou la soumission d’un 
#		formulaire, par exemple).
#
#
#	- Controlleur
#
#		Le contrôleur prend en charge tous les événements de 
#		l’utilisateur (accès à une page, soumission d’un formulaire, 
#		etc.). Il se charge, en fonction de la requête de 
#		l’utilisateur, de récupérer les données voulues dans les 
#		modèles. Après un éventuel traitement de ces données, il 
#		transmet celles-ci à la vue, afin qu’elle s’occupe de les 
#		afficher.
#
#
#	- MVT
#
#		Django gère lui-même la partie contrôleur (gestion des 
#		requêtes du client, des droits sur les actions…). Ainsi, nous 
#		parlons plutôt de framework utilisant l’architecture MVT : 
#		Modèle-Vue-Template. (Pas fini voir OpenClassrooms)
#
#
#
#
#
#
#
#
#__INSTALLATION______________________________________________________
#
#
#	- PIP
#
#		- sudo apt-get install python3-pip :
#		Installation de pip
#
#		- pip3 install Django==2.0 :
#		Installation de Django (version 2.0)
#
#
#	- Initialisation
#
#		- python3 -m django startproject nom_du_projet :
#		Initialisation d'un nouveau projet "nom_du_projet" dans le 
#		dossier courant
#
#
#	- Autres Commandes
#
#		- sudo apt remove python3-pip :
#		Désinstallation de pip
#
#		- pip3 install Django --upgrade :
#		Mise à jour de django
#
#		- sudo pip3 uninstall django :
#		Désinstallation de django
#
#
#
#
#
#
#
#
#__MANAGE.PY_________________________________________________________
#
#
#	- python3 manage.py help :
#	Affiche la liste des sous-commandes de la commande 'manage.py'.
#
#	- python3 manage.py runserver :
#	Démarre le projet (si l'on se trouve à sa racine). Accessible à 
#	l'adresse 'http://localhost:8000'
#
#	- python3 manage.py startapp blog :
#	Création d'une nouvelle application de type blog (le faire à la 
#	racine du projet?). Ne pas oublier de modifier la section 
#	'INSTALLED_APPS' dans le fichier 'settings.py'
#
#
#
#
#
#
#
#
#
#
#__SETTINGS.PY_________________________________________________________
#
#
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
#	La variable BASE_DIR est définie automatiquement selon le chemin 
#	du fichier courant (celui de 'settings.py').
#	La fonction dirname  est appelée deux fois, afin de remonter d’un 
#	dossier et ainsi d’avoir le chemin vers la racine du projet. La 
#	variable BASE_DIR peut être ainsi utilisée pour référencer des 
#	chemins vers des fichiers au sein du projet (ressources CSS, 
#	JavaScript, fichiers de test, base de données SQLite...).
#
#
DEBUG = True
#
#	Cette variable permet d’indiquer si le site web est en mode 
#	« debug ». Le mode de débogage affiche des informations pour 
#	déboguer les applications en cas d’erreur. Ces informations 
#	affichées peuvent contenir des données sensibles du fichier de 
#	configuration. Il ne faut donc jamais mettre DEBUG = True  en 
#	production.
#
#
ALLOWED_HOSTS = []
#
#	Cette variable permet de renseigner les noms de domaine et 
#	adresses IP par lesquels le projet est accessible lorsque le mode 
#	DEBUG est désactivé.
#
#
#
#
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
#
#	Liste toutes les applications qui ont été ajoutées au projet. Ne 
#	pas oublier de modifier cette partie à chaque fois qu'on en 
#	installe une nouvelle.
#
#
#
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
#
#	Configuration de la base de données. Déjà rempli pour gérer une 
#	base de données SQLite. L’avantage de SQLite comme gestionnaire 
#	de base de données est simple : il ne s’agit que d’un simple 
#	fichier. Il n’y a donc pas besoin d’installer un service à part, 
#	Python et Django se chargent de tout.
#
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
#			Backends disponibles : 'postgresql', 'mysql', 'sqlite3' 
#			et 'oracle'.
#
        'NAME': 'crepes_bretonnes',
#			Nom de la base de données
#
        'USER': '<nom d\'utilisateur>',
        'PASSWORD': '<mot de passe MySQL>',        
        'HOST': '127.0.0.1',
#			Utile si votre base de données est sur une autre machine
#
        'PORT': '3306',
#			... et si elle utilise un autre port que celui par défaut
#
    }
}
#
#	Si l'on souhaite utiliser une base de données MySQL, par exemple,
#	plus de champs sont nécessaires.
#
#
#
#
#
#
#
#
#__APPLICATION_________________________________________________________
#
#
#	- admin.py
#
#		Va permettre de définir ce que l'on veut afficher et 
#		modifier comme modèles (depuis l’administration de 
#		l’application).
#
#
#	- apps.py
#
#		Permet de configurer certaines propriétés de l’application, 
#		notamment son nom.
#
#
#	- models.py
#
#		Contient les modèles.
#
#
#	- tests.py
#
#		Permet la création de tests unitaires.
#
#
#	- views.py
#
#		Contient les vues.
#
#
#	- migrations
#
#		(A remplir)