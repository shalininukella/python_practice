# Time complexity : O(n)
#     Each tree node is:
#         Enqueued once
#         Dequeued once
#         Added to a result list once
#         Reversing a level costs O(k), but across all levels the total is still O(n)
# ✅ Overall: O(n), where n is the number of nodes in the tree.

# 💾 Space Complexity : O(n)
#     Breakdown:
#         Queue can hold up to O(n) nodes (worst case: last level of a complete tree)
#         Result list stores O(n) values
#         Temporary level list per iteration
# ✅ Overall auxiliary space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        res = []
        q = collections.deque()
        q.append(root)
        left_to_right = True
        
        while q:

            size = len(q)
            seq = []

            for i in range(size):
                curr = q.popleft()

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                
                seq.append(curr.val)

            #if the left to right flag is not true then we just need to reverse the seq list
            if not left_to_right:
                seq.reverse()
            
            left_to_right = not left_to_right
        
            res.append(seq)
 
        return res

#or just based on the flag insert in the seq in the reverse order

# Time Complexity: (O(n)) — Every node is visited once.
# Space Complexity: (O(n)) — For the output and queue.
# class Solution:
#     def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []

#         res = []
#         q = collections.deque()
#         q.append(root)
#         left_to_right = True

#         while q:
#             size = len(q)
#             seq = [0] * size

#             for i in range(size):

#                 curr = q.popleft()

#                 if curr.left:
#                     q.append(curr.left)
#                 if curr.right:
#                     q.append(curr.right)

#                 if left_to_right == True:
#                     index = i
#                 else:
#                     index = (size-1) - i
                
#                 seq[index] = curr.val
            
#             res.append(seq)
#             left_to_right = not left_to_right

#         return res

# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/submissions/1861874480/