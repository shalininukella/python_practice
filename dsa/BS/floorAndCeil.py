def getFloorAndCeil(a, n, x):
    # Write your code here.
    low = 0
    high = n-1
    ceil = -1
    floor = -1
    while low<=high:
        mid = low+(high-low)//2
        if a[mid] <= x:
            floor = mid
            low = mid + 1
        else:
            high = mid - 1

    low = 0
    high = n - 1
    while low <= high:
        mid = low + (high-low)//2
        if a[mid] >= x:
            ceil = mid
            high = mid - 1
        else:
            low = mid+1

    floor_val = a[floor] if floor != -1 else -1
    ceil_val = a[ceil] if ceil != -1 else -1
    return floor_val, ceil_val
# https://www.naukri.com/code360/problems/ceiling-in-a-sorted-array_1825401?leftPanelTabValue=SUBMISSION
    
