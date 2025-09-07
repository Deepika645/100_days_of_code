class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 0
        summ = 0
        max_sum = float("-inf")
        for j in range(len(nums)):
            summ += nums[j]
            max_sum = max(max_sum, summ)
            while summ < 0:
                summ -= nums[i]
                i += 1
            
        return max_sum
                