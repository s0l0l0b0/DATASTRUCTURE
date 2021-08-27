class queue():
    queue = []
    count = 0

    def enqueue(self, items):
        self.queue.append(items)
        self.count += 1

    def dequeue(self):
        done = self.queue.pop(0)
        return done
        self.count -= 1

    def size(self):
        return self.count


object = queue()

object.enqueue(1)
object.enqueue(2)
print(object.dequeue())
object.enqueue(3)
object.enqueue(4)
print(object.dequeue())
object.enqueue(5)

print(object.size())
