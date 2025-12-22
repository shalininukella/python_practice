# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#recursive
# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
        
#         def helper(root):

#             #base
#             if not root:
#                 return 
            
#             helper(root.left)
#             helper(root.right)
#             res.append(root.val)

#         helper(root)
#         return res

#iterative - 1 - reversal algorithm - reverse of preorder
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        stack = collections.deque()
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                res.append(curr.val)
                curr = curr.right

            curr = stack.pop()
            curr = curr.left
        res.reverse() 
        return res

# #iterative - 2 - reversal algorithm - reverse of preorder
# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:          
            
#         while curr or stack:

#             if curr:
#                 res.append(curr.val) # Add before going to children
#                 stack.append(curr)
#                 curr = curr.right
            
#             else:
#                 curr = stack.pop()
#                 curr = curr.left
            
#         res.reverse()
#         return res

# https://leetcode.com/problems/binary-tree-postorder-traversal/submissions/1859752596/