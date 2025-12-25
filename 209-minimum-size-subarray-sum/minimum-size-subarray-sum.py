class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        min_l = float('inf')
        summ = 0
        for j in range(len(nums)):
            summ += nums[j]
            while summ>= target:
                min_l = min(min_l, j-i+1)
                summ-=nums[i]
                i+=1
        return 0 if min_l == float('inf') else min_l


        