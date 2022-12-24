class Solution:
    def numTilings(self, n: int) -> int:
        @lru_cache(None)
        def compute(n):
            if n==1:
                return 1
            if n==2:
                return 2
            if n==3:
                return 5
            elif n<0:
                return 0
            else:
                return sum([
                    compute(n-3),
                    compute(n-1),
                    compute(n-1)
                ])
        mod = 10**9 +7
        return compute(n)%mod
                    
            