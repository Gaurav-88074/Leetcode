class Solution(object):
    def numDecodings(self, s):
        if s[0]=="0":return 0
        
        # @lru_cache(None)
        dp = {}
        def compute(index,value):
            if index==len(s): 
                return 1
            key = (index,value)
            if key in dp: return dp[key]
            
            
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
            
            dp[key] = a+b
            return a+b
        return compute(0,0)
        