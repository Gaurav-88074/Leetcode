class Solution:
    def printVertically(self, s: str) -> List[str]:
        res = []
        # v = []
        s = s.split(" ")
        m = max([len(i) for i in s])
        
        space = " "
        # print(m)
        for i in range(m):
            v = []
            for j in range(len(s)):
                strr = s[j]
                if i<len(strr):
                    v.append(strr[i])
                else:
                    v.append(space)
            # print(v)
            resv = "".join(v).rstrip()
            res.append(resv)
        return res