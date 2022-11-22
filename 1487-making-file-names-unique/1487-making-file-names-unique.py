class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        d =defaultdict(int)
        
        res= []
        for w in names:
            
            if w in d:
                v = d[w]
                nw = f"{w}({v+1})"
                d[w] = v+1
                while nw in d:
                    v = d[w]
                    nw = f"{w}({v+1})"
                    d[w] = v+1
                d[nw] = 0
                res.append(nw)
            else:
                res.append(w)
                d[w]=0
        return res