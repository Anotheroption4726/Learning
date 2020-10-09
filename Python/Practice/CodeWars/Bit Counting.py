"""
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary
representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
"""

def main():
    print(countBits(inputFunction()))
    print(countBitsSolution(inputFunction()))
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
def countBits(intInputValue):
    binaryNumber = bin(intInputValue)
    oneCounter = 0
    i = 2
    while i < len(binaryNumber):
        if int(binaryNumber[i]) == 1:
            oneCounter += 1
        i += 1
    return oneCounter
#
#
def countBitsSolution(intInputValue):
    return bin(intInputValue).count("1")
#
#
if __name__ == "__main__":
    main()
#
