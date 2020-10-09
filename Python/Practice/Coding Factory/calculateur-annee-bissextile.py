#
# Variable de fin du programme
#
fin = False
#
#
#
while not fin:
    print("Indiquez une année: ")
    texte = input()
    #
    # On regarde si texte correspond à "fin"
    #
    if texte == "fin":
        print("programme fini")
        fin = True
    #
    # On regarde si texte correspond à un nombre
    #
    elif texte.isnumeric():
        annee = int(texte)
        #
        if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
            #print(annee)
            print(f"{annee} est bissextile")
        #
        else:
            print(annee)
            print(f"{annee} n'est pas bissextile")
    #
    # Si aucune condition n'a été remplie, on renvoie une erreur
    #
    else:
        print("Erreur")

#
#
#
