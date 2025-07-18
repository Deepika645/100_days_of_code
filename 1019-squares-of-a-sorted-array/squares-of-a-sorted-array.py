class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """for i in range(len(nums)):
            nums[i] = nums[i]**2
        nums.sort()
        return nums"""
        res = [0]*len(nums)
        l, r = 0, len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if abs(nums[l])>abs(nums[r]):
                res[i] = nums[l]**2
                l+=1
            else:
                res[i] = nums[r]**2
                r-=1
        return res
      
  



