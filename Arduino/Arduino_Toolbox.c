/*
CONSOLE/MONITEUR SERIE
*/

Serial.begin(9600);

/*
Le 9600 dans les parenthèse de l'initialisation correspond à un nombre de caractères par seconde qu'on appelle des bauds.
L'Arduino peut donc envoyer un maximum de 9600 caractères par seconde à l'ordinateur dans cette configuration.
Ne pas confondre avec l'unité bps, qui veut dire bits par seconde. Un caractère pour l'Arduino c'est 8 bits.

La vitesse de communication entre Arduino et l’ordinateur peut prendre d’autres valeurs que 9600 bauds. 
Vous trouverez ces valeurs sur le site officiel avec ce lien: https://www.arduino.cc/reference/en/language/functions/communication/serial/begin/
9600 est la valeur généralement utilisée.

Le moniteur série utilise les connexions 0 et 1 de l'Arduino (0 pour la diode RX et 1 pour la diode TX lors d'une utilisation en communication). 
Donc si on utilise le port série, il ne faut pas utiliser les connexions 0 et 1 pour d'autres choses dans votre projet.
*/


void setup()
{
    Serial.begin(9600);// initialisation de la communication
    Serial.println("Communication initialisée");// envoi d'un message
}
void loop()
{
    Serial.println("Je suis dans la boucle !");//envoi d'un autre message
}




/*
BUILT-IN DIODES

LED: "Light-Emitting Diode"

La LED ON est verte quand l'Arduino est sous tension.
Les LEDs TX et RX clignotent quand l'Arduino reçoit ou envoie des informations.
La LED L clignote si on appuie sur le bouton reset, sinon elle ne fait rien tant qu'on ne lui a pas dit.

La force de l'Arduino (entre autres)  est d'envoyer du courant, ou non, par les connexions numérotées de 0 à 13. Et la diode L s'allume quand on dit à l'Arduino d'envoyer du courant dans la connexion 13.
Nous appellerons "pin", les connexions disponibles sur l'Arduino. Le pin 13 correspondra donc à la connexion 13 (ou broche 13, ou trou 13).
*/




void setup()
{
	pinMode(13,OUTPUT);
}
//	Signale à l’Arduino que la connexion 13 doit pouvoir envoyer du courant


digitalWrite(13,HIGH);
//	Demande à l’Arduino d’envoyer du courant dans la connexion 13


void loop()
{
  digitalWrite(13,HIGH);
  delay (1000);
  digitalWrite(13,LOW);
  delay (1000);
}
//	Fait clignoter la LED 13 toutes les 1000 millisecondes (soit 1 seconde)




/*
FREQUENCE ET PERIODE

Quand on se penche un peu sur la documentation de l'Arduino, on peut lire :

"Chaque module possède au moins un régulateur linéaire 5 V et un oscillateur à quartz 16 MHz (ou un résonateur céramique dans certains modèles)."

Ça veut dire que d'une part, la tension de sortie au niveau des connexions est de cinq volts (nous y reviendrons plus tard) et que notre processeur est cadencé (j'adore ce mot) à 16 MHz (seize méga hertz)
*/

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  unsigned long tempsFin; //variable pour noter le temps final
  unsigned long  tempsDepart=micros(); //variable du temps de départ initialisée au temps actuel
  //bloc à tester
  tempsFin=micros(); //on récupère à nouveau le temps actuel
  Serial.println(tempsFin-tempsDepart); // on affiche la différence en microsecondes
}