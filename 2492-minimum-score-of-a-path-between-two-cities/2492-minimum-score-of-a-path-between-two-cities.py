class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        d = defaultdict(list)
        
        for a,b,w in roads:
            d[a].append([b,w])
            d[b].append([a,w])
        v = set()
        res = [float('inf')]
        # print(d)
        def dfs(node,res):
            # global res
            if node  in v:
                return
            v.add(node)
            for nx,w in d[node]:
                res[0] = min(res[0],w)
                # if nx!=n:
                
                dfs(nx,res)
        dfs(1,res)
        v.add(1)
        # print(v)
        for a,b,c in roads:
            if a in v or b in v:
                res[0] = min(res[0],c)
        return res[0]
            