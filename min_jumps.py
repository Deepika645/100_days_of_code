#Given an array of N integers arr[] where each element represents the maximum length of the jump that can be made forward from that element(gfg problem)
def minJumps(self, arr, n):
    #code here
        n = len(arr)
 
        if n == 0 or arr[0] == 0:
            return -1
        if n==1 and arr[0]>1: return 0 # for single elements which are greater than 1
        jumps = 1  # Initial jump from the first element
        max_reach = arr[0]  # Maximum index that can be reached with the current jump
        steps_available = arr[0]  # Steps available in the current jump
    
        for i in range(1, n):
            if i == n - 1:
                return jumps
    
            max_reach = max(max_reach, i + arr[i])
            steps_available -= 1
    
            if steps_available == 0:
                jumps += 1
    
                if i >= max_reach:
                    return -1  # Cannot reach the end
    
                steps_available = max_reach - i
    
        return -1 