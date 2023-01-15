import numpy as np
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0]*n for _ in range(n)]
        # mat = np.array(mat)
        # for a,b,c,d in queries:
            # mat[a:c+1, b:d+1] += 1
        
        for x1,y1,x2,y2 in queries:
            
            for i in range(x1,x2+1):
                mat[i][y1]+=1
                if y2+1<n:
                    mat[i][y2+1]-=1
        for i in range(n):
            v=0
            for j in range(n):
                v+=mat[i][j]
                mat[i][j]=v
        return mat