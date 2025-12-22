# Time Complexity: O(N), each node is processed once in DFS Traversal.
# Space Complexity: O(H), auxiliary stack space, where H is height of Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int: 
        maxi = root.val

        def helper(node):
            nonlocal maxi
            #base 
            if not node:
                return 0

            # to avoid negative numbers, igore them by computing max on 0 and the recursively computed maximum sum of the left and right subtree paths
            left_sum = max(0, helper(node.left))
            right_sum = max (0, helper(node.right))

            # update the maximum path sum encountered so far(with split)
            maxi = max(maxi, (left_sum + right_sum + node.val))

            # return the maximum sum of the path(without split)
            return node.val + max(left_sum, right_sum)

        helper(root)
        return maxi
# https://leetcode.com/problems/binary-tree-maximum-path-sum/submissions/1861750563/