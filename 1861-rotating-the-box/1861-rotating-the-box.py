class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        def fix(a,b,row):
            # print(a,b)
            sub = row[a:b+1]
            # print(sub)
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
        
        res= [[] for i in range(n)]
        for i in range(m):
            for j in range(n):
                res[j].append(box[-(i+1)][j])
        
        
        return res