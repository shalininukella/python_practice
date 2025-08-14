#1
# TLE o(n rootn)
#def sumOfDivisor(n):
#     sum = 0
#     for i in range(1, n+1):
#         if n%i == 0:
#             sum += i
#     return sum

# def sumOfAllDivisors(n: int) -> int:
#     sum = 0
#     for i in range (1, n+1):
#         sum += sumOfDivisor(i)

#     return sum


'''
    Time Complexity: O(n*sqrt(n))
    Space Complexity: O(1)

    Where 'n' is the given integer.
'''

#2
# import math

# def sumOfAllDivisors(n):
#     ans = 0

#     # Iterating over all 'i'.
#     for i in range(1, n+1):

#         # Calculating the value of 'sumOfDivisors(i)' for current 'i'.
#         for j in range(1, int(math.sqrt(i)) + 1):
#             if i % j == 0:

#                 # Avoid counting sqrt(i) twice.
#                 if i // j == j:
#                     ans += j
#                 else:
#                     ans += j + i // j

#     return ans

#3
# Instead of checking all numbers 1...n and finding their divisors one by one, do this:
# ?? Loop from i = 1 to n:
# Ask: How many numbers from 1 to n is i a divisor of?
# Answer: Exactly n // i numbers.
# For example, if n = 10 and i = 2, then 2 is a divisor of:
# 2, 4, 6, 8, 10 ? 5 numbers ? n // i = 10 // 2 = 5
# So the contribution of 2 to the total is:
# 2 * 5 = 10
# Do this for every number i from 1 to n.

'''
    Time Complexity: O(n)
    Space Complexity: O(1)

    Where 'n' is the given integer.
'''

# def sumOfAllDivisors(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += (n // i) * i
#     return total


#4
'''
    Time Complexity: O(sqrt(n))
    Space Complexity: O(1)

    Where 'n' is the given integer.
'''

def sumOfAllDivisors(n):
    ans = 0
    l = 1

    # Iterating over all values of 'l' such that 'n/l' is distinct.
    # There at most 2*sqrt(n) such values.
    while l <= n:
        val = n // l

        # 'r' = maximum value of 'i' such that 'n/i' is val.
        r = n // val
        ans += ((r * (r + 1)) // 2 - (l * (l - 1)) // 2) * val
        
        # moving on to next range.
        l = r + 1

    return ans


# https://www.naukri.com/code360/problems/sum-of-all-divisors_8360720?leftPanelTabValue=SUBMISSION