def merge(arr,lo,mid,hi):
    temp = []
    left = lo
    right = mid+1
    while(left<= mid and right<=hi):
        if arr[left]<= arr[right]:
            temp.append(arr[left])
            left +=1
        else:
            temp.append(arr[right])
            right +=1

    while(left<=mid):
        temp.append(arr[left])
        left+=1

    while(right<=hi):
        temp.append(arr[right])
        right+=1

    for i in range(lo,hi+1):
        arr[i] = temp[i-lo]
    


def mergesort(arr,lo,hi):
    if lo == hi:
        return
    mid = (lo+hi)//2
    mergesort(arr,lo,mid)
    mergesort(arr,mid+1,hi)
    merge(arr,lo,mid,hi)
    return arr
arr = [3,4,7,8,2,3,1,2,4,9,10,1,5]
print(mergesort(arr,0,len(arr)-1))



