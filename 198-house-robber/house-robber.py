class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        a = nums[0]
        b = max(nums[0], nums[1])
        for i in range(2,n):
            curr_loot = max(nums[i]+a,b)
            a, b = b, curr_loot
        return b
        