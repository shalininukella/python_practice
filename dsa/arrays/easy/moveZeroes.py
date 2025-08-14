class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     n = len(nums)
    #     i = 0
    #     idx = 0
    #     for i in range(n):
    #         if nums[i] == 0:
    #             idx = i
    #             break

    #     for j in range(idx, n):
    #         if nums[i] == 0 and nums[j] != 0:
    #             nums[i], nums[j] = nums[j], nums[i]
    #             i += 1

#or        
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        i = 0
        for j in range(n):
            if nums[i] != 0:
                i += 1
            elif nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

# https://leetcode.com/problems/move-zeroes/