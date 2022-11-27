class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        zrow = defaultdict(int)
        zcol = defaultdict(int)
        orow = defaultdict(int)
        ocol = defaultdict(int)
        
        index = 0
        for r in grid:
            z = r.count(0)
            zrow[index] = z
            orow[index] = len(r)-z
            index+=1
        m = len(grid)
        n = len(grid[0])
        
        index = 0
        for c in zip(*grid):
            z = c.count(0)
            zcol[index] = z
            ocol[index] = len(c)-z
            index+=1
        for i in range(m):
            for j in range(n):
                grid[i][j] = orow[i] + ocol[j] - zrow[i] - zcol[j]
        # print("zero",ocol)
        # print("zero",zcol)
        # print(orow[0], ocol[0] ,zrow[0] ,zrow[0])
        return grid
                                                                       