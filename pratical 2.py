'''Given a sorted and a target value, return the index if the target is found. if not, return the index  
 where it would be if where inserted in order'''


def search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return mid
    return low

nums = [1, 3, 4, 6, 7, 8]
target = 9
result = search(nums, target)

if result < len(nums) and nums[result] == target:
    print("Element is present at index: ", result)
else:
    print(" new element index is :",result)
