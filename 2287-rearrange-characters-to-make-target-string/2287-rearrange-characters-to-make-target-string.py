from typing import Counter
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        # d = [0]*26
        # for i in s:
        #     v = ord(i)-97
        #     d[v]+=1
        # res = 0
        # temp = []
        # for k in range(100):
        #     for i in target : 
        #         v = ord(i)-97
        #         if d[v]!=0:
        #             temp.append(i)
        #             d[v]-=1
        # s = "".join(temp)
        # # m = float('inf')
        # # check  = True
        # # # comp = d[ ord(target[0])-97 ]
        # # # for i in target:
        # # #     v = ord(i)-97
        # # #     if d[v] =1:
        # # #         check = False 
        # # for i in target:
        # #     v = ord(i)-97
        # #     m = min(m,d[v])
        # #     if(d[v]==0):
        # #         return 0
        # # if len(set(list(target)))==1:
        # #     return 1
        # return s.count(target)
        c = Counter(s)
        v = Counter(target)
        res = 0
        # print(c)
        # print(v)
        while True:
            for i in v:
                # print("checking for",i)
                count = v[i]
                if c[i]<count:
                    return res
                else:
                    c[i]-=count
            res+=1
        return res