class Solution(object):
    
    def reverse(self, x: int) -> int:
        ans = 0
        sign = -1 if x < 0 else 1
        x *= sign

        while x:
            ans = ans * 10 + x % 10
            x //= 10

        # Directly return the signed result
        return sign * ans if ans <= 2**31 - 1 else 0
