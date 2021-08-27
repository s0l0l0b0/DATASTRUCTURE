class LinkedList:
    def __init__(self):
        self.head = None

class Node:
    value = 0
    next = None
    def __init__(self,value):
        self.value = value

list = LinkedList()

node = Node(4)
node.next = Node(2)
node.next.next = Node(6)
node.next.next.next = Node(7)
node.next.next.next.next = Node(2)

list.head = node;

def showList(list):
    temp = list.head
    while(temp is not None):
        print(temp.value, end=" ")
        temp = temp.next

def tailInsert(list):
    userInput = int(input("\nEnter somoething at the end: "))
    tempNode = Node(userInput)

    temp = list.head
    while(temp.next is not None):
        temp = temp.next
    temp.next = tempNode
    

def insert(list):
    userInput = int(input("\nEnter somoething at the beginning: "))
    tempNode = Node(userInput)
    tempNode.next =  list.head
    list.head = tempNode

showList(list)
insert(list)
showList(list)
insert(list)
showList(list)
tailInsert(list)
showList(list)

