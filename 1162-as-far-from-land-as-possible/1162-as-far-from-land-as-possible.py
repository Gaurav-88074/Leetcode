class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        res = -1
        
        q = deque()
        row,col = len(grid),len(grid[0])
        
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    q.append([r,c,0])
        def isValid(x,y):
            return x<row and y<col and x>-1 and y>-1
        moves = [[0,1],[0,-1],[1,0],[-1,0]]

        visited=set()
        while q:
            # print(q)
            r,c,d = q.popleft()
            res = max(res,d)
            for a,b in moves:
                nR,nC = r+a , c + b
                if isValid(nR,nC) and (nR,nC) not in visited and grid[nR][nC]==0: 
                    visited.add((nR,nC))
                    q.append([nR,nC,d+1])
        return res if res!=0 else -1
                
            
            
            