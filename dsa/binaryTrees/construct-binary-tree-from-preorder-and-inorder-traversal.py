# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # hashmap to store inorder indices
        mp = {}
        for i in range(len(inorder)):
            mp[inorder[i]] = i

        # for efficient popping of elements from the left
        preorder = collections.deque(preorder)

        def helper(start, end):
            # base - This indicates no subtree exists for this range.
            if start > end:
                return None

            root = TreeNode(preorder.popleft())  # from the preorder
            mid = mp[root.val]  # index in the inorder list

            # Recursively build the left subtree
            root.left = helper(start, mid - 1)
            # Recursively build the right subtree
            root.right = helper(mid + 1, end)

            return root

        res = helper(0, len(inorder) - 1)
        return res

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/submissions/1868827900/
