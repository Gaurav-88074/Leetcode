class node:
    def __init__(self):
        self.arr = defaultdict(int)

    def get(self,c):
        i = ord(c)-97
        return self.arr[i]
    
    def add(self,c):
        i = ord(c)-97
        self.arr[i]+=1
    
    def merge(self,obj):
        for i in obj.arr:
            self.arr[i]+=obj.arr[i]


class Solution:
    
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        tree = defaultdict(list)
        visited=set()
        for a,b in edges:
            tree[a].append(b)
            tree[b].append(a)
        res= [0]*n
        def compute(i):
            # if len(tree[i])==0:
            #     return node()
            visited.add(i)
            obj = node()
            #------------------------
            for nxt in tree[i]:
                if nxt in visited:
                    continue
                thatObj = compute(nxt); 
                obj.merge(thatObj)
            #------------------------
            obj.add(labels[i])
            #--------------------------
            res[i] = obj.get(labels[i])
            #---------------------
            return obj
        compute(0)
        return res
        