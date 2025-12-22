# Time Complexity: O(N) where N is the number of nodes in the Binary Tree.
# Space Complexity: O(N) where N is the number of nodes in the Binary Tree to store the boundary nodes of the tree. 
# O(H) or O(log2N) Recursive stack space while traversing the tree. In the worst case scenario the tree is skewed and 
# the auxiliary recursion stack space would be stacked up to the maximum depth of the tree, resulting 
# in an O(N) auxiliary space complexity.

class Solution:
    def boundary(self, root):
        res = []

        if not root:
            return res

        def is_leaf(node):
            return not node.left and not node.right

        # 1. Root
        if not is_leaf(root):
            res.append(root.data)

        # 2. Left Boundary (excluding leaves)
        curr = root.left
        while curr:
            if not is_leaf(curr):
                res.append(curr.data)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right

        # 3. Leaf Nodes
        def add_leaves(node):
            if not node:
                return
            if is_leaf(node):
                res.append(node.data)
                return
            add_leaves(node.left)
            add_leaves(node.right)

        add_leaves(root)

        # 4. Right Boundary (excluding leaves, bottom-up)
        curr = root.right
        temp = []
        while curr:
            if not is_leaf(curr):
                temp.append(curr.data)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left

        res.extend(reversed(temp))

        return res

# https://takeuforward.org/data-structure/boundary-traversal-of-a-binary-tree

# https://leetcode.com/problems/boundary-of-binary-tree/