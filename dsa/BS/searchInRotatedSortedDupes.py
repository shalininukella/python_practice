class Solution:

    #    in this we have to find the target in the duplicate containing array sorted
    #      we have to find the  left sorted array 
    #      then we have to find the right sorted array
    #      then we have to cover the edge case if low = high = mid 

    def search(self, nums: List[int], target: int) -> bool:
        low = 0
        n = len(nums)
        high = n-1
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] == target:
                return True

            #handle the duplicates, kyunki ye case decide nhi hone deta ki konsi side sorted hai.
            elif nums[low] == nums[mid] and nums[mid] == nums[high]:
                low += 1
                high -= 1

            #left part
            elif nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            #right part
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False

# approach 

# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/solutions/7118276/very-easy-and-most-optimal-approach-beats-100
         

#question

# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/