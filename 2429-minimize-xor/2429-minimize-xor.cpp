class Solution {
public:
    int minimizeXor(int num1, int num2) {
        int bb= __builtin_popcount(num2);
        int aa= __builtin_popcount(num1);
        
        
        int res=0;
        
        int bitmask;
        int c;
        for(int i=0;i<=31;i++){
            bitmask=1<<i;
            c= num1 & bitmask;
            
            
            if(c==0 && bb>aa){
                res |=(bitmask);
                bb-=1;
            }
            else if(c && aa>bb){
                aa-=1;
            }
            
            else{
                res|=c;
            }
        }
        
        
        return res;
    }
};