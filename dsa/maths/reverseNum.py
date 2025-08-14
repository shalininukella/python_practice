class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        temp = x
        if x < 0:
            x = abs(x)
        prev = 0
        while x > 0:
            curr = x % 10
            prev = prev*10 + curr
            x //= 10
        
         # Check for 32-bit overflow
        if prev < INT_MIN or prev > INT_MAX:
            return 0 

        if temp < 0:
            prev = -prev

        return prev


# https://leetcode.com/problems/reverse-integer/ 