class Solution:
    def countHomogenous(self, s: str) -> int:
        res = 0
        mod = 10**9 + 7
        pre = None
        c = 0
        for i,v in enumerate(s):
            if v==pre:
                c+=1
            else:
                res+= (c*(c+1))//2
                res%=mod
                c = 1
            pre = v
            
        res+= (c*(c+1))//2
        res%=mod
        
        return res