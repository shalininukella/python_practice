# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# iterative inorder traversal using stack

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = collections.deque()
        prev = None

        while stack or root:

            # go till the left most leaf
            while root:
                stack.append(root)
                root = root.left

            # comes out of the loop when leaf node
            root = stack.pop()

            # check if this poped one is greater than the previous val
            if prev and root.val <= prev.val:
                return False

            prev = root

            #go right
            root = root.right

        return True

# https://leetcode.com/problems/validate-binary-search-tree/submissions/1865349739/


# recursive inorder

# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         prev = float(-inf)

#         def helper(curr):
#             nonlocal prev

#             if not curr:
#                 return True
            
#             # go left till the leaf
#             left = helper(curr.left)

#             # work on each of the nodes(means the current function)

#             if not left:
#                 return False

#             if curr.val <= prev:
#                 return False
#             prev = curr.val

#             # go right
#             right = helper(curr.right)
#             if not right:
#                 return False
            
#             else:
#                 return True


#         return helper(root)

# https://leetcode.com/problems/validate-binary-search-tree/submissions/1865830977/