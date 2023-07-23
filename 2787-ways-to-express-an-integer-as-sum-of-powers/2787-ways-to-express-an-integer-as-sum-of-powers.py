import math
class Solution:
    dp = {}
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10**9 + 7
        till = int(pow(n,1/x))+1
        powermap = {}
        for i in range(1,till+2):
            powermap[i]=pow(i,x,mod)
        # @lru_cache(None)
        def compute(n,x,i):
            key = (n,x,i)
            
            if n==0:
                return 1
            
            if n<0 or n-powermap[i]<0:
                return 0
            #--------------------------
            if key in Solution.dp:
                return Solution.dp[key]
            #-----------------------------
            take = compute(n - powermap[i] ,x, i+1)%mod
            skip = compute(n,x,i+1)%mod
            
            res = (take+skip)%mod
            
            Solution.dp[key]=res
            
            return res
        return compute(n,x,1)%mod