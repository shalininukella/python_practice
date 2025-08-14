from typing import List
#takes too long - TLE - passing 39/40 test cases
# def sumFirstN(n: int) -> int:
#     # Write your code here.
#     if n <= 1:
#         return 1

#     return n + sumFirstN(n-1)

def sumFirstN(n):
    return n*(n+1)//2

# https://www.naukri.com/code360/problems/sum-of-first-n-numbers_8876068?leftPanelTabValue=SUBMISSION