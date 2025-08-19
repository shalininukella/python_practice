class Solution:
    def reverseWords(self, s: str) -> str:
        wordList = s.split() #splits the input string s into a list of words. The split() method, without any arguments, automatically splits the string by whitespace and removes extra spaces.
        n = len(wordList)
        res = ""
        for i in range(n-1, -1, -1):
            res += wordList[i] + " "
        
        return res.strip()
# https://leetcode.com/problems/reverse-words-in-a-string/


        