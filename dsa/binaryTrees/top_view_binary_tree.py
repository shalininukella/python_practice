# time = O(n) = n is the no. of nodes in a balanced binary tree
#     bfs = O(n), 
#     for loop = O(n) ( worst case all the nodes like a pyramid and the inside khali)

# space = Space Complexity: O(N/2 + N/2) where N represents the number of nodes in the Binary Tree. 
#     The main space consuming data structure is the queue used for BFS traversal. It acquires space proportional to the number of nodes in the level it is exploring hence in the worst case of a balanced binary tree, the queue will have at most N/2 nodes which is the maximum width.
#     Additionally, the map is used to store the top view nodes based on their vertical positions hence its complexity will also be proportional to the greatest width level. In the worst case, it may have N/2 entries as well.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict
class Solution:
    def topView(self, root):
        if not root:
            return []

        res = []
        q = deque()
        col = 0 # root node
        q.append((root, col))
        mp = defaultdict(int) #dict to store key, val pairs of col and the node's value -> easily store the negatives

        # bfs
        while q:
            curr_node, col = q.popleft()
            
            # if the node at that col already exixts, don't add the node(it's hidden when seen from the top)
            if col not in mp:
                mp[col] = curr_node.data
            
            if curr_node.left:
                q.append((curr_node.left, col - 1))
            if curr_node.right:
                q.append((curr_node.right, col + 1))
        # sort based on the col cuz left most col no. will be neg and to the right pos
        for key in sorted(mp.keys()):
            res.append(mp[key])

        return res
# https://takeuforward.org/data-structure/top-view-of-a-binary-tree
            

