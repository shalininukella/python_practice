# Using map - only 5 %

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         mp = defaultdict(int)
#         for i in nums:
#             mp[i] += 1
        
#         for key, val in mp.items():
#             if val > 1:
#                 return True
#         return False


#or using set - 60%
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False

# https://leetcode.com/problems/contains-duplicate/