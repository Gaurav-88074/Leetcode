class Solution(object):
    def getSmallestString(self, n, k):
        res = []
        while n>0:
            v = k+1 - n
            if v>=26:
                res.append(chr(96+26))
                k-=26
            else:
                res.append(chr(96+v))
                k-=v
            n-=1
        res.reverse()
        # print(res)
        return "".join(res)
        