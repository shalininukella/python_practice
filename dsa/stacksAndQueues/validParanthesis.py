class Solution:
    def isValid(self, s: str) -> bool:
        mp = {"(" : ")", "{" : "}", "[" : "]"}
        stack = []
        
        for char in s:

            #if mp[char] present = means the char is an opening bracket -> so puch into the stack
            if char in mp:
                stack.append(char)

            #i.e mp[char] is not present = a closing bracket, so check if the last ele in the stack is the corresponding opening or not 
            else:
                if not stack or mp[stack[-1]] != char:
                    return False
                stack.pop()
        if not stack:
            return True #if the stack is empty
        else:
            return False
# https://leetcode.com/problems/valid-parentheses/