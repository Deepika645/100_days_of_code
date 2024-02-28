#in this code i will be solving to find the no.of rotations in an sorted rotated array through binary search approach
def find_rotns(nums,n):
    lo,hi = 0,len(nums)-1
    while lo<=hi:
        mid = (lo+hi)//2
        if mid>0 and nums[mid]<nums[mid-1]:
            return mid
        elif nums[mid]<nums[n-1]:
            hi = mid-1
        elif nums[mid]>nums[n-1]:
            lo = mid+1
    return 0

            


    