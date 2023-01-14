from sortedcontainers import *
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        d =defaultdict(set)
        n = len(s1)
        for i in range(n):
            a = s1[i]
            b = s2[i]
            d[a].add(b)
            d[b].add(a)
        # print(d)
        def dfs(graph,node,visited,MV):
            visited.add(node)
            MV[0] = min(MV[0],node)
            for i in graph[node]:
                if i not in visited:
                    dfs(graph,i,visited,MV)
        res = []
        for i in baseStr:
            MV = [i]
            dfs(d,i,set(),MV)
            res.append(MV[0])
        return "".join(res)
        