# Time Complexity: O(2^N),In the worst case (all unique elements), we generate all possible subsets, which is 2^N. Sorting takes O(N log N), so total complexity is O(2^N + N log N) ≈ O(2^N).
# Space Complexity: O(N) ,Due to recursion depth and storage of the current subset in the call stack. The output storage is O(2^N) for all subsets.

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        seq = []

        nums.sort()

        def helper(ind):
            #every call contributes to the total means we haven't added the curent sum yet but the previous total is yet to add in the res
            res.append(seq[:])

            #for loop to avoid dupes
            for i in range(ind, len(nums)):

                #avoid the dupes 
                if i > ind and nums[i] == nums[i-1]:
                    # don't take the nums[i] and skip to the net num
                    continue

                #take
                seq.append(nums[i])
                helper(i+1)
            
                #not take
                seq.pop()

        helper(0)
        return res

# https://leetcode.com/problems/subsets-ii/submissions/1858176235/