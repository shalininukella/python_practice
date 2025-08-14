from typing import *
# # using reversed function
# def reverseArray(n: int, nums: List[int]) -> List[int]:
#     # Write your code here
#     return reversed(nums)
#     pass


# #using loop
# def reverseArray(n: int, nums: List[int]) -> List[int]:
#     i = 0
#     j = n-1
#     while i<=j:
#         temp = nums[i]
#         nums[i] = nums[j]
#         nums[j] = temp
#         i += 1
#         j -= 1
#     return nums


#using recursion
def reverseArray(n: int, nums: List[int]) -> List[int]:
    def helper(i, j):
        if i>=j:
            return
        nums[i], nums[j] = nums[j], nums[i]
        helper(i+1, j-1)
    helper(0, n-1)
    return nums


# https://www.naukri.com/code360/problems/reverse-an-array_8365444?leftPanelTabValue=SUBMISSION