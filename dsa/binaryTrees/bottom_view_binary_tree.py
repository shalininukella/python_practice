# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right



#✅ Time Complexity: O(N) where N is the number of nodes in the Binary Tree. This complexity arises from visiting each node exactly once during the BFS traversal.

#✅ Space Complexity: O(N/2 + N/2) where N represents the number of nodes in the Binary Tree.


# BFS approach
from collections import deque
class Solution:
    def bottomView(self, root):
        if not root:
            return []

        q = deque()
        q.append((root, 0))   # (node, column)
        mpp = {}              # column -> node.data

        while q:
            curr, col = q.popleft()

            # overwrite for bottom view
            mpp[col] = curr.data

            if curr.left:
                q.append((curr.left, col - 1))
            if curr.right:
                q.append((curr.right, col + 1))

        res = []
        for key in sorted(mpp.keys()):
            res.append(mpp[key])

        return res


# ✅Time Complexity: O(N + K log K)  →  O(N log N) (worst case)
#     DFS function : O(N)
#     Sorting takes:
#         👉 O(K log K) where K = number of distinct columns
#         Worst case: K = N, where N = no. of nodes

# ✅Total Space Complexity : O(N) = (map + recursion stack)
#     1️⃣ Map (mpp)
#         Stores one entry per column
#         Worst case: O(N)

#     2️⃣ Recursion stack
#         Depends on tree height H
#         Worst case (skewed tree): O(N)
#         Best case (balanced tree): O(log N)

## DFS approach
class Solution:
    def bottomView(self, root):
        if not root:
            return []

        mpp = {}   # col -> (node.data, row)

        def dfs(node, col, row):
            if not node:
                return

            # take the node if it is deeper (greater row)
            if col not in mpp or row >= mpp[col][1]:
                mpp[col] = (node.data, row)

            dfs(node.left, col - 1, row + 1)
            dfs(node.right, col + 1, row + 1)

        dfs(root, 0, 0)

        res = []
        for key in sorted(mpp.keys()):
            res.append(mpp[key][0])

        return res

# https://takeuforward.org/data-structure/bottom-view-of-a-binary-tree
