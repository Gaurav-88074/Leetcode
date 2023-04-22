class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        res= 0
        if k>len(s):return False
        for i in Counter(s).values():
            if (i&1)==1:res+=1
        return res<=k