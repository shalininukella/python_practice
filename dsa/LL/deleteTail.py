from operator import le, length_hint
from pyparsing import null_debug_action


class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def delete_tail(head):
    #single ele or empty
    while head is Node or head.next is None:
        return None
    
    #don't tamper the head, cuz we're gonna return the head
    temp = head

    while temp.next.next is not None:
        temp = temp.next
    
    #when we reach at the second last ele
    temp.next = None

    return head

def printLL(head):
    lengthLL = 0
    while head is not None:
        print(head.val, end=" ")
        head = head.next
        lengthLL += 1 
    print()
    print(lengthLL, "is the length")

if __name__ == "__main__":
    a = arr = [12, 8, 5, 7]


    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])

    #print
    print("Before deleting:")
    printLL(head)

    #insert at head
    head = delete_tail(head)

    #print the modified ll
    print("After deleting:")
    printLL(head)


