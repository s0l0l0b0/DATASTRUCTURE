#creating a node class


class node:
    def __init__(self,val):
        self.childleft = None
        self.childright = None
        self.nodedata = val


#creating an instance of the Node class to construct the tree...

root = node(1)
root.childleft = node(2)
root.childright = node(3)
root.childleft.childleft = node(4)
root.childleft.childright = node(5)

print('in order')

def in_order(root):
    if root:
        in_order(root.childleft)
        print(root.nodedata)
        in_order(root.childright)
in_order(root)

print('\npre order')

def pre_order(root):
    if root:
        print(root.nodedata)
        pre_order(root.childleft)
        pre_order(root.childright)
pre_order(root)

print('\npost order')

def post_order(root):
    if root:
        post_order(root.childleft)
        post_order(root.childright)
        print(root.nodedata)
post_order(root)