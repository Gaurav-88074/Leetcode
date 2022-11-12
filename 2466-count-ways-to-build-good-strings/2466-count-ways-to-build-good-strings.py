class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod  =10**9 +7
        
        @lru_cache(None)
        def compute(size):
            res = 0
            if size>high:return 0
            if size>=low and size<=high:
                res+=1 
            res+=compute(size+one)
            res+=compute(size+zero)
            res%=mod
            return res
        return compute(0)%mod
            