class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40, 
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        res = 0
        pre = s[0]
        for i in range(1,len(s)):
            c  = s[i]
            if pre!="" and pre + c in d:
                res+=d[pre+c]
                # print(pre+c)
                pre=""
            elif pre!="":
                res+=d[pre]
                # print(pre)
                pre=c
            else:
                pre = c
        if pre!="":
            res+=d[pre]
        return res
        