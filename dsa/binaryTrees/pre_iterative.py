# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# # recursive
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         def preorder(node):
#             #base case
#             if node is None:
#                 return

#             res.append(node.val)
#             preorder(node.left)
#             preorder(node.right)

#         preorder(root)
#         return res

# #iterative - 1
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         stack = collections.deque()
#         curr = root

#         while stack or curr:

#             while curr:
#                 stack.append(curr)
#                 res.append(curr.val)
#                 curr = curr.left
            
#             curr = stack.pop()
#             curr = curr.right

#         return res


#iterative - 2
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        stack = collections.deque()
        curr = root

        while curr or stack:

            if curr:
                stack.append(curr)
                res.append(curr.val)
                curr = curr.left
            
            else:
                curr = stack.pop()
                curr = curr.right

        return res
    
# https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/1859727304/