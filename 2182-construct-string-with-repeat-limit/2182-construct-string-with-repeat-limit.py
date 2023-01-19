from sortedcontainers import SortedList, SortedDict,SortedSet
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        l = SortedList(key = lambda x :-ord(x[0]))
        c = Counter(s)
        for i in c:
            l.add([i,c[i]])
        # print(l)
        res = []
        while len(l)!=0:
            obj = l.pop(0)
            count= 0
            while count<repeatLimit and obj[1]>0:
                res.append(obj[0])
                obj[1]-=1
                count+=1
            #-------------------------------------
            if obj[1]>0 and len(l)==0: return "".join(res)
            #---------------------------------
            if obj[1]>0 and len(l)!=0:
                secondObj = l.pop(0)
                # count=0
                res.append(secondObj[0])
                secondObj[1]-=1
                # while count<repeatLimit and secondObj[1]>0:
                #     res.append(secondObj[0])
                #     secondObj[1]-=1
                #     count+=1
                if secondObj[1]>0:
                    l.add(secondObj)
            #-----------------------------------
            if obj[1]>0:
                    l.add(obj)
        # print(res)
        return "".join(res)