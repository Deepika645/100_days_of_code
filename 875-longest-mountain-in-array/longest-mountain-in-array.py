class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr)<3:
            return 0
        n = len(arr)
        i = 1
        max_len = 0
        while i <n-1:
            if arr[i-1]<arr[i]>arr[i+1]:
                left = i-1
                right = i+1
                while left> 0 and arr[left -1]< arr[left]:
                    left -= 1
                while right < n-1 and arr[right +1]< arr[right]:
                    right +=1
                max_len = max((right-left+1),max_len)
                i = right
            else:
                i+=1
            
        return max_len
            


        
 