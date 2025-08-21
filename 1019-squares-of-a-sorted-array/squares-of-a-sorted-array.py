class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        j = n-1
        arr = [0]*n
       
        while i<=j:
            if abs(nums[i])> abs(nums[j]):
                arr[n-1] = abs(nums[i])**2
                i+=1
            else:
                arr[n-1] = abs(nums[j])**2
                j-=1
            n-=1
        return arr


                