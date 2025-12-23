def build_path(node, path, target):
    # base
    if not node:
        return False

    # build the path
    path.append(node)

    # found the ele
    if node == target:
        return True

    if build_path(node.left, path, target) or build_path(node.right, path, target):
        return True

    # before returning to the pervious node( previous recursive function ) pop the current node's value from the sequence
    path.pop()

    # return false cuz
    # yaha tak aye h iska mtlb yahi hua na ki true kabhi return hua hi nhi tha
    return False
