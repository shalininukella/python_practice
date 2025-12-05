# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# #1. brute force - usign 2 loops, for each ele of 1st list, compare with the each ele of the 2nd list

# # Time Complexity: O(m × n) - TLE
# # Space Complexity: O(1)

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         while headA:
#             temp = headB
#             while temp:
#                 if temp == headA:
#                     return temp
#                 temp = temp.next

#             headA = headA.next

#         return None


##2. using hashing - use sets to store one list, then compare the each ele if present in the list or not

# # Time Complexity: O(m) + O(n)
# # Space Complexity: O(n), Storing list 1 node addresses in an unordered_set.

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         st = set()
#         while headA:
#             st.add(headA)
#             headA = headA.next

#         while headB:
#             if headB in st:
#                 return headB
#             headB = headB.next
        
#         return None


# #3. traversing the longest list from the point where both longest and shortest have equal no. of nodes to the end of the node

# #  Time Complexity: O(m) + O(n)
#         # Step 1: O(n + m)
#         #     while temp:   # list A
#         #     while temp:   # list B

#         # Step 2: O(|n − m|)
#         #     while diff:
#         #     #diff = abs(n - m) which is ≤ max(n, m)

#         # Step 3: O(min(n, m))
#         #     while headA != headB:
#         #     #This traversal is at most min(n, m)

#         # So - O(n + m) + O(|n − m|) + O(min(n, m)) = O(m+n)

# #  Space Complexity: O(1), No extra space is used.

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         l1 = 0
#         l2 = 0

#         #calculate the length of the list A
#         temp = headA
#         while temp:
#             l1 += 1
#             temp = temp.next

#         #calculate the length of the list B
#         temp = headB
#         while temp:
#             l2 += 1
#             temp = temp.next

#         #traverse to the point in the longest list from where both the lists have equal no. of nodes
#         if l1 > l2:
#             diff = l1 - l2
#             while diff:
#                 headA = headA.next
#                 diff -= 1

#         elif l2 > l1:
#             diff = l2 - l1
#             while diff:
#                 headB = headB.next
#                 diff -= 1
            
#         while headA != headB:
#             headA = headA.next
#             headB = headB.next
        
#         return headA
        

##4. optimal - using 3+2 = 5 and 2+3 = 5 priciple

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        i  = headA
        j = headB

        while i != j:
            i = i.next if i else headB
            j = j.next if j else headA

        return i

# https://leetcode.com/problems/intersection-of-two-linked-lists/