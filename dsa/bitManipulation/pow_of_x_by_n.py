# # 1. Brute force - iterative
# # Multiplying x n times
# # Gives TLE 

# class Solution:
#     def myPow(self, x, n):
#         # Base case
#         if n == 0 or x == 1.0:
#             return 1
        
#         temp = n  # to avoid integer overflow
        
#         # Handle negative exponents
#         if n < 0:
#             x = 1 / x
#             temp = -1 * n

#         ans = 1

#         for i in range(temp):
#             # Multiply ans by x for n times
#             ans *= x 
#         return ans




# # 2. divide and conquer with recursion

# # Time: O(log2(n)), where n is the given power
# # Space: O(log n)
#     Recursion depth: O(log n)
#     Space: O(log n)

# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         #base case when n is neg
#         if n < 0:
#             return 1/self.myPow(x, -n) #if n = -3, then -(-3) = 3

#         #base case when n == 0
#         if n == 0:
#             return 1
        
#         half = self.myPow(x, n//2)

#         if n%2 == 0:
#             #even power 
#             return half * half
        
#         else:
#             #odd power
#             return half * half * x


# 3. Binary Exponentiation
# COMPLEXITY

# Time: O(log2(n)), where n is the given power
# Space: O(1), in-place


class Solution:
    def myPow(self, x: float, n: int) -> float:

        # Handle negative power
        if n < 0:
            x = 1/x
            n = -n # if n = -13, then n = -n => n = -(-13) = 13 => (1/x) ^ 13

        res = 1
        while n > 0:

            #check if n is odd or even - id n&1 == 1 then n is odd else even
            if (n&1) != 0:
                # if n is odd, multiply res by x
                res = res * x

            # square the base
            x = x * x

            # divide exponent by 2 (integer division)

            #  n = n >>> 1 
            # # to handle the negative powers use unsigned right shift
            # # acts as dividing the number n(power) into half => n//2 in cpp or java

            #or

            n = n >> 1

        return res

# # https://leetcode.com/problems/powx-n/submissions/1850398369/