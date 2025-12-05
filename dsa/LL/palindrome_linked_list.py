# 1. solution  1 - arrays

#     Time complexity: O(n)
#     Space complexity: O(n)

# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         arr = []

#         while head:
#             arr.append(head.val)
#             head = head.next
        
#         left = 0
#         right = len(arr) - 1

#         while left < right:
#             if arr[left] != arr[right]:
#                 return False
#             left += 1
#             right -= 1
        
#         return True
        

# 2. solution  2 - stacks (deque)

#     Time complexity: O(n)
#     Space complexity: O(n)

# from collections import deque

# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         st = deque()

#         # 1. Count length correctly
#         cnt = 0
#         temp = head
#         while temp:
#             cnt += 1
#             temp = temp.next

#         # 2. Push first half into stack
#         temp = head
#         for _ in range(cnt // 2):
#             st.append(temp.val)
#             temp = temp.next

#         # 3. Skip middle element for odd-length list
#         if cnt % 2 == 1:
#             temp = temp.next

#         # 4. Compare second half with stack
#         while temp:
#             if st.pop() != temp.val:
#                 return False
#             temp = temp.next
        
#         return True


# 3. solution  3 - fast and slow

#     Time complexity: O(n)
#     Space complexity: O(1)

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head 

        #1. find the center
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # slow will be at the center, if 2 centers are there then the slow will be the 2nd center

        #2. reverse the 2nd half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        first, second = head, prev

        #3. compare both the heads
        while second:
            if first.val != second.val:
                return False

            first = first.next
            second = second.next

        return True

# https://leetcode.com/problems/palindrome-linked-list/