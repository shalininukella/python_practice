# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

# 📌📌“DFS is more space-efficient for deep trees; BFS avoids recursion depth issues.”
# Both DFS and BFS run in O(N) time.
# DFS uses O(H) space due to recursion, while BFS uses O(N) space due to the queue.

# DFS

# Complexity

#     Time: O(N) — every node visited once
#     Space: O(H) — recursion stack (H = tree height)


class Solution:
    def allRootToLeaf(self, root):

        res = []
        seq = []

        def is_leaf(node):
            return (not node.right) and (not node.left)

        def dfs(node, seq):
            if not node:
                return
            
            #for every node add in the sequence
            seq.append(node.data)

            if is_leaf(node):
                res.append(seq[:])
        
            dfs(node.left, seq)
            dfs(node.right, seq)
        
            seq.pop()

        dfs(root, seq)
        return res
        
#BFS

# Complexity

#     Time: O(N) — every node visited once
#     Space: O(N) — Queue can store up to O(N) nodes (with path copies).

from collections import deque

class Solution:
    def allRootToLeaf(self, root):
        if not root:
            return []

        res = []
        q = deque()
        q.append((root, [root.data]))

        while q:
            curr, path_till_curr = q.popleft()

            # if leaf node
            if (not curr.left) and (not curr.right):
                res.append(path_till_curr)

            # else, build the path for the next left and right nodes of this curr
            if curr.left:
                q.append((curr.left, path_till_curr + [curr.left.data]))
            if curr.right:
                q.append((curr.right, path_till_curr + [curr.right.data]))

        return res

# https://takeuforward.org/data-structure/print-root-to-node-path-in-a-binary-tree
# https://takeuforward.org/plus/dsa/problems/print-root-to-note-path-in-bt