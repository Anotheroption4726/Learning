"""
4. Write a Python program which accepts the radius of a circle from the user and compute the area.
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""

from math import pi
#
#
def main():
    finDeProgramme = False
    while not finDeProgramme:
        print("Indiquez une longueur de rayon: ")
        rayonInput = input()
        if rayonInput.isnumeric() or isFloat(rayonInput) == True:
            rayonNombre = float(rayonInput)
            print(rayonNombre*rayonNombre*pi)
            finDeProgramme = True
        else:
            print("Erreur")
#
#
def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
#
#
if __name__ == "__main__":
    main()

#