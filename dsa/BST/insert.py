# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity :- BigO(N), where N is height of binary search tree

# Space Complexity :- BigO(1)

# iterative
# class Solution:
#     def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         if not root:
#             return TreeNode(val)

#         node = root

#         while True:

#             if val > node.val:
#                 if node.right:
#                     node = node.right
#                 else:
#                     node.right = TreeNode(val)
#                     break
#             else:
#                 if node.left:
#                     node = node.left
#                 else:
#                     node.left = TreeNode(val)
#                     break
#         return root


# Time Complexity :- BigO(N)

# Space Complexity :- BigO(H) as considering recursion stack, takes place in internal memory, if not consider then O(1)

# recursive
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return TreeNode(val)
            if val > node.val:
                # right
                node.right = dfs(node.right)
            else:
                node.left = dfs(node.left)
            return node
        res = dfs(root)
        return res

# https://leetcode.com/problems/insert-into-a-binary-search-tree/submissions/1864504883/
