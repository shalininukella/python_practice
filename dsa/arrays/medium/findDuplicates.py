class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        mp = {}
        ans = []
        for i in nums:
            if i not in mp:
                mp[i] = 1 
            else:
                mp[i] += 1
        
        for key, value in mp.items():
            if value > 1:
                ans.append(key)

        return ans
# https://leetcode.com/problems/find-all-duplicates-in-an-array/