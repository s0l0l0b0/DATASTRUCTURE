class Stack:
    stack = []
    count = 0


    def top(self):
        return self.stack[self.count -1]

    def push(self, items):
            self.stack.append(items)
            self.count += 1

    def pop(self):
        lastEle = self.stack[self.count - 1]
        del self.stack[self.count - 1]
        self.count -= 1
        return lastEle

    def size(self):
        return self.count


"""to check wheter the implementation is ok or not"""
if __name__ == "__main__":     
    object = Stack()

    object.push(1)
    print("\nStack:",object.stack)
    print("Size of the stack is: ",object.size())
    object.push(2)
    print("\nStack:",object.stack)
    print("Size of the stack is: ",object.size())
    object.pop()
    print("\nStack:",object.stack)
    print("Size of the stack is: ",object.size())
    object.push(3)
    print("\nStack:",object.stack)
    print("Size of the stack is: ",object.size())
    object.push(4)
    print("\nStack:",object.stack)
    print("Size of the stack is: ",object.size())
    object.pop()
    print("\nStack:",object.stack)
    print("Size of the stack is: ",object.size())
    object.push(5)
    print("\nStack:",object.stack)
    print("Size of the stack is: ",object.size())
    object.pop()
    print("\nStack:",object.stack)
    print("Size of the stack is: ",object.size())
    print("\nStack:",object.stack)
    print("Size of the stack is: ",object.size())

    # print("")

    # while(object.size() > 0):
    #     print(object.pop())

    

    

