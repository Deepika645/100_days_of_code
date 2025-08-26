class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        if n<2:
            return 0
        arr.sort()
        min_d = float(inf)
        arr2 = []
        i = 0
        j = 1
        while j<n:
            diff = abs(arr[j]-arr[i])
            # min_d = min(min_d,diff)
            if diff< min_d:
                min_d = diff
                arr2 = [[arr[i],arr[j]]]
            elif diff == min_d:
                arr2.append([arr[i],arr[j]])
            i+=1
            j+=1
        return arr2
           
        