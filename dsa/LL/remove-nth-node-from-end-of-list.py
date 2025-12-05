# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# #brute force - 2 passes - mysolution
# # time = O(n)
# # space = O(1)

# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

#         temp = head
#         cnt = 0

#         while temp: #temp.next if not None then only temp.next.next will work
#             temp = temp.next
#             cnt += 1

#         if cnt == 1: #when only one element is there
#             return None

#         if cnt-n == 0: #when n == cnt(len of the ll), then remove the first element
#             return head.next

#         temp = head

#         # Traverse to the node before target
#         for i in range(cnt - n - 1):
#             temp = temp.next
        
#         x = temp.next
#         temp.next = temp.next.next
#         del x

#         return head



class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head #take it till the end of the linked list
        slow = head #maintain the gap one less than n i.e pointer to the node before the nth node

        for i in range(n):
            fast = fast.next

        #edge case when length of ll == n
        if not fast:
            return head.next #the fast = None from the loop, fast = fast.next make it run n times and makes it point outside of the end of the ll

        while fast.next: #not while fast:, cuz we need fast at the last node of the ll, not out of the loop, the loop exixts when fast is out of the loop if we write while fast:
            fast = fast.next
            slow = slow.next

        #now slow is at one before the nth node of from the last
        slow.next = slow.next.next

        return head
        
# # https://leetcode.com/problems/remove-nth-node-from-end-of-list/