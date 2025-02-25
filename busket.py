import math

def bucketSort(customList):
    no = round(math.sqrt(len(customList)))

    maxValue = max(customList)
    arr = []

    for i in range(no):
        arr.append([])
    
    for j in customList:
        index_b = math.ceil(j * no / maxValue)
        arr[index_b - 1].append(j)

    for i in range(no):
        arr[i] = insertionSort(arr[i])

    k = 0
    for i in range(no):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1

    return customList

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key

    return arr

print(bucketSort([5, 2, 7, 3, 8, 10, 4, 1, 6]))