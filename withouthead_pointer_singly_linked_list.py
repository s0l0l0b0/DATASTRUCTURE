class Node():
    value = 0
    next = None 
    def __init__(self, value):
        self.value = value

node = Node(2)
node.next = Node(4)
node.next.next = Node(3)

def showList():
    global node
    temp = node
    # head = list.head
    while(temp is not None):
        print(temp.value)
        temp = temp.next

def headInsertion():
    global node
    head = node
    userInput = int(input("Enter something: "))
    newNode = Node(userInput)
    newNode.next = head
    head = newNode
    node = head



    
showList()
headInsertion()
showList()
headInsertion()
showList()