class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        s = sum(skill)
        size = len(skill)//2
        
        t = s//size
        
        c = Counter(skill)
        # print(c)
        res = 0
        # print("============")
        # print(t)
        v = set()
        for i in skill:
            r = t-i
            if r in v:
                continue
            if r==i:
                d = c[i]
                if d%2!=0:return -1
                else:
                    res+=(r*i)*(d//2)
                    c[i]-=d
            elif r not in c or c[r]==0:
                # print("hit",r,c)
                return -1
            elif c[r]!=c[i]:
                return -1
            else:
                
                a = i
                b = r
                p = c[i]
                # print(a,b,p)
                res+=((a*b)*p)
                c[i]-=p
                c[r]-=p
                
                v.add(r)
                v.add(i)
        return res
        