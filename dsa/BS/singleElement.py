# ✅ Key Observations:

# The array is sorted.
# All elements appear twice, except one element.
# Because of the sorting, the pairs will start at even indices:
# If the single element is not yet encountered, then:
# nums[even] == nums[even + 1]
# Once the single element is passed, the above pattern breaks.

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        n = len(nums)
        high = n-1
        while low < high:
            mid = low + (high - low) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid+1]:
                #the ele is in the rigth part
                low = mid + 2
            else:
                # when nums[mid] != nums[mid+1] 
                # it happens only when 
                # either nums[mid] is the wanted element
                # or we are after the element wanted
                # wanted element is in the left part or at mid
                high = mid
        return nums[low]
# https://leetcode.com/problems/single-element-in-a-sorted-array/
