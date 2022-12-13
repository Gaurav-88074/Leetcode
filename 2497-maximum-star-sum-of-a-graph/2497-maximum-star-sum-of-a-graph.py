class Solution(object):
    def maxStarSum(self, vals, edges, k):
        n = len(vals)
        maxres = max(vals)
        g = defaultdict(list)
        
        for a,b in edges:
            g[a].append(vals[b])
            g[b].append(vals[a])
            
        for i in range(n):
            res = vals[i]
            g[i].sort(reverse=True)
            for x in g[i][:k]:
                if x < 0:
                    break
                res += x
            maxres = max(maxres, res)
        
        return maxres
        