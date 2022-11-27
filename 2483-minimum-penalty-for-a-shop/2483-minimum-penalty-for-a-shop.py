class Solution:
    def bestClosingTime(self, c: str) -> int:
        costr= [{"Y":0 , "N":0} for i in range(len(c))]
        costl= [{"Y":0 , "N":0} for i in range(len(c))]
        Y = 0
        N = 0
        res = float('inf')
        for i in range(len(c)-1,-1,-1):
            if c[i]=="Y":
                Y+=1
            else:
                N+=1
            
            costr[i]["Y"] = Y
            costr[i]["N"] = N
        Y = 0
        N = 0
        for i in range(len(c)):
            if c[i]=="Y":
                Y+=1
            else:
                N+=1
            costl[i]["Y"] = Y
            costl[i]["N"] = N
        # print(costr)
        # print(costl)
        
        res = 0
        value = float('inf')
        for i in range(len(c)):
            p1 = costr[i]["Y"]+ (costl[i-1]["N"] if i-1>=0 else 0)
            # print("penealty at ",i,p1)
            if p1<value:
                value = p1
                res = i
            # res = min(res,p1)
        p1 = costl[-1]["N"]
        # print("penealty at ",i,p1)
        if p1<value:
            value = p1
            res = len(c)
            
            
        return res