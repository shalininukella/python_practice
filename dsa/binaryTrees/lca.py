# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


## My Solution - DFS BRUTE FORCE ( REDUCE THE SPACE COMPLEXITY )

# Time Complexity: O(N) — each node is visited once when building paths.
# Space Complexity: O(N) — storing paths for p and q

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/1863662236/

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

#         if not root:
#             return None

        # def build_path(node, path, target):

        #     # base
        #     if not node:
        #         return False

        #     # build the path
        #     path.append(node)

        #     # found the ele
        #     if node == target:
        #         return True

        #     if build_path(node.left, path, target) or build_path(node.right, path, target):
        #         return True

        #     # before returning to the pervious node( previous recursive function ) pop the current node's value from the sequence
        #     path.pop()

        #     # return false cuz
        #     # yaha tak aye h iska mtlb yahi hua na ki true kabhi return hua hi nhi tha
        #     return False 

#         path_p = []
#         path_q = []

#         build_path(root, path_p, p)
#         build_path(root, path_q, q)

#         p_path_len = len(path_p)
#         q_path_len = len(path_q)

#         res = None
#         # compare 
#         for i in range(min(p_path_len, q_path_len)):
#             if path_p[i] == path_q[i]:
#                 res = path_p[i]
#             else:
#                 break
#         return res


# DFS - optimal 

# time = O(n) - dfs each node
# space = O(h), h = logn or n

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # base - mainly to return something at the node
        # if root is null return None
        if (root is None):
            return root
        elif root == p:
            return root
        elif root == q:
            return root
        
        # Search in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # Result
        if not left and not right:
            return None
        if not left:
            return right
        elif not right:
            return left
        # if both are present, return the parent of left and right, i.e the curr node
        else:
            return root

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/1863673569/