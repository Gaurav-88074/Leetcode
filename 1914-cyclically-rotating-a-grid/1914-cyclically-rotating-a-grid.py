class Solution:
    
    def rotateGrid(self, l: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(l),len(l[0])
        def rotate(i):
            save = l[i][i]
            for j in range(i,n-i-1):
                l[i][j] = l[i][j+1]
            for j in range(i,m-i-1):
                l[j][n-i-1] = l[j+1][n-i-1]
            for j in range(n-i-1,i,-1):
                l[m-i-1][j] = l[m-i-1][j-1]
            for j in range(m-i-1,i,-1):
                l[j][i] = l[j-1][i]
            l[i+1][i]=save

        x=int(min(m,n)/2)
        for i in range(x):
            a=k%(2*(m+n-4*i)-4)
            for j in range(a):
                rotate(i)
        return l
        