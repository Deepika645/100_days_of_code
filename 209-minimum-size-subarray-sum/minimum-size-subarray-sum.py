class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        min_l = float("inf")
        curr_sum = 0
        
        for j in range(n):
            curr_sum += nums[j]
            while curr_sum >= target:
                min_l = min(min_l, j - i + 1)
                curr_sum -= nums[i]
                i += 1
        
        return 0 if min_l == float("inf") else min_l



            
        

        