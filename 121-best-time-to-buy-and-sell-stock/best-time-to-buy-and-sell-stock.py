class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        i = 0
        j = 1
        maxp = 0
        while j<n:
            p = prices[j] - prices[i]
            maxp = max(maxp, p)
            if prices[i]>prices[j]:
                i=j
            j+=1
        return maxp
#[2,3,5,1,11]


        