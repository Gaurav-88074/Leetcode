class Solution:
    def replaceWords(self, d: List[str], s: str) -> str:
        
        res=[]
        d=set(d)
        s =s.split(" ")
        for i in s:
            v=""
            c=0
            for x in i:
                v+=x
                if v in d:
                    res.append(v)
                    c=1
                    break
            if c==0:
                res.append(v)
        return " ".join(res)
        