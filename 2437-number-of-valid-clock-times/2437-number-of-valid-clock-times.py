class Solution:
    
            
    def countTime(self, time: str) -> int:
        def compute(time,index,v):
            if index==len(time):
                return 1
            if index==0 and time[0]=="?":
                if time[index+1]=="?" or int(time[index+1])<4:
                    time[0] = "0"
                    a = compute(time,index+1,v)
                    time[0] = "1"
                    b = compute(time,index+1,v)
                    time[0] = "2"
                    c = compute(time,index+1,v)
                    return a+b+c
                else:
                    time[0] = "0"
                    a = compute(time,index+1,v)
                    time[0] = "1"
                    b = compute(time,index+1,v)
                    return a+b
            elif index==1 and time[1]=="?":
                if time[index-1]=="0" or time[index-1]=="1":
                    return sum([
                        compute(time,index+1,v) for i in range(10)
                    ])
                else:
                    return sum([
                        compute(time,index+1,v) for i in range(4)
                    ])
            elif index==3 and time[3]=="?":
                return sum([
                        compute(time,index+1,v) for i in range(6)
                ])
            elif index==4 and time[4]=="?":
                return sum([
                        compute(time,index+1,v) for i in range(10)
                ])
            else:
                return compute(time,index+1,v)
                
        # d = {
        #     0 : 2
        #     1 : 4
        #     3 : 6
        #     4 : 10
        # }
        time = list(time)
        mod = 10**9 + 7
        res = compute(time,0,0)%mod
        return res
            
            
                