class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)<=2: return len(points)
        d  = defaultdict(list)
        def slope(c,d):
            if (d[0]-c[0])==0:return float('inf')
            slop = (d[1]-c[1])/(d[0]-c[0])
            return slop
        r=0
        for i in points:
            d  = defaultdict(list)
            for j in points:
                if i!=j :
                    slop = slope(i,j)
                    d[slop].append(str(i))
                    d[slop].append(str(j))
            for i in d:
                r = max(r,len(set(d[i])))
        return r