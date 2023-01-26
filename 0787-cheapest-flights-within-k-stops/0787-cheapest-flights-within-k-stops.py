class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst, k) -> int:
        graph  = defaultdict(list)
        k+=1
        for a,b,cost in flights:
            graph[a].append([b,cost])
        # print(graph)
        visited = set()
        
        @lru_cache(None)
        def compute(node,count):
            if node==dst and count<=k:
                # print("reached",count)
                return 0
            if count>k :#or node in visited:
                return float('inf')
            visited.add(node)
            ans = float('inf')
            for b,cost in graph[node]:
                value = cost + compute(b,count+1)
                # print("At",node,"to",b,"cost =",value)
                ans = min(ans,value)
            visited.discard(node)
            return ans
        #----------------------------------
        res = compute(src,0)
        if res==float('inf'):
            return -1
        return res