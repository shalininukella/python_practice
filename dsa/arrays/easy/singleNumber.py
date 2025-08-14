# #Using xor
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         xor = 0
#         for i in nums:
#             xor ^= i
#         return xor


#using map
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mp = {}
        for i in nums:
            if i in mp:
                mp[i] += 1
            else:
                mp[i] = 1

        for key, value in mp.items():
            if value == 1:
                return key
            
# https://leetcode.com/problems/single-number/