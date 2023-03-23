class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        #------------------
        c=len(connections)
        if (c>=(n-1))==False:
            return -1
        #-------------------
        self.v = set()
        self.c=0
        d=defaultdict(set)
        
        for a,b in connections:
            d[a].add(b)
            d[b].add(a)
        
        def dfs(node,frm):
            if node in self.v:
                return
            self.c+=1
            self.v.add(node)
            for nxt in d[node]:
                dfs(nxt,node)
        g=[]
        for i in range(n):
            if i not in self.v:
                self.c=0
                dfs(i,-1)
                g.append(self.c)
        # print(g)
        # print(d)
        # print(self.extra)
        
        return len(g)-1