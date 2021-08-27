"""
Algorithm
1. Scan the infix expression from left to right.
2. If the scanned character is an operand, output it.
3. Else,
    - If the precedence of the scanned operator is greater than the precedence of the operator in the stack(or the stack is empty or the stack contains a ‘(‘ ), push it.
    - Else, Pop all the operators from the stack which are greater than or equal to in precedence than that of the scanned operator. 
    After doing that Push the scanned operator to the stack. 
4. If the scanned character is an ‘(‘, push it to the stack.
5. If the scanned character is an ‘)’, pop the stack and and output it until a ‘(‘ is encountered, and discard both the parenthesis.
6. Repeat steps until infix expression is scanned.
7. Print the output
8. Pop and output from the stack until it is not empty.
"""

class Conversion:

    """constructor to initialize the class variables"""
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity

        self.stack = []
        self.output = []
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}


    """function to check whethere the stack is empty"""

    def isEmpty(self):
        return True if self.top == -1 else False


    """function to return the top of the stack"""

    def Top(self):
        return self.stack[-1]


    """function to push element"""

    def push(self, operator):
        self.top += 1
        self.stack.append(operator)


    """function to pop element"""
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.stack.pop()
        else:
            return "$"


    """function to check is the given charactere oprarand or not"""

    def isOperanad(self, character):
        return character.isalpha()

    """function to check precedence of operator is less...
     than the top of the stack or not""" 

    def notGreater(self, i): 
        try: 
            a = self.precedence[i] 
            b = self.precedence[self.Top()] 
            return True if a  <= b else False
        except KeyError:  
            return False


    """function that will convert the infix to postfix"""


    def inFixToPostFix(self, expression):
        for i in expression:
            # if the character is an operand, add it to the output
            if self.isOperanad(i):
                self.output.append(i)
            # if the character is "(", push it to the stack
            elif i == "(":
                self.push(i)
            # if character is ")", pop and output from the stack until "(" is found
            elif i == ")":
                while((not self.isEmpty()) and self.Top() != "("):
                    a =self.pop()
                    self.output.append(a)
                if(not self.isEmpty() and self.Top() != "("):
                    return -1
                else:
                    self.pop()
            # an operator is encountered
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)
        # pop all the operator from the stack
        while not self.isEmpty():
            self.output.append(self.pop())

        print("\n\nThe postfix expression is: "+"".join(self.output))


# expression = input("Please enter the expression here: ")

expression = "a+b*(c^d-e)^(f+g*h)-i"
obj = Conversion(len(expression))
obj.inFixToPostFix(expression)
print()


    



