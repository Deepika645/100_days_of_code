class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        n = len(nums)
        i = 0 
        j = 0
        summ = 0
        while j<n:
            summ += nums[j]
            max_sum = max(max_sum, summ)
            if summ<0:
                summ = 0
                j+=1
                i=j
            else:
                j+=1
        return max_sum

        