# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right


# 1. min max approach - refer the notepad

# Time: O(h) where h is height of BST
# Space: O(1) (iterative, no recursion)

class Solution:
    def succPredBST(self, root, key):
        
        def succ(root):
            succ = None

            while root:
                if key >= root.data:
                    # go right and find the greater ele greater than the key
                    root = root.right
                
                # go left, and greater ele of the key for now is the root
                else:
                    # key.data < root.data:
                    succ = root.data
                    root = root.left
                
            return -1 if not succ else succ
        
        def pre(root):
            pre = None

            while root:
                # go left and find the next smaller ele smaller than the key
                if key <= root.data:
                    root = root.left
                else:
                    # key.data > root.data:
                    pre = root.data
                    root = root.right
            return -1 if not pre else pre

        return [pre(root), succ(root)]

# 2. inorder traversal, then sorted array, then bs on the sorted array
# 3. Morris traversal


# https://takeuforward.org/data-structure/inorder-successorpredecessor-in-bst
 