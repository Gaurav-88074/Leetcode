class Solution {
    public int minPairSum(int[] nums) {
        Arrays.sort(nums);
        int left = 0;
        int right=nums.length-1;
        int res = nums[left]+nums[right];
        int value;
        while(left<right){
            value = nums[left]+nums[right];
            res = res>value ? res :value;
            left++;
            right--;
        }
        return res;
    }
}