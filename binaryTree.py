from stack_push_pop import Stack

class Node():
    nodeData = None
    left = None
    right = None

    def __init__(self, nodedata):
        self.nodedata = nodedata




def createTree(inputString):
    stack = Stack()
    root = Node(inputString[0])
    stack.push(root)

    for i in range(1,len(inputString)):
        if inputString[i] != '^':
            while(stack.top().left is not None and stack.top().right is not None):
                stack.pop()

            node = Node(inputString[i])
            if stack.top().left == None:
                stack.top().left =  node
            else: stack.top().right = node

            stack.push(node)
        else:
            node = stack.top()
            # pop if it is a leaf node
            if node.left is None and node.right is None:
                stack.pop()
            # pop if it has both the child
            if node.left is not None and node.right is not None:
                stack.pop()
    
    return root


def in_order(root):
    if root:
        in_order(root.left)
        print(root.nodedata, end = " ")
        in_order(root.right)



def pre_order(root):
    if root:
        print(root.nodedata, end = " ")
        pre_order(root.left)
        pre_order(root.right)



def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.nodedata, end = " ")

# def printBFS(root):
#     q = []
#     q.append(root)

#     while q:
#         start = q.pop(0)
        
#         if start.left is not None:
#             q.append(start.left)
            
#         if start.right is not None:
#             q.append(start.right)
            
#         print(start.nodedata, end = " ")
    

def main():
    tree = createTree("ABC^^DE^G^^F^^")
    print("PreOrder: ")
    pre_order(tree)
    print("\n\nIn order: ")
    in_order(tree)
    print("\n\nPost order: ")
    post_order(tree)
    # print("\nBFS: ")
    # printBFS(tree)

main()


