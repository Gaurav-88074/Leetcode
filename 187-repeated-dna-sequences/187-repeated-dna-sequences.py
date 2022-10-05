class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s)<10:
            return []
        d = defaultdict(int)
        
        for i in range(0,len(s)-9):
            v = s[i : i+10]
            d[v]+=1
        # print(d)
        res = []
        for i in d:
            v = d[i]
            if v>1:
                res.append(i)
        return res