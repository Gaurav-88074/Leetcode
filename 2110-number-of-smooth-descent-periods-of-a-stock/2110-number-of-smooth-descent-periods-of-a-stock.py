class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        res = 0
        c = 0
        pre=None
        for i in prices:
            if pre==None:
                c+=1
            elif pre-i==1:
                c+=1
            else:
                c = 1
            #------
            res+=c
            pre = i
            #------
        return res
    