class Solution:
    def balancedStringSplit(self, s: str) -> int:
        v =0
        res = 0
        for i in s:
            if i=='R':
                v+=1
            if i=='L':
                v-=1
            if v==0:
                res+=1
        return res