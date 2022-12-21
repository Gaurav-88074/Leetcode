class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for a,b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        def compute(node,color,visited,markedColor):
            if visited[node]==True:
                return markedColor[node]==color
            visited[node]=True
            markedColor[node]=color
            
            res = True
            for nxt in graph[node]:
                res = res and compute(nxt,1-color,visited,markedColor) 
            return res
        markedColor = [-1] * (n+1)
        visited = [False] * (n+1)
        
        res = True
        for i in range(1,n+1):
            if visited[i]==False:
                res = res and compute(i,1,visited,markedColor)
                if not res: return res
        return res