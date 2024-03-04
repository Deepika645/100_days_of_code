#Given an array of integers. Find the Inversion Count in the array. 
class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr, n):
        # Your Code Here
        overall_count = 0
        for i in range(n):
            count = 0
            for j in range(i+1,n):
                if(arr[i] > arr[j]):
                    count+=1
                    
            overall_count+=count
            
        return overall_count