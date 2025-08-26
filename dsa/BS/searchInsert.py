class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        n = len(nums)
        high = n - 1
        
        ans = n
        while low <= high:
            mid = low + (high - low)//2
            if target <= nums[mid]:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans        
# https://leetcode.com/problems/search-insert-position/