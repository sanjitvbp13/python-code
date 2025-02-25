class MinHeap:
    def __init__(self, capacity):  # Fixed constructor
        self.capacity = capacity
        self.size = 0
        self.array = [0] * capacity

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]
    
    def extract_min(self):
        if self.size == 0:
            return -1
        if self.size == 1:
            self.size -= 1
            return self.array[0]
        
        root = self.array[0]
        self.array[0] = self.array[self.size - 1]
        self.size -= 1
        self.min_heapify(0)
        return root

    def min_heapify(self, idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < self.size and self.array[left] < self.array[smallest]:
            smallest = left
        if right < self.size and self.array[right] < self.array[smallest]:
            smallest = right

        if smallest != idx:
            self.swap(idx, smallest)
            self.min_heapify(smallest)
    
    def insert(self, value):
        if self.size == self.capacity:
            print("Heap is full")
            return
        self.size += 1
        i = self.size - 1
        self.array[i] = value
        
        while i != 0 and self.array[(i - 1) // 2] > self.array[i]:
            self.swap(i, (i - 1) // 2)
            i = (i - 1) // 2

    def print_heap(self):
        for i in range(self.size):
            print(self.array[i], end=" ")
        print()
    
    def is_empty(self):
        return self.size == 0
    

# Testing the corrected class
min_heap = MinHeap(10)

min_heap.insert(10)
min_heap.insert(5)
min_heap.insert(15)
min_heap.insert(20)
min_heap.insert(30)
min_heap.insert(25)
min_heap.insert(35)
min_heap.insert(40)
min_heap.insert(50)

print("Min Heap:", end=" ")
min_heap.print_heap()

sorted_elements = []
while not min_heap.is_empty():
    sorted_elements.append(min_heap.extract_min())

print("Sorted Extract Min:", sorted_elements)

print("Min Heap after extraction:", end=" ")
min_heap.print_heap()
