import math
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10**9 + 7
        till = int(pow(n,1/x))+1
        
        @lru_cache(None)
        def compute(n,i):
            if n==0:
                return 1
            
            if n<0 or n-pow(i,x)<0:
                return 0
            
            # print("I took",i**x)
            take = compute(n - pow(i,x) , i+1)%mod
            skip = compute(n,i+1)%mod
            res = (take+skip)%mod
            return res
        return compute(n,1)%mod