class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict1 = {}
        for i in nums:
            dict1[i] = dict1.get(i, 0) + 1
            if dict1[i] > 1:
                return True
        return False
        
        