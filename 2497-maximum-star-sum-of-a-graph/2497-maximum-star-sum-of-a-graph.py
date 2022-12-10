class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        if k==0 or len(edges)==0:
            q =max(vals)
            # if q<0:
            #     return 0
            return q
        graph = defaultdict(list)
        node=set()
        for a,b in edges:
            node.add(a)
            node.add(b)
            if vals[b]>0:
                graph[a].append(vals[b])
            if vals[a]>0:
                graph[b].append(vals[a])
        res = float('-inf')
        for i in graph:
            graph[i].sort(reverse = True)
        #     t = vals[i]
        #     v = graph[i]
        #     for j in range(0,min(k,len(v))):
        #         t+=graph[i][j]
        #     res = max(res,t)
        
        node = list(node)
        for i in node:
            arr = graph[i]
            v = arr[0:k]
            # t = vals+sum(v)
            res = max(res,sum(v)+vals[i])
            # res = max(res,sum(v))
        return res
        