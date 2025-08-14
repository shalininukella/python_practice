class Solution:
    def fib(self, n: int) -> int:
        if n == 1 or n == 0:
            return n
        a = 0
        b = 1
        fib = 0
        for i in range(2, n+1):
            fib = a + b
            a = b
            b = fib
        return fib


#recursion
# class Solution:
#     def fib(self, n: int) -> int:
#         if n == 1 or n == 0:
#             return n
#         return self.fib(n-1) + self.fib(n-2)

# https://leetcode.com/problems/fibonacci-number/submissions/1734896249/