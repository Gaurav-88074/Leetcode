class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        d = defaultdict(set)
        for a,b in connections:
            d[a].add(b)
        
        for a,b in connections:
            graph[a].append(b)
            graph[b].append(a)
        self.res = 0
        
        def dfs(root,v,frm):
            if root in v:
                return
            v.add(root)
            if frm in d and root in d[frm]:
                # print(frm,root)
                self.res+=1
              
            for nxt in graph[root]:
                dfs(nxt,v,root)
        dfs(0,set(),-1)
        return self.res