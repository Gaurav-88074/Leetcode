# from sortedcollections import OrderedSet
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        c = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    self.x = i
                    self.y = j
                if grid[i][j]==-1:
                    c+=1
        size = len(grid) * len(grid[0])
        size-=c
        # print(size-c)

        s =set()
        l=[]
        self.res = 0
        def go(x,y,start):
            key = (x,y)
            if x==-1 or y==-1 or x==len(grid) or y==len(grid[0]) or \
                (key in s and start==False) or grid[x][y]==-1:
                return
            if grid[x][y]==2 and len(s)==size-1:
                # l.append(key)
                # print(l)
                # l.pop()
                self.res+=1
                return
            s.add((x,y))
            # l.append(key)
            left = go(x,y-1,False)
            right= go(x,y+1,False)
            top  = go(x-1,y,False)
            down = go(x+1,y,False)
            s.discard((x,y))
            # l.pop()
        s.add((self.x,self.y))
        go(self.x,self.y,True)
        return self.res