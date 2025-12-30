# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS + indexing

# AS EACH NODE IS VISITED ONCE
# Time Complexity O(N)
# Space Comlexity O(N)

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append((root, 0))
        max_width = 1

        while q:
            size = len(q)
            # min idx is the index of the first element in each level
            min_idx = q[0][1]

            # first and last indices in each level
            first_i = 0
            last_i = 0

            for i in range(size):
                curr, curr_idx = q.popleft()

                # from segment trees concept, we will have the respective indices
                # left child will be 2 * idx + 1
                # right chils will be 2 * idx + 2

                # to avoid the overflow of 2*curr_idx if curr_idx is too large
                idx = curr_idx - min_idx

                if i == 0:
                    first_i = idx

                elif i == size-1:
                    last_i = idx

                if curr.left:
                    q.append((curr.left, (idx * 2) + 1))
                if curr.right:
                    q.append((curr.right, (idx * 2) + 2))

            # for every level calculate the maximum width
            max_width = max(max_width, last_i - first_i + 1)

        return max_width

# https://leetcode.com/problems/maximum-width-of-binary-tree/submissions/1866952976/
