class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        dp = [-1]*(n+1)
        # dp[0] = 0
        # dp[1] = 1
        
        def compute(i):
            if i<=1:
                return i
            else:
                if dp[i]!=-1:
                    return dp[i]
                if i%2==0:
                    dp[i] = compute(i//2)
                    return dp[i]
                else:
                    dp[i] = compute(i//2) + compute((i//2)+1)
                    return dp[i]
        dp[n] = compute(n)
        for i in range(n,-1,-1):
            dp[i] = compute(i)
        return max(dp)