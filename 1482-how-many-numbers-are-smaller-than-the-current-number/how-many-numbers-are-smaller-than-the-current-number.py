class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = []
        n = len(nums)
        for i in range(n):
            a = 0
            for j in range(n):
                if nums[i]>nums[j]:
                    a+=1
                j+=1
            arr.append(a)
            i+=1
        return arr
        