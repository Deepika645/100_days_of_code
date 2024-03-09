#Given an array A of N elements. Find the majority element in the array.
class Solution:
    def majorityElement(self, A, N):
        from collections import Counter
        c=Counter(A)
        for i,j in c.items():
            if j>N/2:return i
        return -1