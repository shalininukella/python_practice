# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N), as ach node is visited once.
# Space Complexity: O(N), for the hashmap and recursion stack (worst case when tree is skewed).

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        mp = {}
        for i in range(len(inorder)):
            mp[inorder[i]] = i

        def helper(start, end):
            if start > end:
                return None

            root = TreeNode(postorder.pop())
            mid = mp[root.val]

            root.right = helper(mid + 1, end)
            root.left = helper(start, mid - 1)

            return root

        res = helper(0, len(inorder) - 1)
        return res
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/submissions/1868831069/
