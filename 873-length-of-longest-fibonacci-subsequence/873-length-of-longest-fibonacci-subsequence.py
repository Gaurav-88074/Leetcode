class Solution(object):
    def lenLongestFibSubseq(self, arr):
        #-----------------------------------------
        n = len(arr)
        res = 0
        s = set(arr)
        #------------------------------------------
        def binarySearch(array,key,start,end):
            if(start>end) : return -1
            mid = (start+end)//2
            if key==array[mid] : return mid
            elif key<array[mid] : return binarySearch(array,key,start,mid-1);
            else : return binarySearch(array,key,mid+1,end)
        #----------------------------------------
        def compute(array,first,second,s):
            key = first + second
            
            if key in s:
                third = second + first
                return 1 + compute(array,second,third,s)
            else:
                return 0
        #----------------------------------------
        for i in range(n):
            for j in range(i+1,n):
                first = arr[i]
                second= arr[j]
                # self.v=[first,second]
                value = compute(arr,first,second,s)
                if value==0:continue
                res = max(res,value+2)
        #-----------------------------------------
        return res