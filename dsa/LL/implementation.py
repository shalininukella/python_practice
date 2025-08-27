class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
        #next is a reference to another object holding value and the next i.e the node of the ll

def printLL(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()

def insertAtHead(head, val):
    temp = Node(val, head)
    return temp

if __name__ == "__main__":
    arr = [12, 8, 5, 7]
    val = 100

    head = Node(arr[0]) #head stores the reference to the object holding the val = arr[0] and the next = None, next is again an object's reference
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])

    #print
    print("Before inserting at head:")
    printLL(head)

    #insert at head
    head = insertAtHead(head, val)

    #print the modified ll
    print("After inserting at head:")
    printLL(head)