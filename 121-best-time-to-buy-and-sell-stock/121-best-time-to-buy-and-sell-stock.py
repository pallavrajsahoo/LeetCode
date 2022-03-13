class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_profit = 0
        for right in range(left+1, len(prices)):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right 
        return max_profit
        