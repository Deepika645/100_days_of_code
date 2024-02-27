#finding no of times array got rotated based on the given rotated sorted array through linear search
class Solution:
    def findKRotation(self,arr,  n):
        # code here
        position = 0
        while position<len(arr):
            if position>0 and arr[position]<arr[position-1]:
                return position
            position +=1
        return 0
