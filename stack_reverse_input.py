# analysis
"""
1. Create an empty stack.
2. For the string input tokenize the input string into words using spaces as separator.
3.Push the words into the stack.
4.Pop the words from the stack until the stack is not empty which will be in reverse order.
"""

def reverseString(givenString):
    s = []

    token = userInput.split()

    for item in token:
        s.append(item)

    while (len(s)):
        print(s.pop(), end = " ")


def reverseInteger():
    s = []

    size = int(input("Enter the list size: "))
    for i in range(0,size):
        items = input(f"Enter number at {i+1}: ")
        s.append(items)
    
    # there are many ways to reverse the stack/list in Python, few of them are following:
    """
    print(s[::-1],) # accesing the elements from the last elements to the first element
    """

    while (len(s)):
        print(s.pop(), end = " ")

# in python we can use reverse() method as well. example-
"""
    print(s.reverse())
"""

print("1. Input String\n2. Input Numbers")
options = int(input())

if (options == 1):
    userInput = input("Enter the string here: ")
    reverseString(userInput)
elif(options == 2):
    reverseInteger()
else:
    ("Enter a valid operation(1 or 2) please")
