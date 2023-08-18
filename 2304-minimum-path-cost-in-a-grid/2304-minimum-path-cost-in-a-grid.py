class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        d = defaultdict(int)
        #-----------------------------------------
        r_index =0 
        n = len(grid)
        for rowNodes in grid: 
            for node in rowNodes:
                if r_index+1<n:
                    ii = 0
                    for next_row_node in grid[r_index+1]:
                        key = (node,next_row_node)
                        d[key] = moveCost[node][ii]
                        ii+=1
            r_index += 1
        # print(d)
        #-----------------------------------------
        @lru_cache(None)
        def compute(i,preNode):
            if i==n:
                return 0
            res = float('inf')
            if preNode==None:
                for node in grid[i]:
                    val = node + compute(i+1,node)
                    res = min(val,res)
            else:
                for node in grid[i]:
                    val = d[(preNode,node)] + node + compute(i+1,node)
                    res = min(val,res)
            return res
        #-----------------------------------
        return compute(0,None)
                