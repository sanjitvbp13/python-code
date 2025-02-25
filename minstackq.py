#write a program implementing a MINISTACK 1)construct a stack of n-capacity
                                        #2)push an element
                                         # 3)pop element
                                         # 4)top elememt
                                         # 5)retrive element
class MinStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
        self.min_stack = []

    def push(self, element):
        if len(self.stack) < self.capacity:
            self.stack.append(element)
            if len(self.min_stack) == 0 or element <= self.min_stack[-1]:
                self.min_stack.append(element)

    def pop(self):
        if len(self.stack) == 0:
            raise IndexError("Underflow: Stack is empty")
        popped = self.stack.pop()
        if popped == self.min_stack[-1]:
            self.min_stack.pop()
        return popped

    def top(self):
        if len(self.stack) == 0:
            print("Stack is empty")
            return None
        return self.stack[-1]

    def min(self):
        if len(self.min_stack) == 0:
            print("Stack is empty")
            return None
        return self.min_stack[-1]

    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        print(self.stack)
