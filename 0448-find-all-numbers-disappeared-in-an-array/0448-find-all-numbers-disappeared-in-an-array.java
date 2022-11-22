class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> res = new LinkedList<>();
        
        int index;
        for(int i : nums){
            index = Math.abs(i)-1;
            nums[index]=Math.abs(nums[index]) * -1;
        }
        index = 1;
        for(int i :nums){
            if(i>0){
                res.add(index);
            }
            index+=1;
        }
        return res;
    }
}