import math

def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j >= 0 and customList[j] > key:
            customList[j + 1] = customList[j]
            j -= 1
        customList[j + 1] = key
    return customList

def bucketsort(customList):
    no_of_buckets = round(math.sqrt(len(customList)))
    max_value = max(customList)
    arr = [[] for _ in range(no_of_buckets)]

    
    for j in range(len(customList)):
        index = math.floor(customList[j] * no_of_buckets / (max_value + 1))
        arr[index].append(customList[j])

   
    k = 0
    for i in range(no_of_buckets):
        insertionSort(arr[i])
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1

    return customList


clist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(bucketsort(clist))