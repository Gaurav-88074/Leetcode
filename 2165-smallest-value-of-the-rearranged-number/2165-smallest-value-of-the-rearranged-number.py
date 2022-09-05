class Solution:
    def smallestNumber(self, num: int) -> int:
        if num<0:
            res = []
            num = -num
            while num>0:
                res.append(num%10)
                num//=10
            res.sort(reverse = True)
            v = 0
            for i in res:
                v+=i
                v*=10
            return -v//10
        else:
            res = []
            while num>0:
                res.append(num%10)
                num//=10
            res.sort()
            for i  in range(len(res)):
                if res[i]>0:
                    res[0],res[i] = res[i],res[0]
                    break
            v = 0
            for i in res:
                v+=i
                v*=10
            return v//10