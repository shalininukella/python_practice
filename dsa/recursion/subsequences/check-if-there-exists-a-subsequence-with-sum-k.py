# backtracking
# Time Complexity: O(2^n), 
# Space Complexity: O(n)

def checkSubsequenceSum(nums, k):
    #your code goes here
    total = k
    def helper(index, total):

        #base 1: when sum == 0
        if total == 0:
            return True
            
        #base 2: when sum < 0 or index == len(nums)
        if total < 0 or index == len(nums):
            return False

        #take
        take = helper(index + 1, total - nums[index])

        #not take
        not_take = helper(index + 1, total)

        return take or not_take

    return "Yes" if helper(0, total) else "No"

nums = [4, 3, 9, 2] 
k = 10

y = checkSubsequenceSum(nums, k)
print(y)

# https://takeuforward.org/data-structure/check-if-there-exists-a-subsequence-with-sum-k