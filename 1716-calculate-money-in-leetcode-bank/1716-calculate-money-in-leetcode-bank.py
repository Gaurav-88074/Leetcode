class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        day = [0,0,0,0,0,0,0]
        pre = 0
        # i  =0
        for i in range(n):
            if i%7==0:
                pre = day[0]+1
                day[0] = pre
            res+=pre
            pre+=1
        return res
        