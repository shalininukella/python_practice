# Time Complexity: O(2^n) (Catalan number): C(n) = (2n)! / (n!(n+1)!) is the number of valid sequences.
# Each sequence takes O(n) to build.
# So, total complexity: O(C(n) × n)

# Space Complexity: O(n) recursion depth.
# O(C(n) × n) to store results.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def constructSequence(seq, open_cnt, close_cnt):
            if len(seq) == 2 * n:
                res.append(seq)
                return

            if open_cnt < n:
                constructSequence(seq + "(", open_cnt+1, close_cnt)
            
            if close_cnt < open_cnt: #close_cnt < open_cnt bcuz, then above if might have exited only when open open_cnt == n
                constructSequence(seq + ")", open_cnt, close_cnt+1)
            
        constructSequence("", 0, 0)
        return res

            
# https://leetcode.com/problems/generate-parentheses/      