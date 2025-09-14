class Solution:
    def rob(self, nums: List[int]) -> int:
    
        n = len(nums)
        if n == 1:
            return nums[0]
        max_loot = [0]*n
        max_loot[0] = nums[0]
        max_loot[1] = max(nums[1], nums[0])
        for i in range(2,n):
            max_loot[i] = max(max_loot[i-2]+nums[i], max_loot[i-1])
        return max_loot[-1]
       

        