class value:
    def __init__(self,v):
        self.val = v
class Solution:
    def minTime(self, size: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        tree = defaultdict(list)
        for a,b in edges:
            tree[a].append(b)
            tree[b].append(a)
        def compute(node,p):
            if len(tree[node])==0:
                return [hasApple[node],0]
            
            res = 0
            applePresent = hasApple[node]
            for n in tree[node]:
                if n==p:continue
                #----------------------------
                isApple,count = compute(n,node)
                # print("At node",node,"res =",count,"isapple",isApple)
                res+=count
                if isApple:
                    res+=2
                #----------------------------------------
                applePresent = applePresent or isApple
                #----------------------------------------
                
            return [applePresent,res]
        # print(tree)
        return compute(0,0)[1]
            
            
            