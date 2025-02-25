#write a program to impliment linear queue implement the below function.
#    1)Enqueue
#    2)Dequeue
#    3)front
#    4) rear
class LinearQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Dequeue from empty queue")

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Front from empty queue")

    def rear(self):
        if not self.is_empty():
            return self.queue[-1]
        else:
            raise IndexError("Rear from empty queue")

    def is_empty(self):
        return len(self.queue) == 0
queue = LinearQueue()
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(3)
print("Front element is:", queue.front())
print("Rear element is:", queue.rear())
print("Dequeued:", queue.dequeue())
print("Front element is:", queue.front())