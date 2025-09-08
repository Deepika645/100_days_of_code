class NumArray:

    def __init__(self, nums: List[int]):
        self.sumarr = []
        currsum = 0
        for i in nums:
            currsum+= i
            self.sumarr.append(currsum)
        

    def sumRange(self, left: int, right: int) -> int:
        leftsum = self.sumarr[left-1] if left > 0 else 0
        rightsum = self.sumarr[right]
        return rightsum - leftsum 
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)