class Solution:
    def minMoves(self, target: int, d: int) -> int:
        res = 0
        given = target
        while given!=1:
            if given%2==0 and d>0:
                given//=2
                d-=1
            else:
                given-=1
            if d==0:
                return res+given
            res+=1
        return res
        