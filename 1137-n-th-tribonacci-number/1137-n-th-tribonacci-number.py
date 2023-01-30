class Solution:
    def tribonacci(self, n: int) -> int:
        
        @lru_cache(None)
        def compute(n):
            if n==0 or n==1:
                return n
            elif n<0:
                return 0
            else:
                return compute(n-3)+compute(n-2)+compute(n-1)
        return compute(n)