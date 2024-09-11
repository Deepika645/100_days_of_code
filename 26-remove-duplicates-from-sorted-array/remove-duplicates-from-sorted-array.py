class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_pos = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[unique_pos]:
                unique_pos+=1
                nums[unique_pos] = nums[i]
        return unique_pos+1
