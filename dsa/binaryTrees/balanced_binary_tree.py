# Optimized: O(N) — Single-pass DFS with height + balance check.
# Space: O(N) (worst case skewed tree), O(log N) (balanced).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def goright(node):
            if not node:
                return [0, True]

            max_right, right_balanced = goright(node.right)
            max_left, left_balanced = goright(node.left)

            diff = abs(max_left - max_right)
            is_balanced = right_balanced and left_balanced and diff <= 1

            return [max(max_left, max_right) + 1, is_balanced]
        
        max_height, is_balanced = goright(root)

        if is_balanced:
            return True
        return False
 
# https://leetcode.com/problems/balanced-binary-tree/submissions/1861019160/