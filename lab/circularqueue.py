class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, value):
        if ((self.rear + 1) % self.size == self.front):
            print("The queue is full")
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value

    def dequeue(self):
        if (self.front == -1):
            print("The queue is empty")
        elif (self.front == self.rear):
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    def front_element(self):
        if(self.front == -1):
            print("The queue is empty")
            return None
        return self.queue[self.front]

    def rear_element(self):
        if(self.rear == -1):
            print("The queue is empty")
            return None
        return self.queue[self.rear]

# Example usage:
cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
print("Front element is:", cq.front_element())
print("Rear element is:", cq.rear_element())
print("Dequeued:", cq.dequeue())
print("Front element is:", cq.front_element())