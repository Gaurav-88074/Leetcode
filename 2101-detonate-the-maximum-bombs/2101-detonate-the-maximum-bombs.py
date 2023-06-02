class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        def computeDistance(a,b):
            return math.sqrt(abs(a[0]-b[0])**2 + abs(a[1]-b[1])**2)
        for i,v in enumerate(bombs):
            key = tuple([i,*v])
            radius = v[2]
            for j,w in enumerate(bombs):
                if i!=j:
                    dist= computeDistance(v,w)
                    if dist<=radius:
                        graph[key].append([j,*w])
        # print(graph)
        res = 0
        def computeMax(node,visited):
            if node in visited:
                return 
            visited.add(node)
            for nxt in graph[node]:
                computeMax(tuple(nxt),visited)
            return
        for i,v in enumerate(bombs):
            x,y,r =v
            node = tuple([i,x,y,r])
            #----------------------------
            visited = set()
            computeMax(node,visited)
            #----------------------------
            res = max(res,len(visited))
            #----------------------------
        return res
                    