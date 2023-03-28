class Solution:
    
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        res = 0
        if cost1<cost2:
            cost1,cost2=cost2,cost1
        r = total//cost1
        for i in range(r+1):
            # print(((total - (cost1*i))//cost2)+1)
            res+= ((total - (cost1*i))//cost2)+1
        return res
            
        