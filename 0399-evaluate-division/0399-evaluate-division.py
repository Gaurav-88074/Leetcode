class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        res = []
        d = defaultdict(int)
        graph = defaultdict(list)
        i = 0
        for a,b in equations:
            d[(a,b)]=values[i]
            d[(b,a)]=1/values[i]
            i+=1
            graph[a].append(b)
            graph[b].append(a)
        # print(d)
        # print(graph)
        def compute(node,dest,prev,v):
            if node in v:
                return float('inf')
            if node==dest and node in graph:
                return 1
            v.add(node)
            res = float('inf')
            for nxt in graph[node]:
                cv =d[(node,nxt)] * compute(nxt,dest,prev,v)
                res=min(cv,res)
            # if res:return min(res)
            return res
        for a,b in queries:
            val = compute(a,b,None,set())
            if val==float('inf'):
                res.append(-1)
            else:
                res.append(val)
        return res
            