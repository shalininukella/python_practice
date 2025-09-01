# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2

        headMerged = ListNode()
        currMerged = headMerged # like k in the res array to keep track of the res index

        while head1 != None and head2 != None:
            if head1.val < head2.val:
                currMerged.next = head1
                head1 = head1.next
            else:
                # head1.val > head2.val or head1.val == head2.val
                currMerged.next = head2
                head2 = head2.next
            
            currMerged = currMerged.next

        if head1 != None:
            currMerged.next = head1
        else:
            currMerged.next = head2

        return headMerged.next #cuz headMerged has 0 value initially and the required number started in the .next part

#recursive - didn't learn yet, learn it

# def mergeTwoLists(list1, list2):
#     if not list1 or not list2:
#         return list1 or list2

#     if list1.val < list2.val:
#         list1.next = mergeTwoLists(list1.next, list2)
#         return list1
#     else:
#         list2.next = mergeTwoLists(list1, list2.next)
#         return list2


#question

#https://leetcode.com/problems/merge-two-sorted-lists/submissions/1756366509/