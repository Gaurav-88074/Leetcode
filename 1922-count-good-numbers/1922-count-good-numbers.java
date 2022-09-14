class Solution {
    public int mod = 1000000000 + 7;
    long powr(long a, long b){
        long res = 1; 
 
        while (b > 0) {
            if ((b & 1) != 0)
                res = res * a;
            res%=mod;
            b = b >> 1; 
            a = a * a; 
            a%=mod;
        }
        return res % mod;
    }
    long multiply(long a,long b){
        long res = 0;
        while(b>0){
            if ( (b&1)==1 ){
                res = res+a;
                res%=mod;
            }
            a*=2;
            a%=mod;
            b/=2;  
        }
        return res % mod;
    }
    public int countGoodNumbers(long n) {
        long h = n/2;

        if((n&1)==1){
            return (int)multiply(powr(4,h),powr(5,h+1));
        }
        else{
            return (int)multiply(powr(4,h),powr(5,h));
        }

    }
}