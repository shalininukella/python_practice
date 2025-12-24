# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


## DFS 


# Time Complexity: O(log N),Each step eliminates half of the tree, just like binary search. However, in the worst case (unbalanced tree), it could be O(N).

# Space Complexity:O(h) 
#     worst case = O(n)
#     best =  O(logn)

# class Solution:
#     def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

#         if not root:
#             return None

#         if val == root.val:
#             return root
#         # go right
#         if val > root.val:
#            return self.searchBST(root.right, val)
#         #go right
#         if val < root.val :
#             return self.searchBST(root.left, val)



# BFS     

# Time Complexity: O(log N),Each step eliminates half of the tree, just like binary search. However, in the worst case (unbalanced tree), it could be O(N).

# Space Complexity:O(1),Iterative solution uses constant space as no recursion stack is involved.

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        while root:
            if val == root.val:
                break
            elif val > root.val:
                root = root.right
            else:
                root = root.left

        return root
         

# https://leetcode.com/problems/search-in-a-binary-search-tree/submissions/1864330843/       