# #recursive

# tc - O(2^n) - every element of the array have 2 possibilities - take or not take, 
# sc - O(2^n) - Stores 2ⁿ integers

class Solution:
    def subsetSums(self, nums):
        res = []
        
        def helper(i, total):
            #base 
            if i == len(nums):
                res.append(total)
                return

            #take
            total += nums[i]
            #explore all the take possibilities
            helper(i+1, total)

            #not take
            total -= nums[i]
            helper(i+1, total)

        helper(0, 0)
        return res

#bitmaksing - powerset - just like the all_subsets problem

# tc - O(n * 2^n) 
# sc - O(2^n) - for storing 2^n combinations ke sums

class Solution:
    def subsetSums(self, nums):
        res = []

        for poss in range (1 << n):
            total = 0
            for i in range(n):
                #check if any index ke place pe bit set hai ya nhi
                if (poss & (1<<i)):
                    total += nums[i]
                
            res.append(total)

        return res

# https://takeuforward.org/plus/dsa/problems/subsets-i