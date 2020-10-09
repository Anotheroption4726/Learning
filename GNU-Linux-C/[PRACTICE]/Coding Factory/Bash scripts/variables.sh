#!/bin/bash

# Ne pas oublier de mettre un parametre lors de l'appel sinon ça marche pas

message='Bonjour tout le monde'
echo $message

read -p 'Entrez un nom puis un prénom: ' nom prenom
echo "Bonjour $prenom $nom !"

EDITOR=nano

echo "Editeur par défaut: $EDITOR"

if [ $prenom = "Adrien" ]
  then
    echo "Salut Adrien !"
  else
    echo "Salut inconnu"
fi

if [ $1 = "Bruno" ]
  then
    echo "Salut Bruno !"
  else
    echo "Je ne te connais pas"
fi

while [ -z $reponse ] || [ $reponse != "oui" ]
do
  read -p 'Dites oui : ' reponse
done
