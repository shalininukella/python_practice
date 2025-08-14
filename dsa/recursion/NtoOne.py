# won't work for large x

# from typing import List

# def printNos(x: int) -> List[int]:
#     # Write your code here
#     if x <= 1:
#         return [1]
#     return [x]+printNos(x-1)


'''
    Time Complexity: O(n) 
    Space Complexity: O(n)
    
    where n is the integer.
'''
from typing import List

def recursiveFunction(x: int, ans: List[int]):
    if x == 0:
        return
    ans.append(x)
    recursiveFunction(x - 1, ans)

def printNos(x: int) -> List[int]:
    ans = []
    recursiveFunction(x, ans)
    return ans

# https://www.naukri.com/code360/problems/n-to-1-without-loop_8357243?leftPanelTabValue=SUBMISSION