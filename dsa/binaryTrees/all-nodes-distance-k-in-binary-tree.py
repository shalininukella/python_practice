# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# BFS + parent mapping (converts a tree into a graph)

# Time Complexity: O(N), 
    # building the parent map = BFS = O(N). 
    # BFS traversal from the target, O(N). 
    # N = no. of nodes in the binary tree.

# Space Complexity: O(N) , 
        # The parent map stores one entry per node,O(N). 
        # The queue and visited set used in BFS also take up to O(N) space in the worst case.     Therefore, the total space complexity is O(N).

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        mp = {} # store the node's val and it's parent
        q = collections.deque()
        q.append(root)

        # build the map for each node's parents for moving upwards
        while q:
            curr = q.popleft()

            if curr.left:
                q.append(curr.left)
                mp[curr.left.val] = curr

            if curr.right:
                q.append(curr.right)
                mp[curr.right.val] = curr

        visited = {} # store the visitied nodes
        q.append(target)

        # now from the taget move in all the three directions by 1
        while q and k > 0:
            size = len(q)

            for i in range(size):
                curr = q.popleft()

                visited[curr.val] = 1

                if curr.left and curr.left.val not in visited:
                    q.append(curr.left)

                if curr.right and curr.right.val not in visited:
                    q.append(curr.right)

                if curr.val in mp and mp[curr.val].val not in visited:
                    q.append(mp[curr.val])
            
            #decrement the k to keep track of the distance
            k -= 1

        res = []
        for i in range(len(q)):
            res.append(q.popleft().val)

        return res
    
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/submissions/1867036036/