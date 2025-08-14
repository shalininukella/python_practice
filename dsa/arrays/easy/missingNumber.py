# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums)
#         sum = n*(n+1)//2
#         total = 0
#         for i in nums:
#             if i!=0:
#                 total += i
#         return sum - total

#using XOR
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor1 = xor2 = 0
        for i in range(n):
            xor1 ^= i+1
            xor2 ^= nums[i]

        return xor1^xor2

# https://leetcode.com/problems/missing-number/submissions/1735176325/