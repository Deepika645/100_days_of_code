#Given two strings, one is a text string and other is a pattern string. 
class Solution:
    def search(self, pattern, text):
        
        ch_value = lambda c: ord(c) - ord('a') + 1
        
        # code here
        p, m = 31, 10**9+9
        pl, tl = len(pattern), len(text)
        pow = [0]*max(pl, tl)
        pow[0] = 1
        for i in range(1, len(pow)):
            pow[i] = pow[i-1]*p%m 
        
        tv = [0]*(tl+1)
        for i in range(tl):
            tv[i+1] = (tv[i]+ch_value(text[i])*pow[i])%m
        
        ph = 0
        for i in range(pl):
            ph = (ph+ch_value(pattern[i])*pow[i])%m
            
        ans = []
        
        for i in range(tl):
            if i + pl - 1 >= tl:
                break
            cur_hash = (tv[i+pl]-tv[i]-m)%m
            if cur_hash == ph * pow[i] % m:
                ans.append(i+1)
        return ans
