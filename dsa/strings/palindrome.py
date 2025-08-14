class Solution:
    # def isPalindrome(self, s: str) -> bool:
    #     s = ''.join(c.lower() for c in s if c.isalnum())
    #     newS = s[::-1]
    #     if s == newS:
    #         return True
    #     return False
        

    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        i = 0
        j = len(s) - 1
        while i<=j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
# https://leetcode.com/problems/valid-palindrome/    