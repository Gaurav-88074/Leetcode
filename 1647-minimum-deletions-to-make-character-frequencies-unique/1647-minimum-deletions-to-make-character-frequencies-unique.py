class Solution:
    def minDeletions(self, s: str) -> int:
        d = [0]*26
        for i in range(len(s)):
            d[ord(s[i])-97]+=1
        # print(d)
        arr=[]
        for i in range(len(d)):
            if d[i]>0:
                arr.append(d[i])
        arr.sort(reverse=True)
        # print(arr)
        res = 0
        pre = float('inf')
        
        v = [arr[0]]
        for i in range(1,len(arr)):
            if arr[i]<v[-1]:
                v.append(arr[i])
            else:
                v.append(v[-1]-1)
            #-------------
            
            #-------------
        # print(v)
        for i in range(len(arr)):
            if v[i]<0:
                res+=arr[i]
                continue
            if arr[i]!=v[i]:res+=abs(arr[i]-v[i])
                
        return res 