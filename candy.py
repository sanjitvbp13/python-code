def countCandies(arr, n):
    sum = 0
    ans = [1] * n
    if (n == 1):
        return 1
    for i in range(n - 1):
        if (arr[i + 1] > arr[i]):
            ans[i + 1] = ans[i] + 1
    for i in range(n - 2, -1, -1):
           if (arr[i] > arr[i + 1] and
                ans[i] <= ans[i + 1]):
          
            ans[i] = ans[i + 1] + 1
       
        sum += ans[i]
    sum += ans[n - 1]
  
    return sum
if __name__ == '__main__':
    arr = [1, 0, 2]
    N = len(arr)
    print(countCandies(arr, N))


