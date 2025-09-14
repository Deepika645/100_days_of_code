class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n==1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        a = nums[0]
        b = max(nums[0], nums[1])
        c = nums[1]
        d = max(nums[1],nums[2])
        for i in range(2, n-1):
            curr_sum = max(nums[i]+a,b)
            a,b = b, curr_sum
        for j in range(3,n):
            curr_sum2 = max(nums[j]+c,d)
            c,d = d, curr_sum2
        return max(b,d)