class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        mini = prices[0]
        for i in range(len(prices)):
            mini = min(mini, prices[i])
            maxi = max(maxi, prices[i] - mini)
        
        return maxi
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1735873168/
