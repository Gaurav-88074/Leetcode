class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        
        org = n
        def get(v):
            ar=list(map(int,list(str(v))))
            return sum(ar)
        check = list(map(int,str(n).split()))
        if sum(check)<=target:return 0
        
        s =str(n)
        l =len(s)
        res = 0
        mul = 1
        
        while get(n)>target:
            value = n//mul
            last = value%10
            if last!=0:
                need = 10-last
                n+=need*mul
                res+=need*mul
            # print(n)
            mul*=10
        return n-org
            
        # return value-n
        # return 3