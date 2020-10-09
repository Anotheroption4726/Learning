#!/usr/bin/python3.8
# -*-coding:Utf-8 -*
#
from random import randrange
from math import ceil
#
#
gameOver = False
credits = 100
#
while gameOver is not True:
    print("Vous disposez de ", credits, " crédits")
    print("""Combien souaitez-vous miser? (tapez 'quitter' pour sortir)""")
    userInput = input()
    #
    if userInput.lower() == "quitter":
        gameOver = True
        continue
    #
    try:
        stake = int(userInput)
        assert stake > 0
        assert stake <= credits
    except ValueError:
        print(userInput, ": Ceci n'est pas un nombre.")
    except AssertionError:
        print(stake, ": Nombre de crédits non valable.")
    else:
        credits -= stake
        numberSelection = False
        selectedNumber = int()
        #
        while numberSelection is not True:
            print("Choisissez un nombre entre 0 et 49")
            userInput = input()
            #
            try:
                selectedNumber = int(userInput)
                assert selectedNumber >= 0
                assert selectedNumber < 50
            except ValueError:
                print(userInput, ": Ceci n'est pas un nombre.")
            except AssertionError:
                print(stake, ": Le nombre doit être compris entre 0 et 49.")
            else:
                numberSelection = True
        #
        randomNumber = randrange(50)
        print("Le résultat est: ", randomNumber)
        #
        if selectedNumber == randomNumber:
            print("Jackpot! Vous récupérez trois fois la mise.")
            credits += 3 * stake
        elif randomNumber % 2 == 0 and selectedNumber % 2 == 0:
            print("Nombre pair, vous récupérez la moitié de la mise.")
            credits += ceil(stake / 2)
        elif randomNumber % 2 != 0 and selectedNumber % 2 != 0:
            print("Nombre impair, vous récupérez la moitié de la mise.")
            credits += ceil(stake / 2)
        else:
            print("Dommage, vous avez perdu.")
    #
    if credits == 0:
        print("Vous n'avez plus de crédits. Merci d'avoir joué.")
        gameOver = True