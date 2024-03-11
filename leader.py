#Given an array A of positive integers. Your task is to find the leaders in the array.
class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        leaders_list = []
        max_right = A[N - 1]
        leaders_list.append(max_right)
    
        for i in range(N - 2, -1, -1):
            if A[i] >= max_right:
                max_right = A[i]
                leaders_list.append(max_right)
        return leaders_list[::-1]