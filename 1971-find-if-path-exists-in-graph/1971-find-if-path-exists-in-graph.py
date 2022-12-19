class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node,v):
            if node in v:
                return False
            if node==destination:
                return True
            v.add(node)
            
            res = False
            for nxt in graph[node]:
                res = res or dfs(nxt,v)
                if res:
                    return res
            return res
        v=set()
        return dfs(source,v)