def binary_search(arr,x):
    low = 0
    high = len(arr)-1
    mid=0
    while low<=high:
        mid = (low+high)//2
        if arr[mid]==x:
            low = mid +1
        elif arr[mid]>x:
            high = mid -1
        else:
            return mid
    return -1
arr = [7,1,2,3,6,4,9]
x=6
result = binary_search(arr,x)
if result != -1:
    print("Element is present at index",str(result))
else:
    print("Element is not present in array")