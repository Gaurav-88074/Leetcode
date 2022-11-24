from typing import Counter
import re
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        
        b = set(banned)
        q = "!?',;."
        q=set(list(q))
        
        res = None
        c = 0
        
        nw = []
        for i in paragraph: 
            if i not in q:
                nw.append(i)
            else:
                nw.append(" ")
        nw = "".join(nw)
        
        p = nw.split()
        d = defaultdict(int)
        for i in p:
            v = i.strip().lower()
            d[v]+=1
            
            if v not in b and d[v]>c:
                res = v
                c = d[v]
                
                
        
        # print(c)
        return res
        
        