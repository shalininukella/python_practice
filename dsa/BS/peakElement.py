class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0
        
        if nums[0] > nums[1] :
            return 0
        if nums[n-1] > nums[n-2]:
            return n-1

        low = 0
        high = n-1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            elif nums[mid+1] > nums[mid]:
                #go right, cuz it's increasing on the right, peak will be on the right side for sure
                low = mid+1
            else:
                #a[mid-1]>a[mid]:
                #go right, cuz it's increasing on the right, peak will be on the right side for sure
                high = mid-1
        return low

#or to avoid checking the boundaries:
# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         left = 0
#         right = len(nums) - 1

#         while left < right:
#             mid = (left + right) // 2
#             if nums[mid] > nums[mid + 1]:
#                 right = mid
#             else:
#                 left = mid + 1

#         return left


#question

# https://leetcode.com/problems/find-peak-element/