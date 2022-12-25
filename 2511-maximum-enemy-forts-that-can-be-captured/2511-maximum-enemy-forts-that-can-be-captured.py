class Solution:
    def captureForts(self, forts: List[int]) -> int:
        
        def right(i):
            c = 0
            for i in range(i+1,len(forts)):
                if forts[i]==0:
                    c+=1
                
                if forts[i]==1:
                    return c
                if forts[i]==-1:
                    return 0
            return 0
        def left(i):
            c = 0
            for i in range(i-1,-1,-1):
                if forts[i]==0:
                    c+=1
                if forts[i]==1:
                    return c
                if forts[i]==-1:
                    return 0
            return 0
        res = 0
        for i,v in enumerate(forts):
            if v==-1:
                res = max(res,left(i),right(i))
        return res