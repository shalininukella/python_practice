# # 1. BACKTRACKING

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []

#         def helper(nums, idx, seq):
#             if idx == len(nums):
#                 res.append(seq[:])
#                 #or
# #               res.append(seq.copy())  #copy cuz we are passing the reference of the seq list, not the copy of it
#                 return
                
#             # NOT TAKE nums[idx]
#             helper(nums, idx + 1, seq)

#             # TAKE nums[idx]
#             seq.append(nums[idx])
#             #explore the takes
#             helper(nums, idx + 1, seq)

#             #not take
#             seq.pop()  # backtrack

#         helper(nums, 0, [])
#         return res


## 2. RECURSION
# tc - O(n * 2^n) - every element of the array have 2 possibilities - take or not take
# sc - O(n * 2^n) - refer my dsa docs
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        seq = []

        def subSeq(i):
            #base
            if i >= len(nums):
                res.append(seq[:])
                return

            #take
            seq.append(nums[i])

            #explore all the possibilities(take and not take) of the elements which come after the current element with this current element
            subSeq(i+1)

            # now not take the current elem, since we will be back after exploring all the possibilities of the take
            seq.pop()

            #now explore all the possibilities (take and not take) by not taking the current element
            subSeq(i+1)
        
        subSeq(0)
        return res

##3. Powerset
# tc - O(n * 2^n) 
# sc - O(n * 2^n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        for possible_seq in range (1 << n): #run 2^n times

            # for each possibility check if each index k place of that possibility me the digit is set or not
            seq = []
            for i in range (n):
                if (possible_seq & (1 << i)):
                    #if set
                    seq.append(nums[i])            
            res.append(seq)
        return res

# https://leetcode.com/problems/subsets/