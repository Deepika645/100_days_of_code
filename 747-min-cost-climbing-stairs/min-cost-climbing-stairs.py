class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_sum = cost + [0]

        n = len(min_sum)
        for i in range(2, len(min_sum)):
            min_sum[i] = min(min_sum[i]+min_sum[i-1], min_sum[i]+ min_sum[i-2])
        return min_sum[n-1]
        