#Finding the first element that occurs atleast k number of times. If no such element exists in the array, return -1.
class Solution:
    def firstElementKTime(self, n, k, a):
        # code here
        res = {}
        for i in range(n):
            if res.get(a[i]) and res[a[i]] + 1 == k:
                return a[i]
            elif res.get(a[i]):
                res[a[i]] += 1
            else:
                res[a[i]] = 1
        return -1

