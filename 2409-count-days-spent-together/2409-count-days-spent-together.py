class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        a1,b1 = arriveAlice.split("-")
        a1,b1 = int(a1),int(b1)
        
        a2,b2 = leaveAlice.split("-")
        a2,b2 = int(a2),int(b2)
        
        c1,d1 = arriveBob.split("-")
        c1,d1 = int(c1),int(d1)
        
        c2,d2 = leaveBob.split("-")
        c2,d2 = int(c2),int(d2)
        
        
        y = {
            1 : 31,
            2 : 28,
            3 : 31,
            4 : 30,
            5 :  31,
            6 :  30,
            7 :  31,
            8  : 31,
            9  : 30,
            10 : 31,
            11:  30,
            12 : 31
        }
        
        s1 = []
        s2 = []
        
        
        flag = 0
        while a1<=a2:
            
            start = b1 if flag ==0 else  1
            for date in range(start,y[a1]+1):
                if a1==a2 and date>b2:
                    break
                s1.append(str(date)+"-"+str(a1))
            flag=1
            a1+=1

            
        # print(s1)
        
        flag = 0
        while c1<=c2:
            start = d1 if flag ==0 else  1
            for date in range(start,y[c1]+1):
                if c1==c2 and date>d2:
                    break
                s2.append(str(date)+"-"+str(c1))
            c1+=1
            flag=1
            
        # print(s2)
        
        s1 = set(s1)
        s2 = set(s2)
        
        s3 = s1.intersection(s2)
        
        return len(s3)            
        
        
    