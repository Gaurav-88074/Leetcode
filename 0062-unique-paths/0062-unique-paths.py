class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[m-1][n-1] = 1
        mod  = 10**9 + 7
        for x in range(m-1,-1,-1):
            for y in range(n-1,-1,-1):
                right= 0
                down = 0

                if y+1<n:
                    right = dp[x][y+1]
                if x+1<m:
                    down  = dp[x+1][y]
                
                val = (right+down)
                dp[x][y]=max(dp[x][y],val)
        return dp[0][0]