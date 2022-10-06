class Solution(object):
    def rotateTheBox(self, box):
        def fix(a,b,row):
            # sub = row[a:b+1]
            # sub.sort(reverse = True)
            # for i in sub:
            #     row[a]=i
            #     a+=1
            hashh = 0
            dot = 0
            for i in range(a,b+1):
                if row[i]=="#": 
                    hashh+=1
                else: 
                    dot+=1
            while dot!=0:
                row[a]="."
                dot-=1
                a+=1
            while hashh!=0:
                row[a]="#"
                hashh-=1
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
        