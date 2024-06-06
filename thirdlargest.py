#given an array of elements with no duplicates you need to find the third largest element if no such element is present return -1
import sys
def thirdlar(arr,n):
    if n<3:
        return -1
    first = arr[0]
    second = -sys.maxsize
    third = -sys.maxsize
    for i in range(1,n):
        if arr[i]>first:
            third = second
            second = first
            first = arr[i]
        elif arr[i]>second:
            third = second
            second = arr[i]
        elif arr[i]> third:
            third = arr[i]
    return third if third != -sys.maxsize else -1
arr = [10,3,8,9,0]
n = len(arr)
print(thirdlar(arr,n))
        
