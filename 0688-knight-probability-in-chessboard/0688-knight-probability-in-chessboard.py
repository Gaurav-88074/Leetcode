class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [
                    [-2,-1],[-1,-2],
                    [ 1,-2],[ 2,-1],
                    [ 2, 1],[ 1, 2],
                    [-1, 2],[-2, 1]
                ]
        @lru_cache(None)
        def compute(x,y,k):
            if x<0 or x>=n or y<0 or y>=n:
                return 0
            if k==0:
                return 1
            res = 0
            for a,b in moves:
                res += compute(x+a,y+b,k-1)/8
            return res
        return compute(row,column,k)