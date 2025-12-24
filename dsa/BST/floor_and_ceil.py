# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def floorCeilOfBST(self, root, key):
        def ceilVal(root, ceil):
            while root:
                if root.data == key:
                    ceil = root.data
                    break
                # you need to find the key or a number just greater than then key, be it any side
                elif key > root.data:
                    # go right
                    root = root.right
                else:
                    # when root.data >= key:
                    # update the result ciel and move to the next to find if we can find any better res
                    ceil = root.data
                    root = root.left
            return ceil

        def floorVal(root, floor):
            while root:
                if root.data == key:
                    floor = root.data
                    break
                elif root.data <= key:
                    floor = root.data
                    root = root.right
                else:
                    root = root.left
            return floor

        return [floorVal(root, -1), ceilVal(root, -1)]
