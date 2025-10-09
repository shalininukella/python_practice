class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""

        #when s or t are empty or target string is smaller than the main string s
        if not s or not t or len(s) < len(t):
            return res
        
        mini = float('inf')
        start_idx = 0
        i = 0
        j = 0
        n = len(s)

        mp1 = defaultdict(int)
        mp2 = defaultdict(int)

        for ch in t:
            mp1[ch] += 1

        req = len(mp1)
        cnt = 0

        while i <= j and j < n:
            curr = s[j]
            mp2[curr] += 1

            if curr in mp1 and mp2[curr] == mp1[curr]:
                cnt += 1
            
            #when window is hit - all the elements of t are in the window of size j-i+1
            while i <= j and cnt == req:
                if j-i+1 < mini:
                    mini = j-i+1
                    start_idx = i
                
                mp2[s[i]] -= 1
                
                if s[i] in mp1 and mp2[s[i]] < mp1[s[i]]:
                    cnt -= 1
                i += 1
            
            j += 1

        if mini != float('inf'):
            res = s[start_idx : start_idx + mini]

        return res
# https://leetcode.com/problems/minimum-window-substring/description/