"""
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
"""

def main():
    inputString_1 = "abcde"             #0
    inputString_2 = "aabbcde"           #2
    inputString_3 = "aabBcde"           #2
    inputString_4 = "indivisibility"    #1
    inputString_5 = "Indivisibilities"  #2
    inputString_6 = "aA11"              #2
    inputString_7 = "ABBA"              #2

    print(duplicate_count(inputString_1))
    print(duplicate_count(inputString_2))
    print(duplicate_count(inputString_3))
    print(duplicate_count(inputString_4))
    print(duplicate_count(inputString_5))
    print(duplicate_count(inputString_6))
    print(duplicate_count(inputString_7))
#
#
def duplicate_count(text):
    charCountList = []
    i = 0
    while i < len(text):
        j = 0
        while j < len(text):
            if j != i and text[j].lower() not in charCountList and text[i].lower() == text[j].lower():
                charCountList.append(text[i].lower())
            j += 1
        i += 1
    return len(charCountList)
#
#
if __name__ == "__main__":
    main()
#