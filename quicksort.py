#pick a pivot and place it in it's place, i am honna take the first element as pivot
#smaller elemnets to the left of the pivot and the larger elemnets to thr right of the pivot
def pivotfind(arr,lo,hi):
    pivot = arr[lo]

    i = lo
    j = hi
    while i<j:
        while(arr[i]<=pivot and i<=hi-1):
            i+=1
        while(arr[j]>pivot and j>= lo+1):
            j-=1
        if i<j:

            arr[i],arr[j] = arr[j],arr[i]

    arr[lo], arr[j] = arr[j], arr[lo]
    return j

    

   

def quicksort(arr,lo,hi):
    n = len(arr)
    if lo<hi:
        pivot_index = pivotfind(arr,lo,hi)
        quicksort(arr,lo,pivot_index-1)
        quicksort(arr,pivot_index+1,hi)
    return arr

arr = [3,4,7,8,2,3,1,2,4,9,10,1,5]
print(quicksort(arr,0,len(arr)-1))

"""def pivotfind(arr, lo, hi):
    pivot = arr[lo]
    i = lo
    j = hi

    while i < j:
        # Move `i` to the right until an element larger than the pivot is found
        while i <= hi and arr[i] <= pivot:
            i += 1

        # Move `j` to the left until an element smaller than or equal to the pivot is found
        while j >= lo and arr[j] > pivot:
            j -= 1

        # If `i` is still less than `j`, swap the elements at `i` and `j`
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot element with the element at `j` to place the pivot in the correct position
    arr[lo], arr[j] = arr[j], arr[lo]

    return j

def quicksort(arr, lo, hi):
    if lo < hi:
        # Find the pivot index
        pivot_index = pivotfind(arr, lo, hi)
        
        # Recursively sort elements before and after the pivot
        quicksort(arr, lo, pivot_index - 1)
        quicksort(arr, pivot_index + 1, hi)

    return arr

# Example usage
arr = [3, 4, 7, 8, 2, 3, 1, 2, 4, 9, 10, 1, 5]
print(quicksort(arr, 0, len(arr) - 1))"""
