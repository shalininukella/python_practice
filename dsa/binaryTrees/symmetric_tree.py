# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time complexity: O(n)
# Space complexity: O(h)

#DFS

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(p, q):

            # if both the nodes are null
            if not p and not q:
                return True

            # if any one of them is null
            if not p or not q:
                return False

            is_left = dfs(p.left, q.right)
            is_right = dfs(p.right, q.left)

            is_same_data = p.val == q.val
            # at each side, need to check if both or equal or not
            return is_left and is_right and is_same_data
        
        res = dfs(root.left, root.right)
        return res

# https://leetcode.com/problems/symmetric-tree/submissions/1863077731/