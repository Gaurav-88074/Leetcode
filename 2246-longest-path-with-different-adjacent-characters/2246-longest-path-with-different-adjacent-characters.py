from sortedcontainers import SortedList,SortedDict
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = defaultdict(list)
        for i,v in enumerate(parent):
            tree[v].append(i)
        res = [0]
        def dfs(node,res):
            c = 0
            l = SortedList()
            for nxt in tree[node]:
                value = dfs(nxt,res)
                if s[node] != s[nxt]:
                    c = max(c,1 + value)
                    l.add(1 + value)
            # print(tree[node],l)
            if len(l)>=2:
                res[0] = max(l[-1] + l[-2] ,res[0])
            res[0]=max(c,res[0])
            return c
        
        v = 1 + dfs(tree[-1][0],res)
        return max(res[0]+1,v)