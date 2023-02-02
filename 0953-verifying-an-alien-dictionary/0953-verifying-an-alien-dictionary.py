class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = dict()
        for i,v in enumerate(order):
            d[v]=i+1
        def compareTo(a,b):
            for i in range(min(len(a),len(b))):
                c1 = a[i]
                c2 = b[i]
                
                v1 = d[c1]
                v2 = d[c2]
                
                if v1!=v2:
                    return v1-v2
            if len(a)>len(b):
                return 1
            if len(b)>len(a):
                return -1
            return 0
        nw = [*words]
        nw.sort(key = cmp_to_key(compareTo))
        return nw==words 