from sys import *
from collections import *
from math import *

# def largestElement(arr: [], n: int) -> int:

#     # Write your code from here.
#     maxi = -2**31
#     for i in arr:
#         if i > maxi:
#             maxi = i
#     return maxi


# or using max 
def largestElement(arr: [], n: int) -> int:
    # Write your code from here.
    maxi = -2**31
    for i in arr:
        maxi = max(maxi, i)
    return maxi

# https://www.naukri.com/code360/problems/largest-element-in-the-array-largest-element-in-the-array_5026279?leftPanelTabValue=SUBMISSION