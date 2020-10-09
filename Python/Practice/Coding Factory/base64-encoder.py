#
# Story 1 (Thierry)
#
def string_ini():
    """ Initialiser une chaine
    Returns :
        chaine entrer par utilisateur
    """
    chaine = input("Veuillez entrer une chaine svp ==> ")
    return chaine


#
# Story 2 (Adrien)
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
# Story 3 (Antoine)
#
def conv_listString_toListInt(char_string):
    """ Convertir une liste de chaines en une liste d'entiers
    Args:
        char_string:liste de chaines
    Returns:
        liste d'entiers
    """
    int_string = []
    for element in char_string:
        element = ord(element)
        int_string.append(element)
    return int_string


#
# Story 4 (Antoine)
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
# Story 5 (Thierry & Adrien)
#
def just_ListStringBin_toEightChar(listString):
    """ Cadrer les élémnts de la liste à droite sue huit caractères
    Args:
        liste de strings
    Returns:
        liste de string 8 chars
    """
    i = 0
    while i < len(listString) :
        j = 0
        k = 8 - len(listString[i])
        while j < k :
            listString[i] = "0" + listString[i]
            j += 1

        i += 1
    return listString


#
# Story 6 & 11 (Adrien)
#
def conv_listString_toString(listString):
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
# Story 7 (Adrien)
#
def conv_stringBin_toListStringBin(stringBin):
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
        while j < 6 and j < len(stringBin) - i:
            sixChar += stringBin[i + j]
            j += 1
        listStringBin.append(sixChar)
        i += 6
    return listStringBin


#
# Story 8 (Antoine)
#
def just_ListStringBin_toSixChar(list_string_bin):
    """ Verifie et ajuste le nombre de 0 pour qu'il soit fixé a 6
        Args:
            list_string_bin: liste de chaines de nombres binaires
        Returns:
            liste de chaines represenations binaires fixé à 6
        """
    tmp = len(list_string_bin[-1])

    while tmp < 6:
        list_string_bin[-1] += '0'
        tmp += 1
    return list_string_bin


#
# Story 9 (Thierry)
#
def conv_list_StringBin_toListInt(listString):
    """ Convertir en entier chaque éléments de la liste
    Args:
        liste de string sur 6 chars
    Returns:
        liste de int sur 6 chars
    """
    tab = [32, 16, 8, 4, 2, 1]
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
# Story 10 (Thierry)
#
def conv_listInt_toListString(listInt):
    """ Convertir chaque éléments de la liste en base 64
    Args:
        liste de Int
    Returns:
        liste Base 64
    """
    base64t = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
               "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
               "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+",
               "/"]
    tab = []
    i = 0
    while (i < len(listInt)):
        tab.append(base64t[listInt[i]])
        i = i + 1
    return tab


#
# Story 12 (Adrien)
#
def just_string_toMultipleFour(stringText):
    """This function justifies a string variable so it has a length multiple of 4
    Args:
        String variable containing encoded text
    Returns:
        String variable containing encoded text with a length that is multiple of 4
    """
    justStringText = stringText
    completed = False
    #
    while completed is False:
        if len(justStringText) % 4 == 0:
            completed = True
        else:
            justStringText += "="

    return justStringText


#
# Main (Thierry)
#
def main():
    """ Main function
        The main function is automatically called if the script is
        directly given as first agument to Python interpreter
    """
    temp = string_ini()
    temp = conv_string_toList(temp)
    temp = conv_listString_toListInt(temp)
    temp = conv_listInt_toListStringBin(temp)
    temp = just_ListStringBin_toEightChar(temp)
    temp = conv_listString_toString(temp)
    temp = conv_stringBin_toListStringBin(temp)
    temp = just_ListStringBin_toSixChar(temp)
    temp = conv_list_StringBin_toListInt(temp)
    temp = conv_listInt_toListString(temp)
    temp = conv_listString_toString(temp)
    print(just_string_toMultipleFour(temp))


if __name__ == "__main__":
    main()
