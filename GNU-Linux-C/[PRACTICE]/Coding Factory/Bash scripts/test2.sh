#!/bin/bash
exec < $1 # redirection de l'entrée standard
while read ligne ; do
  echo ">$ligne"
done
