import time
from decimal import Decimal, getcontext

class Node():
    data = 0
    next = None 
    def __init__(self, value):
        self.data = value


def tailInsert(node):
    global head
    temp = head
    while(temp.next is not None):
        temp = temp.next
    temp.next = node


def showList(head):
    temp = head
    while(temp is not None):
        print(temp.data, end=" ")
        temp = temp.next


def insert(head,val):
    temp = head
    newNode = Node(val)
    while(temp is not None and temp.data+1 != val):
        temp = temp.next
    newNode.next = temp.next
    temp.next = newNode


i = 1
head = Node(0)
temp = head


maxIter = 20000  #the size of the lisnked list and the array list
insertVal = 1500 #number to insert in the linked list and the array list


#creating the linked list
while(i<=maxIter):
    if i != insertVal:
        tailInsert(Node(i))
    i+=1


# showList(head)
print()

start = Decimal(time.time())

insert(head,insertVal)

end = Decimal(time.time())
# showList(head)



print("Linked_list insertion time: ",end-start)



""" list insertion """

def listInsertion(maxVal, insertVal):
    myList = []
    for i in range(0,maxVal + 1):
        if(i!=insertVal):
            myList.append(i)

    myList.append(None)
    # print(myList)
    start = Decimal(time.time())
    # starting the shift from second last element
    for i in range(len(myList) -2, insertVal -1, -1 ):
        myList[i+1] = myList[i]
    
    myList[insertVal] = insertVal

    end = Decimal(time.time())

    # print(myList)
    print("List insertion time       : ", end - start)


listInsertion(maxIter,insertVal)



