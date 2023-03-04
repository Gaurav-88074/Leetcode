class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s=list(s)
        jump = k<<1
        res = [*s]
        for i in range(0,len(s),jump):
            # segment = s[i : i+k]
            # res[i : i+k] = segment[::-1]
            
            s[i : i+k] = s[i : i+k][::-1]
        return "".join(s)