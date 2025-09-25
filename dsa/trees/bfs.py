# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        if root is None:
            return ans

        q = collections.deque()
        q.append(root)

        while q:

            level = []

            for i in range(len(q)):

                curr = q.popleft()

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

                level.append(curr.val)

            ans.append(level)

        return ans


# https://leetcode.com/problems/binary-tree-level-order-traversal/
