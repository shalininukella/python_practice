# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
# h1 = l1
# h2 = l2
# n1 = ""
# n2 = ""

# # Convert l1 to a string (reverse the order while traversing)
# while h1 is not None:
#     n1 = str(h1.val) + n1  # Prepend each digit (reverse order)
#     h1 = h1.next

# # Convert l2 to a string (reverse the order while traversing)
# while h2 is not None:
#     n2 = str(h2.val) + n2  # Prepend each digit (reverse order)
#     h2 = h2.next

# n1 = int(n1)
# n2 = int(n2)

# sumi = n1 + n2
# sumi = str(sumi)
# sumi = sumi[::-1]

# dummy = ListNode()
# current = dummy

# for digit in sumi:
#     current.next = ListNode(int(digit))
#     current = current.next

# return dummy.next  # Return the next node (the actual head)


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        total = 0
        carry = 0

        dummy = ListNode()
        curr = dummy

        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next

            if l2:
                total += l2.val
                l2 = l2.next

            carry = total // 10  # except the one's digit
            num = total % 10  # last digit (one's digit) - remainder

            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next


# https://leetcode.com/problems/add-two-numbers/
