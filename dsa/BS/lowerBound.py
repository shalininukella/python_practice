def lowerBound(arr: [int], n: int, x: int) -> int:
    # Write your code here
    n = len(arr)
    low = 0
    high = n-1
    ans = n
    while low <= high:
        mid = (low+high)//2
        if x <= arr[mid]:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1 
    return ans
    

# https://www.naukri.com/code360/problems/lower-bound_8165382?leftPanelTabValue=PROBLEM