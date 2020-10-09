#
# User Input
#
def string_ini():
    """ Initialiser une chaine
    Returns :
        chaine entrer par utilisateur
    """
    chaine = input("Veuillez entrer une chaine svp ==> ")

    return chaine


#
# Story 1 (Antoine)
#
def remove_char(char_string):
    """Enlever les "=" à la fin de la liste
    :param char_list: liste de carrarctères avec des '='
    :return: une liste de carractère sans '='
    """
    result = char_string
    for i in range(len(char_string) - 1, 0, -1):
        if char_string[i] == '=':
            result = result[0:len(result) - 1]
        else:
            break
    return result


#
# Story 2
#
def conv_string_toList(userInput):
    """This function converts a string variable into a list of characters
    Args:
        userinput: string variable given by input from the user
    Returns:
        list of strings each containing only one character from useriput
    """
    listChar = []
    i = 0
    while i < len(userInput):
        listChar.append(userInput[i])
        i += 1
    return listChar


#
# Story 3 (Thierry)
#
def conv_listString_toListInt_64(listString):
    """ Utiliser la base 64 pour convertir chaque caractère de la liste nombre
    args :
        Une liste de string
    Returns :
        Une liste de int (convertion avec la base 64
    """
    base64t = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
               "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
               "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+",
               "/"]
    tab = []
    i = 0
    while (i < len(listString)):
        j = 0
        while (j < len(base64t)):
            if (base64t[j] == listString[i]):
                tab.append(j)
            j = j + 1
        i = i + 1
    return tab


#
# Story 4
#
def conv_listInt_toListStringBin(int_string):
    """ Convertir une liste d'entiers dans leur representation binaire
    Args:
        binary_string: liste d'entiers
    Returns:
        liste de represenations binaires
    """
    liste_binaire = []
    for element in int_string:
        element = bin(element)
        element = element[2:]
        liste_binaire.append(element)
    return liste_binaire


#
# Story 4.5
#
def just_ListStringBin_toSixChar(listString):
    """ Cadrer les élémnts de la liste à droite sue huit caractères
    Args:
        liste de strings
    Returns:
        liste de string 6 chars
    """
    i = 0
    while i < len(listString):
        j = 0
        k = 6 - len(listString[i])
        while j < k:
            listString[i] = "0" + listString[i]
            j += 1

        i += 1
    return listString


#
# Story 5 old (Adrien)
#
def remove_char_toMultipleEightOld(listStringBin):
    """ Rendre le total de caractères compris dans une liste de caractères multiple de huit (en décrémentant par la gauche)
    Args:
        liste de strings contenant des nombres binaires
    Returns :
        liste de strings contenant des octets en binaire
    """
    totalchar = 0
    i = 0
    increment = False
    while i < len(listStringBin):
        j = 0

        while j < len(listStringBin[i]):
            totalchar += 1
            j += 1

        i += 1

    while totalchar % 8 != 0:
        if listStringBin[-1][0] == "0" and increment == False:
            listStringBin[-1] = listStringBin[-1][1:len(listStringBin[-1])]
            totalchar -= 1
        else:
            if len(listStringBin[-1]) < 6:
                listStringBin[-1] = "0" + listStringBin[-1]
            else:
                listStringBin.append("0")
            totalchar += 1
            increment = True

    return listStringBin


#
# Story 5 (Adrien)
#
def remove_char_toMultipleEight(listStringBin):
    """ Rendre le total de caractères compris dans une liste de caractères multiple de huit (en décrémentant par la gauche)
    Args:
        liste de strings contenant des nombres binaires
    Returns :
        liste de strings contenant des octets en binaire
    """
    totalchar = 0
    i = 0
    while i < len(listStringBin):
        j = 0

        while j < len(listStringBin[i]):
            totalchar += 1
            j += 1

        i += 1

    while totalchar % 8 != 0:
        listStringBin[-1] = listStringBin[-1][0 : len(listStringBin[-1]) - 1]
        totalchar -= 1

    return listStringBin


#
# Story 6 & 10
#
def conv_listString_toString(listString) :
    """This function converts a string list into a single string variable
    Args:
        list of strings each containing octets values
    Returns:
        A single string variable that regroups all of listStringBin' strings
    """
    stringText = ""
    i = 0
    while i < len(listString) :
        stringText += listString[i]
        i += 1
    return stringText


#
# Story 7
#
def conv_stringBin_toListStringOctet(stringBin) :
    """This function converts a string variable into a list of strings each containing 6 characters
    Args:
        string variable containing concatenated binary octets
    Returns:
        list of binary numbers grouped into strings of 6 characters
    """
    listStringBin = []
    i = 0
    while i < len(stringBin) - 1:
        sixChar = ""
        j = 0
        while j < 8 and j < len(stringBin) - i:
            sixChar += stringBin[i + j]
            j += 1
        listStringBin.append(sixChar)
        i += 8
    return listStringBin


#
# Story 8
#
def conv_list_StringOctet_toListInt(listString):
    """ Convertir en entier chaque éléments de la liste
    Args:
        liste de string sur 6 chars
    Returns:
        liste de int sur 6 chars
    """
    tab = [128, 64, 32, 16, 8, 4, 2, 1]
    tab2 = []
    compteur = 0
    i = 0
    while (i < len(listString)):
        test = listString[i]
        j = 0
        while (j < len(test)):
            compteur = compteur + (int(test[j]) * tab[j])
            j = j + 1
        tab2.append(compteur)
        compteur = 0
        i = i + 1
    return tab2


#
# Story 9 (Thierry)
#
def conv_listInt_toListString_32(listInt):
    """ Utiliser la base 64 pour convertir chaque caractère de la liste nombre
        args :
            Une liste de string
        Returns :
            Une liste de int (convertion avec la base 64
    """
    tab = []
    for element in listInt:
        element = chr(element)
        tab.append(element)
    return tab


#
# main
#
def main():
    """Main function
        The main function is automatically called if the script is
        directly given as first agument to Python interpreter
    """
    # QUJDRA==
    # VGhpZXJyeSBERUNLRVI=
    temp = string_ini()
    temp = remove_char(temp)
    temp = conv_string_toList(temp)
    temp = conv_listString_toListInt_64(temp)
    temp = conv_listInt_toListStringBin(temp)
    temp = just_ListStringBin_toSixChar(temp)
    temp = remove_char_toMultipleEight(temp)
    temp = conv_listString_toString(temp)
    temp = conv_stringBin_toListStringOctet(temp)
    temp = conv_list_StringOctet_toListInt(temp)
    temp = conv_listInt_toListString_32(temp)
    temp = conv_listString_toString(temp)
    print(temp)


if __name__ == "__main__":
    main()
