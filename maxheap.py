#max heapq 

import heapq

def productofthree(list):
    max_heap = []
    if len(list) < 3:
        return None
    for num in list:
        heapq.heappush(max_heap, -num)
        if len(max_heap) > 3:
            heapq.heappop(max_heap)
    product = 1
    while max_heap:
        product *= -heapq.heappop(max_heap)
    return product

if __name__ == "__main__":
    list = [3, 1, 4, 4, 5, 2]
    list1 = set(list)
    print("The product of three:", productofthree(list1))
