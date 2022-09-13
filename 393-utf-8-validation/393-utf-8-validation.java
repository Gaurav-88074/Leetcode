class Solution {
    public boolean checkBitOne(int value,int index){
        int mask = 1<<index;
        return (value&mask)>0;
    } 
    public boolean checkBitZero(int value,int index){
        int mask = 1<<index;
        return (value&mask)==0;
    } 
    public int countLastSet(int value){
        int res = 0;
        int index = 7;
        while(index>-1){
            if(checkBitOne(value,index)){
                res+=1;
                index-=1;
            }
            else{
                return res;
            }
        }
        return res;
    }
    public boolean lastOneZero(int value){
        boolean index7 = checkBitOne(value,7);
        boolean index6 = checkBitZero(value,6);
        return (index7 && index6);
    }
    public boolean compute(int[] data,int in){
        System.out.println("for index : "+in);
        System.out.println("value : "+data[in]);
        int start = data[in];
        int n = countLastSet(start);
        System.out.println("bit count : "+n);
        if(n==1 || n>4)return false;
        
        int i;
        for(i=in+1 ; i<(in+n) ; i++){
            if(i==data.length)return false;
            
            if(lastOneZero(data[i])==false){
                return false;
            }
        }
        if(i<data.length){
            return compute(data,i);
        }
        return true;
    }
    public boolean validUtf8(int[] data) {
        return compute(data,0);
    }
}