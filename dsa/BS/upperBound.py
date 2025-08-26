def upperBound(arr: [int], x: int, n: int) -> int:
    # Write your code here.
    low = 0
    n = len(arr)
    high = n-1
    ans = n
    while low <= high:
        mid = low + (high-low)//2
        if x < arr[mid]:
            ans = mid
            high = mid - 1
        else:
            low = mid+1
    return ans
# https://www.naukri.com/code360/problems/implement-upper-bound_8165383?leftPanelTabValue=SUBMISSIO
    