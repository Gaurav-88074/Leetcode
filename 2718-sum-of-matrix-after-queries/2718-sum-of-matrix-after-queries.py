class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        row =set()
        col =set()
        res = 0
        r = n
        c = n
        for t,i,v in queries[::-1]:
            if t==0:
                if i not in row:
                    row.add(i)
                    res+= v*r
                    c-=1
            else:
                if i not in col:
                    col.add(i)
                    res+= v*c
                    r-=1
        return res
            
            