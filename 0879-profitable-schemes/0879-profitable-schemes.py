class Solution:
    def profitableSchemes(self, n, minProfit, group, profit) -> int:
        mod = 10**9 + 7
        # @lru_cache(None)
        dp = [[[None]*101 for i in range(101)] for j in range(101)]
        def compute(i,p,g):
            key = (i,p,g)
            if g>n:
                return 0
            if i==len(profit):
                if p>=minProfit:
                    return 1
                else:
                    return 0
            if dp[i][p][g]!=None :
                return dp[i][p][g]
            
            take = compute(i+1,min(minProfit,p+profit[i]),g+group[i])
            skip = compute(i+1,p,g)
            
            res = (take+skip)%mod
            
            dp[i][p][g] =res
            
            return res
        return compute(0,0,0)%mod
        