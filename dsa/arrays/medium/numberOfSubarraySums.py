# #sliding window - only works for positive numbers
# from typing import List

# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         i = 0
#         total = 0
#         cnt = 0
#         n = len(nums)

#         for j in range(n):
#             total += nums[j]

#             # Shrink the window from the left if total > k
#             while total > k and i <= j:
#                 total -= nums[i]
#                 i += 1

#             # Check if the current window's sum is equal to k
#             if total == k:
#                 cnt += 1

#         return cnt


#using prefix sum, with dict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        n = len(nums)
        cnt = 0
        mp = {0: 1}  # ✅ To count subarrays starting from index 0

        for i in range(n):
            total += nums[i]

            if (total-k) in mp:
                cnt += mp[(total-k)]
            if total not in mp:
                mp[total] = 1
            else: 
                mp[total] += 1
        
        return cnt
    
# https://leetcode.com/problems/subarray-sum-equals-k/