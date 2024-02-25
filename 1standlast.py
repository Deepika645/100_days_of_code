#this is a code to find the 1st and last occurance of a particular element in the array through binary search

class Solution:
    
    def find_occurrence(self, array, length, target, occ):
        left, right = 0, length - 1
        occurrence = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if array[mid] == target:
                occurrence = mid
                if occ == "first":
                    right = mid - 1
                elif occ == "last":
                    left = mid + 1
            elif array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return occurrence
    
    def find(self, arr, n, x):
        # code here
        first_occurrence = self.find_occurrence(arr, n, x, "first")
        last_occurrence = self.find_occurrence(arr, n, x, "last")
        return (first_occurrence, last_occurrence)