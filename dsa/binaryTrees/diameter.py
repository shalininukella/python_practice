# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def helper(root):
            nonlocal res  # allows us to modify the outer function's (diameterOfBinaryTree()) res, else it creates a local copy of the res and finally the outer functions res will not be changed.

            if not root:
                return 0
            
            left = helper(root.left)
            right = helper(root.right)

            res = max(res, left + right) #we are using max to save the case where the Diameter does NOT go through the root

            return max(left, right) + 1

        helper(root) # no need to assign; we only care about res
        return res

# https://leetcode.com/problems/diameter-of-binary-tree/submissions/1861053237/