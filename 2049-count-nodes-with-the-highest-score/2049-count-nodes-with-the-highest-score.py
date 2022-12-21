class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        tree = defaultdict(list)
        self.res = defaultdict(int)
        self.mx = float('-inf')
        self.score=0
        for i,v in enumerate(parents):
            tree[v].append(i)
        nodes = len(parents)
        def  dfs(node):
            child = tree[node]
            
            if len(child)==2:
                left =  dfs(child[0])
                right=  dfs(child[1])
                total = 1 + left +right
                # print("child of",node,total-1)
                v = 1 if (nodes-total)==0 else  (nodes-total)
                score = left*right*v
                self.mx = max(self.mx,score)
                self.res[score]+=1
                return total
                
            elif len(child)==1:
                left =  dfs(child[0])
                total = 1 + left
                # print("child of",node,total-1)
                score =None
                if nodes-total==0:
                    score = left
                else:
                    score = left*(nodes-total)
                self.mx = max(self.mx,score)
                self.res[score]+=1
                return total
            else:
                # print("child of",node,0)
                score = (nodes-1)
                self.mx = max(self.mx,score)
                self.res[score]+=1
                return 1
        dfs(tree[-1][0])
        # print(self.res)
        return self.res[self.mx]
                