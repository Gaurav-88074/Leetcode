class Solution(object):
    def maximumEvenSplit(self, finalSum):
        res = []
        value = finalSum
        s =set()
        v = 2
        if (value&1)==1: return res
        
        while value>0:
            s.add(v)
            value-=v
            res.append(v)
            
            if value in s:
                res.pop()
                res.append(value+v)
                return res
            
            v+=2
        return res
        
        