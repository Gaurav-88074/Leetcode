class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> d=  new HashMap<>();
        for(int i =0 ; i<nums.length ; i++){
            if(d.containsKey(nums[i])){
                return new int[]{i ,d.get(nums[i])};
            }
            d.put(target-nums[i],i);
        }
        return new int[]{};
    }
}