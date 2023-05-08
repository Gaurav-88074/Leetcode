class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        m,n = len(mat),len(mat[0])
        if (m&1)==1:
            res-=mat[m//2][m//2]
        # print(res)
        for i in range(m):
            res+=mat[i][i]+mat[i][-(i+1)]
        return res