#given an array with duplicates you need to find out the second largest element in the array
import sys
def thirdlar(arr,n):
    if n<2:
        return -1
    first = arr[0]
    second = -sys.maxsize
    for i in range(1,n):
        if arr[i]>first:
            second = first
            first = arr[i]
        elif arr[i]>second and arr[i] != first:
            second = arr[i]
        
    return second if second != -sys.maxsize else -1
arr = [10,10,3,8,9,0]
n = len(arr)
print(thirdlar(arr,n))
        
