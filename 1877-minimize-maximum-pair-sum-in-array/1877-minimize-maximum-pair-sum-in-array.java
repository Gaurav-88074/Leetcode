class Solution {
    public int minPairSum(int[] nums) {
        Arrays.sort(nums);
        int left = 0;
        int right=nums.length-1;
        int res = nums[left]+nums[right];
        while(left<right){
            res = res>(nums[left]+nums[right]) ? res:nums[left]+nums[right];
            left++;
            right--;
        }
        return res;
    }
}