"""
Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out, because 9^2 is 81 and 1^2 is 1.

Note: The function accepts an integer and returns an integer
"""

def main():
    print(square_digits(inputFunction()))
    print(square_digits_solution(inputFunction()))
#
#
def inputFunction():
    finDeProgramme = False
    while not finDeProgramme:
        print("Indiquez un nombre entier non négatif: ")
        valueInput = input()
        if valueInput.isnumeric():
            intInput = int(valueInput)
            return intInput
        else:
            print("La valeur indiquée n'est pas un entier positif")
#
#
def square_digits(num):
    numInputString = str(num)
    numOutputList = []
    numOutputString = ""
    i = 0
    while i < len(numInputString):
        numOutputList.append(str(int(numInputString[i])*int(numInputString[i])))
        i += 1
    i = 0
    while i < len(numOutputList):
        numOutputString += numOutputList[i]
        i += 1
    num = int(numOutputString)
    return num
#
#
def square_digits_solution(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)
#
#
if __name__ == "__main__":
    main()
#