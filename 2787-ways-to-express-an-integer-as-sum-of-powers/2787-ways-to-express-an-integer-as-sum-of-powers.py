import math
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10**9 + 7
        till = int(pow(n,1/x))+1
        powermap = {}
        for i in range(1,till+2):
            powermap[i]=pow(i,x,mod)
        @lru_cache(None)
        def compute(n,i):
            if n==0:
                return 1
            
            if n<0 or n-powermap[i]<0:
                return 0
            
            take = compute(n - powermap[i] , i+1)%mod
            skip = compute(n,i+1)%mod
            
            res = (take+skip)%mod
            
            return res
        return compute(n,1)%mod