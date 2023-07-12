class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res=[]
        #------------------------------
        computed = dict()
        def compute(node):
            if node in computed:
                return computed[node]
            #-----------------------------
            computed[node] = False
            for nextNode in graph[node]:
                if compute(nextNode)==False:
                    return False
            computed[node] = True
            return True
        #----------------------------
        for i in range(len(graph)):
            c = compute(i)
            if c:
                res.append(i)
        return res
    
        """
        0->nill
        1->0,2,3,4
        2->3
        3->4
        4->nil
        
        """