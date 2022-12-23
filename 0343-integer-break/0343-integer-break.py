class Solution:
    def integerBreak(self, n: int) -> int:
        @lru_cache(None)
        def compute(n):
            if n==1 or n==2:
                return 1
            res = 1
            for i in range(1,n):
                v1 = compute(n-i)
                v2 = compute(i)
                res = max(res,v1*v2)
                res = max(res,i*(n-i))
                res = max(res,v1 * (i))
                res = max(res,v2 * (n-i) )
            return res
        return compute(n)