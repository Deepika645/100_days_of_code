def insertionsort(arr):
    n = len(arr)
    for i in range(n):
       
        j = i
        
        while j>0 and arr[j-1]>arr[j]:
            arr[j-1],arr[j]= arr[j], arr[j-1]
            j-=1
            
    return arr
arr = [5,9,10,7,6]
print(insertionsort(arr))