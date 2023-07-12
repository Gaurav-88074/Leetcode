class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(node,parent):
            if parent[node]==node:
                return node
            parent[node]= find(parent[node],parent)
            return parent[node]
        def union(x,y,rank,parent):
            x_rep = find(x,parent)
            y_rep = find(y,parent)
            if x_rep==y_rep:
                return False
            else:
                if rank[x_rep]<rank[y_rep]:
                    parent[x_rep]=y_rep
                elif rank[x_rep]>rank[y_rep]:
                    parent[y_rep]=x_rep
                else:
                    parent[x_rep]=y_rep
                    rank[y_rep]+=1
            return True
        n = len(edges)
        rank = [0]*(n+1)
        parent=[i for i in range(0,n+1)]
        
        res=[]
        
        for a,b in edges:
            if union(a,b,rank,parent)==False:
                res = [a,b]
        return res
