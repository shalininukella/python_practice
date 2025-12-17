# # tc - O(2^n) - tle, when target = 30 and every ele is 1 in the array then 2^30 - causes tle - 10 times more than the standard at max tc = 10^8 i.e almost 10 * 10 ^ 8

# # sc = O(n)

# class Solution:
#     def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
#         nums.sort()
#         res = []
#         seq = []

#         def helper(i, target):
#             #base
#             if target == 0:
#                 if seq not in res:
#                     res.append(seq[:])
#                 return

#             if target < 0 or i == len(nums):
#                 return
            
#             #take
#             seq.append(nums[i])
#             helper(i+1, target - nums[i])
#             #not take
#             seq.pop()
#             helper(i+1, target)

#         helper(0, target)
#         return res


#backtracking with for lopp to avoid dupes

# Time Complexity: O(2n * k), For each of the 2n subsequences, storing takes O(k) time where k is the average length of each combination.
# Space Complexity: O(k * x), To store all x valid combinations, each of average length k.

class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        seq = []

        def helper(i, target):
            #base case 
            if target == 0:
                res.append(seq[:])
                return

            if target < 0:
                return

            #for each of the elements explore the take non take combinations
            for ele in range(i, len(nums)):

                #this will be executed only after the pop() is executed means the not take case, then the not take case comes, we dont wanna take the same element again right
                if ele > i and nums[ele] == nums[ele-1]:
                    continue #continue means let's not take this as the same index vala element again
                if nums[ele] > target:
                    break #means break a don't explore this anymore - so we are not even adding this in the seq, no need to explore furhter cuz the array is sorted
                #take
                seq.append(nums[ele])
                helper(ele+1, target - nums[ele])

                #not take
                seq.pop()

        helper(0, target)
        return res
# https://leetcode.com/problems/combination-sum-ii/
