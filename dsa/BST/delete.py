# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# https://leetcode.com/problems/delete-node-in-a-bst/submissions/1865278383/
#standard recursive solution

# Time Complexity : O(h) = h = height of the tree.
# (Worst case Time Complexity : O(n) )

# Space complexity: O(h) = recursive stack

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # if the left subtree of the key is not present
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # node to be deleted is found
            # find the inorder successor

            curr = root.right
            while curr.left:
                curr = curr.left
            
            # replace node to be delted with this smallest ele of the right subtree
            root.val = curr.val

            # now delete this curr
            # so this root(replaced one) should be linked to a subtree with the deleted curr node
            root.right = self.deleteNode(root.right, curr.val)

        return root


#-------------------------------------------------------------------------------------------

# recursive

# Time = O(h)
#     Balanced BST:
#     h = log n → O(log n)

#     Skewed BST (like a linked list):
#     h = n → O(n)

# Space = O(1) auxiliary space


# https://leetcode.com/problems/delete-node-in-a-bst/submissions/1865297439/

# class Solution:
#     def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

#         def helper(node):
#             if not node.left:
#                 return node.right
#             if not node.right:
#                 return node.left

#             #else when both exists
#             curr = node.left
#             while curr.right:
#                 curr = curr.right

#             curr.right = node.right
#             return node.left    
        
#         if not root:
#             return None

#         if root.val == key:
#             return helper(root)

#         # else when the root is not the key 
#         # find the key
#         # this while loop will break only when the root is null, root becomes null only when we couldn't find the key

#         temp = root
#         while temp:

#             # key on right
#             if key < temp.val:
#                 if temp.left and temp.left.val == key:
#                     temp.left = helper(temp.left)

#                 else:
#                     # temp.left.val != key
#                     # just go left
#                     temp = temp.left

#             # key on right
#             else:
#                 # key > temp.val:
#                 if temp.right and temp.right.val == key:
#                     temp.right = helper(temp.right)
#                 else:
#                     temp = temp.right

#         return root
