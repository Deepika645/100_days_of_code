class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxl = 0
        sett = set()
        l = 0
        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l+=1
            w = r-l + 1
            maxl = max(maxl, w)
            sett.add(s[r])
        return maxl



        