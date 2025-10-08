# class Solution:
#     def longestPalindrome(self, s: str) -> str:

""" it won't work for the case:
    # "eabcb"

    # Use Testcase
    # Output
    # "b"
    # Expected
    # "bcb"
"""
        # def is_palindrome(st, i, j):

        #     while i<=j:
        #         if st[i] != st[j]:
        #             return False
        #         i += 1
        #         j -= 1
        #     return True

        # i = 0
        # j = len(s) - 1

        # res = ''

        # while i <= j:
        #     if is_palindrome(s, i, j):
        #         return s[i:j+1]

        #     elif is_palindrome(s, i+1, j):
        #         return s[i+1:j+1]

        #     elif is_palindrome(s, i, j-1):
        #         return s[i:j]

        #     else:
        #         i += 1
        #         j -= 1

        # return res

        
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(s):
            i = 0
            j = len(s) - 1

            for k in range(len(s) // 2):
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        # when s="" or one char is there
        if not s or len(s) == 1:
            return s

        n = len(s)

        # We’re searching for palindromes from longest → shortest, so we can return early when found.
        for i in range(n, 0, -1):
            # visit all the possible substrs of lengths from max len to min len i.e 0
            for j in range(n - i + 1):
                if is_palindrome(s[j : j + i]):
                    return s[j : j + i]
        return ""


# https://leetcode.com/problems/longest-palindromic-substring/
