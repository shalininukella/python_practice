def find_min(root):
    if root is None:
        return None
    while root.left:
        root = root.left
    return root.data

def find_max(root):
    if root is None:
        return None
    while root.right:
        root = root.right
    return root.data


# Time Complexity - O(h), where h is the height of the BST
#     Best case (balanced BST): O(log n)
#     Worst case (skewed BST): O(n)

# Space complexity - O(1)
