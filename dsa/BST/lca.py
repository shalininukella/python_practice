# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# ✅Hare Krishna

# ✅ Recursive

# ✅Time complexity: O(h),
# You are not traversing the whole tree
# At every step, you move only one direction: left or right
# So the number of calls = height of the BST
#     Best / Average case (balanced BST): O(log n)
#     Worst case (skewed BST): O(n)

# ✅Space complexity: O(h)
# Recursive call stack goes as deep as the tree height
# No extra data structures

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

#         def helper(node):
#             # base
#             if not node:
#                 return None

#             # if both are on the left
#             if p.val < node.val and q.val < node.val:
#                 return helper(node.left)

#             # if both are on the right
#             elif p.val > node.val and q.val > node.val:
#                 return helper(node.right)

#             # when p is on the left, and q is on the left of the current node or vice versa, then the node is only the common parent
#             else:
#                 # it also has the case when p.val == node.val or q.val == node.val, then it will return itself (node)
#                 return node

#         res = helper(root)
#         return res

# ✅iterative

# ✅Time complexity: O(h)
# ✅Space complexity: O(1)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # no need of this condition cus in the constraints:
        # The number of nodes in the tree is in the range [2, 105].
        # if not root:
        #     return None

        while root:
            # if p and q on the left
            if p.val < root.val and q.val < root.val:
                root = root.left

            # if p and q on the right
            elif p.val > root.val and q.val > root.val:
                root = root.right

            # p and q on the opposite sides along with the case when:
                # p.val == node.val or
                # q.val == node.val
            else:
                return root

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/1865924052/
