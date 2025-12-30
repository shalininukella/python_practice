# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "null"

        res = []

        q = collections.deque()
        q.append(root)

        while q:
            node = q.popleft()

            # means when the tree comes, check if the node on which we are traversing is null or not
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("null")

        # res = ["1", "2", "3", "null", "4"] => "1,2,3,null,4"
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
    
            data = "1, 2, 3"
            data.split(',')
            # ['1', ' 2', ' 3']  ← spaces remain
        """
        if data == "null":
            return None

        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))

        q = collections.deque()
        q.append(root)
        i = 1

        while q:
            curr = q.popleft()

            if nodes[i] != "null":
                curr.left = TreeNode(int(nodes[i]))
                q.append(curr.left)
            i += 1

            if i < len(nodes) and nodes[i] != "null":
                curr.right = TreeNode(int(nodes[i]))
                q.append(curr.right)
            i += 1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/submissions/1868850676/
