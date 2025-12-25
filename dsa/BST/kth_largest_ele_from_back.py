
# DFS - REVERSE OF INORDER TRAVERSAL
# reverse of the kth smallest
# Time complexity: O(n)
# In the worst case, we may need to visit all nodes.
# Space complexity: O(h)
# Due to recursion stack, where h is the height of the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0
        cnt = 0

        def dfs(node):
            nonlocal cnt, res

            # base
            if not node:
                return

            dfs(node.right)
            cnt += 1

            if cnt == k:
                res = node.val
                return
            dfs(node.left)

        dfs(root)
        return res
