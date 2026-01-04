class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        lo = 0
        hi = len(nums) - 1
        
        while lo<=hi:
            mid = (lo + hi)//2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[lo] and nums[mid] == nums[hi]:
                lo +=1
                hi -=1
            elif nums[mid] <= nums[hi]:
                if target > nums[mid] and target <= nums[hi]:
                    lo = mid+1
                else:
                    hi = mid-1
            else:
                if target < nums[mid] and target >= nums[lo]:
                    hi = mid-1
                else:
                    lo = mid+1
        return False
                    
                    
        
        