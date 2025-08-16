class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp = defaultdict(int)
        for i in s:
            mp[i] += 1
        
        for i in range(len(s)):
            if mp[s[i]] == 1:
                return i
        
        return -1
    
# https://leetcode.com/problems/first-unique-character-in-a-string/