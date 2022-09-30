class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        c = Counter(tasks)
        res = 0
        for i in c:
            v = c[i]
            if v==1:
                return -1
            if v==2 or v==3:
                res+=1
                continue
            else:
                if v%3==0:
                    res+=v//3
                elif v%3==2:
                    res+=v//3
                    res+=1
                else:
                    res+=v//3
                    res-=1
                    res+=2
        return res
            