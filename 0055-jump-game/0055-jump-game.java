// import java.util.*;
class Solution {
    public boolean canJump(int[] nums) {
        // if(nums.length==1) return true;
        int energy = nums[0];
        int index = 0;
        while(energy>0 || nums[index]!=0){
            energy = Math.max(energy,nums[index]);
            // System.out.println(energy+ " : "+index);
            index+=1;
            energy-=1;
            if(index>=nums.length){
                return true;
            }
        }
        return index>=nums.length-1;
    }
}