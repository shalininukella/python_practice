# Time Complexity: O(2^n), where n = t/d  in the worst case, as we explore all subsets of candidates.
# Space Complexity: O(target/min(candidate)), representing the depth of the recursion.
# cuz jitni bar min(candidate) ko plus karte karte target pohochenge utne ka lenght of the word hoga. I'm relating to any word of length n so each letter has 2 possibilities.

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #base case would be target == 0
        res = []
        seq = []

        def helper(i, target):
            if target == 0:
                res.append(seq[:])
                return
            
            if i == len(nums) or target < 0:
                return

            #take the current element
            seq.append(nums[i])
            helper(i, target - nums[i])

            #not take the current element
            seq.pop()
            helper(i + 1, target)
        
        helper(0, target)
        return res

# https://leetcode.com/problems/combination-sum/