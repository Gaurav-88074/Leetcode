from collections import defaultdict
class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        def ps(arr):
            l = [0]*len(arr) 
            r = [0]*len(arr)
            
            left=0
            for i in range(len(arr)):
                left+=arr[i]
                l[i] = left
            right=0
            for i in range(len(arr)):
                right+=arr[-(i+1)]
                r[-(i+1)] = right
            return l,r
            
            
        d = defaultdict(list)
        
        for i in range(len(arr)):
            v  = arr[i]
            d[v].append(i)
        # print(d)
        
        
        res = [0]*len(arr)
        
        for arr in d.values():
            l,r = ps(arr)
            # print()
            # print(l)
            # print(r)
            #LIMR
            if len(arr)==1:
                res[arr[0]]=0
                continue
            for i in range(len(arr)):
                index = arr[i]
                a = 0
                b = 0
                if i==0:
                     b = r[i+1]  - (len(arr)-i-1)*arr[i]
                elif i==len(arr)-1:
                     a = (i * arr[i]) -  l[i-1]
                else:
                    a = (i * arr[i]) -  l[i-1]
                    b = r[i+1] - (len(arr)-i-1)*arr[i]
                res[index]=a+b  
        return res