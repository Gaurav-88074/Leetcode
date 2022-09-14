class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 1000000007
        def powr(a, b):
            res = 1; 
            while (b > 0):
                if ((b & 1) != 0):
                    res = res * a
                res%=mod
                b = b >> 1
                a = a * a
                a%=mod
            
            return res % mod
        
        def multiply(a,b):
            res = 0
            while(b>0):
                if ( (b&1)==1 ):
                    res = res+a
                    res%=mod
                a*=2
                a%=mod
                b = b>>1
            
            return res % mod
        
        h = n//2;

        if((n&1)==1):
            return multiply(powr(4,h),powr(5,h+1))
        else:
            return multiply(powr(4,h),powr(5,h))
        
        