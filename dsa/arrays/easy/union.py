from typing import List

def sortedArray(a: List[int], b: List[int]) -> List[int]:
    n = len(a)
    m = len(b)
    res = []
    i = j = 0

    while i < n and j < m:
        if a[i] < b[j]:
            if not res or res[-1] != a[i]:
                res.append(a[i])
            i += 1
        elif a[i] > b[j]:
            if not res or res[-1] != b[j]:
                res.append(b[j])
            j += 1
        else:  # a[i] == b[j]
            if not res or res[-1] != a[i]:
                res.append(a[i])
            i += 1
            j += 1

    # Remaining elements from a
    while i < n:
        if not res or res[-1] != a[i]:
            res.append(a[i])
        i += 1

    # Remaining elements from b
    while j < m:
        if not res or res[-1] != b[j]:
            res.append(b[j])
        j += 1

    return res

# https://www.naukri.com/code360/problems/sorted-array_6613259?leftPanelTabValue=SUBMISSION