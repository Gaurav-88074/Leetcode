class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def getMatrix(m,n):
            return [[float('inf') for i in range(n)] for j in range(m) ]
        #----------------------------------
        dist = getMatrix(len(mat),len(mat[0]))
        #-----------------------------------
        queue = deque()
        #----------------------------------
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    dist[i][j] = 0
                    queue.append((i,j))
        #-----------------------------------
        row,col = len(mat),len(mat[0])
        #---------------------------------
        visited = set()
        #---------------------------------
        while queue:
            node = queue.popleft()
            x,y  = node
            #-------------------------------------
            if y-1>=0:
                oldValue = dist[x][y-1]
                dist[x][y-1] = min(dist[x][y-1] , 1 + dist[x][y])
                if oldValue!=dist[x][y-1]:
                    queue.append((x,y-1))
            #----------------------------------------
            if y+1 < col:
                oldValue = dist[x][y+1]
                dist[x][y+1] = min(dist[x][y+1] , 1 + dist[x][y])
                if oldValue!=dist[x][y+1]:
                    queue.append((x,y+1))
            #-----------------------------------------
            if x-1>=0:
                oldValue = dist[x-1][y]
                dist[x-1][y] = min(dist[x-1][y] , 1 + dist[x][y])
                if oldValue!=dist[x-1][y]:
                    queue.append((x-1,y))
            #----------------------------------------------
            if x+1<row:
                oldValue = dist[x+1][y]
                dist[x+1][y] = min(dist[x+1][y] , 1 + dist[x][y])
                if oldValue!=dist[x+1][y]:
                    queue.append((x+1,y))
        #--------------------------------------------
        return dist
        
