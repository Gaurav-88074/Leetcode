class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        res = []
        
        def gen(s,n):
            if n==0:
                # print(s)
                res.append(s)
                return
            if s=="":
                gen(s+'a',n-1)
                gen(s+'b',n-1)
                gen(s+'c',n-1)
            elif s[-1]=="a":
                gen(s+'b',n-1)
                gen(s+'c',n-1)
            elif s[-1]=="b":
                gen(s+'a',n-1)
                gen(s+'c',n-1)
            else:
                gen(s+'a',n-1)
                gen(s+'b',n-1)
        gen("",n)
        
        # print(res)
        if k>len(res):
            return ""
        res.sort()
        # print(res)
        return res[k-1]