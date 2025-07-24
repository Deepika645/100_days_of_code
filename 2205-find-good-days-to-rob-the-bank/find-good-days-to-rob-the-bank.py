class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        res = []
        k = time
        n = len(security)
        nums1 = [1]*n # for decreasing order or eqaul till i 
        nums2 = [1]*n # for increasing order after i but reverse we will do 
        for i in range(1,n):
            if security[i]<=  security[i-1]:
                nums1[i] = nums1[i-1]+1
        for i in range(n-2, -1, -1):
            if security[i]<= security[i+1]:
                nums2[i] = nums2[i+1]+1
        for i in range(k, n-k):
            if nums1[i]>= k+1 and nums2[i]>=k+1:
                res.append(i)
        return res

        




        