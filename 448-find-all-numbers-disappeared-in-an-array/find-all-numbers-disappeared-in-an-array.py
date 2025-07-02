class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            nums[abs(i)-1] = -abs(nums[abs(i)-1])
        for i in range(len(nums)):
            if nums[i]>0:
                ans.append(i+1)
        return ans
        