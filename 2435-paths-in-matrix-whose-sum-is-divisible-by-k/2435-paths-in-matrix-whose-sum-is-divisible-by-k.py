class Solution(object):
    def numberOfPaths(self, grid, k):
        mod = 10**9 + 7
        m  =len(grid)
        n = len(grid[0])
        dp =[[None]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                dp[i][j] = [None]*k
        
        # @lru_cache(None)
        def compute(x,y,s):
            if x==len(grid)-1 and y==len(grid[0])-1:
                s+=grid[x][y]
                if s%k==0:
                    return 1
                return 0
            if x==len(grid) or y==len(grid[0]):
                return 0
            
            s+=grid[x][y]
            s%=k
            if dp[x][y][s]!=None : return dp[x][y][s]
            
            right = compute(x,y+1,s)
            down = compute(x+1,y,s)
            
            res  = right + down
            dp[x][y][s] = res%mod
            return res%mod
        
        return compute(0,0,0)%mod