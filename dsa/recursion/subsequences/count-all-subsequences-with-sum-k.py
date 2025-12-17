##RECURSION

class Solution:
    def countSubsequenceWithTargetSum(self, nums, k):
        
        def dfs(i, current_sum):
            # If sum exceeds k, no need to continue (optimization)
            if current_sum > k:
                return 0

            # If we've considered all elements
            if i == len(nums):
                return 1 if current_sum == k else 0

            # Option 1: include nums[i]
            take = dfs(i + 1, current_sum + nums[i])

            # Option 2: do NOT include nums[i]
            skip = dfs(i + 1, current_sum)

            return take + skip

        # We must exclude the empty subsequence
        return dfs(0, 0)



# or backtracking
# Time Complexity: O(2^n), 
# Space Complexity: O(n)

class Solution:
    def countSubsequenceWithTargetSum(self, nums, k):
        #your code goes here
        total = k

        def helper(index, total):

            # Base case: if sum is negative or index exceeds array size
            if index == len(nums) or total < 0:
                return 0

             # Base case: if sum is 0, one valid subsequence is found
            if total == 0:
                return 1

            #take
            # Recurse by including current number 
            take_count = helper(index+1, total - nums[index])

            #not take
            # Recurse by excluding it from the sum
            not_take_count = helper(index + 1, total)

            return take_count + not_take_count
        
        res = helper(0, total)
        return res

        
# https://takeuforward.org/data-structure/count-all-subsequences-with-sum-k