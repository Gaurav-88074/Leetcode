class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        arr  = [*special,bottom,top]
        arr.sort()
        start = arr.index(bottom)
        end = arr.index(top)
        res = 0
        
        while start+1<len(arr) and arr[start]==arr[start+1]: 
            start+=1
        #----------------------
        a = start+1
        b = a+1
        #---------------------
        # print(a,b)
        #----------------------------------------
        res = 0
        while b<end:
            v =arr[b]-arr[a]-1 if arr[b]-arr[a]>1 else 0
            res=max(v,res)
            a+=1
            b+=1
        #-----------------------------------------
        # print(arr,start,end)
        if start-1>=0 and arr[start]==arr[start-1] and start+1<len(arr):
            res =max(res,arr[start+1] - arr[start] - 1)
        elif start+1<len(arr):
            res =max(res,arr[start+1] - arr[start])
        if end+1<len(arr) and arr[end]==arr[end+1]:
            res=max(res,arr[end] -arr[end-1]  - 1)
        elif end-1>=0:
            res=max(res,arr[end] - arr[end-1])
        return res