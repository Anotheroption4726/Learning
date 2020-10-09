"""
Amidakuji ( https://en.wikipedia.org/wiki/Ghost_Leg ) is a method of lottery designed to create random pairings between two sets comprised of an equal number of elements.

Your task is to write a function amidakuji that returns the final positions of each element. Note that the elements are an ascending sequence of consecutive integers starting with 0 (from left to right).

Input
Your function will receive an array/list of equal-length strings consisting of 0 and 1 characters; this represents the "ladder" structure. The 1s represent the rungs of the ladder and the 0s represent empty space.

Each element begins at the top of its corresponding vertical rail, as illustrated in the diagram below.
During the descent of the ladder, whenever a vertical rail intersects a horizontal rung, it swaps values with the adjacent connecting vertical rail.

Output
Your function should return an array of integers, with each integer in its final position.

Other Technical Details
No two rungs will ever be adjacent (so there is no ambiguity about directional path)
"""

example_tests = [
    [
        '000001',
        '010010',
        '101001',
        '010100',
        '001010',
        '010000',
        '100010',
        '010100'],
    [
        '01000100',
        '00101000',
        '01010101',
        '10000000',
        '10000100',
        '10001000',
        '00001010',
        '01001000'],
    [
        '00000100',
        '01000101',
        '00001001',
        '10000010',
        '01001000',
        '00101010',
        '10001010',
        '10101001'],
    [
        '00010000',
        '10000100',
        '10100010',
        '10010100',
        '10101001',
        '01000000',
        '01000100',
        '00100001',
        '00000100',
        '01000010'],
    [
        '0010001010',
        '1001000000',
        '0100010010',
        '0101001000',
        '0100100001',
        '1001001010',
        '0100101010',
        '1001001000',
        '1000101001',
        '0001000100']
]
#
example_solutions = [
    [6, 3, 2, 1, 0, 5, 4],
    [3, 2, 0, 6, 4, 1, 8, 5, 7],
    [2, 1, 0, 3, 5, 4, 7, 8, 6],
    [0, 4, 1, 3, 7, 2, 5, 6, 8],
    [3, 0, 1, 2, 4, 7, 6, 8, 5, 9, 10]
]
#
#
def main():
    print(amidakuji(example_tests[0]))
    print(amidakuji(example_tests[1]))
    print(amidakuji(example_tests[2]))
    print(amidakuji(example_tests[3]))
    print(amidakuji(example_tests[4]))
#
#
def amidakuji(inputLadder):
    startList = createInitialList(inputLadder[0])
    endList = startList
    i = 0
    while i < len(startList):
        currentIndex = i
        j = 0
        while j < len(inputLadder):
            if currentIndex < len(startList) - 1 and inputLadder[j][currentIndex] == "1":
                currentIndex += 1
            elif currentIndex > 0 and inputLadder[j][currentIndex - 1] == "1":
                currentIndex -= 1
            j += 1
        endList[currentIndex] = i
        i += 1
    return endList
#
#
def createInitialList(tableWidth):
    numberList = []
    i = 0
    while i <= len(tableWidth):
        numberList.append(i)
        i += 1
    return numberList
#
#
if __name__ == "__main__":
    main()
#
