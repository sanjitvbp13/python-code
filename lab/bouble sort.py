'''Python program for implementation of Bubble Sort'''

def bubble_sort(arr):
    n = len(arr)  
    for i in range(n):
        
        swapped = False
       
        for j in range(0, n - i - 1):
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
                swapped = True
        
        if not swapped: 
            break


if __name__ == "__main__":
    arr = [55,35,34,56,2]
    print("normal list is ",arr)
    bubble_sort(arr)
    print("after the sorting ")
    print("bouble sort list : ", arr)
    