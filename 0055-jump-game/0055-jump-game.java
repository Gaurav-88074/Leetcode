// import java.util.*;
class Solution {
    public boolean canJump(int[] nums) {
        // if(nums.length==1) return true;
        int energy = nums[0];
        int index = 0;
        while(energy >0 && index<nums.length-1){
            energy-=1;
            energy = Math.max(energy,nums[index]);
            // System.out.println(energy+ " : "+index);
            index+=1;
            // energy-=1;
            // if(index>=nums.length){
            //     return true;
            // }
            if(energy<=0)return false;
        }
        return index>=nums.length-1;
    }
}