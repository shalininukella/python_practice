# Time complexity: O(min(N,M))
# Space complexity: O(min(H1,H2)), where H1 and H2 are the heights of the two trees,

#     Best case (balanced tree): O(log n) or O(log m)
#     Worst case (skewed tree): O(n) or O(m)
# where n = height of the first tree
#       m = height of the second tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def helper(p, q):

            # both are null
            if (not p) and (not q): 
                return True

            # one is null, the other isn't
            if not p or (not q): 
                return False
            
            is_left = helper(p.left, q.left)
            is_right = helper(p.right, q.right)

            return is_left and is_right and p.val == q.val

        res = helper(p, q)
        return res

# https://leetcode.com/problems/same-tree/submissions/1861825463/   
