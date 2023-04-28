class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def find(node,parent):
            if parent[node]==node:
                return node
            parent[node]= find(parent[node],parent)
            return parent[node]
        def union(x,y,rank,parent):
            x_rep = find(x,parent)
            y_rep = find(y,parent)
            if x_rep==y_rep:
                return
            else:
                if rank[x_rep]<rank[y_rep]:
                    parent[x_rep]=y_rep
                elif rank[x_rep]>rank[y_rep]:
                    parent[y_rep]=x_rep
                else:
                    parent[x_rep]=y_rep
                    rank[y_rep]+=1
        def isPossiblePair(a,b):
            c=0
            for i,j in zip(a,b):
                if i!=j:
                    c+=1
                if c>2:
                    return False
            return True
        rank = defaultdict(int)
        parent = dict({i:i for i in strs})
                      
        res = len(strs)
        # print(rank,parent)
        for i in range(len(strs)):
            a = strs[i]
            for j in range(i+1,len(strs)):
                b = strs[j]
                # if a==b:
                #     res-=1
                #     continue
                if isPossiblePair(a,b) and parent[a]!=parent[b]:
                    union(a,b,rank,parent)
                    # res-=1
                    
        # print(parent)
        return len(set([find(x,parent) for x in strs]))
        # return res
                
        
