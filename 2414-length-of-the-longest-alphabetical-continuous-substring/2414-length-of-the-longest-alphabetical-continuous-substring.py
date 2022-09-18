class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        pre = 96
        c = 0
        res = 0
        for i in s:
            if ord(i)==pre+1:
                pre = ord(i)
                c+=1
            else:
                res = max(res,c)
                c = 1
                pre = ord(i)
        res = max(res,c)
        return res
        