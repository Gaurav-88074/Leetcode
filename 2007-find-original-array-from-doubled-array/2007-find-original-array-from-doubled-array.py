class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        n = len(changed)
        
        if (n&1)==1:return []
        
        changed.sort()
        c = dict(Counter(changed))
        res = []
        # print(c)
        zero = 0
        
        if 0 in c :
            if (c[0]&1)==1 : 
                return []
            else:
                zero = c[0]//2
                c.pop(0)
        for i in changed:
            if i==0 : 
                continue
            if i in c and i*2 in c:
                key = i*2
                value=c[key]
                
                c.pop(key)
                value-=1
                if value>0:
                    c[key] = value
                res.append(i)
                
                #================
                key = i
                value=c[i]
                c.pop(key)
                value-=1
                if value>0:
                    c[key] = value
            elif i in c and i*2 not in c:
                return []
        
        
        for i in range(zero):
            res.append(0)
            
        if len(res)!=len(changed)//2:
            return []
        
        return res
        