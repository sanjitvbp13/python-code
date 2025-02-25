'''finding the minimum element '''


A = [10, 5, 20, 9]

for i in range(len(A)-1):

    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

    A[i], A[min_idx] = A[min_idx], A[i]

for i in range(len(A)):
    print(A[i], end=" , ")