class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        s={i for i in range(1,n+1)}
        d=defaultdict(int)
        for a,b in trust:
            d[b]+=1
            s.discard(a)
        return -1 if not s else  -1 if d[min(s)]!=n-1 else min(s)
        