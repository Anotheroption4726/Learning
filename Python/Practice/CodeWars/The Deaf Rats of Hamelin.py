"""
The Pied Piper has been enlisted to play his magical tune and coax all the rats out of town.

But some of the rats are deaf and are going the wrong way!

Kata Task
How many deaf rats are there?

Legend
P = The Pied Piper
O~ = Rat going left
~O = Rat going right

Example
ex1 ~O~O~O~O P has 0 deaf rats
ex2 P O~ O~ ~O O~ has 1 deaf rat
ex3 ~O~O~O~OP~O~OO~ has 2 deaf rats

"""

def main():
    piedPiperRatsInput_1 = "~O~O~O~O P"
    piedPiperRatsInput_2 = "P O~ O~ ~O O~"
    piedPiperRatsInput_3 = "~O~O~O~OP~O~OO~"
    print(count_deaf_rats(piedPiperRatsInput_1))
    print(count_deaf_rats(piedPiperRatsInput_2))
    print(count_deaf_rats(piedPiperRatsInput_3))
#
#
def count_deaf_rats(town):
    foundPiedPiper = False
    deafRatsCount = 0
    i = 0
    while i < len(town):
        if town[i] == " ":
            i += 1
        elif town[i] == "~":
            if foundPiedPiper:
                deafRatsCount += 1
            i += 2
        elif town[i] == "O":
            if not foundPiedPiper:
                deafRatsCount += 1
            i += 2
        else:
            foundPiedPiper = True
            i += 1
    return deafRatsCount
#
#
if __name__ == "__main__":
    main()
#