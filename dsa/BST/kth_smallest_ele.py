# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# DFS - INORDER TRAVERSAL

# Time complexity: O(n)
# In the worst case, we may need to visit all nodes.
# Space complexity: O(h)
# Due to recursion stack, where h is the height of the tree.


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        res = 0

        def dfs(node):
            nonlocal cnt, res
            # base
            if not node:
                return

            dfs(node.left)

            cnt += 1  # increment the number of visited nodes , this counts the current node

            if k == cnt:  # found the node
                res = node.val
                return

            dfs(node.right)

        dfs(root)
        return res

#  https://leetcode.com/problems/kth-smallest-element-in-a-bst/submissions/1865332837/
