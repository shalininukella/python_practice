# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#If the list has no cycle, fast reaches None and we return False.
#If the list has a cycle, the fast pointer must eventually meet the slow pointer, their meet is guaranteed.
    
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next and slow:
#because fast.next.next would crash if fast.next is None, 
    #AttributeError: 'NoneType' object has no attribute 'next'
            
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
            
        return False
# https://leetcode.com/problems/linked-list-cycle/submissions/1749593572/
