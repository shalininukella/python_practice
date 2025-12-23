# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# BFS

# time = O(n)
# space = O(n)
#     in a queue at max n/2 nodes will be stored, and res list has at max n nodes.
#     hence O(n)


# from collections import deque
# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []

#         q = deque()
#         q.append(root)

#         res = []

#         while q:
#             size = len(q)

#             for i in range(size):
#                 curr = q.popleft()

#                 #append only the last element in the loop in a level
#                 if i == (size - 1):
#                    res.append(curr.val)
#                 if curr.left:
#                     q.append(curr.left)
#                 if curr.right:
#                     q.append(curr.right)

#         return res


# DFS

# time = O(n) - dfs
# space = O(n)​
    # res list = O(n)
    # dfs = Height of the tree = h
    #     Best case (balanced): O(logn)
    #     Worst case (skewed): O(n)

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs_right_first(node, row):
            #base
            if not node:
                return

            # the res will be at the level where we need to add the ele for the first time
            if row == len(res):
                res.append(node.val)
            
            dfs_right_first(node.right, row + 1)
            dfs_right_first(node.left, row + 1)

        dfs_right_first(root, 0)
        return res

# https://leetcode.com/problems/binary-tree-right-side-view/submissions/1863039711/        