class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        ans=0
        m=len(grid)
        n=len(grid[0])
        if grid[0][0]==1 or grid[m-1][n-1]==1:
            return -1

        q=[(0,0)]
        while q:
            tmp_q=[]
            ans+=1

            while q:
                x,y=q.pop()
                if(x,y)==(m-1,n-1):
                    return ans

                for dx,dy in(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1):
                    xx,yy=x+dx,y+dy

                    if 0<=xx<m and 0<=yy<n and not grid[xx][yy]:
                        grid[xx][yy]=1

                        tmp_q.append((xx,yy))

            q=tmp_q

        return -1                            
        