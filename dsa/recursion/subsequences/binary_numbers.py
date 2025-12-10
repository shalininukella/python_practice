# #my approach

# class Solution:
#     def generateBinaryStrings(self, n):
#         # Your code goes here
#         res = set()
#         self.helper(n, "0", "", res)
#         self.helper(n, "1", "", res)
#         return sorted(res)

#     def helper(self, n, curr, seq, res):

#         # if two 1's appear consecutively, stop
#         if len(seq) > 0 and curr == "1" and seq[-1] == "1":
#             return

#         # if complete binary string formed
#         if len(seq) == n:
#             res.add(seq)
#             return

#         # build sequence
#         seq = seq + curr

#         # try adding 0 and 1
#         self.helper(n, "0", seq, res)
#         self.helper(n, "1", seq, res)


#easier 
# Time Complexity: O(2^n), since each position has 2 choices.
# Space Complexity: O(n) per recursive path (due to call stack)

class Solution:
    def generateBinaryStrings(self, n):
        res = []
        self.helper(n, "", res)
        return res

    def helper(self, n, seq, res):

        if len(seq) == n:
            res.append(seq)
            return

        # Always allowed to add '0'
        self.helper(n, seq + "0", res)

        # Allowed to add '1' only if previous char != '1'
        if not seq or seq[-1] != "1":
            self.helper(n, seq + "1", res)



            