def linearSearch(n: int, num: int, arr: [int]) -> int:
    # Write your code here.
    idx = -1
    n = len(arr)
    for i in range(n):
        if num == arr[i]:
            idx = i
            break

# https://www.naukri.com/code360/problems/linear-search_6922070?leftPanelTabValue=SUBMISSION
