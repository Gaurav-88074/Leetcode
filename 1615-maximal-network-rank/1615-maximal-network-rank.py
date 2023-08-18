class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        
        for a,b in roads:
            graph[a].add(b)
            graph[b].add(a)
        #---------------------
        def areTheyConnected(nodeA,nodeB):
            return nodeA in graph[nodeB] or nodeB in graph[nodeA]
        #---------------------
        res = 0
        for nodeA in range(n):
            for nodeB in range(n):
                if nodeA==nodeB:
                    continue
                else:
                    degree_A = len(graph[nodeA])
                    degree_B = len(graph[nodeB])
                    
                    value = degree_A + degree_B
                    
                    if areTheyConnected(nodeA,nodeB):
                        value-=1
                    res = max(res,value)
        return res
                        
                    
        