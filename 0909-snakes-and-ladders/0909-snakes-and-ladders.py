class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def getPair():
            change=None
            if n%2==0:
                change = -1
            else:
                change = 1
            value = n**2
            if change>0:
                value-= (n-1)
            d=defaultdict(tuple)
            for i in range(0,n):
                for j in range(0,n):
                    # print([i,j,value],end=" ")
                    d[value] = (i,j)
                    value+=change
                if change<0:
                    value-= (n-1)
                else:
                    value-=(n+1)
                change*=-1
            return d
        d = getPair()
        
        total = n**2
        q = deque()
        distance = [-1]*((n+1)**2)
        
        distance[1] = 0
        
        start = 1
        
        q.append(start)
        while len(q)!=0:
            currentValue = q.popleft()
            
            for upnext in range(currentValue + 1,min(total,currentValue+6)+1):
                pos = d[upnext]
                row,col = pos
                
                dest = upnext if board[row][col]==-1 else board[row][col]
                
                if distance[dest]==-1:
                    distance[dest] = distance[currentValue] + 1
                    q.append(dest)
        # print(distance)
        return distance[n*n]
        
        #DFS won't work
        # @lru_cache(None)
        # def getMinValue(position):
        #     #---------------------------
        #     if position not in d:
        #         return float('inf')
        #     #----------------------------
        #     if position==total:
        #         return 0
        #     #--------------------------
        #     curr_pos = d[position]
        #     i,j = curr_pos
        #     if board[i][j]!=-1:
        #         upnext = board[i][j]
        #         return getMinValue(upnext)
        #     #---------------------------
        #     res = float('inf')
        #     for i in range(1,7):
        #         value = 1 + getMinValue(position + i)
        #         res = min(res,value)
        #     return res
        # #------------------------
        # res = getMinValue(1)
        # #------------------------
        # if res==float('inf'):
        #     return -1
        # return res