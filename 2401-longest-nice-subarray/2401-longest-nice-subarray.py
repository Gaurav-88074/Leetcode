class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        state = [0] * 32
        #-----------------------------------------
        def removeIt(state,value):
            index=0
            while value>0:
                if (value&1)==1:
                    state[index]=0
                index+=1
                value>>=1
        #-----------------------------------------
        def mergeIt(state,value):
            index=0
            while value>0:
                if (value&1)==1:
                    state[index]=1
                index+=1
                value>>=1
        #-------------------------------------------
        def isMergePossible(state,value):
            index = 0
            while value>0:
                if (value&1)==1 and state[index]==1:
                    return False
                index+=1
                value>>=1
            return True
        #=-------------------------------------
        res = 0
        pre = 0
        for i,v in enumerate(nums):
            if isMergePossible(state,v):
                mergeIt(state,v)
            else:
                #--------------------
                while isMergePossible(state,v)!=True and pre<i:
                    removeIt(state,nums[pre])
                    pre+=1
                #-------------------
                mergeIt(state,v)
            res = max(res,i-pre+1)  
        return res
                
                
                
                
           