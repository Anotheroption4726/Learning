#!/usr/bin/python3.8
# -*-coding:Utf-8 -*
#
inventaire = [
    ("pommes", 22),
    ("melons", 4),
    ("poires", 18),
    ("fraises", 76),
    ("prunes", 51),
]
#
#
inventaireList = []
#
for element in inventaire:
    inventaireList.append(list(reversed(element)))

inventaireList.sort(reverse=True)
#
#
#print(inventaireList)
#
#
#
#
#   - CORRECTION:
#
print(inventaire)
inventaire_inverse = [(qtt, nom_fruit) for nom_fruit, qtt in inventaire]
inventaire = [(nom_fruit, qtt) for qtt, nom_fruit in sorted(inventaire_inverse, reverse=True)]
print(inventaire)