from sys import *
from collections import *
from math import *

def rotateArray(arr: [], n: int) -> []:
    # Write your code from here.
    j = n-1
    i = 1
    while i <=j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return reversed(arr)

# https://www.naukri.com/code360/problems/left-rotate-an-array-by-one_5026278?leftPanelTabValue=SOLUTION

