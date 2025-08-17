class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        seen = set()
        n = len(s)
        maxi = 0
        while i<=j and j<n:
            while(s[j] in seen):
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            maxi = max(maxi, j-i+1)
            j += 1
        return maxi
    
# https://leetcode.com/problems/longest-substring-without-repeating-characters/