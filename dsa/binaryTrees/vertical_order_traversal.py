# time = O(nlogn)
#     O(n) for dfs, 
#     O(nlogn) for sorting the n nodes, and 
#     O(n) for putting from nodes to res (for loop)
# space = O(n)​
#     nodes list = O(n)
#     res list = O(n)
#     dfs = Height of the tree = h
#         Best case (balanced): O(logn)
#         Worst case (skewed): O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = []

        # dfs
        def dfs(node, col, row):
            # base
            if not node:
                return
            
            nodes.append((col, row, node.val))
    
            dfs(node.left, col - 1, row + 1)
            dfs(node.right, col + 1, row + 1)

        dfs(root, 0, 0) #call the dfs function
        nodes.sort() # will be sorted based on col then row then val

        res = []
        prev_col = float("-inf")

        for (col, row, val) in nodes:
            #if the columns are not equal then append a new list then append the val
            if col != prev_col:
                res.append([])
                prev_col = col
            res[-1].append(val)

        return res

# can do using bfs also. In python not much useful, but in cpp, maps, sets will automatically order the values, no extra sort method.

# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/submissions/1862712405/
            
