class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        min_l = float("inf")
        sum = nums[i]
        if sum>= target:
            return 1
        for j in range(1,n):
            sum += nums[j]
            while sum>= target:
                min_l = min(min_l, j-i+1)
                sum-=nums[i]
                i+=1
            
        if min_l<float("inf"):
            return min_l
        else:
            return 0 


            
        

        