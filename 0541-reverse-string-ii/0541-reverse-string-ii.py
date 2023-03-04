class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s=list(s)
        jump = k<<1
        res = [*s]
        for i in range(0,len(s),jump):
            segment = s[i : i+k]
            # print(segment,i)
            res[i : i+k] = segment[::-1]
            # print(res)
        return "".join(res)