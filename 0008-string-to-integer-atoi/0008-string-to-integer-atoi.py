class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s)==0:return 0
        # print(s,len(s))
        sign = 1
        i = 0
        if s[0]=='-':
            sign=-1
            i+=1
        if s[0]=='+':
            i+=1
        arr=[]
        while i<len(s) and (ord(s[i])>=48 and ord(s[i])<58):
            arr.append(s[i])
            i+=1
        v = "".join(arr)
        if len(v)==0:return 0
        # print(arr,v,len(v))
        res =  int(v)*sign
        left =-1 * 2**31
        right=(2**31) -1
        if res<left :
            return left
        if res>right:
            return right
        return res