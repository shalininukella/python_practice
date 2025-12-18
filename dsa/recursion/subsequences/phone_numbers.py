##BACKTRACKING

# Time Complexity: O(4^N * N), where n is the length of the input digits. This is because each digit can map to up to 4 letters, and there are n digits.

# Space Complexity: O(N), where n is the length of the input digits. This is due to the recursion stack depth.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        seq = ""

        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def helper(i, seq):

            #base 
            if i == len(digits):
                res.append(seq)
                return

            letters = digit_to_letters[digits[i]]

            for char in letters:

                #take the char
                seq += char
                helper(i+1, seq)
 
                #not take
                seq = seq[:-1]

        helper(0, seq)
        return res

# https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/1858731206/
        