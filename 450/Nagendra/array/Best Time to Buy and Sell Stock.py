#url https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max=0
        buy=0
        n=len(prices)
        for i in range(1,n):
            if prices[buy]>prices[i]:
                buy=i
            if prices[i]-prices[buy]>max:
                max=prices[i]-prices[buy]
        return max
        