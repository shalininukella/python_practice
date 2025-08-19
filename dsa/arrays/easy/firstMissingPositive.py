#really !!!!!!!!! - mera solution h -beats 83.05%

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxi = max(nums)
        i = 1
        while i <= maxi:
            if i not in seen:
                return i
            i += 1
        return i
    
# https://leetcode.com/problems/first-missing-positive/