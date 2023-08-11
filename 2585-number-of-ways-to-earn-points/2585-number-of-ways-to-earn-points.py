class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        mod= 10**9 +7
        
        @lru_cache(None)
        def compute(i,target,j):
            
            if target<0 or i==len(types) or j>types[i][0]:
                return 0
            if target==0:
                return 1
            
            take = compute(i,target-types[i][1],j+1)%mod
            skip = compute(i+1,target,0)%mod
            return (take+skip)%mod
        
        res = compute(0,target,0)
        compute.cache_clear()
        return res