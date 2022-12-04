class Solution {
    public long sum(int[] nums){
        long res = 0;
        for(int i : nums){
            res+=(long)i;
        }
        return res;
    }
    public int minimumAverageDifference(int[] nums) {
        long s = sum(nums);
        long res = 0;
        long prefix = 0;
        long avg = Integer.MAX_VALUE;
        long suffix;
        long a,b;
        long v1,v2;
        long ans;
        for(int i =0 ; i<nums.length ; i++){
            prefix+=(long)(nums[i]);
            suffix = s-prefix;
            a = i+1;
            b = nums.length-a==0 ? 1 : nums.length-a;
            v1 = prefix/a;
            v2 = suffix/b;
            ans = Math.abs(v1-v2);
            if(ans<avg){
                res = i;
                avg =ans;
            }
        }
        return (int)res;
        
    }
}