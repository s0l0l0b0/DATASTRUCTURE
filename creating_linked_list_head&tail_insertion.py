class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

# Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

#Function to add something in the beginning
    def AtBegining(self,newdata):
        NewNode = Node(newdata)

# Update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode


# Function to add newnode
#Function to add something in the end
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode

list = SLinkedList()
list.headval = Node(input("1st element: "))
e2 = Node(input("2nd element: "))
e3 = Node(input("3rd element: "))

list.headval.nextval = e2
e2.nextval = e3

list.AtBegining(input("Enter something in the beginning: "))
list.AtEnd(input("enter something in the end: "))

list.listprint()