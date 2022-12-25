class Solution:
    def countAnagrams(self, s: str) -> int:
        wo= s.split(" ")
        res = 1
        mod=10**9 + 7
        
        for w in wo:
            c = Counter(w)
            up = math.factorial(len(w))
            down = 1
            for i in c:
                if c[i]!=1:
                    down*= math.factorial(c[i])
            res*= (up//down)
            # print(up,down)
        return res%mod