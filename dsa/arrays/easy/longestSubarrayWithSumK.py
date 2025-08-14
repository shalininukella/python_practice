#sliding window

# def longestSubarrayWithSumK(a: [int], k: int) -> int:
#     i = 0
#     curr_sum = 0
#     maxi = 0
#     n = len(a)

#     for j in range(n):
#         curr_sum += a[j]  # always include the new element

#         # shrink window if sum > k
#         while curr_sum > k and i <= j:
#             curr_sum -= a[i]
#             i += 1

#         # check if current window has sum == k
#         if curr_sum == k:
#             maxi = max(maxi, j - i + 1)

#     return maxi


#using prefix sum

def longestSubarrayWithSumK(a: [int], k: int) -> int:
    curr_sum = 0
    maxLen = 0
    prefixSum = {}  # maps sum ? earliest index

    for i in range(len(a)):
        curr_sum += a[i]

        # case when subarray starts from index 0
        if curr_sum == k:
            maxLen = max(maxLen, i + 1)

        # if (curr_sum - k) is seen before, there's a subarray summing to k
        if (curr_sum - k) in prefixSum:
            maxLen = max(maxLen, i - prefixSum[curr_sum - k])

        # store curr_sum only if not seen before (to get longest subarray)
        if curr_sum not in prefixSum:
            prefixSum[curr_sum] = i

    return maxLen

# https://www.naukri.com/code360/problems/longest-subarray-with-sum-k_6682399?leftPanelTabValue=SUBMISSION