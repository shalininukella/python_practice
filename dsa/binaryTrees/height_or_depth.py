#recursive

# Comlexity:
# TC - O(num of nodes) as we are traversing all the nodes of the tree
# SC - O(height of the tree) for the recursive stack

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:

#         def helper(node):
#             #base
#             if not node:
#                 return 0
            
#             right = 1 + helper(node.right)
#             left = 1 + helper(node.left)

#             return right if right >= left else left

#         res = helper(root)
#         return res

#backrtracking
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def helper(root):
            #base
            if not root:
                return 0

            left = helper(root.left)
            right = helper(root.right)

            return max(left, right) + 1

        res = helper(root)
        return res    

# https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/1859819528/   