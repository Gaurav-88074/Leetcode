class Solution:
    def beautySum(self, s: str) -> int:
        res = 0
        
        for i in range(len(s)):
            for j in range(i,len(s)):
                c = s[i:j+1]
                # print(c)
                f =Counter(c).values()
                if not f:
                    continue
                a = min(f)
                b = max(f)
                if b-a>0:
                    res+=b-a
        return res
                