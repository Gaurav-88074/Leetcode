class Solution:
    def minimizeResult(self, expression: str) -> str:
        #==========================
        d = dict()
        self.mv = float('inf')
        #===========================
        
        def computeExp(exp):
            left = exp.split(")")
            right= left[0].split("(")
            
            v = right[1]
            
            v = v.split("+")
            
            brac = int(v[0])+int(v[1])
            
            res = brac
            if right[0]!='':
                res*=int(right[0])
            if left[1]!='':
                res*=int(left[1])
            return res
        # print(computeExp("(3+2)"))
        
        
        def comb(p1,p2,n,s):
            global minValue
            if p1==-1 or p2==n+1:
                return
            nw = [*s]
            nw.insert(p1,"(")
            nw.insert(p2+1,")")
            #------------------
            genStr = "".join(nw)
            value = computeExp(genStr)
            d[value] = genStr
            self.mv = min(self.mv,value)
            #-------------------
            # comb(p1-1,p2+1,n,s)
            comb(p1,p2+1,n,s)
            comb(p1-1,p2,n,s)
        
        
        s =list(expression)
        # print(s)
        index = s.index("+")
        
        comb(index-1,index+2,len(s),s)
        
        return d[self.mv]
            
            
            