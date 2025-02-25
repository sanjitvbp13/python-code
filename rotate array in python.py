from typing import List

class Solution:
    def reverse(self, nums: List[int], li: int, ri: int) -> None:
        while li < ri:
            nums[li], nums[ri] = nums[ri], nums[li]
            li += 1
            ri -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        self.reverse(nums, 0, n - k - 1)
        self.reverse(nums, n - k, n - 1)
        self.reverse(nums, 0, n - 1)


sol = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
sol.rotate(nums, k)
print(nums)  
