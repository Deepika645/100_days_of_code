# Function to perform binary search on a sorted array
# In this file, I have been able to find an element from the given array through binary search 
#Time complexity: O(log(n))
#Space complexity: O(1)
def binarysearch(arr, N, K):
  # Initialize low and high pointers
  low = 0
  high = N - 1

  # Loop until low <= high
  while low <= high:
    # Find the middle index
    mid = (low + high) // 2

    # If the middle element is equal to K, return the index
    if arr[mid] == K:
      return mid
    
    # If the middle element is greater than K, search in the left half
    elif arr[mid] > K:
      high = mid - 1
    
    # If the middle element is less than K, search in the right half
    else:
      low = mid + 1
  
  # If K is not found, return -1
  return -1
