class Solution:
    def maxArea(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        max_area = 0
        min_height = 0

        while left < right:
            min_height = min(nums[left], nums[right])
            max_area = max(max_area, (right - left) * min_height)

            if nums[left] < nums[right]:
                left += 1
            else:
                right -= 1

        return max_area
        
    #question

    # https://leetcode.com/problems/container-with-most-water/

    #solution

    # https://leetcode.com/problems/container-with-most-water/solutions/5139915/video-simple-two-pointer-solution