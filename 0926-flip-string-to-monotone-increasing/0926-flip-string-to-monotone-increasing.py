class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        flipcount=0
        one = 0
        
        for i in s:
            if i=='1':
                one+=1
            else:
                flipcount+=1
                flipcount = min(one,flipcount)
        return flipcount