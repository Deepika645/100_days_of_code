class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        i = 0
        j = 1
        while i<j<n:
            if prices[i]<prices[j]:
                profit = prices[j] - prices[i]
                max_profit += profit
            i+=1
            j+=1
        return max_profit

        