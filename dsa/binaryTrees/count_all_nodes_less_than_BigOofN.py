# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity - O(log n * log n)
# Space (recursion stack) - O(log n)

# REFER NOTEPAD AND STRIVER

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def right_height(node):
            height = 0
            while node:
                height += 1
                node = node.right
            return height

        def left_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        def helper(node):

            left = left_height(node)
            right = right_height(node)

            if left == right:
                # return 2^h - 1
                return (1 << left) - 1
            else:
                # 1 plus is for the root
                return 1 + helper(node.left) + helper(node.right)

        res = helper(root)
        return res

# https://leetcode.com/problems/count-complete-tree-nodes/submissions/1867563575/
