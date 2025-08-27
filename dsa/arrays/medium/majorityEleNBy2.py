class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = nums[0]
        cnt = 0

        for i in range(len(nums)):
            if cnt == 0:
                ele = nums[i]
                cnt = 1
            elif ele == nums[i]:
                cnt += 1
            else:
                #when ele != nums[i]
                cnt -= 1
        return ele

# https://leetcode.com/problems/majority-element/submissions/1736095828/