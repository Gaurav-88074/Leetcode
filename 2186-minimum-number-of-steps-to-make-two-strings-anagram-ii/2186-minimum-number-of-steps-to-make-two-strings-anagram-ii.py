class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d = [0]*26
        for i in s:
            d[ord(i)-97]+=1
        for i in t:
            d[ord(i)-97]-=1
        res = 0
        for i in d:
            res+=abs(i)
        return res
            