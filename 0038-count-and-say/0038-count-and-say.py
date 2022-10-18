class Solution(object):
    def compute(self,arr):
        if len(arr)==1 and arr[0]==1:
            return [1,1]
        res = []
        c=0
        pre = arr[0]
        for i in arr:
            if i==pre:
                c+=1
            else:
                res.append(c)
                res.append(pre)
                pre=i
                c=1
        res.append(c)
        res.append(pre)
        return res
    def countAndSay(self, n):
        
        r = [1]
        for i in range(n-1):
            r = self.compute(r)
            # print(r)
        return "".join(map(str,r))
        