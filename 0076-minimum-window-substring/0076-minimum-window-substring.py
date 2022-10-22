class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        def feasible(c,d):
            for i in c : 
                if d[i]<c[i] : 
                    return False
            return True
        c = Counter(t)
        d =defaultdict(int)
        
        start = 0
        r = []
        res = float('inf')
        for i in range(len(s)):
            v = s[i]
            d[v]+=1
            while feasible(c,d) and start<len(s):
                #---------------
                if i-start<res:
                    res = i - start
                    r= [start,i]
                #----------------
                ch = s[start]
                d[ch]-=1
                start+=1
        if len(r)==0:return ""
        # print(r)
        return s[r[0]:r[1]+1]