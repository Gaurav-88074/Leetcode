class Solution(object):
    def convertToBase7(self, num):
        arr = []
        sign = 1
        if num<0:
            sign=-1
            num*=-1
        while num>=7:
            rem = num%7
            num//=7
            arr.append(rem)
        arr.append(num)
        arr.reverse()
        # print(arr)
        res = list(map(str,arr))
        res = "".join(res)
        if sign==-1:
            return "-"+res
        return res
        