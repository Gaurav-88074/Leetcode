class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 10**9+7
        @lru_cache(None)
        def compute(x,y,moves):
            if x==-1 or y==-1 or x==m or y==n:
                if moves==0:
                    return 1
                else:
                    return 0
            if moves==0:
                return 0
            
            left = compute(x,y-1,moves-1)
            right= compute(x,y+1,moves-1)
            top  = compute(x-1,y,moves-1)
            down = compute(x+1,y,moves-1)
            
            return left + right + top + down
        res = 0
        for i in range(1,maxMove+1):
            res+=compute(startRow,startColumn,i)%mod
        return res%mod
            