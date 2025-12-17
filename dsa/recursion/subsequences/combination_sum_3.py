# myyy solution
# tc = O(k * 2^9)
# sc = O(k)

# class Solution:
#     def combinationSum3(self, k: int, target: int) -> List[List[int]]:
#         #here just like combination sum 1 and 2 , arr is [1... to 9]
#         #and we have to build the subsets of size "k"
#         nums = [1,2,3,4,5,6,7,8,9]
#         res = []
#         seq = []

#         def helper(i, target):
#             #base
#             if target == 0 and len(seq) == k:
#                 res.append(seq[:])
#                 return

#             if i == len(nums):
#                 return

#             #take only if the current element is not greater than the target sum
#             # if nums[i] < target:
#             seq.append(nums[i])
#             helper(i+1, target - nums[i])

#             #not take
#             # if seq: #pop only when there is something in the seq list
#             seq.pop()
#             helper(i+1, target)
        
#         helper(0, target)
#         return res


#bakctracking with for loop
# Complexity
# Time complexity:
# O(C(9,k))
# Since we explore combinations of k elements from 9 total numbers.

# Space complexity:
# O(k) for the recursion stack and current combination.


class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:

        res = []
        seq = []

        def helper(ind, target):

            if len(seq) == k and target == 0:
                res.append(seq[:])

            for i in range(ind, 10):
                
                #base
                if i > target or k <= 0:
                    #just don't explore other options in this recursion depth
                    break #since 1 to 9 is in the ascending order (similar to a sorted ordered nums array containing 1 to 9 numbers), we can completely break out of the loop

                #take
                seq.append(i)
                helper(i+1, target - i)

                seq.pop()
            
        helper(1, target)
        return res

# https://leetcode.com/problems/combination-sum-iii/