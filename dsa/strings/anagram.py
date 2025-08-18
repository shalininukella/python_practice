from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = defaultdict(int)
        if len(s) != len(t):
            return False

        for i in s:
            mp[i] += 1
        
        for i in t:
            if mp[i] == 0:
                return False
            mp[i] -= 1
        
        return True
    
# https://leetcode.com/problems/valid-anagram/