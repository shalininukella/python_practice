class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        n = len(nums)
        high = n-1
        left = -1
        right = -1
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                left = mid
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid+1

        low = 0
        high = n - 1
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                right = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return [left, right]
    # https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/