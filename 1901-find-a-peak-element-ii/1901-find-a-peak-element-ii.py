class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        def isPeak(x,y,value):
            if x==-1 or y==-1 or x==len(mat) or y==len(mat[0]): return True
            
            return value>mat[x][y]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                value = mat[i][j]
                
                if isPeak(i-1,j,value) and isPeak(i+1,j,value) and isPeak(i,j+1,value) and isPeak(i,j-1,value):
                    return [i,j]
        return [-1,-1]