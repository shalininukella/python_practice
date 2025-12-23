# refer the right_view

# DFS

import collections

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs_left_first(node, row):
            #base
            if not node:
                return
            
            # add the node for the first time
            if len(res) == row:
                res.append(node.val)

            dfs_left_first(node.left, row + 1)
            dfs_left_first(node.right, row + 1)

        dfs_left_first(root, 0)
        return res

# BFS
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = collections.deque()
        q.append(root)

        res = []

        while q:
            size = len(q)

            for i in range(size):
                curr = q.popleft()

                #append the starting element of each level
                if i == 0:
                    res.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return res
                

