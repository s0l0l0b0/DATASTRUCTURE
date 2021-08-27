def findChar(str, char):
    count = 0

    for i in range (len(str)):
        if str[i] == char:
            count += 1
    
    print(f"'{char}' is in the string for {count} times")


def findWord(str, word):
    count = 0

    for i in str.split():
        if i == word:
            count += 1
    print(f"'{word}' in the string for {count} times.")




myString = "there are r in this string for five times"
myChar = "r"
findChar(myString,myChar)

myNewString = "is there any is in this string? yes, is in this string for three times"
myWord = "is"
findWord(myNewString, myWord)

# userInput = int(input("1. Search a character\n2. Search a word"))

# if userInput == 1:
#     myString = input("Enter the string here   : ")
#     myWord = input("Enter the character here: ")
#     findChar(myString,myWord)

# else:
#     myString = input("Enter the string here : ")
#     myWord = input("Enter the word here  : ")
#     findWord(myString,myWord)
