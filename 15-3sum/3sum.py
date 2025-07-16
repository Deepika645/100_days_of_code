class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        set1 = set()
        for i in range(len(nums)):
            j, k = i+1, len(nums)-1
            
            while j<k:
                sum = nums[i]+nums[j]+nums[k]
                if sum == 0:
                    set1.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif sum>0:
                    k-=1
                else:
                    j+=1
        return list(set1)
        
            




        