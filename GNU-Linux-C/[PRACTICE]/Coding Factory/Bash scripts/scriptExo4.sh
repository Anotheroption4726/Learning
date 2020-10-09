#!/bin/bash

if [ $2 = "+r" ]
  then
    chmod +r $1/*.$3
fi

if [ $2 = "-r" ]
  then
    chmod -r $1/*.$3
fi

# ./scriptExo4.sh txtTest -r txt
# change les droits de lecture de tous les fichiers du dossier txtTest ac l'extension .txt
