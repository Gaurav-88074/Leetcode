class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        def fix(a,b,row):
            sub = row[a:b+1]
            sub.sort(reverse = True)
            for i in sub:
                row[a]=i
                a+=1
            
        for row in box:
            start = 0
            for i in range(len(row)):
                if row[i]=="*":
                    fix(start,i-1,row)
                    start=i+1
            fix(start,len(row)-1,row)
        # print(box)
        # res = []
        m = len(box)
        n = len(box[0])
        
        res= [[0]*m for i in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][i] = (box[-(i+1)][j])
        
        
        return res