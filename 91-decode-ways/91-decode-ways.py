class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=="0":return 0
        
        @lru_cache(None)
        def compute(index,value):
            if index==len(s): 
                # print(value)
                return 1
            
            newValue = value*10 + int(s[index])
            
            a = 0
            b = 0
            #------------------------------------
            if int(s[index])==0  and newValue>26:
                return 0
            #---------------------------------
            if newValue<=26:
                a = compute(index+1,newValue)
            if int(s[index])!=0 and newValue!=int(s[index]):
                b = compute(index+1,int(s[index]))
                                        
            return a+b
        return compute(0,0)