class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        ele = nums[0]
        for i in range(len(nums)):
            if cnt == 0:
                cnt = 1
                ele = nums[i]
            elif ele == nums[i]:
                cnt += 1
            else:
                cnt -= 1

        return ele

# https://leetcode.com/problems/majority-element/submissions/1736095828/