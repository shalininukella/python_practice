class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        curr = 0
        n = len(nums)
        mp = {}

        for i in range(n):
            rem = target - nums[i]
            if rem in mp:
                return [mp[rem], i]
            mp[nums[i]] = i

        return []

# https://leetcode.com/problems/two-sum/