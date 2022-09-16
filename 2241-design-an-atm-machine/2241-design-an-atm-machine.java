class ATM {
    
    public long[] bank ;
    public int[] note ;
    public ATM() {
        bank = new long[5];
        note = new int[]{
            20,50,100,200,500
        };
    }
    
    public void deposit(int[] banknotesCount) {
        for(int i = 0 ; i<5 ; i++){
            bank[i]+=banknotesCount[i];
        }
        // System.out.println("deposited :"+Arrays.toString(bank));
    }
    
    public int[] withdraw(int amount) {
        int[] res = new int[5];
        long v;
        // System.out.println("--------");
        for(int i=4 ; i>-1 ;i--){
            v = amount/note[i];
            if(v>0 && bank[i]>0){
                if(v>bank[i]){
                    v = bank[i];
                }
                // v = bank[i];
                res[i]+=v;
                amount-=(note[i] * v);
                
                bank[i]-=v;
            }
            // System.out.println(Arrays.toString(res));
            if(amount==0){
                // System.out.println("bank :"+Arrays.toString(bank));
                return res;
            }
        }
        // System.out.println("--------");
        for(int i =0 ; i <5 ; i++){
            bank[i]+=res[i];
        }
        return new int[]{-1};
    }
}

/**
 * Your ATM object will be instantiated and called as such:
 * ATM obj = new ATM();
 * obj.deposit(banknotesCount);
 * int[] param_2 = obj.withdraw(amount);
 */