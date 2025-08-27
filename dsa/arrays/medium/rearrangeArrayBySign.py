# from typing import List

# class Solution:
#     def rearrangeArray(self, A: List[int]) -> List[int]:
#         pos = []
#         neg = []
    
#         # Segregate the array into positives and negatives.
#         for i in range(len(A)):
#             if A[i] > 0:
#                 pos.append(A[i])
#             else:
#                 neg.append(A[i])
    
#         # Positives on even indices, negatives on odd.
#         for i in range(len(pos)):
#             A[2 * i] = pos[i]
#         for i in range(len(neg)):
#             A[2 * i + 1] = neg[i]
    
#         return A

#or 
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posIdx = 0
        negIdx = 1

        n = len(nums)
        res = [0] * n

        for i in nums:
            if i < 0:
                res[negIdx] = i
                negIdx += 2
            else:
                res[posIdx] = i
                posIdx +=2 

        return res
# https://leetcode.com/problems/rearrange-array-elements-by-sign/submissions/1750477868/