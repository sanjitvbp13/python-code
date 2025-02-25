def sort(n, k):
    l1 = [i for i in range(1, n+1)]
    l1.sort(reverse=True)
    for i in range(k-1):
        l2 = l2[:1] + [l2[0]]
        return l2
    return l1
n = int(input("Enter the number of elements: "))
k = int(input("Enter the number of rotations: "))
print(sort(n, k))