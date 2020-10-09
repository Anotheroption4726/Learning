#!/bin/bash

for fichier in $*
do
  if [ -f $fichier ]
    then
      mv $fichier $fichier-old
  fi
done
