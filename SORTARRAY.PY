#Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
class Solution:
    def sort012(self,arr,n):
        l=0
        m=0
        r=len(arr)-1
        while(m<=r):
            if arr[m]==0:
                arr[m],arr[l]=arr[l],arr[m]
                m+=1
                l+=1
            elif arr[m]==1:
                m+=1
            else:
                arr[m],arr[r]=arr[r],arr[m]
                r-=1
        return arr

