class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        n = len(nums)
        high = n-1
        while low <= high:
            mid = low + (high-low)//2

            if nums[mid] == target:
                return mid
            
            #left half if sorted, check if the target is in that sorted part or not
            elif nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
                
            #right half is sorted and check if the target is in the right half or not
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid -1

        return -1
# https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/1749482435/