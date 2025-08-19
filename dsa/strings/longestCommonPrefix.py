class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        v = sorted(strs)
        first = v[0]
        last = v[len(strs)-1]
        minLen = min(len(first), len(last))
        for i in range(minLen):
            if first[i] != last[i]:
                return res
            res += first[i]
        return res

# class Solution:
    # #Horizontal Scanning
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     if not strs:
    #         return ""
        
    #     prefix = strs[0]
        
    #     for s in strs[1:]:
    #         while not s.startswith(prefix):
    #             prefix = prefix[:-1]
    #             if not prefix:
    #                 return ""
    #     return prefix

#vertical scanning
# from typing import List

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
        
#         for i in range(len(strs[0])):
#             char = strs[0][i]
#             for s in strs[1:]:
#                 if i >= len(s) or s[i] != char:
#                     return strs[0][:i]
#         return strs[0]


# https://leetcode.com/problems/longest-common-prefix/submissions/1740830121/

        

                

        

                
