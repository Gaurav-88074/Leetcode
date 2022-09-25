class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        first  = 0
        second = 1
        third  = 1
        arr  =[first,second]
        while third<=k:
            arr.append(third)
            first = second
            second  =third
            third = first + second
        i=1
        res = 0
        while k!=0:
            if arr[-i]<=k:
                res+=1
                k-=arr[-i]
                
            i+=1
        
        return res
        