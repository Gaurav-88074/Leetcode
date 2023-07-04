class Solution {
    public void setBits(int value,int[] bits){
        for(int i=0 ; i<32 ; i++){
            bits[i] +=(value&1);
            value  = value>>1;
        }
    }
    public int singleNumber(int[] nums) {
        int[] bits = new int[32];
        for(int i = 0 ; i<nums.length;i++){
            setBits(nums[i],bits);
        }
        // System.out.println(Arrays.toString(bits));
        for(int i = 0 ; i<32 ;i++){
            bits[i]%=3;
        }
        // System.out.println(Arrays.toString(bits));
        int res = 0;
        for(int i = 0 ; i<32 ;i++){
            res += (1<<i) * bits[i];
        }
        return res;
        
     }
}