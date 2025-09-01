# WRONG ❌ 🔹 Hidden Issue

# Your algorithm only works if at least one val exists.
# If val is not in the array, then:

# nums = [1,2,3,4], val = 5


# First loop never finds val, so idx stays 0

# You start from i=0, and swap incorrectly.

# Final result → i=0 → WRONG ❌ (should return 4).

# So your solution fails when val is not in nums.

# # class Solution:
# #     def removeElement(self, nums: List[int], val: int) -> int:
# #         idx = 0
# #         for i in range(len(nums)):
# #             if nums[i] == val:
# #                 idx = i
# #                 break
# #         i = idx
# #         for j in range(idx, len(nums)):
# #             if nums[i] == val and nums[j] != val:
# #                 nums[i], nums[j] = nums[j], nums[i]
# #                 # nums[i] = nums[j]
# #                 i += 1

# #         return i


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
# https://leetcode.com/problems/remove-element/