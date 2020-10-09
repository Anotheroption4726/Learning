#!/usr/bin/python3.8
# -*-coding:Utf-8 -*
#
print("Indiquez une année:")
userInput = input()
#
try:
	userInput = int(userInput)
	assert userInput > 0
except ValueError:
	print("Ceci n'est pas une année")
except AssertionError:
	print("l'année doit être un nombre positif supèrieur à 0")
else:
	if (userInput % 4 == 0 and userInput % 100 != 0) or userInput % 400 == 0:
		print("Ceci est bien une année bissextile")
	else:
		print("Ceci n'est pas une année bissextile")