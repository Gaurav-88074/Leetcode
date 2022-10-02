class Solution(object):
    def maxSum(self, grid):
        res = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                a = grid[i][j] + grid[i][j+1]+grid[i][j+2]
                b = grid[i+1][j] + grid[i+1][j+1]+grid[i+1][j+2]
                c = grid[i+2][j] + grid[i+2][j+1]+grid[i+2][j+2]
                
                v = a+b+c
                v-=grid[i+1][j]
                v-=grid[i+1][j+2]
                res=max(res,v)
        return res
        