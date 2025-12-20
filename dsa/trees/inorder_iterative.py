# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # res = []
        # def helper(root):

        #     #base case 
        #     if root is None:
        #         return

        #     helper(root.left)
        #     res.append(root.val)
        #     helper(root.right)
        
        # helper(root)
        # return res

#iterative

# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
#         res = []
#         stack = collections.deque()
#         curr = root

#         while stack or curr:
#             # go left as far as possible
#             while curr:
#                 stack.append(curr)
#                 curr = curr.left
            
#             curr = stack.pop()
#             res.append(curr.val)
#             curr = curr.right

#         return res

# https://leetcode.com/problems/binary-tree-inorder-traversal/submissions/1859635885/

#iterative - 2
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        stack = collections.deque()
        curr = root

        while stack or curr:

            if curr:
                stack.append(curr)
                curr = curr.left
            
            else:
                curr = stack.pop()
                res.append(curr.val)
                curr = curr.right

        return res