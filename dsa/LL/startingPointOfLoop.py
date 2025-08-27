# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head 

        while fast and fast.next and slow:

            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                break
        
        if not fast or not fast.next:
            #no cycle
            return None
        
        fast = head

        while fast != slow:
            fast = fast.next
            slow = slow.next

        return slow

# Nice solution

# https://leetcode.com/problems/linked-list-cycle-ii/solutions/6750409/video-3-solutions-two-pointer-set-and-recursion     

# Question

# https://leetcode.com/problems/linked-list-cycle-ii/submissions/1749605876/