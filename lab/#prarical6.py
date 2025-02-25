#prarical6
# write a program for finding the product of largest three distinct elements. 
#use a priority queue to efficently find and remove the largest elements.

#ms word --- python file:- page -7


import heapq

def productofthree(list):
    min_heap = []
    if len(list) < 3:
        return None
    for num in list:
        heapq.heappush(min_heap, num)
        if len(min_heap) > 3:
            heapq.heappop(min_heap)
    product = 1
    while min_heap:
        product *= heapq.heappop(min_heap)
    return product

if __name__ == "__main__":
    list = [3, 1, 4, 4, 5, 2]
    list1 = set(list)
    print("The product of three:", productofthree(list1))







